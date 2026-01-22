---
title: tg-delete-mcp-tool
parent: CLI
review_date: 2026-09-01
---

# tg-delete-mcp-tool

Removes MCP (Model Context Protocol) tool configurations from TrustGraph.

## Synopsis

```bash
tg-delete-mcp-tool --id ID [options]
```

## Description

The `tg-delete-mcp-tool` command permanently deletes an MCP tool configuration by ID. Once deleted, the MCP tool will no longer be available for use by agent tools.

**Note**: This command deletes MCP tool configurations (stored in 'mcp' configuration group). Agent tools that reference MCP tools are managed separately with `tg-delete-tool`.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--id ID` | ID of the MCP tool to delete (case-sensitive) |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Delete MCP Tool
```bash
tg-delete-mcp-tool --id weather
```

### Delete From Remote Instance
```bash
tg-delete-mcp-tool -u http://trustgraph.example.com:8088/ --id calculator
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-mcp-tools`](tg-show-mcp-tools) - List MCP tool configurations
- [`tg-delete-tool`](tg-delete-tool) - Remove agent tool configurations
- [`tg-invoke-mcp-tool`](tg-invoke-mcp-tool) - Test MCP tools

## API Integration

This command uses the Configuration API to delete MCP tool definitions from the 'mcp' configuration group.
