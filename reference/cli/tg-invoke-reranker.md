---
title: tg-invoke-reranker
parent: CLI
review_date: 2027-07-17
---

# tg-invoke-reranker

Reranks documents against one or more queries using the cross-encoder reranker service.

## Synopsis

```bash
tg-invoke-reranker -q QUERY [options] DOCUMENT [DOCUMENT ...]
```

## Description

The `tg-invoke-reranker` command sends a list of documents to the cross-encoder reranker service and returns them ranked by relevance to the given query. Multiple queries can be specified. This is useful for testing the reranker service directly and for evaluating relevance scoring outside of the GraphRAG or Document-RAG pipelines.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-q, --query QUERY` | Query text to rank against (can be specified multiple times) |
| `DOCUMENT` | Documents to rerank (positional, one or more) |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | `$TRUSTGRAPH_WORKSPACE` or `default` | Workspace identifier |
| `-f, --flow-id FLOW` | `default` | Flow identifier |
| `-l, --limit LIMIT` | `10` | Maximum number of results to return |

## Examples

### Basic Reranking
```bash
tg-invoke-reranker -q "climate change effects" \
  "Global warming impacts on agriculture" \
  "History of space exploration" \
  "Rising sea levels and coastal erosion"
```

### Multiple Queries
```bash
tg-invoke-reranker \
  -q "renewable energy" \
  -q "solar power efficiency" \
  "Photovoltaic cell advances in 2025" \
  "Wind turbine maintenance costs" \
  "Solar panel degradation rates"
```

### Limit Results
```bash
tg-invoke-reranker -q "machine learning" -l 5 \
  "Neural network architectures" \
  "Database indexing strategies" \
  "Gradient descent optimisation" \
  "SQL query planning" \
  "Transformer attention mechanisms" \
  "B-tree data structures"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-invoke-graph-rag`](tg-invoke-graph-rag) - Graph-based RAG queries (uses reranker internally)
- [`tg-invoke-document-rag`](tg-invoke-document-rag) - Document-based RAG queries (uses reranker internally)
- [`tg-invoke-graph-embeddings`](tg-invoke-graph-embeddings) - Search graph entities by similarity
