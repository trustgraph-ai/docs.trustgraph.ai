---
title: tg-show-tools
parent: CLI
review_date: 2026-05-23
---

# tg-show-tools
{: .no_toc }

Display all agent tool configurations from TrustGraph.

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Quick Start

```bash
tg-show-tools
```

---

## Synopsis

```bash
tg-show-tools [OPTIONS]
```

---

## Description

The `tg-show-tools` command retrieves and displays all configured agent tools from TrustGraph. It queries the TrustGraph API configuration service and presents each tool in a formatted table showing its properties, arguments, and metadata.

### Supported Tool Types

- **knowledge-query** - Tools that query knowledge graph data
- **structured-query** - Tools that query structured data using natural language
- **text-completion** - Tools for text generation and completion
- **mcp-tool** - References to MCP (Model Context Protocol) tools
- **prompt** - Tools that execute prompt templates

This command is useful for understanding available agent capabilities, debugging tool configuration, and documenting the current tool set.

---

## Options

| Option | Type | Description | Default |
|--------|------|-------------|---------|
| `-u`, `--api-url` | string | TrustGraph API URL | `http://localhost:8088/` or `$TRUSTGRAPH_URL` |
| `-t`, `--token` | string | Authentication token | `$TRUSTGRAPH_TOKEN` |

---

## Examples

### Basic Usage

Display all tools using default settings:
```bash
tg-show-tools
```

### Custom API URL

Query tools from a specific TrustGraph instance:
```bash
tg-show-tools -u http://trustgraph.example.com:8088/
```

### With Authentication

Use an authentication token:
```bash
tg-show-tools -t your-auth-token

# Or set environment variable
export TRUSTGRAPH_TOKEN=your-auth-token
tg-show-tools
```

---

## Output Format

The command displays each tool in a detailed table. The fields shown depend on the tool type:

### Common Fields (All Tool Types)

```
tool-name:
+-------------+----------------------------------------------------------------------+
| id          | tool-name                                                            |
+-------------+----------------------------------------------------------------------+
| name        | Human-Readable Tool Name                                             |
+-------------+----------------------------------------------------------------------+
| description | Detailed description of what the tool does                          |
+-------------+----------------------------------------------------------------------+
| type        | knowledge-query / structured-query / text-completion / mcp-tool /    |
|             | prompt                                                               |
+-------------+----------------------------------------------------------------------+
```

### Type-Specific Fields

**For `mcp-tool` type:**
```
+-------------+----------------------------------------------------------------------+
| mcp-tool    | referenced-mcp-tool-id                                               |
+-------------+----------------------------------------------------------------------+
```

**For `knowledge-query` or `structured-query` types:**
```
+-------------+----------------------------------------------------------------------+
| collection  | collection-name                                                      |
+-------------+----------------------------------------------------------------------+
```

**For `prompt` type:**
```
+-------------+----------------------------------------------------------------------+
| template    | prompt-template-id                                                   |
+-------------+----------------------------------------------------------------------+
| arg 0       | parameter_name: string                                               |
|             | Description of the parameter                                         |
+-------------+----------------------------------------------------------------------+
| arg 1       | another_param: integer                                               |
|             | Description of another parameter                                     |
+-------------+----------------------------------------------------------------------+
```

### Optional Fields (When Present)

**Tool Groups:**
```
+-------------+----------------------------------------------------------------------+
| groups      | group1, group2, group3                                               |
+-------------+----------------------------------------------------------------------+
```

**State Transitions:**
```
+-------------+----------------------------------------------------------------------+
| next state  | state-name                                                           |
+-------------+----------------------------------------------------------------------+
```

**State Availability:**
```
+-------------+----------------------------------------------------------------------+
| available in| all states                                                           |
+-------------+----------------------------------------------------------------------+
```
or
```
+-------------+----------------------------------------------------------------------+
| available in| state1, state2, state3                                               |
+-------------+----------------------------------------------------------------------+
```

### Complete Example Output

```
web-search:
+-------------+----------------------------------------------------------------------+
| id          | web-search                                                           |
+-------------+----------------------------------------------------------------------+
| name        | Web Search                                                           |
+-------------+----------------------------------------------------------------------+
| description | Search the web for information using a search engine                |
+-------------+----------------------------------------------------------------------+
| type        | prompt                                                               |
+-------------+----------------------------------------------------------------------+
| template    | web-search-prompt                                                    |
+-------------+----------------------------------------------------------------------+
| arg 0       | query: string                                                        |
|             | The search query to execute                                          |
+-------------+----------------------------------------------------------------------+
| groups      | web, search                                                          |
+-------------+----------------------------------------------------------------------+
| available in| all states                                                           |
+-------------+----------------------------------------------------------------------+

knowledge-lookup:
+-------------+----------------------------------------------------------------------+
| id          | knowledge-lookup                                                     |
+-------------+----------------------------------------------------------------------+
| name        | Knowledge Graph Query                                                |
+-------------+----------------------------------------------------------------------+
| description | Query the knowledge graph for information                           |
+-------------+----------------------------------------------------------------------+
| type        | knowledge-query                                                      |
+-------------+----------------------------------------------------------------------+
| collection  | default                                                              |
+-------------+----------------------------------------------------------------------+
| groups      | knowledge                                                            |
+-------------+----------------------------------------------------------------------+

```

---

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `TRUSTGRAPH_URL` | Default API URL | `http://localhost:8088/` |
| `TRUSTGRAPH_TOKEN` | Authentication token | None |

**Example:**
```bash
export TRUSTGRAPH_URL=https://trustgraph.example.com
export TRUSTGRAPH_TOKEN=your-auth-token
tg-show-tools
```

---

## Exit Codes

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | Error (prints exception message) |

---

## Related Commands

- [`tg-set-tool`](tg-set-tool) - Configure agent tools
- [`tg-show-mcp-tools`](tg-show-mcp-tools) - Display MCP tool configurations
- [`tg-set-mcp-tool`](tg-set-mcp-tool) - Configure MCP tools
- [`tg-show-config`](tg-show-config) - Show TrustGraph configuration
- [`tg-show-prompts`](tg-show-prompts) - Display available prompts
- [`tg-invoke-agent`](tg-invoke-agent) - Invoke agent with tools
