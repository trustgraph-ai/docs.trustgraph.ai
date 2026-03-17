---
title: tg-show-explain-trace
parent: CLI
review_date: 2027-01-01
---

# tg-show-explain-trace

Shows the full explainability trace for a query session.

## Synopsis

```bash
tg-show-explain-trace QUESTION_ID [options]
```

## Description

Displays the complete reasoning trace for a GraphRAG, DocRAG, or Agent session. Auto-detects the trace type.

- **GraphRAG**: Question -> Grounding -> Exploration -> Focus -> Synthesis
- **DocRAG**: Question -> Exploration -> Synthesis
- **Agent**: Session -> Iterations (thought/action/observation) -> Conclusion

With `--show-provenance`, traces selected edges back to their source documents via reification.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `QUESTION_ID` | Question or session URI to show trace for |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow ID |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLL` | `default` | Collection identifier |
| `--max-answer N` | `500` | Max characters for answer display |
| `--show-provenance` | false | Trace edges back to source documents |
| `--format FORMAT` | `text` | Output format: `text`, `json` |

## Examples

```bash
tg-show-explain-trace "urn:trustgraph:question:abc123"

tg-show-explain-trace --show-provenance "urn:trustgraph:question:abc123"

tg-show-explain-trace --format json "urn:trustgraph:agent:abc123"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-list-explain-traces`](tg-list-explain-traces) - List all explainability sessions
- [`tg-show-extraction-provenance`](tg-show-extraction-provenance) - Show document extraction provenance
- [`tg-invoke-graph-rag`](tg-invoke-graph-rag) - Run Graph RAG with `-x` for inline explainability
