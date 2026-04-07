---
title: Config Types
parent: Configuration
grand_parent: Reference
nav_order: 4
permalink: /reference/configuration/config-types
review_date: 2027-01-01
---

# Configuration Types

TrustGraph stores runtime configuration as typed key-value items in the
config service. Each item has a **type**, a **key**, and a JSON **value**.
Items are managed with the
[`tg-put-config-item`](../cli/tg-put-config-item),
[`tg-get-config-item`](../cli/tg-get-config-item),
[`tg-list-config-items`](../cli/tg-list-config-items), and
[`tg-delete-config-item`](../cli/tg-delete-config-item) CLI commands
(some types also have dedicated CLI tools).

This page documents the general-purpose config types. For agent-specific
types see [Agent Patterns](agent-patterns) and
[Agent Task Types](agent-task-types).

---

## token-cost

Defines per-model token pricing used by the metering processor to
calculate LLM costs via Prometheus metrics.

### Structure

```json
{
  "input_price": 0.01,
  "output_price": 0.03
}
```

| Field | Type | Description |
|-------|------|-------------|
| `input_price` | float | Price per 1M input tokens (USD) |
| `output_price` | float | Price per 1M output tokens (USD) |

The config key is the model identifier (e.g. `claude-sonnet-4-20250514`,
`gpt-4o`).

### Management

```bash
# Dedicated CLI
tg-set-token-costs --model gpt-4o --input-costs 0.0025 --output-costs 0.01
tg-show-token-costs

# Or generic CLI
tg-put-config-item --type token-cost --key gpt-4o --value '{
  "input_price": 0.0025, "output_price": 0.01
}'
```

---

## tool

Defines a tool available to the agent framework. Each tool maps a
function name that the LLM can invoke to a backend implementation.

### Structure

```json
{
  "name": "search_knowledge",
  "description": "Search the knowledge graph for information",
  "type": "knowledge-query",
  "arguments": [
    {
      "name": "query",
      "type": "string",
      "description": "The search query"
    }
  ],
  "collection": "default",
  "group": ["knowledge"],
  "state": "has-context",
  "applicable-states": ["initial", "has-context"]
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Function name the LLM uses to invoke the tool |
| `description` | Yes | Human-readable description presented to the LLM |
| `type` | Yes | Implementation type (see below) |
| `arguments` | Depends on type | List of argument definitions |
| `collection` | No | Target collection for query-based tools |
| `group` | No | Tool group tags for filtering |
| `state` | No | State to transition to after execution |
| `applicable-states` | No | States in which this tool is available |

### Tool Types

| Type | Description | Key Fields |
|------|-------------|------------|
| `knowledge-query` | GraphRAG query against a collection | `collection` |
| `structured-query` | NLP query against structured data | `collection` |
| `row-embeddings-query` | Semantic search on structured data rows | `collection`, `schema-name`, `index-name`, `limit` |
| `text-completion` | Direct LLM text completion | |
| `prompt` | Invoke a prompt template | `template` |
| `mcp-tool` | Invoke an MCP tool | `mcp-tool` |
| `tool-service` | Invoke a dynamic tool service | `service` |

### Management

```bash
# Dedicated CLI
tg-set-tool --id kg-search --name search_knowledge \
  --type knowledge-query --description "Search the knowledge graph" \
  --collection default

tg-show-tools
tg-delete-tool --id kg-search

# Or generic CLI
tg-put-config-item --type tool --key kg-search --value '{ ... }'
```

---

## prompt

Defines prompt templates used by the prompt service. Templates support
placeholder substitution with `{variable}` syntax.

### Structure (Template)

```json
{
  "id": "extract-entities",
  "prompt": "Extract entities from the following text:\n\n{text}",
  "response-type": "json",
  "schema": { ... }
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | Template identifier |
| `prompt` | Yes | Template text with `{placeholder}` variables |
| `response-type` | No | `text` (default) or `json` |
| `schema` | No | JSON schema for validating JSON responses |

### The `system` Key

The key `system` is special: it stores the global system prompt as a
plain string (not a template object). This system prompt is prepended to
all prompt-based LLM interactions.

```bash
tg-set-prompt --system "You are a helpful assistant specialising in financial analysis."
```

### Management

```bash
# Dedicated CLI
tg-set-prompt --id my-template --prompt "Summarise: {text}" --response text
tg-show-prompts

# Set system prompt
tg-set-prompt --system "You are a helpful assistant."
```

---

## mcp

Defines MCP (Model Context Protocol) server endpoints that TrustGraph
can connect to for tool execution.

### Structure

```json
{
  "remote-name": "calculator",
  "url": "http://mcp-server:3000/tools",
  "auth-token": "bearer-token-value"
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `remote-name` | Yes | Tool name as known by the MCP server |
| `url` | Yes | HTTP endpoint of the MCP server |
| `auth-token` | No | Bearer token for authentication |

The config key is the local MCP tool identifier, referenced by `tool`
items of type `mcp-tool`.

### Management

```bash
# Dedicated CLI
tg-set-mcp-tool --id calculator --remote-name calculator \
  --tool-url "http://mcp-server:3000/tools" \
  --auth-token "my-token"

tg-show-mcp-tools
tg-delete-mcp-tool --id calculator
```

---

## collection

Defines collection metadata. Collections provide data isolation,
allowing multiple independent datasets within a single TrustGraph
deployment.

### Structure

```json
{
  "user": "trustgraph",
  "collection": "research-2026",
  "name": "2026 Research Papers",
  "description": "Research papers ingested during 2026",
  "tags": ["research", "2026"]
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `user` | Yes | Owner user identifier |
| `collection` | Yes | Collection identifier (must match config key) |
| `name` | No | Human-readable display name |
| `description` | No | Description of the collection's contents |
| `tags` | No | List of tags for categorisation |

### Management

```bash
# Dedicated CLI
tg-set-collection research-2026 \
  --name "2026 Research Papers" \
  --description "Research papers ingested during 2026" \
  --tag research --tag 2026

tg-list-collections
tg-delete-collection research-2026
```

---

## interface-description

Describes the pub/sub interfaces exposed by a flow. Used by CLI tools
such as `tg-show-flows` to display human-readable interface information.

### Structure

```json
{
  "visible": true,
  "description": "Graph RAG Query",
  "kind": "request-response",
  "request": "request:tg:graph-rag",
  "response": "response:tg:graph-rag"
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `visible` | Yes | Whether the interface is shown in UI and CLI output |
| `description` | Yes | Human-readable interface name |
| `kind` | Yes | `request-response` or `send` |
| `request` | For request-response | Request queue name |
| `response` | For request-response | Response queue name |
| `queue` | For send | Target queue name |

Interface descriptions are typically set during flow deployment and do
not usually need to be managed manually.

---

## tool-service

Defines a dynamic tool service that can be invoked by the agent
framework. Tool services are standalone processors that expose a
request/response interface, allowing custom tool implementations to be
deployed independently.

### Structure

```json
{
  "id": "custom-rag",
  "request-queue": "request:tg:custom-rag",
  "response-queue": "response:tg:custom-rag",
  "config-params": [
    { "name": "collection", "required": true }
  ]
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | Service identifier (must match config key) |
| `request-queue` | Yes | Queue for sending requests to the service |
| `response-queue` | Yes | Queue for receiving responses from the service |
| `config-params` | No | List of configuration parameters the service accepts |

Tool services are referenced by `tool` items with `type: "tool-service"`
and `service: "<service-id>"`. When the agent invokes such a tool, the
request includes the user, any config parameter values, and the tool
arguments.

### Management

```bash
tg-put-config-item --type tool-service --key custom-rag --value '{
  "id": "custom-rag",
  "request-queue": "request:tg:custom-rag",
  "response-queue": "response:tg:custom-rag"
}'
```

---

## See Also

- [Agent Patterns](agent-patterns) - `agent-pattern` config type
- [Agent Task Types](agent-task-types) - `agent-task-type` config type
- [Ontologies](ontologies) - `ontology` config type
- [Schemas](schemas) - `schema` config type
- [Parameter Types](parameters) - `parameter-types` config type
- [Flow Blueprints](flow-blueprints) - `flow-blueprint` config type
- [CLI Reference](../cli/) - CLI commands for config management
