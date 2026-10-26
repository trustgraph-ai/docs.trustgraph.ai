---
title: tg-list-models
parent: CLI
review_date: 2027-10-26
---

# tg-list-models

List available models from the text-completion backend.

## Synopsis

```bash
tg-list-models [options]
```

## Description

Queries the text-completion service for its list of available models and displays them in a table. The returned metadata varies by backend — fields such as context length, parameter size, and quantization are shown when available.

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8888/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | `$TRUSTGRAPH_WORKSPACE` or `default` | Workspace identifier |
| `-f, --flow-id FLOW` | `default` | Flow ID |
| `-j, --json` | false | Output as JSON |

## Examples

```bash
# List models from the active backend
tg-list-models

# JSON output for scripting
tg-list-models --json

# List models from a specific deployment
tg-list-models -u https://trustgraph.example.com:8888/
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-invoke-llm`](tg-invoke-llm) - Direct LLM text completion
- [`tg-list-cloze-models`](tg-list-cloze-models) - List cloze model instances
