---
title: tg-list-cloze-models
parent: CLI
review_date: 2027-10-26
---

# tg-list-cloze-models

List cloze model instances in a workspace.

## Synopsis

```bash
tg-list-cloze-models [options]
```

## Description

Lists all cloze model instances in the current workspace, showing their state (ready/training), labels, accuracy, and dataset sizes.

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
# List models in default workspace
tg-list-cloze-models

# JSON output for scripting
tg-list-cloze-models --json
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-invoke-cloze`](tg-invoke-cloze) - Classify text with a cloze model
- [`tg-list-models`](tg-list-models) - List LLM models
