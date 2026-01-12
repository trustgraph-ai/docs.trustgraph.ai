---
title: Introduction to command-line tools
nav_order: 2.2
parent: How-to Guides
grand_parent: TrustGraph Documentation
review_date: 2026-08-01
guide_category:
  - Building with TrustGraph
guide_category_order: 2
guide_description: Learn to use TrustGraph command-line tools for document processing and knowledge graph operations
guide_difficulty: beginner
guide_time: 15 min
guide_emoji: 💻
guide_banner: /../cli.jpg
guide_labels:
  - CLI
  - Command-line
todo: true
todo_notes: This is just a placeholder.
---

# Getting started with TrustGraph command-line tools

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>A running TrustGraph deployment</li>
<li>Basic command-line familiarity</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Learn to use TrustGraph command-line tools for common tasks and automation."
%}

## Command-line tools installation

The TrustGraph CLI tools are provided in the `trustgraph-cli` Python package.

The CLI tools version should match your deployed TrustGraph version. Check your deployment version and install the corresponding CLI version.

{% capture pip_install_version %}
```bash
pip install trustgraph-cli==1.8.10
```
{% endcapture %}

{% capture uv_install_version %}
```bash
uv pip install trustgraph-cli==1.8.10
```
{% endcapture %}

{% capture poetry_install_version %}
```bash
poetry add trustgraph-cli@1.8.10
```
{% endcapture %}

{% include code_tabs.html
   tabs="pip,uv,poetry"
   content1=pip_install_version
   content2=uv_install_version
   content3=poetry_install_version
%}

## Command-line tools by category

### Flows

- `tg-show-flows` - List flows
- `tg-show-flow-state` - Show flow state
- `tg-start-flow` - Start a flow
- `tg-stop-flow` - Stop a flow
- `tg-show-flow-classes` - List flow classes
- `tg-get-flow-class` - Get flow class details
- `tg-put-flow-class` - Update flow class
- `tg-delete-flow-class` - Delete flow class

### Document library management

- `tg-add-library-document` - Add document to library
- `tg-remove-library-document` - Remove document from library
- `tg-show-library-documents` - List library documents
- `tg-show-library-processing` - Show library processing status
- `tg-start-library-processing` - Start processing library documents
- `tg-stop-library-processing` - Stop library processing

### Getting started

- `tg-load-sample-documents` - Load sample documents for testing

### System monitoring

- `tg-verify-system-status` - Verify system health
- `tg-show-processor-state` - Show processor state
- `tg-show-parameter-types` - List parameter types

### Querying and retrieval

- `tg-invoke-llm` - Invoke LLM directly
- `tg-invoke-prompt` - Execute a prompt
- `tg-invoke-document-rag` - Query using Document RAG
- `tg-invoke-graph-rag` - Query using Graph RAG
- `tg-invoke-nlp-query` - Execute NLP query
- `tg-invoke-objects-query` - Query objects
- `tg-invoke-structured-query` - Execute structured query
- `tg-invoke-agent` - Invoke an agent

### Knowledge graph management

- `tg-load-kg-core` - Load knowledge graph core
- `tg-unload-kg-core` - Unload knowledge graph core
- `tg-show-kg-cores` - List knowledge graph cores
- `tg-get-kg-core` - Get knowledge graph core details
- `tg-put-kg-core` - Update knowledge graph core
- `tg-delete-kg-core` - Delete knowledge graph core
- `tg-show-graph` - Display graph structure
- `tg-graph-to-turtle` - Export graph to Turtle format

### Embeddings management

- `tg-load-doc-embeds` - Load document embeddings
- `tg-save-doc-embeds` - Save document embeddings

### Collections

- `tg-list-collections` - List all collections
- `tg-set-collection` - Set current collection
- `tg-delete-collection` - Delete a collection

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
