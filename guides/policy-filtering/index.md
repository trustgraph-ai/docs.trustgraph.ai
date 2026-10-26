---
title: Policy-Based Query Filtering
nav_order: 3
parent: Managing operations
review_date: 2026-11-01
guide_category:
  - Managing operations
guide_category_order: 3
guide_description: Control which knowledge graph results users can see by writing SHACL-AF policy shapes and attaching user context to queries
guide_difficulty: advanced
guide_time: 45 min
guide_emoji: "\U0001F6E1"
guide_banner: banner.jpg
guide_labels:
  - Policies
  - SHACL-AF
  - Access Control
  - SPARQL
  - CLI
---

# Policy-Based Query Filtering

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>A running TrustGraph deployment with IAM enabled</li>
<li>TrustGraph CLI tools installed</li>
<li>Admin-level access (API key with admin role)</li>
<li>Familiarity with RDF and SPARQL</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Write SHACL-AF policy shapes, load them into TrustGraph, mint user-context tokens, and verify that query results are filtered according to your policies."
%}

**Filter knowledge graph query results based on who is asking**

> **Requires TrustGraph v2.10 or later.** Policy-based query filtering
> is not available in v2.9 or earlier releases.

Policy-based query filtering lets you control which parts of a
knowledge graph each user can see. Policies are written as SHACL-AF
shapes that inspect the user's context (clearance level, department,
role) and the properties of each graph node (classification,
department, sensitivity). Nodes that violate a policy are removed from
query results before the user sees them.

This works across all query types: SPARQL queries, Graph RAG, Document
RAG, and agent interactions all pass through the same policy engine.

## When to Use Policy Filtering

- **Use it when** different users should see different subsets of the
  same knowledge graph: classification levels, departmental
  boundaries, need-to-know compartments, or regulatory restrictions.

- **Don't use it** as a substitute for workspace separation. If two
  groups should never share data at all, put them in separate
  workspaces. Policies are for nuanced, overlapping access within a
  shared graph.

## Core Concepts

### SHACL-AF Policy Shapes

Policies are written as [SHACL Advanced Features](https://www.w3.org/TR/shacl-af/)
node shapes. Each policy has two parts:

1. **A SPARQL target** (`sh:SPARQLTarget`) that selects which graph
   nodes should be blocked for the current user.
2. **A SPARQL rule** (`sh:SPARQLRule`) that emits a validation result
   marking those nodes as blocked.

The target query has access to both the knowledge graph and the user's
context (injected as RDF triples at query time). If a node appears in
the target results, it is blocked.

### User Context

A user context is a structured description of who the user is: their
roles, organisational units, assignments, clearance qualifiers, and
any override authorities. It is carried inside a JWT and converted to
RDF triples that the policy SPARQL can query against.

User contexts use the `tg-uc:` namespace
(`https://trustgraph.ai/ontology/user-context/`):

| Predicate | Purpose |
|-----------|---------|
| `tg-uc:UserContext` | RDF type for the context node |
| `tg-uc:organisationalUnit` | Sections/departments the user belongs to |
| `tg-uc:hasAssignment` | Links to assignment resources with scope and qualifiers |
| `tg-uc:hasOverrideAuthority` | Special override permissions |
| `tg-uc:qualifiers` | Assignment-level properties (e.g. classification level) |

### Tri-State Determinations

When a node is evaluated against policies, the outcome is one of three
states:

| Determination | Meaning | Effect |
|---------------|---------|--------|
| **Allowed** | No policy blocks this node | Node appears in results |
| **Filtered** | A policy silently removes this node | Node is excluded from results |
| **Violation** | A serious policy breach | Node is excluded; the attempt is logged |

The severity is set by `sh:resultSeverity` in the policy rule:
`tg-pol:Filtered` for silent removal, `tg-pol:Violation` for logged
breaches.

### Policy Precedence

Policies are evaluated in order of `sh:order` (lower = higher
priority). Once a node is blocked by any policy, later policies do not
change the outcome. Use `sh:order` to ensure that your most important
security boundaries are evaluated first.

### Enforcement Mode

When any policy shapes exist in the `urn:graph:policy` named graph,
enforcement mode activates automatically. In enforcement mode, every
query **must** include a user context in the JWT. Queries without a
user context are rejected with a `policy-enforcement-error`.

This prevents accidentally bypassing policies by using a plain
authentication token.

## Step-by-Step Guide

This guide uses a simplified version of a WWII signals intelligence
scenario to demonstrate compartmentalised access control. The full
test dataset is available in the TrustGraph source under
`docs/tech-specs/policy-test-data/`.

### Step 1: Prepare Your Knowledge Graph

Create a Turtle file with your knowledge graph data. Each entity that
policies will filter should have properties that the policies can
match against (e.g. classification level, department/section
membership).

For this example, we have intelligence reports belonging to different
sections with different classification levels:

```turtle
@prefix bpo:  <http://bletchleypark.gov.uk/ontology/> .
@prefix bp:   <http://bletchleypark.gov.uk/data/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

# Sections
bp:Hut_3 a bpo:Section ;
    rdfs:label "Hut 3 - Army/Air Force Intelligence" .
bp:Hut_8 a bpo:Section ;
    rdfs:label "Hut 8 - Naval Enigma Cryptanalysis" .
bp:Directorate a bpo:Section ;
    rdfs:label "GC&CS Directorate" .

# Classification levels
bp:Secret a bpo:Classification .
bp:MostSecret a bpo:Classification .
bp:Ultra a bpo:Classification .

# A Secret report in Hut 3 — visible to Hut 3 analysts
bp:KurskReport a bpo:IntelligenceReport ;
    rdfs:label "Operation Citadel — Kursk signals analysis" ;
    bpo:section bp:Hut_3 ;
    bpo:classification bp:Secret .

# A Most Secret method in Hut 8 — visible only to Hut 8 cryptanalysts
bp:Banburismus a bpo:CryptanalyticMethod ;
    rdfs:label "Banburismus sequential analysis" ;
    bpo:section bp:Hut_8 ;
    bpo:classification bp:MostSecret .

# Ultra-classified material — only the Director can see this
bp:ColossusSpec a bpo:TechnicalDocument ;
    rdfs:label "Colossus Mark II specifications" ;
    bpo:section bp:Newmanry ;
    bpo:classification bp:Ultra .
```

Load the graph data:

```bash
tg-load-knowledge -i urn:doc:example graph-data.ttl
```

### Step 2: Write Policy Shapes

Policy shapes are Turtle files that define filtering rules. Each shape
is a `sh:NodeShape` with a SPARQL target and a SPARQL rule.

Here is a compartmentalisation policy that prevents cross-section
access to Secret and above material:

```turtle
@prefix tg-pol: <https://trustgraph.ai/ontology/policy/> .
@prefix tg-uc:  <https://trustgraph.ai/ontology/user-context/> .
@prefix sh:     <http://www.w3.org/ns/shacl#> .
@prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .
@prefix bpo:    <http://bletchleypark.gov.uk/ontology/> .
@prefix bp:     <http://bletchleypark.gov.uk/data/> .

# Prefix declarations for SPARQL queries within the policies
tg-pol:ExamplePrefixes
    sh:declare [
        sh:prefix "bpo" ;
        sh:namespace "http://bletchleypark.gov.uk/ontology/"^^xsd:anyURI ;
    ] , [
        sh:prefix "bp" ;
        sh:namespace "http://bletchleypark.gov.uk/data/"^^xsd:anyURI ;
    ] , [
        sh:prefix "tg-uc" ;
        sh:namespace "https://trustgraph.ai/ontology/user-context/"^^xsd:anyURI ;
    ] , [
        sh:prefix "tg-pol" ;
        sh:namespace "https://trustgraph.ai/ontology/policy/"^^xsd:anyURI ;
    ] .

# Policy: Section Compartmentalisation
#
# Prevents users from seeing Secret or above material
# belonging to sections they are not assigned to.
# Directorate staff are exempt (cross-section oversight).

tg-pol:CompartmentalisationPolicy a sh:NodeShape ;
    rdfs:label "Section compartmentalisation" ;
    rdfs:comment "Filters Secret+ material from outside user's section." ;
    sh:order 1 ;
    sh:target [
        a sh:SPARQLTarget ;
        sh:prefixes tg-pol:ExamplePrefixes ;
        sh:select """
            SELECT ?this
            WHERE {
                ?this bpo:section ?section .
                ?this bpo:classification ?class .
                FILTER (?class IN (bp:Secret, bp:MostSecret, bp:Ultra))

                ?ctx a tg-uc:UserContext .
                FILTER NOT EXISTS {
                    ?ctx tg-uc:organisationalUnit ?section .
                }
                FILTER NOT EXISTS {
                    ?ctx tg-uc:organisationalUnit bp:Directorate .
                }
            }
        """
    ] ;
    sh:rule [
        a sh:SPARQLRule ;
        sh:prefixes tg-pol:ExamplePrefixes ;
        sh:construct """
            CONSTRUCT {
                _:result a sh:ValidationResult ;
                    sh:focusNode $this ;
                    sh:sourceShape tg-pol:CompartmentalisationPolicy ;
                    sh:resultSeverity tg-pol:Filtered ;
                    sh:resultMessage "Data belongs to a section the user is not assigned to." ;
                    tg-pol:blocks true .
            }
            WHERE { }
        """ ;
        sh:order 1
    ] .
```

#### Anatomy of a Policy Shape

Every policy shape follows this structure:

| Part | Purpose |
|------|---------|
| `a sh:NodeShape` | Declares this as a SHACL node shape |
| `sh:order` | Priority (lower = evaluated first) |
| `sh:target` with `sh:SPARQLTarget` | SPARQL SELECT that identifies nodes to block |
| `sh:select` | The query: `?this` is the candidate node, `?ctx` is the user context |
| `sh:rule` with `sh:SPARQLRule` | CONSTRUCT that emits a `sh:ValidationResult` |
| `sh:resultSeverity` | `tg-pol:Filtered` (silent) or `tg-pol:Violation` (logged) |
| `tg-pol:blocks true` | Marks the node as blocked |
| `sh:prefixes` | Links to prefix declarations used in the SPARQL |

The SPARQL target query is the core of the policy. It receives:
- The knowledge graph triples (your data)
- The user context as RDF triples (injected at query time)

If the SELECT returns a node as `?this`, that node is blocked.

#### Layering Multiple Policies

You can define multiple policies with different priorities. For
example, a complete access control system might layer:

| Order | Policy | Severity | Purpose |
|-------|--------|----------|---------|
| 0 | Ultra security barrier | Violation | Hard security boundary for top-secret material |
| 1 | Section compartmentalisation | Filtered | Need-to-know between departments |
| 2 | Classification clearance | Filtered | Clearance-level checks |
| 3 | Methods/sources separation | Filtered | Analysts see product, not methods |

Lower `sh:order` values are evaluated first. A Violation-severity
policy at order 0 ensures that the most critical security boundaries
are enforced before softer filtering rules.

### Step 3: Load Policies

Policies must be loaded into the `urn:graph:policy` named graph. Use
`tg-load-knowledge` with the `--graph` flag:

```bash
tg-load-knowledge -i urn:doc:policies \
  policies.ttl \
  --graph urn:graph:policy
```

Once policies are loaded into this named graph, enforcement mode
activates automatically. From this point, all queries require a user
context in the JWT.

> **Important:** Loading policies is currently a CLI operation. There is
> no UI for policy management. To update policies, load a new version of
> the policy file — existing policy shapes with the same URIs are
> replaced.

### Step 4: Create User Context Tokens

Use `tg-mint-token` to create JWTs with user context claims. The
`--user-context` argument takes a JSON object describing the user's
identity for policy evaluation.

```bash
# An analyst in Hut 3 with Secret clearance
export TOK_ANALYST=$(tg-mint-token --username admin -w default \
  --user-context '{
    "user_id": "http://bletchleypark.gov.uk/data/usr_margaret",
    "roles": [],
    "organisational_units": [
      "http://bletchleypark.gov.uk/data/Hut_3"
    ],
    "assignments": [{
      "resource": "http://bletchleypark.gov.uk/data/Hut_3",
      "scope": "IntelligenceAnalysis",
      "status": "Active",
      "valid_from": "",
      "valid_to": "",
      "qualifiers": {
        "classification": "Secret"
      }
    }],
    "entitlements": [],
    "override_authorities": [],
    "delegation": null,
    "purpose": ""
  }')
```

```bash
# The Director with Ultra clearance and override authority
export TOK_DIRECTOR=$(tg-mint-token --username admin -w default \
  --user-context '{
    "user_id": "http://bletchleypark.gov.uk/data/usr_travis",
    "roles": [],
    "organisational_units": [
      "http://bletchleypark.gov.uk/data/Directorate"
    ],
    "assignments": [{
      "resource": "http://bletchleypark.gov.uk/data/GC_CS",
      "scope": "DirectorOversight",
      "status": "Active",
      "valid_from": "",
      "valid_to": "",
      "qualifiers": {
        "classification": "Ultra"
      }
    }],
    "entitlements": [],
    "override_authorities": [{
      "policy_area": "UltraDissemination",
      "condition": ""
    }],
    "delegation": null,
    "purpose": ""
  }')
```

The minted token is printed to stdout. Store it in an environment
variable for use with query commands.

#### User Context Fields

| Field | Type | Purpose |
|-------|------|---------|
| `user_id` | string | URI identifying the user |
| `roles` | array | Role URIs the user holds |
| `organisational_units` | array | Section/department URIs the user belongs to |
| `assignments` | array | Resource assignments with scope and qualifiers |
| `entitlements` | array | Specific entitlements granted to the user |
| `override_authorities` | array | Policy areas where the user has override rights |
| `delegation` | object or null | Delegated authority from another user |
| `purpose` | string | The purpose of the current session |

The `qualifiers` object within an assignment carries arbitrary
key-value pairs that your policies can match against. A common pattern
is `"classification": "Secret"` for clearance levels.

### Step 5: Query with Policy Filtering

Pass the minted token using the `-t` flag on any query command. The
policy engine evaluates every result node against the loaded policies
using the token's user context.

#### SPARQL Queries

```bash
# The analyst sees only Hut 3 material
tg-invoke-sparql-query -t "$TOK_ANALYST" -q '
  SELECT ?report ?label WHERE {
    ?report a <http://bletchleypark.gov.uk/ontology/IntelligenceReport> .
    ?report <http://www.w3.org/2000/01/rdf-schema#label> ?label .
  }'

# The Director sees all material across all sections
tg-invoke-sparql-query -t "$TOK_DIRECTOR" -q '
  SELECT ?report ?label WHERE {
    ?report a <http://bletchleypark.gov.uk/ontology/IntelligenceReport> .
    ?report <http://www.w3.org/2000/01/rdf-schema#label> ?label .
  }'
```

#### Graph RAG Queries

Policy filtering also applies to RAG queries. The same token
controls what context the LLM receives:

```bash
# The analyst's answer is limited to Hut 3 intelligence
tg-invoke-graph-rag -t "$TOK_ANALYST" \
  -q "What intelligence was gathered about Kursk?"

# The Director gets a comprehensive answer across all sections
tg-invoke-graph-rag -t "$TOK_DIRECTOR" \
  -q "What intelligence was gathered about Kursk?"
```

#### Enforcement Mode — No Token

If you query without a user context while policies are active, the
request is rejected:

```bash
# This fails with a policy-enforcement-error
tg-invoke-sparql-query -t "$TRUSTGRAPH_TOKEN" -q '
  SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10'
```

### Step 6: Verify Your Policies

Test each policy systematically by querying for data that should be
visible, filtered, and violation-blocked for each user role:

| Test | User | Expected | What It Verifies |
|------|------|----------|------------------|
| Query own section's reports | Analyst | Results returned | Allowed access works |
| Query another section's reports | Analyst | Empty results | Compartmentalisation filtering |
| Query Ultra material | Analyst | Empty results | Ultra barrier (Violation) |
| Query all sections | Director | All results | Override authority works |
| Query without user context | Admin token | Error | Enforcement mode active |

## Writing Effective Policies

### Keep Targets Precise

The SPARQL target runs against every candidate node. Broad targets
that match many nodes slow down queries. Use specific type checks and
property filters:

```sparql
# Good: targets only nodes with a specific classification
?this bpo:classification bp:MostSecret .

# Avoid: targets all nodes then filters in the rule
?this ?p ?o .
```

### Use Exemptions Carefully

Exemptions (FILTER NOT EXISTS clauses that allow access) should be
explicit. Common patterns:

- **Organisational exemption:** Directorate or management roles with
  cross-section oversight
- **Liaison exemption:** External users with specific section
  assignments
- **Override authority:** Named policy areas where specific users have
  bypass rights

### Test with Multiple Personas

Create user contexts for each distinct access pattern in your system.
The Bletchley Park test data demonstrates five personas covering:
analyst, cryptanalyst, machine operator, liaison officer, and
director. Each exercises a different combination of policies.

## Next Steps

- **[Managing Users and Workspaces](../managing-users/)** — Set up
  IAM users and workspaces
- **[`tg-load-knowledge`](../../reference/cli/tg-load-knowledge)** — CLI
  reference for loading triples
- **[`tg-mint-token`](../../reference/cli/tg-mint-token)** — CLI
  reference for minting user context tokens
- **[`tg-invoke-sparql-query`](../../reference/cli/tg-invoke-sparql-query)** — CLI
  reference for SPARQL queries
