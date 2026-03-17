---
title: tg-invoke-document-embeddings
parent: CLI
review_date: 2027-01-01
---

# tg-invoke-document-embeddings

Queries document chunks by text similarity.

## Synopsis

```bash
tg-invoke-document-embeddings QUERY [options]
```

## Description

Searches for document chunks similar to the query text using vector embeddings. Returns matching chunk IDs with similarity scores.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `QUERY` | Query text to search for similar document chunks |

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
tg-invoke-document-embeddings "return policy terms"

tg-invoke-document-embeddings -l 5 -C legal "data protection requirements"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-embeddings`](tg-invoke-embeddings) - Convert text to embeddings
- [`tg-invoke-graph-embeddings`](tg-invoke-graph-embeddings) - Search graph entities by similarity
- [`tg-invoke-document-rag`](tg-invoke-document-rag) - Document RAG queries
