---
title: Document RAG using CLI
nav_order: 4
parent: Advanced knowledge management
grand_parent: How-to Guides
review_date: 2026-08-01
guide_category:
  - Advanced knowledge management
guide_category_order: 3
guide_description: Use command-line tools to build Document RAG workflows
guide_difficulty: beginner
guide_time: 15 min
guide_emoji: 📄
guide_banner: banner.jpg
guide_labels:
  - RAG
  - Vector Search
  - Embeddings
  - CLI
---

# Document RAG Using CLI

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>TrustGraph deployed (<a href="../getting-started/quickstart">Quick Start</a>)</li>
<li>Familiarity with Document RAG concepts</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Use CLI tools to load documents, create Document RAG flows, and query using vector similarity search."
%}

This guide covers the same Document RAG workflow as the [Document RAG guide](../document-rag/), but using command-line tools instead of the Workbench.

**New to Document RAG?** Read the [Document RAG guide](../document-rag/) first to understand the concepts and limitations.

This guide demonstrates:
- Loading documents via CLI
- Creating Document RAG flows
- Querying with vector search

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

### Step 2: Create a Collection

Create an 'intelligence' collection:

```bash
tg-set-collection -n Intelligence -d 'Intelligence analysis' intelligence
```

### Step 3: Create the Flow

Create a Document RAG flow:

```bash
tg-start-flow -n document-rag -i doc-rag -d "Document RAG"
```

### Step 4: Submit the Document for Processing

Submit the document for processing:

```bash
tg-start-library-processing \
    --flow-id doc-rag \
    --document-id https://trustgraph.ai/doc/phantom-cargo \
    --collection intelligence \
    --processing-id urn:processing-01
```

### Step 5: Monitoring (Optional)

Processing is fast for Document RAG. For monitoring details, see the [Document RAG guide monitoring section](../document-rag/#step-5-monitoring).

### Step 6: Query with Document RAG

Query using vector similarity search:

```bash
tg-invoke-document-rag \
    -f doc-rag -C intelligence \
    -q 'What is the PHANTOM CARGO report about?'
```

Expected output:

```
The PHANTOM CARGO report is about an operation that detected unusual shipping
patterns involving a Dubai-based freight company, Meridian Logistics LLC...
```

## Next Steps

### Related CLI Commands

- [`tg-add-library-document`](../../reference/cli/tg-add-library-document) - Add documents to library
- [`tg-set-collection`](../../reference/cli/tg-set-collection) - Create collections
- [`tg-start-flow`](../../reference/cli/tg-start-flow) - Start processing flows
- [`tg-invoke-document-rag`](../../reference/cli/tg-invoke-document-rag) - Query with Document RAG

### Other Guides

- **[Document RAG (Workbench)](../document-rag/)** - Full walkthrough with concepts and limitations
- **[Graph RAG](../graph-rag/)** - Leverage knowledge graph relationships
- **[Ontology RAG](../ontology-rag/)** - Use structured schemas for extraction
- **[Troubleshooting](../../deployment/troubleshooting)** - Common issues
