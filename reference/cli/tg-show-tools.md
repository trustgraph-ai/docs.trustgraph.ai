---
title: tg-show-tools
parent: CLI
review_date: 2026-05-23
---

# tg-show-tools

Displays all agent tool configurations from TrustGraph.

## Synopsis

```bash
tg-show-tools [options]
```

## Description

The `tg-show-tools` command retrieves and displays all configured agent tools from TrustGraph, showing properties, arguments, and metadata for each tool.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Show All Tools
```bash
tg-show-tools
```

### Using Custom API URL
```bash
tg-show-tools -u http://production:8088/
```

## Tool Types

| Type | Description |
|------|-------------|
| `knowledge-query` | Query knowledge graph data |
| `structured-query` | Query structured data using natural language |
| `text-completion` | Text generation and completion |
| `mcp-tool` | References to MCP tools |
| `prompt` | Execute prompt templates |

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-set-tool`](tg-set-tool) - Configure agent tools
- [`tg-delete-tool`](tg-delete-tool) - Remove tool configurations
- [`tg-show-mcp-tools`](tg-show-mcp-tools) - List MCP tools

## API Integration

This command uses the Configuration API to retrieve agent tool definitions from the 'tool' configuration group.
