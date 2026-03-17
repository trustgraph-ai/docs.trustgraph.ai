---
title: tg-invoke-rows-query
parent: CLI
review_date: 2027-01-01
---

# tg-invoke-rows-query

Queries structured data rows.

## Synopsis

```bash
tg-invoke-rows-query [options]
```

## Description

Queries structured data rows from the row store. Renamed from `tg-invoke-objects-query` in v2.0.

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow ID |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLL` | `default` | Collection identifier |

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-row-embeddings`](tg-invoke-row-embeddings) - Semantic search on structured data
- [`tg-invoke-structured-query`](tg-invoke-structured-query) - NLP structured data queries
- [`tg-load-structured-data`](tg-load-structured-data) - Load structured data
