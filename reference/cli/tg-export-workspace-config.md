---
title: tg-export-workspace-config
parent: CLI
review_date: 2027-10-26
---

# tg-export-workspace-config

Export a workspace's configuration to a JSON file.

## Synopsis

```bash
tg-export-workspace-config -o OUTPUT [options]
```

## Description

Exports a curated subset of a workspace's configuration to a JSON file for later import into another workspace. Useful for cloning test setups or migrating configuration between environments.

Exported configuration types: `mcp-tool`, `tool`, `flow-blueprint`, `token-cost`, `agent-pattern`, `agent-task-type`, `parameter-type`, `interface-description`, `prompt`.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-o, --output FILE` | Output JSON file path (use `"-"` for stdout) |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8888/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | `$TRUSTGRAPH_WORKSPACE` or `default` | Source workspace |

## Examples

```bash
# Export config to a file
tg-export-workspace-config -o my-config.json

# Export from a specific workspace to stdout
tg-export-workspace-config -w production -o -
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-import-workspace-config`](tg-import-workspace-config) - Import workspace configuration
- [`tg-export-workspace`](tg-export-workspace) - Export full workspace bundle (config + data)
