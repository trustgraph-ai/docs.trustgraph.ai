---
title: Command-line document management
nav_order: 2.3
parent: How-to Guides
grand_parent: TrustGraph Documentation
review_date: 2026-08-01
guide_category:
  - Building with TrustGraph
guide_category_order: 3
guide_description: Managing documents with command-line tools
guide_difficulty: beginner
guide_time: 20 min
guide_emoji: 📄
guide_banner: /../cli-docs.jpg
guide_labels:
  - CLI
  - Documents
  - Workflows
todo: true
todo_notes: This is just a placeholder.
---

# Document management with the command-line

## Command-line tools by category

### Flows

Flows are persistent processing workflows that run continuously, monitoring
queues and processing data as it arrives. Each flow is launched from a flow
class definition, which provides the blueprint for the flow.

**Discovering available flow classes:**

Use `tg-show-flow-classes` to see what flow classes are available:

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

Flow classes define different processing capabilities - choose the one that matches your needs.

**Managing flow instances:**
- `tg-show-flows` - List running flow instances
- `tg-show-flow-state -i <flow-id>` - View flow execution state and status
- `tg-start-flow -n <flow-class> -i <flow-id> -d <description>` - Start a flow instance from a flow class
- `tg-stop-flow -i <flow-id>` - Stop a running flow instance

Example output from `tg-show-flows`:
```
+------------+----------------------------------------------------------------------+
| id         | default                                                              |
| class      | everything                                                           |
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

Example - start a document processing flow:
```bash
tg-start-flow -n everything -i my-doc-flow -d "My document processing flow"
```

Example - start a flow with parameters:
```bash
tg-start-flow -n everything -i my-flow -d "Custom flow" \
  --param llm-model=gpt-4 --param temperature=0.7
```

Example - stop a running flow:
```bash
tg-stop-flow -i my-doc-flow
```

**Managing flow definitions:**

Flow class definitions are JSON configurations that specify the processing components, parameters, and queue routing for flows.

- `tg-get-flow-class -n <flow-class>` - Retrieve flow class configuration as JSON
- `tg-put-flow-class -n <flow-class> -c '<json>'` - Create or update a flow class definition
- `tg-delete-flow-class -n <flow-class>` - Remove a flow class definition

Example - export a flow class definition:
```bash
tg-get-flow-class -n everything > everything-flow.json
```

Example - create or update a flow class:
```bash
tg-put-flow-class -n my-custom-flow -c "$(cat my-flow-definition.json)"
```

Example - delete a flow class:
```bash
tg-delete-flow-class -n old-flow-class
```

### Document library

The document library provides organized storage for documents with metadata. Documents added to the library can be processed by library processing flows.

**Add a document:**

`tg-add-library-document` uploads a document with metadata to the library.

Required arguments:
- `-k, --kind` - Document MIME type (e.g., `text/plain`, `application/pdf`)
- `files` - Path to file(s) to upload

Optional metadata:
- `-U, --user` - User ID (default: `trustgraph`)
- `--name` - Document name
- `--description` - Document description
- `--identifier, --id` - Document identifier/URL
- `--keyword` - Keywords (space-separated)
- `--tags` - Tags (comma-separated)

Example:
```bash
tg-add-library-document -U trustgraph \
  --name "Mark's cats" \
  --description "A document about cats" \
  --keyword cats pets "domestic life" \
  --identifier "https://trustgraph.ai/docs/cats" \
  -k text/plain \
  --tags "cats,pets,domestic life" \
  ../sources/README.cats
```

**Remove a document:**

`tg-remove-library-document` removes a document from the library by its identifier.

```bash
tg-remove-library-document --identifier "https://trustgraph.ai/docs/cats"
```

**List documents:**

`tg-show-library-documents` displays all documents in the library.

```bash
tg-show-library-documents
```

Example output:
```
+-------+---------------------------------+
| id    | https://trustgraph.ai/docs/cats |
| time  | 2026-01-12 15:04:29             |
| title | Mark's cats                     |
| kind  | text/plain                      |
| note  | A document about cats           |
| tags  | cats, pets, domestic life       |
+-------+---------------------------------+
```

### Collections

Collections provide logical grouping for documents and knowledge graphs. Each user can have multiple collections to organize different projects or data domains.

**List collections:**

`tg-list-collections` displays all collections for a user.

```bash
tg-list-collections
```

Filter by tags:
```bash
tg-list-collections -t research -t experimental
```

Example output:
```
+------------+--------------------+--------------------+---------+
| Collection | Name               | Description        | Tags    |
+------------+--------------------+--------------------+---------+
| default    | Default Collection | Default collection | default |
+------------+--------------------+--------------------+---------+
```

**Create or update a collection:**

`tg-set-collection` creates a new collection or updates metadata for an existing one.

Example - create a new collection:
```bash
tg-set-collection my-research \
  -n "Research Documents" \
  -d "Documents for research project" \
  -t research -t academic
```

**Delete a collection:**

`tg-delete-collection` removes a collection and all its data.

```bash
tg-delete-collection my-research
```

Skip confirmation prompt:
```bash
tg-delete-collection my-research -y
```

### Document library processing

To process a document in TrustGraph, first add it to the library, then submit it for processing. Processing records track which documents have been submitted to flows for processing.

**Show processing status:**

`tg-show-library-processing` displays all active processing records.

```bash
tg-show-library-processing
```

**Start processing:**

`tg-start-library-processing` submits a library document for processing through a flow.

Required arguments:
- `-d, --document-id` - Document identifier (from library) - must be a URI
- `--id, --processing-id` - Processing record identifier - must be a URI

Note: Document IDs and processing IDs must be URIs (e.g., `https://trustgraph.ai/docs/cats`) because they are used as document entity identifiers in the knowledge graph.

Optional arguments:
- `-i, --flow-id` - Flow to use for processing (default: `default`)
- `--collection` - Collection name (default: `default`)
- `--tags` - Tags for processing (comma-separated)

Example - process the cats document:
```bash
tg-start-library-processing \
  -d "https://trustgraph.ai/docs/cats" \
  --id "cats-processing-2026-01" \
  -i default \
  --collection default
```

**Stop processing:**

`tg-stop-library-processing` removes a processing record. Note that this only removes the record - it does not stop in-flight processing (reserved for future functionality).

```bash
tg-stop-library-processing --id "cats-processing-2026-01"
```

### Querying and retrieval

TrustGraph provides multiple ways to query and retrieve information using LLMs and RAG techniques.

**Invoke LLM directly:**

`tg-invoke-llm` sends a direct request to the LLM with system and user prompts.

```bash
tg-invoke-llm "You are a helpful assistant" "What is 2+2?"
```

Output:
```
2 + 2 = 4
```

**Execute a prompt template:**

`tg-invoke-prompt` uses predefined prompt templates with variable substitution.

```bash
tg-invoke-prompt question question="What is a fish?"
```

Template variables replace `{{key}}` placeholders in the prompt template.

**Query using Graph RAG:**

`tg-invoke-graph-rag` retrieves relevant knowledge graph entities and relationships to answer questions.

```bash
tg-invoke-graph-rag -q "Tell me what the document says about cats?"
```

Example output:
```
The document states that cats have the species name Felis catus. They are
also referred to as domestic cats or house cats. Cats are small domesticated
carnivorous mammals.
```

Optional arguments:
- `-e, --entity-limit` - Maximum entities to retrieve (default: 50)
- `--triple-limit` - Maximum triples to retrieve (default: 30)
- `-s, --max-subgraph-size` - Maximum subgraph size (default: 150)
- `-p, --max-path-length` - Maximum path length (default: 2)

**Invoke an agent:**

`tg-invoke-agent` uses an agentic system that can reason and use tools to answer questions.

```bash
tg-invoke-agent -v -q "Research and summarize the key findings"
```

Optional arguments:
- `-l, --plan` - Agent plan
- `-s, --state` - Agent initial state
- `-g, --group` - Tool groups available to agent
- `-v, --verbose` - Show agent thinking and observations

Example verbose output:

```
❓ What is the latin name for a cat?

🤔  The user is asking for the Latin name of a cat. This is a factual question 
🤔  that can be answered by querying a knowledge base.

💡  Felis catus

🤔  The user is asking for the latin name of a cat. I have already used the 
🤔  "Knowledge query" tool and received the answer "Felis catus". I have 
🤔  sufficient information to answer the question.

The latin name for a cat is Felis catus.
```

**Other query commands:**

- `tg-invoke-nlp-query` - Execute NLP query
- `tg-invoke-objects-query` - Query objects
- `tg-invoke-structured-query` - Execute structured query
