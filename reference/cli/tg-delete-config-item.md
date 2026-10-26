---
title: tg-delete-config-item
parent: CLI
review_date: 2027-10-26
---

# tg-delete-config-item

Delete a configuration item.

## Synopsis

```bash
tg-delete-config-item --type TYPE --key KEY [options]
```

## Description

Deletes a single configuration item identified by its type and key from the workspace configuration store.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--type TYPE` | Configuration type (e.g. `prompt`, `tool`, `flow-blueprint`) |
| `--key KEY` | Configuration key |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8888/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | `$TRUSTGRAPH_WORKSPACE` or `default` | Workspace identifier |

## Examples

```bash
# Delete a prompt template
tg-delete-config-item --type prompt --key my-custom-prompt

# Delete a tool definition
tg-delete-config-item --type tool --key obsolete-tool -w production
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-get-config-item`](tg-get-config-item) - Retrieve a configuration item
- [`tg-put-config-item`](tg-put-config-item) - Create or update a configuration item
- [`tg-list-config-items`](tg-list-config-items) - List configuration items
