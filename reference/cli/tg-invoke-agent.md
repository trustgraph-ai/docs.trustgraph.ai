---
title: tg-invoke-agent
parent: CLI
review_date: 2027-01-01
---

# tg-invoke-agent

Answers questions using the ReAct agent via WebSocket.

## Synopsis

```bash
tg-invoke-agent -q "your question" [options]
```

## Description

Provides an interactive interface to TrustGraph's ReAct agent. The agent uses configured tools and knowledge sources to answer questions. Supports verbose mode to show thinking/observation steps, and explainability mode to capture provenance events.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-q, --question QUESTION` | Question to ask the agent |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id FLOW` | `default` | Flow ID |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLLECTION` | `default` | Collection identifier |
| `-l, --plan PLAN` | None | Agent plan specification |
| `-s, --state STATE` | None | Agent initial state |
| `-g, --group GROUP [GROUP ...]` | None | Agent tool groups |
| `-v, --verbose` | false | Show thinking process and observations |
| `--no-streaming` | false | Disable streaming |
| `-x, --explainable` | false | Show provenance events: Session, Iterations, Conclusion |
| `--debug` | false | Show debug output |

## Examples

```bash
# Basic query
tg-invoke-agent -q "What is the capital of France?"

# Verbose with explainability
tg-invoke-agent -v -x -q "Explain quantum computing"

# With tool group filter
tg-invoke-agent -q "Search for AI papers" -g knowledge read-only
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-graph-rag`](tg-invoke-graph-rag) - Graph RAG queries
- [`tg-set-tool`](tg-set-tool) - Configure agent tools
- [`tg-show-tools`](tg-show-tools) - List configured tools
- [`tg-show-explain-trace`](tg-show-explain-trace) - Review full explainability traces
