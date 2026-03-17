---
title: tg-invoke-row-embeddings
parent: CLI
review_date: 2027-01-01
---

# tg-invoke-row-embeddings

Queries structured data rows by text similarity.

## Synopsis

```bash
tg-invoke-row-embeddings -s SCHEMA_NAME QUERY [options]
```

## Description

Searches for structured data rows similar to the query text using vector embeddings on indexed fields. Returns matching rows with index values and similarity scores.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-s, --schema-name NAME` | Schema name to search within |
| `QUERY` | Query text to search for similar rows |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow ID |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-c, --collection COLL` | `default` | Collection identifier |
| `-i, --index-name NAME` | None | Index name to filter search |
| `-l, --limit N` | `10` | Maximum results |

## Examples

```bash
tg-invoke-row-embeddings -s customers "John Smith"

tg-invoke-row-embeddings -s products -i description -l 5 "wireless headphones"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-embeddings`](tg-invoke-embeddings) - Convert text to embeddings
- [`tg-invoke-rows-query`](tg-invoke-rows-query) - Query structured data rows
- [`tg-invoke-structured-query`](tg-invoke-structured-query) - NLP structured data queries
