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

Document RAG (also called "basic RAG", "naive RAG", or simply "RAG") is a retrieval-augmented generation approach that uses vector embeddings to find relevant document chunks and provides them as context to an LLM for generating responses.

## What is Document RAG?

Document RAG works by:
1. **Chunking** documents into smaller pieces
2. **Embedding** each chunk as a vector
3. **Storing** vectors in a vector database
4. **Retrieving** similar chunks based on query embedding
5. **Generating** responses using retrieved context

### When to Use Document RAG

✅ **Use Document RAG when**:
- You need semantic search over documents
- Questions can be answered from isolated passages
- You want simple, fast implementation
- Document context is self-contained

⚠️ **Consider alternatives when**:
- You need to understand relationships between entities → Use [Graph RAG](graph-rag)
- You need structured schema-based extraction → Use [Ontology RAG](ontology-rag)
- Answers require connecting information across documents → Use [Graph RAG](graph-rag)

## Prerequisites

Before starting:
- ✅ TrustGraph deployed ([Quick Start](../getting-started/quickstart))
- ✅ Understanding of [Core Concepts](../getting-started/concepts)
- ✅ Documents ready to load

## Step-by-Step Guide

### Step 1: Prepare Your Documents

TrustGraph supports multiple document formats:
- PDF files (`.pdf`)
- Text files (`.txt`)
- Markdown (`.md`)
- HTML (`.html`)

**Best practices**:
- Keep documents focused on specific topics
- Use clear formatting and structure
- Remove unnecessary metadata or headers
- Ensure text is extractable (not scanned images)

### Step 2: Configure Document Processing

Configure chunking parameters in your flow:

**Chunk Size**: Number of characters per chunk
- **Small (500-800)**: Better precision, more chunks
- **Medium (1000-1500)**: Balanced approach (recommended)
- **Large (2000-3000)**: More context, fewer chunks

**Chunk Overlap**: Characters shared between consecutive chunks
- **Typical**: 50-100 characters
- **Purpose**: Ensures context continuity at boundaries

**Example configuration**:
```yaml
chunker:
  type: recursive
  chunk_size: 1000
  overlap: 50
```

### Step 3: Load Documents

#### Using CLI

**Load a single PDF**:
```bash
tg-load-pdf my-document.pdf
```

**Load from a directory**:
```bash
for file in documents/*.pdf; do
  tg-load-pdf "$file"
done
```

**Load with specific collection**:
```bash
tg-load-pdf --collection my-project document.pdf
```

#### Using the Workbench

1. Navigate to **Library** page at `http://localhost:8888`
2. Click **Upload** or drag-and-drop documents
3. Documents appear in the library
4. Select documents and click **Submit**
5. Choose a processing flow
6. Click **Submit** to start processing

### Step 4: Process Documents

Documents must be processed to create embeddings:

**Using CLI**:
```bash
# Check flow status
tg-show-flows

# Start the default flow
tg-start-flow default-flow

# Monitor processing
tg-show-processor-state
```

**Using Workbench**:
1. Go to **Library** page
2. Select unprocessed documents
3. Click **Submit** in action bar
4. Select processing flow
5. Click **Submit**

**Monitor in Grafana**:
- Access `http://localhost:3000`
- Watch processing backlog
- Track chunk embeddings created
- Monitor LLM token usage

### Step 5: Query Using Document RAG

#### CLI Method

**Basic query**:
```bash
tg-invoke-document-rag "What is the main topic of these documents?"
```

**Query specific collection**:
```bash
tg-invoke-document-rag --collection my-project "Summarize the key findings"
```

**Adjust number of retrieved chunks**:
```bash
tg-invoke-document-rag --limit 5 "What are the main conclusions?"
```

#### API Method

**Endpoint**: `/api/document-rag`

**Request**:
```json
{
  "query": "What is the main topic?",
  "collection": "my-project",
  "limit": 3
}
```

**Response**:
```json
{
  "answer": "The main topic is...",
  "sources": [
    {
      "text": "Relevant chunk...",
      "score": 0.85,
      "document": "document-name.pdf"
    }
  ]
}
```

#### Workbench Method

1. Navigate to **Document RAG** tab
2. Select collection (optional)
3. Enter your question
4. Click **Submit**
5. View answer and source chunks
6. Click sources to see context

### Step 6: Verify and Refine

**Check retrieval quality**:
```bash
# View vector search results
tg-invoke-vector-search "your query term"
```

**Tune parameters if needed**:
- Increase chunk size if answers lack context
- Decrease chunk size if results are too broad
- Adjust overlap if context boundaries are poor
- Increase retrieval limit if missing relevant information

## Understanding Document RAG Results

### Source Attribution

Document RAG returns:
- **Answer**: LLM-generated response
- **Sources**: Retrieved chunks used for context
- **Scores**: Similarity scores for each chunk
- **Documents**: Origin documents for each chunk

### Confidence Indicators

**High confidence** (score > 0.8):
- Query closely matches document content
- Retrieved chunks directly relevant

**Medium confidence** (score 0.6-0.8):
- Semantic similarity present
- May need broader context

**Low confidence** (score < 0.6):
- Weak match to query
- Consider query reformulation

## Common Patterns

### Multi-Document Search

Query across all documents:
```bash
tg-invoke-document-rag "What trends appear across all reports?"
```

### Collection-Specific Queries

Query within a specific project:
```bash
tg-invoke-document-rag --collection project-2024 "What are the Q4 results?"
```

### Iterative Refinement

Start broad, then narrow:
```bash
# Broad query
tg-invoke-document-rag "What topics are covered?"

# Focused follow-up
tg-invoke-document-rag "Explain the methodology in detail"
```

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
