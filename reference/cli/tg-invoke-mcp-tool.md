---
title: tg-invoke-mcp-tool
parent: CLI
review_date: 2026-04-16
---

# tg-invoke-mcp-tool

Invokes MCP (Model Context Protocol) tools through the TrustGraph API.

## Synopsis

```bash
tg-invoke-mcp-tool -n TOOL_NAME [options]
```

## Description

The `tg-invoke-mcp-tool` command executes MCP tools by name with optional JSON parameters. This is useful for testing MCP tool functionality, debugging configurations, and executing tools directly from the command line.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-n, --name TOOL_NAME` | Name of the MCP tool to invoke (case-sensitive) |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id FLOW` | `default` | Flow identifier for execution context |
| `-P, --parameters JSON` | `{}` | Tool parameters as JSON dictionary |

## Examples

### Invoke Without Parameters
```bash
tg-invoke-mcp-tool -n weather
```

### Invoke With Parameters
```bash
tg-invoke-mcp-tool -n weather -P '{"location": "New York", "units": "celsius"}'
```

### Complex Parameters
```bash
tg-invoke-mcp-tool -n document-analyzer -P '{
  "document_id": "doc123",
  "analysis_type": "sentiment",
  "options": {
    "include_entities": true,
    "confidence_threshold": 0.8
  }
}'
```

### Custom Flow Context
```bash
tg-invoke-mcp-tool -f my-analysis-flow -n data-processor \
  -P '{"dataset": "sales_data", "operation": "summarize"}'
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-mcp-tools`](tg-show-mcp-tools) - List configured MCP tools
- [`tg-set-tool`](tg-set-tool) - Configure MCP tools
- [`tg-delete-tool`](tg-delete-tool) - Remove MCP tool configuration
- [`tg-invoke-agent`](tg-invoke-agent) - Invoke agents that may use MCP tools

## API Integration

This command uses the MCP Tool Invocation API to execute tools with the specified parameters.
