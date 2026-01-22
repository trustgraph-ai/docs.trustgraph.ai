---
title: CLI
nav_order: 1
has_children: true
parent: Reference
review_date: 2026-12-07
---

# TrustGraph CLI Documentation

The TrustGraph Command Line Interface (CLI) provides comprehensive command-line access to all TrustGraph services. These tools wrap the REST and WebSocket APIs to provide convenient, scriptable access to TrustGraph functionality.

## Installation

The CLI tools are installed as part of the `trustgraph-cli` package:

```bash
pip install trustgraph-cli
```

> [!NOTE]
> The CLI version should match the version of TrustGraph being deployed. 

## Global Options

Most CLI commands support these common options:

- `-u, --api-url URL`: TrustGraph API URL (default: `$TRUSTGRAPH_URL` or `http://localhost:8088/`)
- `-U, --user USER`: User identifier (default: `trustgraph`)
- `-C, --collection COLLECTION`: Collection identifier (default: `default`)
- `-f, --flow-id FLOW`: Flow identifier (default: `default`)

## Command Categories

### System Administration & Configuration

**System Setup:**
- [`tg-init-trustgraph`](tg-init-trustgraph) - Initialize Pulsar with TrustGraph configuration
- [`tg-init-pulsar-manager`](tg-init-pulsar-manager) - Initialize Pulsar manager setup
- [`tg-show-config`](tg-show-config) - Display current system configuration

**Token Management:**
- [`tg-set-token-costs`](tg-set-token-costs) - Configure model token costs
- [`tg-show-token-costs`](tg-show-token-costs) - Display token cost configuration
- [`tg-show-token-rate`](tg-show-token-rate) - Show token usage rates

**Prompt Management:**
- [`tg-set-prompt`](tg-set-prompt) - Configure prompt templates and system prompts
- [`tg-show-prompts`](tg-show-prompts) - Display configured prompt templates

### Flow Management

**Flow Operations:**
- [`tg-start-flow`](tg-start-flow) - Start a processing flow
- [`tg-stop-flow`](tg-stop-flow) - Stop a running flow
- [`tg-show-flows`](tg-show-flows) - List all configured flows
- [`tg-show-flow-state`](tg-show-flow-state) - Show current flow states

**Flow Blueprint Management:**
- [`tg-put-flow-blueprint`](tg-put-flow-blueprint) - Upload/update flow blueprint definition
- [`tg-get-flow-blueprint`](tg-get-flow-blueprint) - Retrieve flow blueprint definition
- [`tg-delete-flow-blueprint`](tg-delete-flow-blueprint) - Remove flow blueprint definition
- [`tg-show-flow-blueprints`](tg-show-flow-blueprints) - List available flow blueprints

### Knowledge Graph Management

**Knowledge Core Operations:**
- [`tg-load-kg-core`](tg-load-kg-core) - Load knowledge core into processing
- [`tg-put-kg-core`](tg-put-kg-core) - Store knowledge core in system
- [`tg-get-kg-core`](tg-get-kg-core) - Retrieve knowledge core
- [`tg-delete-kg-core`](tg-delete-kg-core) - Remove knowledge core
- [`tg-unload-kg-core`](tg-unload-kg-core) - Unload knowledge core from processing
- [`tg-show-kg-cores`](tg-show-kg-cores) - List available knowledge cores

**Graph Data Operations:**
- [`tg-show-graph`](tg-show-graph) - Display graph triples/edges
- [`tg-graph-to-turtle`](tg-graph-to-turtle) - Export graph to Turtle format
- [`tg-load-turtle`](tg-load-turtle) - Import RDF triples from Turtle files

### Document Processing & Library Management

**Document Loading:**
- [`tg-load-pdf`](tg-load-pdf) - Load PDF documents into processing
- [`tg-load-text`](tg-load-text) - Load text documents into processing
- [`tg-load-sample-documents`](tg-load-sample-documents) - Load sample documents for testing

**Library Management:**
- [`tg-add-library-document`](tg-add-library-document) - Add documents to library
- [`tg-show-library-documents`](tg-show-library-documents) - List documents in library
- [`tg-remove-library-document`](tg-remove-library-document) - Remove documents from library
- [`tg-start-library-processing`](tg-start-library-processing) - Start processing library documents
- [`tg-stop-library-processing`](tg-stop-library-processing) - Stop library document processing
- [`tg-show-library-processing`](tg-show-library-processing) - Show library processing status

**Document Embeddings:**
- [`tg-load-doc-embeds`](tg-load-doc-embeds) - Load document embeddings
- [`tg-save-doc-embeds`](tg-save-doc-embeds) - Save document embeddings

### AI Services & Agent Interaction

**Query & Interaction:**
- [`tg-invoke-agent`](tg-invoke-agent) - Interactive agent Q&A via WebSocket
- [`tg-invoke-llm`](tg-invoke-llm) - Direct LLM text completion
- [`tg-invoke-prompt`](tg-invoke-prompt) - Use configured prompt templates
- [`tg-invoke-document-rag`](tg-invoke-document-rag) - Document-based RAG queries
- [`tg-invoke-graph-rag`](tg-invoke-graph-rag) - Graph-based RAG queries
- [`tg-invoke-nlp-query`](tg-invoke-nlp-query) - Convert natural language to GraphQL
- [`tg-invoke-structured-query`](tg-invoke-structured-query) - Execute queries against structured data

**Agent Tool Management:**
- [`tg-set-tool`](tg-set-tool) - Configure agent tools (knowledge-query, text-completion, mcp-tool, prompt)
- [`tg-show-tools`](tg-show-tools) - List available agent tools
- [`tg-delete-tool`](tg-delete-tool) - Remove agent tool configurations

**MCP Tool Management:**
- [`tg-set-mcp-tool`](tg-set-mcp-tool) - Configure MCP (Model Context Protocol) tools
- [`tg-show-mcp-tools`](tg-show-mcp-tools) - List MCP tool configurations
- [`tg-delete-mcp-tool`](tg-delete-mcp-tool) - Remove MCP tool configurations
- [`tg-invoke-mcp-tool`](tg-invoke-mcp-tool) - Test and execute MCP tools directly

**Prompt Management:**
- [`tg-set-prompt`](tg-set-prompt) - Configure prompt templates
- [`tg-show-prompts`](tg-show-prompts) - List configured prompts

### System Monitoring & Debugging

**System Status:**
- [`tg-show-processor-state`](tg-show-processor-state) - Show processing component states

**Debugging:**
- [`tg-dump-msgpack`](tg-dump-msgpack) - Dump MessagePack data for debugging

## Quick Start Examples

### Basic Document Processing
```bash
# Start a flow
tg-start-flow --flow-id my-flow --blueprint-name document-processing

# Load a document
tg-load-text --flow-id my-flow --text "Your document content" --title "Test Document"

# Query the knowledge
tg-invoke-graph-rag --flow-id my-flow --query "What is the document about?"
```

### Knowledge Management
```bash
# List available knowledge cores
tg-show-kg-cores

# Load a knowledge core into a flow
tg-load-kg-core --flow-id my-flow --kg-core-id my-knowledge

# Query the knowledge graph
tg-show-graph --limit 100
```

### Flow Management
```bash
# Show available flow blueprints
tg-show-flow-blueprints

# Show running flows
tg-show-flows

# Stop a flow
tg-stop-flow --flow-id my-flow
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL for all commands
- `TRUSTGRAPH_USER`: Default user identifier
- `TRUSTGRAPH_COLLECTION`: Default collection identifier

## Authentication

CLI commands inherit authentication from the environment or API configuration. See the main TrustGraph documentation for authentication setup.

## Error Handling

All CLI commands provide:
- Consistent error reporting
- Exit codes (0 for success, non-zero for errors)
- Detailed error messages for troubleshooting
- Retry logic for network operations where appropriate

## Related Documentation

- [TrustGraph API Documentation](../apis/README)
- [TrustGraph WebSocket Guide](../apis/websocket)
- [TrustGraph Pulsar Guide](../apis/pulsar)
