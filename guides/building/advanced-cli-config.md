---
title: Command-line advanced configuration
nav_order: 2.6
parent: How-to Guides
grand_parent: TrustGraph Documentation
review_date: 2026-08-01
guide_category:
  - Building with TrustGraph
guide_category_order: 6
guide_description: Configure prompts, tools, and system settings using advanced command-line tools
guide_difficulty: advanced
guide_time: 45 min
guide_emoji: ⚙️
guide_banner: /../cli-config.jpg
guide_labels:
  - CLI
  - Configuration
  - Advanced
todo: true
todo_notes: This is just a placeholder.
---

# Advanced configuration settings with command-line tools

### Getting started

- `tg-load-sample-documents` - Load sample documents for testing

### System monitoring

- `tg-verify-system-status` - Verify system health
- `tg-show-processor-state` - Show processor state
- `tg-show-parameter-types` - List parameter types

### Context core management

- `tg-load-kg-core` - Load knowledge graph core
- `tg-unload-kg-core` - Unload knowledge graph core
- `tg-show-kg-cores` - List knowledge graph cores
- `tg-get-kg-core` - Get knowledge graph core details
- `tg-put-kg-core` - Update knowledge graph core
- `tg-delete-kg-core` - Delete knowledge graph core

### Knowledge graph management

- `tg-show-graph` - Display graph structure
- `tg-graph-to-turtle` - Export graph to Turtle format

### Embeddings management

- `tg-load-doc-embeds` - Load document embeddings
- `tg-save-doc-embeds` - Save document embeddings

### Tools and MCP

- `tg-show-tools` - List available tools
- `tg-set-tool` - Configure a tool
- `tg-delete-tool` - Delete a tool
- `tg-show-mcp-tools` - List MCP tools
- `tg-set-mcp-tool` - Configure MCP tool
- `tg-delete-mcp-tool` - Delete MCP tool
- `tg-invoke-mcp-tool` - Invoke MCP tool

### Prompts

- `tg-show-prompts` - List prompts
- `tg-set-prompt` - Configure a prompt

### Configuration

- `tg-show-config` - Display configuration
- `tg-list-config-items` - List configuration items
- `tg-get-config-item` - Get configuration item
- `tg-put-config-item` - Update configuration item
- `tg-delete-config-item` - Delete configuration item

### Token management

- `tg-show-token-costs` - Display token costs
- `tg-show-token-rate` - Show token rate
- `tg-set-token-costs` - Configure token costs

### Initialization and utilities

- `tg-init-trustgraph` - Initialize TrustGraph
- `tg-dump-msgpack` - Dump MessagePack data
- `tg-dump-queues` - Dump queue contents
