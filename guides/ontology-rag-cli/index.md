---
title: Ontology RAG using CLI
nav_order: 3
parent: Advanced knowledge management
grand_parent: How-to Guides
review_date: 2026-08-01
guide_category:
  - Advanced knowledge management
guide_category_order: 2
guide_description: Use command-line tools to build Ontology RAG workflows with custom schemas
guide_difficulty: advanced
guide_time: 30 min
guide_emoji: 📋
guide_banner: banner.jpg
guide_labels:
  - RAG
  - Ontology
  - Schema
  - CLI
---

# Ontology RAG Using CLI

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>TrustGraph deployed (<a href="../getting-started/quickstart">Quick Start</a>)</li>
<li>Familiarity with Ontology RAG concepts and OWL ontologies</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Use CLI tools to import ontologies, extract structured knowledge, and query ontology-based knowledge graphs."
%}

This guide covers the same Ontology RAG workflow as the [Ontology RAG guide](../ontology-rag/), but using command-line tools instead of the Workbench.

**New to Ontology RAG?** Read the [Ontology RAG guide](../ontology-rag/) first to understand the concepts, workflow, and see visual examples.

This guide demonstrates:
- Loading ontologies via CLI
- Creating ontology-based flows
- Processing documents with schema-guided extraction
- Querying with Ontology RAG

## Step-by-Step Guide

### Step 1: Load Your Document

Download and load the example document:

```bash
wget -O phantom-cargo.md https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/tracking/operation-phantom-cargo.md

tg-add-library-document \
  --name "PHANTOM CARGO" \
  --description "Intelligence report: Operation PHANTOM CARGO" \
  --tags 'maritime,intelligence,cargo,grey arms' \
  --id https://trustgraph.ai/doc/phantom-cargo \
  --kind text/plain \
  phantom-cargo.md
```

### Step 2: Load the Ontology

We'll use the SSN/SOSA ontology (W3C standard for sensors and observations). For details about this ontology, see the [Ontology RAG guide](../ontology-rag/#step-2-load-the-ontology).

Download and install the ontology:

```bash
wget -O ssn-ontology.json https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/tracking/ssn-ontology.json

cat ssn-ontology.json | tg-put-config-item --type ontology --key ssn --stdin
```

### Step 3: Create a Collection

Create an 'intelligence' collection:

```bash
tg-set-collection -n Intelligence -d 'Intelligence analysis' intelligence
```

### Step 4: Create the Flow

Create an Ontology RAG flow:

```bash
tg-start-flow -n onto-rag -i onto-rag -d "Ontology RAG"
```

### Step 5: Submit the Document for Processing

Submit the document for processing:

```bash
tg-start-library-processing \
    --flow-id onto-rag \
    --document-id https://trustgraph.ai/doc/phantom-cargo \
    --collection intelligence \
    --processing-id urn:processing-03
```

### Step 6: Monitoring (Optional)

Processing can take time for large documents. For monitoring details, see the [Ontology RAG guide monitoring section](../ontology-rag/#step-6-monitoring).

### Step 7: Query with Ontology RAG

Query the ontology-based knowledge graph:

```bash
tg-invoke-graph-rag \
    -f onto-rag -C intelligence \
    -q 'What intelligence resources were using during the PHANTOM CARGO operation?'
```

Expected output:

```
The intelligence resources used during the PHANTOM CARGO operation were:
* SIGINT
* MASINT
* Electro-Optical HUMINT
* FININT
* AIS
* synthetic aperture radar (SAR)
* GPS coordinates
```

**Explore visually**: For graph exploration and ontology visualization, see the visual tools in the [Ontology RAG guide](../ontology-rag/#step-8-explore-the-knowledge-graph).

## Next Steps

### Related CLI Commands

- [`tg-put-config-item`](../../reference/cli/tg-put-config-item) - Load ontologies and configuration
- [`tg-start-flow`](../../reference/cli/tg-start-flow) - Start processing flows
- [`tg-invoke-graph-rag`](../../reference/cli/tg-invoke-graph-rag) - Query with Ontology RAG

### Other Guides

- **[Ontology RAG (Workbench)](../ontology-rag/)** - Visual walkthrough with ontology editor
- **[Graph RAG](../graph-rag/)** - Schema-free knowledge extraction
- **[Working with Context Cores](../context-cores/)** - Package and share knowledge
