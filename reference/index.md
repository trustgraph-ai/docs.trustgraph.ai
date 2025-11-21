---
title: Reference
layout: default
nav_order: 8
has_children: true
parent: TrustGraph Documentation
---

# Reference Documentation

**Technical specifications, API docs, and command references**

## What's in This Section?

This section provides **exhaustive technical details** for developers integrating with TrustGraph or operators managing systems. These are reference materials you look up when you need specific technical information.

### This Section is For:
- **Developers** integrating TrustGraph via APIs
- **DevOps engineers** using CLI tools
- **System integrators** building custom extensions
- **Technical architects** reviewing capabilities

### Not What You Need?
- **Learning how to do something?** → See [How-to Guides](../guides/)
- **Want working code examples?** → Check [Examples](../examples/)
- **Understanding concepts?** → Read [Overview](../overview/)

## Quick Find

### I need to...

| Task | Reference |
|------|-----------|
| Call a TrustGraph API | [API Documentation](apis/) |
| Use a CLI command | [CLI Reference](cli/) |
| Understand container architecture | [Containers](containers) |
| Build a custom processor | [Extending](extending) |
| Use Python libraries | [Python Packages](python-packages) |
| Configure TrustGraph | [Configuration](configuration/) |
| See release notes | [Changelog](changelog/) |

## Reference Categories

### [APIs](apis/)
**HTTP API specifications** - Complete API reference for all TrustGraph services.

**Contains:**
- REST API endpoints
- Request/response formats
- Authentication methods
- Error codes
- WebSocket APIs
- Pulsar message formats

**Use this when**: You're integrating TrustGraph into applications or building custom clients.

**Quick links:**
- [Agent API](apis/api-agent) - AI agent operations
- [Collection API](apis/api-collection) - Collection management
- [Flow API](apis/api-flow) - Processing flow control
- [GraphRAG API](apis/api-graph-rag) - Graph RAG queries
- [Query APIs](apis/) - Various query interfaces

### [CLI Commands](cli/)
**Command-line interface** - Complete reference for all `tg-*` commands.

**Contains:**
- ~60 CLI commands with full syntax
- Usage examples
- Option descriptions
- Output formats

**Use this when**: You're scripting operations, managing TrustGraph from the terminal, or automating workflows.

**Common commands:**
- `tg-load-pdf` - Load PDF documents
- `tg-invoke-graph-rag` - Query using GraphRAG
- `tg-show-graph` - View knowledge graph
- `tg-show-flows` - List processing flows
- [See all commands →](cli/)

### [SDL (Schema Definition Language)](sdl)
**Data schema specifications** - SDL format for defining extraction schemas.

**Contains:**
- SDL syntax reference
- Schema definition examples
- Type system documentation

**Use this when**: Defining custom extraction schemas for structured data.

### [Configuration](configuration/)
**System configuration** - Configuration file formats and options.

**Contains:**
- Configuration file structure
- Environment variables
- Service configuration
- Storage configuration

**Use this when**: Configuring TrustGraph deployments or customizing behavior.

### [Containers](containers)
**Container architecture** - Docker container specifications and architecture.

**Contains:**
- Container image descriptions
- Service dependencies
- Port mappings
- Volume requirements

**Use this when**: Understanding the container architecture or building custom deployments.

### [Python Packages](python-packages)
**Python libraries** - Python package documentation.

**Contains:**
- Package descriptions
- Installation instructions
- API usage

**Use this when**: Using TrustGraph Python libraries in your code.

### [Extending](extending/)
**Custom development** - Building custom processors and services.

**Contains:**
- Processor development guide
- Service extension patterns
- Plugin architecture

**Use this when**: Building custom functionality or extending TrustGraph.

### [Changelog](changelog/)
**Release history** - Version history and release notes.

**Contains:**
- [TrustGraph releases](changelog/trustgraph)
- [Workbench releases](changelog/workbench)
- Breaking changes
- New features

**Use this when**: Checking what's new or planning upgrades.

## Using Reference Documentation

### Reference vs. Guides

**Reference documentation:**
- ✅ Look up specific technical details
- ✅ Check syntax and parameters
- ✅ Find all available options
- ✅ Verify API contracts

**Guides are better for:**
- ❌ Learning how to accomplish tasks
- ❌ Understanding workflows
- ❌ Following step-by-step instructions

### How to Read References

1. **Use search** - Reference docs are designed for lookup, not linear reading
2. **Check examples** - Most references include usage examples
3. **Follow links** - References link to related topics
4. **Copy and adapt** - Code examples are meant to be copied

## API Quick Reference

### Most-Used APIs

| API | Purpose | Doc Link |
|-----|---------|----------|
| Graph RAG | Query knowledge graphs | [api-graph-rag](apis/api-graph-rag) |
| Document RAG | Query documents | [api-document-rag](apis/api-document-rag) |
| Agent | Agent operations | [api-agent](apis/api-agent) |
| Flow | Control processing | [api-flow](apis/api-flow) |
| Collection | Manage collections | [api-collection](apis/api-collection) |
| Objects Query | Query structured data | [api-objects-query](apis/api-objects-query) |
| NLP Query | Natural language queries | [api-nlp-query](apis/api-nlp-query) |

**See complete API index:** [APIs →](apis/)

## CLI Quick Reference

### Most-Used Commands

| Command | Purpose |
|---------|---------|
| `tg-load-pdf` | Load PDF documents |
| `tg-invoke-graph-rag` | Run GraphRAG queries |
| `tg-show-graph` | Display knowledge graph |
| `tg-show-flows` | List processing flows |
| `tg-start-flow` | Start a processing flow |
| `tg-show-processor-state` | Check system status |

**See complete CLI index:** [CLI →](cli/)

## Next Steps

### Ready to Integrate?

1. **Start with**: [API Documentation](apis/) or [CLI Reference](cli/)
2. **Follow**: [How-to Guides](../guides/) for integration patterns
3. **Use**: [Examples](../examples/) for working code

### Building Extensions?

1. **Read**: [Extending](extending/) for architecture
2. **Review**: [Python Packages](python-packages) for libraries
3. **Check**: [Containers](containers) for deployment

### Need Help?

- **Can't find what you need?** Use site search (Ctrl+K)
- **API not working as expected?** Check [Troubleshooting](../deployment/troubleshooting)
- **Have questions?** Visit [Getting Help](../contributing/getting-help)
