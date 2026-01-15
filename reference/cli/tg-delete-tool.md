---
title: tg-delete-tool
parent: CLI
review_date: 2025-12-30
---

# tg-delete-tool

Removes agent tool configurations from TrustGraph.

## Synopsis

```bash
tg-delete-tool --id ID [options]
```

## Description

The `tg-delete-tool` command permanently deletes an agent tool configuration by ID. Once deleted, the tool will no longer be available for use by agents.

**Note**: This command deletes agent tools (stored in 'tool' configuration group). To remove MCP tool configurations, use `tg-delete-mcp-tool` instead.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--id ID` | ID of the tool to delete (case-sensitive) |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Delete Tool
```bash
tg-delete-tool --id weather
```

### Delete From Remote Instance
```bash
tg-delete-tool -u http://trustgraph.example.com:8088/ --id calculator
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-set-tool`](tg-set-tool) - Configure agent tools
- [`tg-show-mcp-tools`](tg-show-mcp-tools) - List MCP tool configurations
- [`tg-delete-mcp-tool`](tg-delete-mcp-tool) - Remove MCP tool configurations

## API Integration

This command uses the Tool Configuration API to delete agent tool definitions from the 'tool' configuration group.
