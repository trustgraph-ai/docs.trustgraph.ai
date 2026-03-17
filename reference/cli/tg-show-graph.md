---
title: tg-show-graph
parent: CLI
review_date: 2027-01-01
---

# tg-show-graph

Dumps knowledge graph triples using streaming.

## Synopsis

```bash
tg-show-graph [options]
```

## Description

Queries the knowledge graph and streams triples in human-readable format. Supports filtering by named graph and configurable limits and batch sizes.

Named graphs:
- Default graph (no filter): Core knowledge facts
- `urn:graph:source`: Extraction provenance (document/chunk sources)
- `urn:graph:retrieval`: Query-time explainability traces

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id FLOW` | `default` | Flow ID |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLLECTION` | `default` | Collection identifier |
| `-l, --limit N` | `10000` | Maximum triples to return |
| `-b, --batch-size N` | `20` | Triples per streaming batch |
| `-g, --graph GRAPH` | None | Filter by named graph. Use `""` for default graph only. |
| `--show-graph` | false | Show named graph column in output |

## Examples

```bash
# Dump all triples
tg-show-graph

# Show provenance triples only
tg-show-graph -g "urn:graph:source"

# Show all triples with graph column
tg-show-graph --show-graph

# Default graph only (core facts)
tg-show-graph -g ""
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-query-graph`](tg-query-graph) - Selective pattern-matching queries
- [`tg-graph-to-turtle`](tg-graph-to-turtle) - Export graph to Turtle format
- [`tg-invoke-graph-rag`](tg-invoke-graph-rag) - Graph RAG queries
