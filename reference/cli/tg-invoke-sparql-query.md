---
title: tg-invoke-sparql-query
parent: CLI
review_date: 2027-01-01
---

# tg-invoke-sparql-query

Execute SPARQL queries against the TrustGraph knowledge graph.

## Synopsis

```bash
tg-invoke-sparql-query -q "SPARQL query" [options]
tg-invoke-sparql-query -i query.sparql [options]
```

## Description

Executes a SPARQL 1.1 query against the knowledge graph via the SPARQL query service. Supports SELECT, ASK, CONSTRUCT, and DESCRIBE query forms. Results are streamed in batches and can be output as a formatted table or JSON.

## Options

### Query Input (one required)

| Option | Description |
|--------|-------------|
| `-q, --query QUERY` | SPARQL query string |
| `-i, --input FILE` | Read SPARQL query from file (use `-` for stdin) |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id FLOW` | `default` | Flow ID |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLLECTION` | `default` | Collection identifier |
| `-l, --limit N` | `10000` | Maximum number of results |
| `-b, --batch-size N` | `20` | Streaming batch size |
| `--format FORMAT` | `table` | Output format: `table` or `json` |

## Examples

```bash
# Simple SELECT query
tg-invoke-sparql-query -q "SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10"

# ASK query
tg-invoke-sparql-query -q "ASK { <http://example.org/entity> ?p ?o }"

# CONSTRUCT query with JSON output
tg-invoke-sparql-query -q "CONSTRUCT { ?s ?p ?o } WHERE { ?s ?p ?o }" --format json

# Read query from file
tg-invoke-sparql-query -i query.sparql

# Read query from stdin
cat query.sparql | tg-invoke-sparql-query -i -

# With custom flow and collection
tg-invoke-sparql-query -f my-flow -C my-collection -q "SELECT ?s WHERE { ?s ?p ?o }"
```

## Output Formats

**Table format** (default): Displays SELECT results as an aligned table with column headers and separators.

**JSON format**: Outputs SELECT results as a JSON array of objects keyed by variable name. CONSTRUCT/DESCRIBE results are output as a JSON array of triples.

**ASK queries**: Prints `true` or `false`.

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-graph`](tg-show-graph) - Dump graph triples
- [`tg-query-graph`](tg-query-graph) - Pattern-matching graph queries
- [`tg-invoke-graph-rag`](tg-invoke-graph-rag) - Graph-based RAG queries
- [`tg-graph-to-turtle`](tg-graph-to-turtle) - Export graph to Turtle format
