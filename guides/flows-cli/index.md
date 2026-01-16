---
title: Managing Flows using CLI
parent: Advanced knowledge management
grand_parent: How-to Guides
nav_order: 5
review_date: 2026-06-01
guide_category:
  - Advanced knowledge management
guide_category_order: 5
guide_description: Use command-line tools to create, manage, and configure processing flows
guide_difficulty: intermediate
guide_banner: banner.jpg
guide_time: 10 min
guide_emoji: 🔄
guide_labels:
  - Flows
  - Pipelines
  - Processing
  - CLI
---

# Managing Flows Using CLI

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>TrustGraph instance running</li>
<li>Familiarity with flow concepts</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Use CLI tools to list, create, start, and stop processing flows for different use cases."
%}

This guide covers flow management using command-line tools instead of the Workbench.

**New to flows?** Read the [Introduction to Flows guide](../flows/) first to understand what flows are, how they work, and the concept of flow blueprints.

This guide demonstrates:
- Listing available flows and blueprints
- Creating flows from blueprints
- Starting and stopping flows
- Viewing flow configuration

## Step-by-Step Guide

### Step 1: View Available Flow Blueprints

Before creating a flow, see what blueprints are available:

```bash
tg-show-flow-blueprints
```

Output shows available flow blueprints:

```
+-------------+-----------------------------------------------------------------------------------------------------------+
| name        | everything                                                                                                |
| description | GraphRAG, DocumentRAG, structured data + knowledge cores                                                  |
| tags        | document-rag, graph-rag, knowledge-extraction, structured-data, kgcore                                    |
| parameters  | llm-model: LLM model [llm-model (default: gemini-2.5-flash-lite)]                                         |
|             |   llm-rag-model: LLM model for RAG [llm-model (default: gemini-2.5-flash-lite)]                           |
|             |   llm-temperature: LLM temperature [llm-temperature (default: 0.3)]                                       |
|             |   llm-rag-temperature: LLM temperature for RAG [llm-temperature (default: 0.3)]                           |
|             |   embeddings-model: Embeddings model [embeddings-model (default: sentence-transformers/all-MiniLM-L6-v2)] |
|             |   chunk-size: Chunk size [chunk-size (default: 2000)]                                                     |
|             |   chunk-overlap: Chunk overlap [chunk-overlap (default: 50)]                                              |
+-------------+-----------------------------------------------------------------------------------------------------------+

+-------------+-----------------------------------------------------------------------------------------------------------+
| name        | graph-rag                                                                                                 |
| description | GraphRAG only                                                                                             |
| tags        | graph-rag, knowledge-extraction                                                                           |
| parameters  | llm-model: LLM model [llm-model (default: gemini-2.5-flash-lite)]                                         |
|             |   llm-rag-model: LLM model for RAG [llm-model (default: gemini-2.5-flash-lite)]                           |
|             |   llm-temperature: LLM temperature [llm-temperature (default: 0.3)]                                       |
|             |   llm-rag-temperature: LLM temperature for RAG [llm-temperature (default: 0.3)]                           |
|             |   embeddings-model: Embeddings model [embeddings-model (default: sentence-transformers/all-MiniLM-L6-v2)] |
|             |   chunk-size: Chunk size [chunk-size (default: 2000)]                                                     |
|             |   chunk-overlap: Chunk overlap [chunk-overlap (default: 50)]                                              |
+-------------+-----------------------------------------------------------------------------------------------------------+
```

Each blueprint defines a different processing pipeline. Choose the one that matches your use case e.g.:
- **document-rag** - Vector similarity search only
- **graph-rag** - Knowledge graph extraction
- **ontology-rag** - Schema-based extraction
- **document-rag+graph-rag+kgcore** - Comprehensive processing with core creation
- **everything** - All capabilities enabled

### Step 2: View Existing Flows

List all configured flows:

```bash
tg-show-flows
```

Output:

```
+------------+----------------------------------------------------------------------+
| id         | default                                                              |
| blueprint  | everything                                                           |
| desc       | Default processing flow                                              |
| parameters | • LLM model: Gemini 2.5 Flash Lite                                   |
|            | • LLM model for RAG: Gemini 2.5 Flash Lite (controlled by llm-model) |
|            | • LLM temperature: 0.300                                             |
|            | • LLM temperature for RAG: 0.300                                     |
|            | • Embeddings model: all-MiniLM-L6-v2                                 |
|            | • Chunk size: 2000                                                   |
|            | • Chunk overlap: 50                                                  |
| queue      | document-load: persistent://tg/flow/document-load:default            |
|            | text-load: persistent://tg/flow/text-document-load:default           |
+------------+----------------------------------------------------------------------+
```

TrustGraph starts with a single "default" flow based on the "everything" blueprint.

### Step 3: Create a New Flow

Create a specialized flow from a blueprint:

```bash
tg-start-flow \
  -n graph-rag \
  -i my-graph-rag \
  -d "Graph RAG processing"
```

Parameters:
- `-n` - Blueprint name to use
- `-i` - Unique ID for the new flow
- `-d` - Description

You can also customize flow parameters when creating it using parameters
which can be seen in the flow blueprint using `tg-show-flow-blueprints`.

```bash
tg-start-flow \
  -n graph-rag \
  -i my-graph-rag \
  -d "Graph RAG processing" \
  --param llm-temperature=0.4 \
  --param llm-model=gemini-2.5-flash
```

This creates a flow with custom settings:
- `llm-temperature=0.4` - Sets the LLM temperature for more focused responses
- `llm-model=gemini-2.5-flash` - Specifies which LLM model to use

To discover all available parameters:

```bash
tg-show-parameter-types
```

This displays all configurable parameters including:
- LLM model settings (`llm-model`, `llm-temperature`)
- Chunking configuration (`chunk-size`, `chunk-overlap`)
- Embedding settings (`embeddings-model`)
- Graph traversal parameters
- And more

```
(env) [try]$ tg-show-parameter-types 
+-------------+---------------+
| name        | chunk-overlap |
| description | Chunk overlap |
| type        | integer       |
| default     | 50            |
| constraints | required      |
+-------------+---------------+

+--------------+--------------------------------------------------------------------+
| name         | llm-model                                                          |
| description  | LLM model to use                                                   |
| type         | string                                                             |
| default      | gemini-2.5-flash-lite                                              |
| valid values | • gemini-2.5-pro (Gemini 2.5 Pro)                                  |
|              | • gemini-2.5-flash (Gemini 2.5 Flash)                              |
|              | • gemini-2.5-flash-lite (Gemini 2.5 Flash Lite)                    |
|              | • gemini-2.0-flash-exp (Gemini 2.0 Flash (experimental))           |
|              | • claude-3-5-sonnet@20241022 (Claude 3.5 Sonnet (via VertexAI))    |
|              | • claude-3-5-haiku@20241022 (Claude 3.5 Haiku (via VertexAI))      |
|              | • claude-3-opus@20240229 (Claude 3 Opus (via VertexAI))            |
|              | • claude-3-sonnet@20240229 (Claude 3 Sonnet (via VertexAI))        |
|              | • claude-3-haiku@20240307 (Claude 3 Haiku (via VertexAI))          |
|              | • llama3-405b-instruct-maas (Llama 3 405B Instruct (via VertexAI)) |
|              | • llama3-70b-instruct-maas (Llama 3 70B Instruct (via VertexAI))   |
|              | • llama3-8b-instruct-maas (Llama 3 8B Instruct (via VertexAI))     |
| constraints  | required                                                           |
+--------------+--------------------------------------------------------------------+
```

### Step 4: Verify the New Flow

List flows again to see your new flow:

```bash
tg-show-flows
```

Output:

```
+------------+----------------------------------------------------------------------+
| id         | default                                                              |
| blueprint  | everything                                                           |
| desc       | Default processing flow                                              |
| parameters | • LLM model: Gemini 2.5 Flash Lite                                   |
|            | • LLM model for RAG: Gemini 2.5 Flash Lite (controlled by llm-model) |
|            | • LLM temperature: 0.300                                             |
|            | • LLM temperature for RAG: 0.300                                     |
|            | • Embeddings model: all-MiniLM-L6-v2                                 |
|            | • Chunk size: 2000                                                   |
|            | • Chunk overlap: 50                                                  |
| queue      | document-load: persistent://tg/flow/document-load:default            |
|            | text-load: persistent://tg/flow/text-document-load:default           |
+------------+----------------------------------------------------------------------+

+------------+----------------------------------------------------------------------+
| id         | my-graph-rag                                                         |
| blueprint  | graph-rag                                                            |
| desc       | Graph RAG processing                                                 |
| parameters | • LLM model: Gemini 2.5 Flash                                        |
|            | • LLM model for RAG: Gemini 2.5 Flash Lite (controlled by llm-model) |
|            | • LLM temperature: 0.4                                               |
|            | • LLM temperature for RAG: 0.3                                       |
|            | • Embeddings model: all-MiniLM-L6-v2                                 |
|            | • Chunk size: 2000                                                   |
|            | • Chunk overlap: 50                                                  |
| queue      | document-load: persistent://tg/flow/document-load:my-graph-rag       |
|            | text-load: persistent://tg/flow/text-document-load:my-graph-rag      |
+------------+----------------------------------------------------------------------+

```

### Step 5: Using the Flow

Now that the flow exists, you can use it when processing documents. Specify the flow ID when submitting documents for processing:

```bash
tg-start-library-processing \
  --flow-id my-graph-rag \
  --document-id https://trustgraph.ai/doc/my-document \
  --collection my-collection \
  --processing-id urn:processing-01
```

The document will be processed using your custom flow with the parameters you specified (e.g., the custom LLM model and temperature settings).

### Step 6: Stop a Flow

If you need to deactivate a flow:

```bash
tg-stop-flow -i my-graph-rag
```

Output:

```
Flow 'my-graph-rag' stopped
```

**Note:** Stopping a flow prevents new documents from being processed by it, but doesn't delete the flow configuration.

### Step 7: Get Flow Blueprint

View details of a specific flow blueprint:

```bash
tg-get-flow-blueprint -n graph-rag
```

This dumps out the flow blueprint in JSON form.

Output:

```
Flow 'my-graph-rag' stopped
```

**Note:** Stopping a flow prevents new documents from being processed by it, but doesn't delete the flow configuration.

## Next Steps

### Related CLI Commands

- [`tg-show-flows`](../../reference/cli/tg-show-flows) - List all flows
- [`tg-show-flow-blueprints`](../../reference/cli/tg-show-flow-blueprints) - List available flow blueprints
- [`tg-start-flow`](../../reference/cli/tg-start-flow) - Create and start a flow
- [`tg-stop-flow`](../../reference/cli/tg-stop-flow) - Stop a running flow
- [`tg-get-flow-blueprint`](../../reference/cli/tg-get-flow-blueprint) - View flow configuration
- [`tg-put-flow-blueprint`](../../reference/cli/tg-put-flow-blueprint) - Create or update a flow blueprint
- [`tg-delete-flow-blueprint`](../../reference/cli/tg-delete-flow-blueprint) - Delete a flow blueprint

### Other Guides

- **[Introduction to Flows (Workbench)](../flows/)** - Visual walkthrough with detailed explanations
- **[Graph RAG CLI](../graph-rag-cli/)** - Use flows for knowledge graph extraction
- **[Document RAG CLI](../document-rag-cli/)** - Use flows for vector search
- **[Ontology RAG CLI](../ontology-rag-cli/)** - Use flows for schema-based extraction
