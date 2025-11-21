---
title: How-to Guides
layout: default
nav_order: 7
has_children: true
parent: TrustGraph Documentation
---

# How-to Guides

**Task-oriented instructions for accomplishing specific goals with TrustGraph.**

Guides answer the question **"How do I...?"** with step-by-step instructions. Each guide focuses on a single task or workflow and provides practical, actionable steps.

## What's in This Section?

**How-to Guides** are practical instructions for:
- Completing specific tasks
- Implementing features
- Integrating with other systems
- Solving common problems

**Not sure if you're in the right place?**
- Want working code to copy? See [Examples](../examples/)
- Want to understand concepts? See [Overview](../overview/)
- Want API reference? See [Reference](../reference/)

## Available Guides

### Agent & Object Extraction
- **[Agent Extraction](agent-extraction)** - Use AI agents to extract structured data from documents
- **[Object Extraction](object-extraction)** - Extract typed objects (products, people, events) from unstructured text

### Structured Data Processing
- **[Structured Processing](structured-processing/)** - Working with structured data extraction
  - [Schemas](structured-processing/schemas) - Define extraction schemas
  - [Load Documents](structured-processing/load-doc) - Load documents for structured extraction
  - [Load Files](structured-processing/load-file) - Load file-based data
  - [Query Data](structured-processing/query) - Query extracted structured data
  - [Agent Integration](structured-processing/agent-integration) - Integrate with AI agents

### Integrations
- **[MCP Integration](mcp-integration/)** - Integrate with Model Context Protocol

### Monitoring & Operations
- **[Monitoring](monitoring/)** - Set up metrics, alerts, and observability

## Planned Guides

{: .wip }
> **Work in Progress**
> The following guides are planned for future releases:

- **RAG Workflows** - DocumentRAG, GraphRAG, and OntologyRAG guides (Phase 4 of refactoring)
- **Security** - Authentication, authorization, and encryption setup
- **Data Integration** - Advanced data loading and processing patterns
- **Querying** - Query optimization and advanced patterns
- **Visualization** - Graph visualization and custom dashboards

## Guide Structure

Each guide follows this format:

1. **Goal**: What you'll accomplish
2. **Prerequisites**: What you need before starting
3. **Steps**: Numbered, actionable instructions
4. **Verification**: How to confirm success
5. **Next Steps**: Related tasks or advanced topics

## Finding the Right Guide

**I want to...**

| Task | Guide |
|------|-------|
| Extract structured data from PDFs | [Agent Extraction](agent-extraction) |
| Extract typed objects (products, etc.) | [Object Extraction](object-extraction) |
| Define what data to extract | [Structured Processing: Schemas](structured-processing/schemas) |
| Query extracted data | [Structured Processing: Query](structured-processing/query) |
| Integrate with MCP | [MCP Integration](mcp-integration/) |
| Monitor TrustGraph | [Monitoring](monitoring/) |

## Contributing Guides

Want to contribute a guide? See our [Contributing Guidelines](../contributing/contributing) for:
- Guide writing templates
- Style guidelines
- How to submit new guides

