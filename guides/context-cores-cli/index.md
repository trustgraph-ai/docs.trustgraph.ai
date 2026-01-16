---
title: Working with Context Cores using CLI
parent: Advanced knowledge management
grand_parent: How-to Guides
nav_order: 5
review_date: 2026-06-01
guide_category:
  - Advanced knowledge management
guide_category_order: 4
guide_description: Use command-line tools to create, download, upload, and load knowledge cores
guide_difficulty: advanced
guide_banner: banner.jpg
guide_time: 15 min
guide_emoji: 🤖
guide_labels:
  - Knowledge Cores
  - Context Management
  - CLI
---

# Working with Context Cores Using CLI

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>TrustGraph instance running</li>
<li>Familiarity with knowledge cores concepts</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Use CLI tools to create, download, upload, and load knowledge cores for sharing and managing extracted knowledge."
%}

This guide covers the same knowledge core workflow as the [Working with Context Cores guide](../context-cores/), but using command-line tools instead of the Workbench.

**New to knowledge cores?** Read the [Working with Context Cores guide](../context-cores/) first to understand what cores are and their lifecycle (offline → online → loaded).

This guide demonstrates:
- Creating flows with core extraction enabled
- Downloading cores via CLI
- Uploading cores to other instances
- Loading cores into retrieval stores

## Step-by-Step Guide

### Step 1: Load Your Document

Download and load the example document:

```bash
wget -O README.cats https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/cats/README.cats

tg-add-library-document \
  --name "README.cats" \
  --description "Brief description of cats" \
  --tags cats,animals \
  --id https://trustgraph.ai/doc/readme-cats \
  --kind text/plain \
  README.cats
```

### Step 2: Create a Collection

Create a collection:

```bash
tg-set-collection -n Cats -d 'Cat information' cats
```

### Step 3: Create the Flow

Create a flow with the `kg-store` processor for core creation:

```bash
tg-start-flow -n document-rag+graph-rag+kgcore -i core-building -d "Core building"
```

### Step 4: Submit the Document for Processing

Submit the document for processing:

```bash
tg-start-library-processing \
    --flow-id core-building \
    --document-id https://trustgraph.ai/doc/readme-cats \
    --collection cats \
    --processing-id urn:processing-03
```

### Step 5: Monitoring (Optional)

Processing can take time. For monitoring details, see the [Working with Context Cores guide monitoring section](../context-cores/#step-5-monitoring).

### Step 6: View the Knowledge Core

List available cores:

```bash
tg-show-kg-cores
```

Output:

```
https://trustgraph.ai/doc/readme-cats
```

### Step 7: Download the Knowledge Core

Download the core as a file:

```bash
tg-get-kg-core \
  --id https://trustgraph.ai/doc/readme-cats \
  --output readme-cats.core
```

Output:

```
Got: 2 triple, 1 GE messages.
```

Verify the download:

```bash
ls -lh readme-cats.core
```

### Step 8: Upload the Knowledge Core

Upload the core to another TrustGraph instance (or the same one with a different ID):

```bash
tg-put-kg-core \
  --id https://trustgraph.ai/doc/cats-copy \
  --input readme-cats.core
```

Output:

```
Put: 2 triple, 1 GE messages.
```

### Step 9: Load the Knowledge Core for Retrieval

Create a new collection and load the core into it:

```bash
tg-set-collection \
  -n "Cats Copy" \
  -d "Loaded from knowledge core" \
  cats-copy

tg-load-kg-core \
  --id https://trustgraph.ai/doc/cats-copy \
  --collection cats-copy
```

The command will report progress as it loads the core:

```
Loading core into retrieval stores...
Loaded: 2 triple batches, 1 GE batches.
```

Verify the core is loaded by performing a GraphRAG query:

```bash
tg-invoke-graph-rag \
  -q "What do you know about cats?" \
  -C cats-copy
```

You should receive a response based on the knowledge extracted from the README.cats document.

**Note:** The core is now "loaded" - the knowledge is available in retrieval stores and can be queried using GraphRAG operations.

## Next Steps

### Related CLI Commands

- [`tg-show-kg-cores`](../../reference/cli/tg-show-kg-cores) - List all knowledge cores
- [`tg-get-kg-core`](../../reference/cli/tg-get-kg-core) - Download a knowledge core
- [`tg-put-kg-core`](../../reference/cli/tg-put-kg-core) - Upload a knowledge core
- [`tg-load-kg-core`](../../reference/cli/tg-load-kg-core) - Load a core into retrieval stores

### Other Guides

- **[Working with Context Cores (Workbench)](../context-cores/)** - Visual walkthrough with detailed explanations
- **[Graph RAG](../graph-rag/)** - Build knowledge graphs from documents
- **[Ontology RAG](../ontology-rag/)** - Use structured schemas for extraction



