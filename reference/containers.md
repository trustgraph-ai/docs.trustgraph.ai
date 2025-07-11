---
title: Containers
layout: default
nav_order: 3
parent: Reference
---

# TrustGraph Containers

TrustGraph uses a modular container architecture where different containers provide specialized capabilities. This approach allows for flexible deployment where only needed capabilities are included, reducing resource usage and attack surface while maintaining full functionality when all containers are deployed together.

## Container Overview

### trustgraph-base
**Purpose**: Foundation container with basic building blocks, client APIs, and base classes.

**Key Features**:
- Core Python runtime (3.12)
- Basic HTTP client capabilities (`aiohttp`)
- Pulsar messaging system integration
- Foundational libraries for other containers

**Use Case**: Required as a base layer for other containers. Contains minimal dependencies focused on core messaging and HTTP capabilities.

### trustgraph-flow
**Purpose**: Main processing container containing the bulk of TrustGraph's capabilities.

**Key Features**:
- **Multi-provider AI integration**: OpenAI, Anthropic, Cohere, Mistral, Google Generative AI, Ollama
- **LangChain ecosystem**: Complete text processing and splitting capabilities
- **Database support**: Vector databases (Milvus), Graph databases (Neo4j, FalkorDB), Cassandra
- **RDF/Semantic web**: Advanced graph processing capabilities
- **Document processing**: Comprehensive text analysis and manipulation

**Use Case**: Core container for most TrustGraph workflows. Deploy when you need full AI processing capabilities, document handling, or database integration.

### trustgraph-mcp
**Purpose**: Model Context Protocol (MCP) server functionality.

**Key Features**:
- MCP server implementation
- WebSocket-based communication
- Lightweight protocol handling

**Use Case**: Deploy when you need MCP server capabilities for model context management and protocol-based communication.

### trustgraph-hf
**Purpose**: Hugging Face model processing with local ML inference.

**Key Features**:
- **PyTorch support**: CPU-optimized PyTorch runtime
- **Hugging Face integration**: Transformers, sentence transformers, embeddings
- **Local ML inference**: Run models without external API calls
- **Pre-loaded models**: Common embedding models (all-MiniLM-L6-v2)

**Use Case**: Deploy when you need local ML model inference, text embeddings, or want to avoid external API dependencies for certain AI tasks.

### trustgraph-ocr
**Purpose**: Optical Character Recognition and document processing.

**Key Features**:
- **Tesseract OCR**: Text extraction from images
- **PDF processing**: Document analysis and content extraction (Poppler utilities)
- **Document workflows**: Complete document processing pipeline

**Use Case**: Deploy when you need to process scanned documents, extract text from images, or handle PDF document analysis.

### trustgraph-bedrock
**Purpose**: AWS Bedrock AI services integration.

**Key Features**:
- AWS Bedrock model access
- Cloud-based AI inference
- Lightweight AWS-specific integration

**Use Case**: Deploy when using AWS Bedrock as your AI provider. Provides dedicated integration without the overhead of other AI providers.

### trustgraph-vertexai
**Purpose**: Google Vertex AI integration.

**Key Features**:
- Google Cloud Vertex AI model access
- Cloud-based AI inference
- Google AI Platform SDK integration

**Use Case**: Deploy when using Google Vertex AI as your AI provider. Provides dedicated integration for Google's AI/ML platform.

## Architecture Principles

### Modular Design
Each container is purpose-built for specific AI providers or capabilities. This allows you to:
- Mix and match containers based on deployment needs
- Reduce resource usage by only including necessary dependencies
- Minimize attack surface by avoiding unused components
- Scale individual components independently

### Common Foundation
All containers share common patterns:
- **Base OS**: Fedora 42 for security and stability
- **Python Runtime**: Python 3.12 for modern language features
- **Messaging**: Pulsar messaging system for distributed communication
- **Build Strategy**: Multi-stage builds for optimized container sizes

### Deployment Flexibility

**Minimal Deployment**: 
- `trustgraph-base` + `trustgraph-flow` for basic AI capabilities
- Add `trustgraph-mcp` for protocol support

**Document Processing**:
- Add `trustgraph-ocr` for document analysis workflows

**Local ML Processing**:
- Add `trustgraph-hf` for local model inference without external APIs

**Cloud AI Integration**:
- Add `trustgraph-bedrock` for AWS Bedrock
- Add `trustgraph-vertexai` for Google Vertex AI

**Full Deployment**:
- All containers for complete functionality across all supported platforms and capabilities

## Container Dependencies

```
trustgraph-base (foundation)
├── trustgraph-flow (main processing)
├── trustgraph-mcp (protocol server)
├── trustgraph-hf (local ML)
├── trustgraph-ocr (document processing)
├── trustgraph-bedrock (AWS AI)
└── trustgraph-vertexai (Google AI)
```

Most containers depend on `trustgraph-base` for core functionality, while specialized containers can be deployed independently based on your specific requirements.
