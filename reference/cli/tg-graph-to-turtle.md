---
title: tg-graph-to-turtle
parent: CLI
review_date: 2027-01-01
---

# tg-graph-to-turtle

Exports knowledge graph data to Turtle format with RDF-star support.

## Synopsis

```bash
tg-graph-to-turtle [options]
```

## Description

Streams triples from the knowledge graph and outputs them in Turtle format to stdout. Supports RDF-star quoted triples, typed literals, and language-tagged literals.

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow ID |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLLECTION` | `default` | Collection to export |
| `-l, --limit N` | `10000` | Maximum triples |
| `-b, --batch-size N` | `20` | Triples per streaming batch |

## Examples

```bash
# Export to stdout
tg-graph-to-turtle

# Export to file
tg-graph-to-turtle > knowledge-graph.ttl

# Export specific collection
tg-graph-to-turtle -C research-data > research.ttl
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-graph`](tg-show-graph) - Display graph triples
- [`tg-query-graph`](tg-query-graph) - Selective graph queries
- [`tg-load-turtle`](tg-load-turtle) - Import Turtle files
- [`tg-load-knowledge`](tg-load-knowledge) - Load knowledge into graph
