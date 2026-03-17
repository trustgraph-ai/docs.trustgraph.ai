---
title: tg-list-explain-traces
parent: CLI
review_date: 2027-01-01
---

# tg-list-explain-traces

Lists explainability sessions (GraphRAG, DocRAG, and Agent).

## Synopsis

```bash
tg-list-explain-traces [options]
```

## Description

Queries the retrieval graph for all recorded explainability sessions and displays them with session IDs, type, question text, and timestamps.

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow ID |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLL` | `default` | Collection identifier |
| `--limit N` | `50` | Maximum results |
| `--format FORMAT` | `table` | Output format: `table`, `json` |

## Examples

```bash
tg-list-explain-traces

tg-list-explain-traces --limit 20 --format json
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-explain-trace`](tg-show-explain-trace) - Show full trace for a session
- [`tg-show-extraction-provenance`](tg-show-extraction-provenance) - Show document extraction provenance
