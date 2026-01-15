---
title: tg-set-tool
parent: CLI
review_date: 2026-03-06
---

# tg-set-tool

Configures and registers agent tools in TrustGraph.

## Synopsis

```bash
tg-set-tool --id ID --name NAME --type TYPE --description DESC [options]
```

## Description

The `tg-set-tool` command creates or updates agent tool configurations. Tools define capabilities that agents can use to perform specific tasks and operations. Supports multiple tool types with parameterized arguments.

## Tool Types

| Type | Description | Required Parameter |
|------|-------------|-------------------|
| `knowledge-query` | Query knowledge bases and graph data | `--collection` |
| `text-completion` | Text generation services | None |
| `mcp-tool` | Reference to MCP (Model Context Protocol) tools | `--mcp-tool` |
| `prompt` | Prompt template execution | `--template` |

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--id ID` | Unique tool identifier |
| `--name NAME` | Human-readable tool name |
| `--type TYPE` | Tool type (see Tool Types table) |
| `--description DESC` | Detailed description of tool capabilities |

### Type-Specific Parameters

| Option | Required For | Description |
|--------|-------------|-------------|
| `--mcp-tool ID` | `mcp-tool` | MCP tool configuration ID |
| `--collection NAME` | `knowledge-query` | Knowledge collection to query |
| `--template ID` | `prompt` | Prompt template ID |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `--argument ARG` | None | Tool argument: `name:type:description` (can specify multiple times) |

### Argument Types

| Type | Description |
|------|-------------|
| `string` | Text parameter |
| `number` | Numeric parameter (integer or decimal) |

## Examples

### Knowledge Query Tool
```bash
tg-set-tool --id weather --name "Weather Lookup" \
  --type knowledge-query \
  --description "Get weather information for locations" \
  --collection weather-data \
  --argument location:string:"Location to query" \
  --argument units:string:"Temperature units (C/F)"
```

### MCP Tool Integration
```bash
tg-set-tool --id calculator --name "Calculator" \
  --type mcp-tool \
  --description "Perform mathematical calculations" \
  --mcp-tool calculator \
  --argument expression:string:"Mathematical expression to evaluate"
```

### Text Completion Tool
```bash
tg-set-tool --id text-generator --name "Text Generator" \
  --type text-completion \
  --description "Generate text content based on prompts" \
  --argument prompt:string:"Text prompt for generation" \
  --argument max_length:number:"Maximum length of generated text"
```

### Prompt Template Tool
```bash
tg-set-tool --id email-writer --name "Email Writer" \
  --type prompt \
  --description "Generate professional emails using templates" \
  --template email-template \
  --argument recipient:string:"Email recipient name" \
  --argument subject:string:"Email subject"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-delete-tool`](tg-delete-tool) - Remove tool configuration
- [`tg-show-mcp-tools`](tg-show-mcp-tools) - List MCP tool configurations
- [`tg-invoke-mcp-tool`](tg-invoke-mcp-tool) - Test MCP tools
- [`tg-invoke-agent`](tg-invoke-agent) - Use agents with configured tools

## API Integration

This command uses the Configuration API to store tool definitions in the 'tool' configuration group.
