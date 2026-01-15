---
title: tg-set-mcp-tool
parent: CLI
review_date: 2026-05-31
---

# tg-set-mcp-tool

Configures and registers MCP (Model Context Protocol) tools in TrustGraph.

## Synopsis

```bash
tg-set-mcp-tool --id ID --tool-url URL [options]
```

## Description

The `tg-set-mcp-tool` command configures MCP tool connections that can be integrated with TrustGraph agents. MCP tools are external services following the Model Context Protocol specification.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--id ID` | Unique identifier for the MCP tool |
| `--tool-url URL` | MCP server endpoint URL |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-r, --remote-name NAME` | Same as `--id` | Name used by the MCP server |

## Examples

### Configure MCP Tool
```bash
tg-set-mcp-tool --id weather --tool-url "http://localhost:3000/weather"
```

### With Remote Name
```bash
tg-set-mcp-tool \
  --id calc \
  --tool-url "http://mcp-server:3000/calculator" \
  --remote-name "calculator-service"
```

### Using Custom API
```bash
tg-set-mcp-tool \
  --id search \
  --tool-url "http://search-mcp:3000" \
  -u http://production:8088/
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-mcp-tools`](tg-show-mcp-tools) - List MCP tool configurations
- [`tg-delete-mcp-tool`](tg-delete-mcp-tool) - Remove MCP tool
- [`tg-invoke-mcp-tool`](tg-invoke-mcp-tool) - Test MCP tools
- [`tg-set-tool`](tg-set-tool) - Configure agent tools that reference MCP tools

## API Integration

This command uses the Configuration API to store MCP tool definitions in the 'mcp' configuration group.
