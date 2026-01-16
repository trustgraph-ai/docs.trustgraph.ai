---
title: Graph RAG using CLI
nav_order: 2
parent: Advanced knowledge management
grand_parent: How-to Guides
review_date: 2026-08-01
guide_category:
  - Advanced knowledge management
guide_category_order: 1
guide_description: Use command-line tools to build Graph RAG workflows
guide_difficulty: intermediate
guide_time: 20 min
guide_emoji: 🕸️
guide_banner: banner.jpg
guide_labels:
  - RAG
  - Knowledge Graph
  - CLI
---

# Graph RAG Using CLI

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>TrustGraph deployed (<a href="../getting-started/quickstart">Quick Start</a>)</li>
<li>Familiarity with Graph RAG concepts</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Use CLI tools to load documents, create Graph RAG flows, and query knowledge graphs."
%}

This guide covers the same Graph RAG workflow as the [Graph RAG guide](../graph-rag/), but using command-line tools instead of the Workbench.

**New to Graph RAG?** Read the [Graph RAG guide](../graph-rag/) first to understand the concepts, workflow, and see visual examples of the knowledge graph in action.

This guide demonstrates:
- Loading documents via CLI
- Creating collections and flows
- Submitting documents for processing
- Querying with Graph RAG
- Monitoring processing

## Step-by-Step Guide

### Step 1: Load Your Document

Download the example document:
```
wget -O phantom-cargo.md https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/tracking/operation-phantom-cargo.md
```

Load it into the TrustGraph library:

```
tg-add-library-document \
  --name "PHANTOM CARGO" \
  --description "Intelligence report: Operation PHANTOM CARGO" \
  --tags 'maritime,intelligence,cargo,grey arms' \
  --id https://trustgraph.ai/doc/phantom-cargo \
  --kind text/plain \
  phantom-cargo.md
```

Verify the document was added:

```bash
tg-show-library-documents
```

### Step 2: Create a Collection

Create an 'intelligence' collection:

```bash
tg-set-collection -n Intelligence -d 'Intelligence analysis' intelligence
```

### Step 3: Create the Flow

Create a Graph RAG flow:

```bash
tg-start-flow -n graph-rag -i graph-rag -d "Graph RAG"
```

### Step 4: Submit the Document for Processing

Submit the document for processing:

```bash
tg-start-library-processing \
    --flow-id graph-rag \
    --document-id https://trustgraph.ai/doc/phantom-cargo \
    --collection intelligence \
    --processing-id urn:processing-02
```

### Step 5: Monitoring (Optional)

Processing can take time for large documents. For details on monitoring flows using Grafana, see the [Graph RAG guide monitoring section](../graph-rag/#step-5-monitoring).

### Step 6: Query with Graph RAG

Query the knowledge graph:

```bash
tg-invoke-graph-rag \
    -f graph-rag -C intelligence \
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

**Explore visually**: For graph exploration, vector search, and 3D visualization, see the visual tools in the [Graph RAG guide](../graph-rag/#step-7-explore-the-knowledge-graph).

## Next Steps

### Related CLI Commands

- [`tg-add-library-document`](../../reference/cli/tg-add-library-document) - Add documents to library
- [`tg-set-collection`](../../reference/cli/tg-set-collection) - Create collections
- [`tg-start-flow`](../../reference/cli/tg-start-flow) - Start processing flows
- [`tg-invoke-graph-rag`](../../reference/cli/tg-invoke-graph-rag) - Query with Graph RAG

### Other Guides

- **[Graph RAG (Workbench)](../graph-rag/)** - Visual walkthrough with graph exploration
- **[Ontology RAG](../ontology-rag/)** - Use structured schemas for extraction
- **[Working with Context Cores](../context-cores/)** - Package and share knowledge
