---
title: Changelog - TrustGraph
layout: default
nav_order: 1
parent: Community
grand_parent: TrustGraph Documentation
---

# Changelog

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

