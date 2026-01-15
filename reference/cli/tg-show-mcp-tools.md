---
title: tg-show-mcp-tools
parent: CLI
review_date: 2026-04-28
---

# tg-show-mcp-tools

Displays configured MCP (Model Context Protocol) tools.

## Synopsis

```bash
tg-show-mcp-tools [options]
```

## Description

The `tg-show-mcp-tools` command displays all configured MCP tools from TrustGraph, including their identifiers, remote names, and endpoint URLs. Useful for debugging connectivity, documentation, and auditing tool configurations.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Display All MCP Tools
```bash
tg-show-mcp-tools
```

### Query Remote Instance
```bash
tg-show-mcp-tools -u http://trustgraph.example.com:8088/
```

## Output Format

The command displays each MCP tool in a table format:

```
+-------------+----------------------------------------------------------------------+
| id          | weather                                                              |
+-------------+----------------------------------------------------------------------+
| remote-name | weather-service                                                      |
+-------------+----------------------------------------------------------------------+
| url         | http://localhost:3000/weather                                        |
+-------------+----------------------------------------------------------------------+
```

Each tool shows:
- **id**: Local identifier used to reference the tool
- **remote-name**: Name used by the MCP server
- **url**: MCP server endpoint URL

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-mcp-tool`](tg-invoke-mcp-tool) - Invoke MCP tools
- [`tg-set-tool`](tg-set-tool) - Configure agent tools that reference MCP tools
- [`tg-delete-tool`](tg-delete-tool) - Remove tool configurations

## API Integration

This command uses the Configuration API to retrieve MCP tool definitions from the 'mcp' configuration group.
