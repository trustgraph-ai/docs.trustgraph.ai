---
title: Changelog - TrustGraph
nav_order: 1
parent: Reference
grand_parent: TrustGraph Documentation
review_date: 2026-02-01
---

# Changelog

## v1.4.0 (2025-10-06)

### New Features
- **Flow Configurable Parameters** (#526, #530, #531, #532, #533, #541):
  Major enhancements to flow parameter system:
  - Flow configurable parameters with dynamic settings
  - LLM dynamic settings using llm-model and llm-rag-model parameters
  - Temperature parameter support for all LLMs
  - Flow creation uses parameter defaults in API and CLI
  - Advanced parameter mode with controlled-by relationships
  - New CLI tools: tg-show-parameter-types
  - Dynamic chunking parameters
- **Structured Data Diagnosis Service** (#518, #519):
  - New structured data diagnosis service plumbed into API gateway
  - Added XML, JSON, CSV detection capabilities
  - Type detector with schema selection
- **Enhanced Collection Management** (#520, #522, #542, #544):
  - Collection metadata management and deletion capabilities
  - Librarian services integrated with collection manager
  - Collection tracking across all processors
  - Explicit collection creation/deletion (removed implicit creation)
  - Fixed collection management synchronization issues
- **User/Collection Isolation** (#509, #510):
  - Neo4j user/collection separation
  - Memgraph user/collection processing

### Improvements
- **Cassandra Performance** (#521):
  - Refactored Cassandra knowledge graph for single table
  - Multi-table implementation for performance enhancement
  - Added Cassandra collection table
- **GraphRAG Optimizations** (#527): Implemented GraphRAG optimizations with
  updated tests
- **Vector Store Enhancements** (#512): Vector stores now create collections
  on query
- **Build System** (#515): Parallel container builds
- **Logging** (#528, #543): Reduced excessive request/response logging and
  log spam

### Bug Fixes
- **Collection Management** (#544): Fixed collection management
  synchronization problems
- **Metrics** (#539, #540): Fixed label names and label issues in metrics
- **WebSocket** (#517): Fixed async websocket closure handling
- **CLI** (#529): Fixed CLI typo
- **Tests** (#534, #535): Fixed failing tests and improved LLM parameter
  test coverage
- **Object Writer** (#544): Fixed object writer management issues
- **Milvus** (#544): Updated Milvus to use ANN correctly

### API Changes
- **Gateway** (#514): Return empty embeddings list as empty list through
  gateway.
- **Parameters**: Changed `parameters` to `parameter-types` for consistency

---

## v1.3.0

### New Features
- **Structured Data Enhancements** (#492, #493, #496, #498, #500): Major improvements to structured data handling:
  - NLP query to GraphQL service for natural language database queries
  - Structured query tool integration with agent framework
  - Enhanced structured query support and object batching
  - Structured data loader CLI with auto mode functionality
  - Object import capabilities with batch processing
- **Collection Management** (#503, #511):
  - Extended use of user + collection fields throughout the system
  - Stores automatically create collections on query
- **Tool Groups** (#484): Added tool grouping functionality for better organization

### Improvements
- **GraphQL Enhancements** (#486, #489):
  - Added GraphQL table query support
  - Removed redundant GraphQL collection parameter
- **Cassandra Configuration Standardization** (#483, #488, #490):
  - Made Cassandra options (user, password, host) consistent across all utilities
  - Consolidated Cassandra configuration for better consistency
  - Refactored Cassandra operations to use common helper functions
- **API Improvements** (#513): Return empty embeddings list as empty list through gateway

### Bug Fixes
- **Vector Store Fixes** (#507): Fixed Milvus vector store integration issues
- **Document Processing** (#506): Fixed document RAG processing issues
- **Monitoring** (#502): Fixed Prometheus incorrect metric names
- **API Consistency** (#481): Fixed trustgraph-base chunks/documents confusion in the API
- **System Integration** (#494): Resolved various system integration issues
- **Import/Export** (#476): Fixed graceful shutdown for import/export operations
- **Knowledge Loading** (#472): Use collection field from request when loading knowledge core

---

## v1.2.17

### New Features
- **MCP Tool Arguments Support** (#462): Added support for Model Context Protocol (MCP) tool arguments, including agent support and additional tests
- **Anthropic Support for VertexAI** (#458): Added Anthropic model support for Google Vertex AI platform
- **Knowledge Load Utility CLI** (#456): New command-line utility for loading knowledge into the system
- **Structured Data MVP** (#452): Initial implementation of structured data handling with:
  - New schemas and architecture principles
  - Object extractor functionality
  - Cassandra object storage support
- **Knowledge Extraction via Agent Framework** (#439): 
  - Implemented KG extraction agent (kg-extract-agent)
  - Using ReAct framework (agent-manager-react)
  - Refactored ReAct manager to use traditional ReAct messages

### Improvements
- **Agent Tool Coverage** (#460): Increased ReAct tool coverage with multi-step tool invocation and reasoning tests
- **Schema Structure Refactor** (#451): Major refactoring of schema structure for better organization
- **Logging Strategy** (#444): Implemented comprehensive logging strategy, converting all print() statements to proper logging invocations
- **Build System Modernization** (#440): Migrated from setup.py to pyproject.toml for modern package infrastructure

### Bug Fixes
- **Agent Tool Resilience** (#461): 
  - Fixed incorrect tool initialization in agent service
  - Made Action parsing more resilient by handling quotation marks
- **Missing Anthropic Import** (#459): Fixed missing import for Anthropic functionality
- **Token Chunker API** (#454, #455): Fixed broken API invocation in token chunker
- **Librarian Collection Validation** (#453): Added validation for librarian collections
- **Mistral OCR** (#448, #450): 
  - Fixed Mistral OCR to use current API
  - Corrected Mistral OCR identifier to standard pdf-decoder
- **Logging Startup Issues** (#445, #446, #447): Resolved multiple logging startup problems

### Infrastructure
- **Build Dependencies** (#441, #442): Added missing build dependencies
- **Template Addition** (#463): Added new template support
- **Python Dependencies**: Updated Python dependencies to version 1.2

### Testing
- **PDF Decoder Tests**: Added comprehensive tests for PDF decoder functionality
- **MCP Arguments Tests**: Added test coverage for MCP tool arguments
- **Multi-step Reasoning Tests**: New tests for multi-step tool invocation scenarios

## v1.1.10
### New Features
- **MCP (Model Context Protocol) Support**: Added MCP server and client support (#419, #425, #426, #427, #428)
- **React Integration**: Added React call MCP functionality (#428)

### Improvements
- Documentation updates for API/CLI changes in v1.0 (#420, #421)
- Enhanced README with messaging improvements and link fixes

---

## v1.0.22
### Major Features
- **Flow API & Management**: Complete flow configuration and management system (#345, #346, #356, #357, #358)
- **Knowledge Management**: Knowledge service, library management, and core CLI tools (#367, #368, #369, #372)
- **Enhanced Gateway**: Reverse gateway functionality and improved API gateway (#416, #356)
- **Performance Improvements**: Multi-threading support for consumers and LLMs (#408, #409)

### New Integrations
- **vLLM Support**: Added vLLM integration (untested) (#410)
- **HuggingFace TGI**: Added HuggingFace Text Generation Inference support (#396)
- **Google AI Updates**: Enhanced Google AI integration (#394)

### Bug Fixes & Improvements
- Fixed command line arguments handling (#417)
- Fixed library translators (#415)
- Fixed missing script issues (#418)
- Improved token rate measurement utility (#412)
- Enhanced translator classes (#414)
- Miscellaneous fixes (#413)

---

## v0.23
### New Features
- **Knowledge Service**: Full knowledge management system with CLI tools
- **Library Management**: Document submission and library CLI functionality
- **Entity Contexts**: Import/export capabilities for entity contexts
- **Configuration Persistence**: Enhanced config management and reload mechanisms

### Infrastructure
- **Container Updates**: Upgraded to Python 3.12 (#386)
- **OCR Improvements**: Ported OCR code to new API architecture
- **Apache 2 License**: Updated licensing (#373)

### Bug Fixes
- Fixed LLM launch bugs (#377, #378)
- Fixed queue initialization issues (#381, #382)
- Fixed chunking not being enabled (#364)
- Fixed OpenAI base URL handling

---

## v0.22
### Major Features
- **Configuration Service**: Dynamic configuration management (#332, #334, #335)
- **Prompt Management**: Dynamic prompt loading and CLI commands (#338)
- **Agent Management**: Enhanced agent configuration system

### Infrastructure Changes
- Removed template directory (moved to separate repository) (#336)
- Enhanced configuration initialization (#335)
- Added config reload handler mechanism (#334)

---

## v0.21
### New Features
- **Librarian Service**: Document processing and management (#304, #305, #307, #310, #311)
- **Mistral AI Support**: Complete Mistral API integration including OCR (#313, #326)
- **LM Studio Integration**: Added LM Studio LLM hosting support (#323, #328)
- **PDF OCR**: Separate PDF OCR package with Tesseract support (#324)
- **Cassandra Integration**: Added Cassandra auth with SSL support (#318)

### Cloud & Infrastructure
- **Azure AKS**: Azure Kubernetes Service integration (#317, #319)
- **AWS Bedrock**: Inference profiles support (#314)
- **FastEmbed**: Enabled FastEmbed component (#316)

### API Improvements
- **Pulsar API Key**: Added API key support (#308)
- **Async/Sync Fixes**: Resolved async/sync loading issues (#315)
- **GraphRAG & DocRAG**: Enhanced parameters and path hops (#312)

### Bug Fixes
- Fixed broken setup.py (#320)
- Fixed async send typos (#322)
- Fixed container build issues (#325)
- Fixed missing OpenAI symbol and base URL specification (#330)
- Fixed Bedrock integration issues (#331)

