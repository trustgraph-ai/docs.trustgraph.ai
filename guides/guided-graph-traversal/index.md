---
title: Guided Graph Traversal
nav_order: 4
parent: Advanced knowledge management
review_date: 2026-11-01
guide_category:
  - Advanced knowledge management
guide_category_order: 4
guide_description: Steer Graph RAG retrieval with seed entities, language filters, and per-hop traversal instructions for precise, focused answers
guide_difficulty: advanced
guide_time: 30 min
guide_emoji: "\U0001F9ED"
guide_banner: banner.jpg
guide_labels:
  - Graph RAG
  - Traversal
  - Seeds
  - Language Filtering
  - CLI
---

# Guided Graph Traversal

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>A running TrustGraph deployment (v2.10 or later)</li>
<li>TrustGraph CLI tools installed</li>
<li>A knowledge graph with loaded data</li>
<li>Familiarity with <a href="../graph-rag/">Graph RAG</a> concepts</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Use grounding seeds, graph seeds, language filters, and traversal instructions to control how Graph RAG explores the knowledge graph."
%}

**Take control of how Graph RAG finds and follows knowledge**

> **New in TrustGraph v2.10.** Guided traversal parameters are not
> available in v2.9 or earlier releases.

Standard Graph RAG works automatically: it extracts concepts from your
question, finds matching entities via embeddings, and traverses the
graph to build context for the LLM. This is effective for general
questions, but sometimes you need more control — to start from
specific entities, restrict traversal to certain relationship types,
or filter out irrelevant languages.

Guided graph traversal gives you four steering mechanisms that can be
used independently or combined:

| Parameter | What It Controls |
|-----------|-----------------|
| **Grounding seeds** | Which concepts to search for (bypasses LLM extraction) |
| **Graph seeds** | Which entities to start traversal from (bypasses embedding lookup) |
| **Language filters** | Which language-tagged literals to include |
| **Traversal instructions** | Which types and relationships to follow at each hop |

## How Graph RAG Traversal Works

Before diving into the steering parameters, it helps to understand the
standard retrieval pipeline:

1. **Grounding** — An LLM extracts key concepts from your question
2. **Entity lookup** — Concepts are embedded and matched against graph
   entity vectors
3. **Hop-and-filter** — Starting from matched entities, the engine
   traverses outward hop by hop, scoring edges with a cross-encoder
   reranker
4. **Synthesis** — The selected subgraph is passed to an LLM to
   generate an answer

Each steering parameter intercepts a different stage of this pipeline.

## Grounding Seeds

**Bypass LLM concept extraction with your own concepts.**

Normally, an LLM call extracts concepts from your question — e.g.
"What trade routes connected Venice to Constantinople?" might produce
concepts like `["Venice", "Constantinople", "trade routes"]`. This
works well but costs an LLM call and the model might miss or
misinterpret domain-specific terms.

Grounding seeds let you provide the concepts directly:

```bash
tg-invoke-graph-rag \
  -q "What trade routes connected Venice to Constantinople?" \
  --grounding-seeds '["Venice", "Constantinople", "trade routes", "maritime commerce"]'
```

The concepts are still embedded and matched against graph entities via
vector similarity — you're just controlling what gets searched for.

**When to use grounding seeds:**
- The LLM misinterprets domain-specific terminology
- You want to include concepts the LLM wouldn't extract
- You want to save the LLM grounding call for latency or cost reasons
- You're building a pipeline where concepts come from an upstream
  process

## Graph Seeds

**Start traversal from specific known entities.**

Graph seeds go further than grounding seeds: they bypass both the LLM
concept extraction *and* the embedding lookup. You provide entity IRIs
directly, and traversal starts from those nodes.

```bash
tg-invoke-graph-rag \
  -q "What are this person's key contributions?" \
  --graph-seeds '["http://example.org/person/Alan_Turing"]'
```

This is the most direct form of steering. You already know which
entity you care about — you just want Graph RAG to explore its
neighbourhood and synthesise an answer.

**When to use graph seeds:**
- You know the exact entity IRIs (e.g. from a prior query, a UI
  selection, or a structured lookup)
- You want to explore the neighbourhood of a specific entity
- You're building a drill-down workflow where the user selects an
  entity and asks a follow-up question

> **Note:** `--grounding-seeds` and `--graph-seeds` are mutually
> exclusive. Use one or the other, not both.

## Language Filters

**Restrict results to specific languages.**

Knowledge graphs often contain literals tagged with language codes
(e.g. `"Berlin"@en`, `"Berlin"@de`). Language filters tell the
traversal engine to only follow edges where literal values match
your specified language tags.

```bash
# Only follow English-tagged and untagged literals
tg-invoke-graph-rag \
  -q "What is the history of Berlin?" \
  --languages '["en", ""]'
```

The empty string `""` matches literals with no language tag, which is
common for URIs, numbers, and data that was loaded without language
annotations.

**When to use language filters:**
- Your knowledge graph contains multilingual data but the user works
  in one language
- You want to avoid mixing languages in the LLM synthesis context
- You need to reduce noise from irrelevant translations

## Traversal Instructions

**Control which types and relationships the traversal follows at each
hop.**

Traversal instructions are the most powerful steering mechanism. They
let you define per-hop restrictions on:

- **`types`** — restrict seed entities to specific RDF types (step 0
  only)
- **`relationships`** — only follow edges with specific predicates
- **`graphs`** — only query specific named graphs

Instructions are a JSON list where each element corresponds to a step:
- Step 0 applies a type filter to the seed entities
- Step 1 restricts the first hop
- Step 2 restricts the second hop
- And so on, up to `max-path-length`

### Example: Restrict to Person Entities and Employment Relationships

```bash
tg-invoke-graph-rag \
  -q "Where did the researchers work?" \
  --traversal-instructions '[
    {"types": ["http://example.org/ontology/Person"]},
    {"relationships": ["http://example.org/ontology/worksFor", "http://example.org/ontology/affiliatedWith"]}
  ]'
```

Step 0 filters the seed entities to only those typed as `Person`.
Step 1 restricts the first hop to only `worksFor` and
`affiliatedWith` edges. Any other relationship types are ignored
during that hop.

### Example: Multi-Hop with Different Restrictions

```bash
tg-invoke-graph-rag \
  -q "What projects are funded by this organisation?" \
  --graph-seeds '["http://example.org/org/DARPA"]' \
  --traversal-instructions '[
    {},
    {"relationships": ["http://example.org/ontology/funds"]},
    {"relationships": ["http://example.org/ontology/hasPI", "http://example.org/ontology/hasOutput"]}
  ]'
```

Step 0 is empty (no type filter on seeds — we provided a specific
entity). Step 1 follows only `funds` edges from DARPA to projects.
Step 2 follows `hasPI` and `hasOutput` edges from projects to
people and outputs.

### Example: Query a Specific Named Graph

```bash
tg-invoke-graph-rag \
  -q "What policies apply?" \
  --traversal-instructions '[
    {},
    {"graphs": ["urn:graph:policies"]}
  ]'
```

### Traversal Instruction Fields

Each step in the instructions list can include any combination of:

| Field | Type | Effect |
|-------|------|--------|
| `types` | list of IRIs | Filter entities to those with a matching `rdf:type` (step 0 only) |
| `relationships` | list of IRIs | Only follow edges with these predicates |
| `graphs` | list of IRIs | Only query these named graphs |

Omitting a field (or passing an empty list) means no restriction on
that dimension for that step.

## Combining Parameters

The four parameters work together. A common pattern is to combine
graph seeds with traversal instructions and language filters:

```bash
tg-invoke-graph-rag \
  -q "Summarise this project's outcomes" \
  --graph-seeds '["http://example.org/project/AlphaResearch"]' \
  --traversal-instructions '[
    {},
    {"relationships": ["http://example.org/ontology/hasOutcome", "http://example.org/ontology/produces"]},
    {"relationships": ["http://example.org/ontology/publishedIn", "http://example.org/ontology/citedBy"]}
  ]' \
  --languages '["en", ""]'
```

This starts from a known project, follows outcome and production
relationships for two hops, and only includes English-language
content.

## Other Tuning Parameters

Beyond the guided traversal parameters, `tg-invoke-graph-rag` also
exposes several tuning parameters that control the scope and precision
of the traversal:

| Parameter | Default | Purpose |
|-----------|---------|---------|
| `--entity-limit` | 50 | Max entities returned from embedding lookup |
| `--triple-limit` | 30 | Max triples queried per frontier entity per hop |
| `--max-subgraph-size` | 150 | Max total edges in the collected subgraph |
| `--max-path-length` | 2 | Number of traversal hops |
| `--edge-limit` | 25 | Max edges selected per hop by the cross-encoder |
| `--max-reranker-input` | 350 | Max candidate edges sent to the reranker per hop |

Increasing `--max-path-length` explores further from the seed
entities but adds latency. Increasing `--edge-limit` keeps more
context per hop but may dilute relevance. The defaults work well for
most cases — adjust when you need deeper traversal or broader context.

## Using Explainability to Debug

The `--explainable` flag (`-x`) shows the retrieval pipeline in
real time, which is invaluable for tuning guided traversal:

```bash
tg-invoke-graph-rag -x \
  -q "What trade routes connected Venice to Constantinople?" \
  --grounding-seeds '["Venice", "Constantinople", "trade routes"]'
```

This prints provenance events as they happen:
- **Grounding** — which concepts were used (your seeds or LLM-extracted)
- **Exploration** — which seed entities were found and how many edges
  were explored
- **Focus** — which edges the cross-encoder selected, with scores
- **Synthesis** — the final document passed to the LLM

Use this to verify that your seeds are resolving to the right
entities, that the traversal is following the paths you expect, and
that relevant edges are being scored highly.

## Next Steps

- **[Graph RAG](../graph-rag/)** — Standard Graph RAG guide
  (Workbench-based)
- **[Graph RAG CLI](../graph-rag-cli/)** — Graph RAG via the command
  line
- **[Explainability](../explainable-ai/)** — Understanding retrieval
  provenance
- **[`tg-invoke-graph-rag`](../../reference/cli/tg-invoke-graph-rag)** — Full
  CLI reference
