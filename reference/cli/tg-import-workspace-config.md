---
title: tg-import-workspace-config
parent: CLI
review_date: 2027-10-26
---

# tg-import-workspace-config

Import workspace configuration from a JSON file.

## Synopsis

```bash
tg-import-workspace-config -i INPUT [options]
```

## Description

Imports a workspace configuration dump produced by `tg-export-workspace-config` into a target workspace. Existing items with the same type and key are overwritten. Accepts both the wrapped export format (with a `config` key) and a bare `{type: {key: value}}` dictionary.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-i, --input FILE` | Input JSON file path (use `"-"` for stdin) |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8888/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | `$TRUSTGRAPH_WORKSPACE` or `default` | Target workspace |
| `--dry-run` | false | Parse and validate the input without writing anything |

## Examples

```bash
# Import config into the default workspace
tg-import-workspace-config -i my-config.json

# Import into a specific workspace with dry run first
tg-import-workspace-config -w staging -i my-config.json --dry-run
tg-import-workspace-config -w staging -i my-config.json

# Pipe from export to import across workspaces
tg-export-workspace-config -w prod -o - | tg-import-workspace-config -w staging -i -
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-export-workspace-config`](tg-export-workspace-config) - Export workspace configuration
- [`tg-import-workspace`](tg-import-workspace) - Import full workspace bundle (config + data)
