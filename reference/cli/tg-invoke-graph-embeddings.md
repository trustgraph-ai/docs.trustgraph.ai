---
title: tg-invoke-graph-embeddings
parent: CLI
review_date: 2027-01-01
---

# tg-invoke-graph-embeddings

Queries graph entities by text similarity.

## Synopsis

```bash
tg-invoke-graph-embeddings QUERY [options]
```

## Description

Searches for graph entities similar to the query text using vector embeddings. Returns matching entities with similarity scores.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `QUERY` | Query text to search for similar graph entities |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow ID |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-c, --collection COLL` | `default` | Collection identifier |
| `-l, --limit N` | `10` | Maximum results |

## Examples

```bash
tg-invoke-graph-embeddings "machine learning algorithms"

tg-invoke-graph-embeddings -l 20 -C research "neural networks"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-embeddings`](tg-invoke-embeddings) - Convert text to embeddings
- [`tg-invoke-document-embeddings`](tg-invoke-document-embeddings) - Search document chunks by similarity
- [`tg-invoke-graph-rag`](tg-invoke-graph-rag) - Graph RAG queries
