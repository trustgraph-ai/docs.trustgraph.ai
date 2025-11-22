---
title: Document RAG
nav_order: 12
parent: How-to Guides
grand_parent: TrustGraph Documentation
review_date: 2026-08-01
todo: true
todo_notes: Verify AI-generated output
---

# Document RAG Guide

**Query documents using vector embeddings and semantic search**

Document RAG (also called "basic RAG", "naive RAG", or simply "RAG") is a
retrieval-augmented generation approach that uses vector embeddings to find
relevant document chunks and provides them as context to an LLM for generating
responses.

Document RAG is the most basic information retrieval flow. It will prove
effective for some limited cases, but you should consider
[GraphRAG](graph-rag) or [Ontology RAG](ontology-rag) for more effective
information retrieval.

## What is Document RAG?

The essential Document RAG ingest flow consists of:
1. **Chunking** documents into smaller pieces
2. **Embedding** each chunk as a vector
3. **Storing** vectors in a vector database along with the chunks
4. **Retrieving** similar chunks based on query embedding
5. **Generating** responses using retrieved context and an LLM

The pros and cons of this approach:
- ✅ *Pro*: Quicker ingest time compared to knowledge extraction flows
- ✅ *Pro*: No token consumption on document ingest
- ⚠️ *Con*: Sentence embeddings are limited for retrieval where chunks
  contain many concepts
- ⚠️ *Con*: Ineffective for resolving complex questions

### When to Use Document RAG

✅ **Use Document RAG when**:
- You need semantic search over documents
- Questions can be answered from isolated passages
- You want simple, fast implementation
- Document context is self-contained in paragraphs or chunks

⚠️ **Consider alternatives when**:
- You need to understand relationships between entities
  → Use [Graph RAG](graph-rag)
- You need structured schema-based extraction
  → Use [Ontology RAG](ontology-rag)
- Answers require connecting information across documents
  → Use [Graph RAG](graph-rag)

## Prerequisites

Before starting:
- ✅ TrustGraph deployed ([Quick Start](../getting-started/quickstart))
- ✅ Understanding of [Core Concepts](../getting-started/concepts)
- ✅ Documents ready to load

## Step-by-Step Guide

### Step 1: Load Your Document

TrustGraph supports multiple document formats:
- PDF files (`.pdf`)
- Text files (`.txt`)
- Markdown (`.md`)
- HTML (`.html`)

We're going to start by using a fictional maritime tracking report
which you can download at this URL:

[https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/tracking/operation-phantom-cargo.md](https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/tracking/operation-phantom-cargo.md).

You can load the document either through the command-line, or using the
Workbench

#### Command-line

You can download the document:
```
wget -O phantom-cargo.md https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/tracking/operation-phantom-cargo.md
```

And use a command-line utility to load the document into the TrustGraph
library:

```
tg-add-library-document \
  --name "PHANTOM CARGO" \
  --description "Intelligence report: Operation PHANTOM CARGO" \
  --tags 'maritime,intelligence,cargo,grey arms' \
  --id https://trustgraph.ai/doc/phantom-cargo \
  --kind text/plain \
  phantom-cargo.md
```

You can then see the document in the library:

```
$ tg-show-library-documents
+-------+----------------------------------------------+
| id    | https://trustgraph.ai/doc/phantom-cargo      |
| time  | 2025-11-22 11:05:05                          |
| title | PHANTOM CARGO                                |
| kind  | text/plain                                   |
| note  | Intelligence report: Operation PHANTOM CARGO |
| tags  | maritime, intelligence, cargo, grey arms     |
+-------+----------------------------------------------+
```

#### Workbench

- Download [the document](https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/tracking/operation-phantom-cargo.md)
- Go the 'Library' page
- Click 'Upload documents'
- Set the title: PHANTOM CARGO
- Set the Comments to: Intelligence report: Operation PHANTOM CARGO
- Set keywords: maritime, intelligence, cargo, grey arms
- Select 'Text' for the upload operation
- Click 'Select text files'
- Add the document you just downloaded
- Click Submit

<img src="load-document.png" alt="Set collection option"/>

### Step 2: Create a Collection

A collection is used to organise a set of related documents or data sources
into a single unit.  Retrieval operations operate across a single collection.

We'll create an 'intelligence' collection:

#### Command-line

```
tg-set-collection -n Intelligence -d 'Intelligence analysis' intelligence
```

#### Workbench

- Go to the 'Library' page
- Select the 'Collections' tab
- Click 'Create Collection'
- Set the ID: intelligence
- Set the name: Intelligence
- Set the description to: Intelligence analysis
- Click 'Submit'

### Step 3: Create the Flow

A flow describes the collection of processing operations.  We're going
to create a single flow for Document RAG processing.

We'll create a 'doc-rag' flow:

#### Command-line

This command allows you to add parameters for LLM model, temperature etc.
but we're just going to use the defaults:

```
tg-start-flow -n document-rag -i doc-rag -d "Document RAG"
```

#### Workbench

- Go to the 'Flows' page
- Click 'Create'
- Select the flow class 'Document RAG'
- Set the ID: doc-rag
- Set the description: Document RAG
- Click 'Create

### Step 4: Submit the Document for Processing

This pushes the document into the flow input.

#### Command-line

This command submits the document for processing.  You need to specify
the flow ID (`doc-rag`) and the document ID which was used when the
document was added to the library in step 1.  The collection ID is
that which was used to create the collection.
Processing objects need an ID, and you can make up any string:

```
tg-start-library-processing \
    --flow-id doc-rag \
    --document-id https://trustgraph.ai/doc/phantom-cargo \
    --collection intelligence \
    --processing-id urn:processing-01
```

#### Workbench

There is a selection widget top right of the screen with an database icon
top left.

<img src="selection.png" alt="Set collection option"/>

Click that to open the collection/flow selector, and select the
Intelligence collection, and Document RAG, both of which you created earlier.

<img src="collection-selected.png" alt="Set collection option"/>

You are ready to submit the document:

- Go to the 'Library' page
- Select the PHANTOM CARGO document so that the tick box is selected
- Click 'Submit' at the bottom of the page
- Change the Processing flow to Document RAG
- Click Submit

### Step 5: Monitoring

If you want to see the document loading, you can go to Grafana at
[`http://localhost:3000`](http://localhost:3000).  The default
login user is admin, password admin.  Grafana is configured with a single
dashboard, which has a 'pub/sub backlog' graph.

<img src="monitoring.png" alt="Set collection option"/>


## Troubleshooting

### Poor Retrieval Quality

**Problem**: Irrelevant chunks retrieved

**Solutions**:
- Verify documents processed successfully: `tg-show-processor-state`
- Check embedding quality: `tg-invoke-vector-search "test query"`
- Adjust chunk size in flow configuration
- Reformulate query for better semantic match

### Missing Context

**Problem**: Answers lack necessary context

**Solutions**:
- Increase chunk size (e.g., 1000 → 1500)
- Increase retrieval limit (more chunks)
- Increase chunk overlap (50 → 100)
- Use [Graph RAG](graph-rag) for relationship-based context

### Slow Queries

**Problem**: Document RAG queries take too long

**Solutions**:
- Reduce number of documents in collection
- Optimize vector database configuration
- Use more powerful hardware
- Consider indexing strategies

### Empty Results

**Problem**: No results returned

**Solutions**:
- Verify documents are processed: `tg-show-processor-state`
- Check collection name is correct
- Verify embeddings created: `tg-show-graph`
- Check for processing errors in logs

## Advanced Configuration

### Custom Embedding Models

Configure different embedding models in your flow:

```yaml
embeddings:
  model: sentence-transformers/all-mpnet-base-v2
  dimension: 768
```

**Popular choices**:
- `all-mpnet-base-v2`: Balanced quality/speed (768d)
- `all-MiniLM-L6-v2`: Fast, smaller (384d)
- `bge-large-en`: High quality (1024d)

### Retrieval Tuning

Adjust retrieval parameters:

```bash
# Get more context (more chunks)
tg-invoke-document-rag --limit 10 "query"

# Focus on top matches (fewer chunks)
tg-invoke-document-rag --limit 2 "query"
```

### Collection Management

**Create collection**:
```bash
tg-set-collection my-project
```

**List collections**:
```bash
tg-list-collections
```

**Delete collection**:
```bash
tg-delete-collection my-project
```

## Document RAG vs. Other Approaches

| Aspect | Document RAG | Graph RAG | Ontology RAG |
|--------|--------------|-----------|--------------|
| **Retrieval** | Vector similarity | Graph relationships | Schema-based |
| **Context** | Isolated chunks | Connected entities | Structured data |
| **Best for** | Semantic search | Complex relationships | Typed extraction |
| **Setup** | Simple | Medium | Complex |
| **Speed** | Fast | Medium | Medium |

**Use multiple approaches**:
- Document RAG for quick semantic search
- [Graph RAG](graph-rag) when relationships matter
- [Ontology RAG](ontology-rag) for structured extraction

## Next Steps

### Explore Other RAG Types

- **[Graph RAG](graph-rag)** - Leverage knowledge graph relationships
- **[Ontology RAG](ontology-rag)** - Use structured schemas for extraction

### Advanced Features

- **[Structured Processing](structured-processing/)** - Extract typed objects
- **[Agent Extraction](agent-extraction)** - AI-powered extraction workflows
- **[Object Extraction](object-extraction)** - Domain-specific extraction

### API Integration

- **[Document RAG API](../reference/apis/api-document-rag)** - API reference
- **[CLI Reference](../reference/cli/)** - Command-line tools
- **[Examples](../examples/)** - Code samples

## Related Resources

- **[Core Concepts](../getting-started/concepts)** - Understanding embeddings and chunks
- **[Vector Search](../getting-started/concepts#vector-embeddings)** - How semantic search works
- **[Deployment](../deployment/)** - Scaling for production
- **[Troubleshooting](../deployment/troubleshooting)** - Common issues
