---
title: tg-invoke-agent
parent: CLI
review_date: 2026-05-14
---

# tg-invoke-agent

Uses the agent service to answer questions via interactive WebSocket connection.

## Synopsis

```bash
tg-invoke-agent -q "your question" [options]
```

## Description

The `tg-invoke-agent` command provides an interactive interface to TrustGraph's agent service via WebSocket. The agent uses available tools and knowledge sources to answer questions, optionally showing its thinking process in verbose mode.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-q, --question QUESTION` | Question to ask the agent |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `ws://localhost:8088/` | TrustGraph API URL (WebSocket) |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id FLOW` | `default` | Flow ID to use |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLLECTION` | `default` | Collection identifier |
| `-l, --plan PLAN` | None | Agent plan specification |
| `-s, --state STATE` | None | Agent initial state |
| `-v, --verbose` | false | Show agent's thinking process and observations |

## Examples

### Basic Agent Query
```bash
tg-invoke-agent -q "What is the capital of France?"
```

### With Verbose Mode
```bash
tg-invoke-agent -q "Explain quantum computing" -v
```

### Specific Flow and Collection
```bash
tg-invoke-agent \
  -q "What research papers discuss AI ethics?" \
  -f research-flow \
  -C academic-papers
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL (automatically converted to WebSocket format)
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-llm`](tg-invoke-llm) - Direct LLM text completion
- [`tg-invoke-graph-rag`](tg-invoke-graph-rag) - Graph RAG queries
- [`tg-set-tool`](tg-set-tool) - Configure agent tools

## API Integration

This command uses the Agent API via WebSocket connection for real-time interactive question answering.
