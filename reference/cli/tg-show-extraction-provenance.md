---
title: tg-show-extraction-provenance
parent: CLI
review_date: 2027-01-01
---

# tg-show-extraction-provenance

Shows the extraction provenance hierarchy for a document.

## Synopsis

```bash
tg-show-extraction-provenance DOCUMENT_ID [options]
```

## Description

Given a document ID, traverses and displays the full derivation hierarchy: Document -> Pages -> Chunks -> Subgraphs, using `prov:wasDerivedFrom` relationships stored in the `urn:graph:source` named graph.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `DOCUMENT_ID` | Document URI to show hierarchy for |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow ID |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLL` | `default` | Collection identifier |
| `--show-content` | false | Include document/chunk content |
| `--max-content N` | `200` | Max characters per content blob |
| `--format FORMAT` | `tree` | Output format: `tree`, `json` |

## Examples

```bash
tg-show-extraction-provenance "urn:trustgraph:doc:abc123"

tg-show-extraction-provenance --show-content --max-content 500 "urn:trustgraph:doc:abc123"

tg-show-extraction-provenance --format json "urn:trustgraph:doc:abc123"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-list-explain-traces`](tg-list-explain-traces) - List query-time explainability sessions
- [`tg-show-explain-trace`](tg-show-explain-trace) - Show query-time trace
- [`tg-show-library-documents`](tg-show-library-documents) - List documents to find document IDs
- [`tg-query-graph`](tg-query-graph) - Query provenance triples directly
