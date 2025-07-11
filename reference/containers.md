---
title: Containers
layout: default
nav_order: 3
parent: Reference
---

# TrustGraph Containers

TrustGraph uses a modular container architecture where different containers provide specialized capabilities. This approach allows for flexible deployment where only needed capabilities are included, reducing resource usage and attack surface while maintaining full functionality when all containers are deployed together.

## Container Overview

| Container | Purpose | Key Features | Use Case |
|-----------|---------|--------------|----------|
| **trustgraph-base** | Foundation container with basic building blocks, client APIs, and base classes | • Core Python runtime (3.12)<br>• Basic HTTP client capabilities (`aiohttp`)<br>• Pulsar messaging system integration<br>• Foundational libraries for other containers | Required as a base layer for other containers. Contains minimal dependencies focused on core messaging and HTTP capabilities. |
| **trustgraph-flow** | Main processing container containing the bulk of TrustGraph's capabilities | • Multi-provider AI integration (OpenAI, Anthropic, Cohere, Mistral, Google Generative AI, Ollama)<br>• LangChain ecosystem with complete text processing<br>• Database support (Milvus, Neo4j, FalkorDB, Cassandra)<br>• RDF/Semantic web capabilities<br>• Document processing and analysis | Core container for most TrustGraph workflows. Deploy when you need full AI processing capabilities, document handling, or database integration. |
| **trustgraph-mcp** | Model Context Protocol (MCP) server functionality | • MCP server implementation<br>• WebSocket-based communication<br>• Lightweight protocol handling | Deploy when you need MCP server capabilities for model context management and protocol-based communication. |
| **trustgraph-hf** | Hugging Face model processing with local ML inference | • PyTorch support (CPU-optimized)<br>• Hugging Face integration (Transformers, sentence transformers, embeddings)<br>• Local ML inference without external API calls<br>• Pre-loaded models (all-MiniLM-L6-v2) | Deploy when you need local ML model inference, text embeddings, or want to avoid external API dependencies for certain AI tasks. |
| **trustgraph-ocr** | Optical Character Recognition and document processing | • Tesseract OCR for text extraction from images<br>• PDF processing with Poppler utilities<br>• Complete document processing pipeline | Deploy when you need to process scanned documents, extract text from images, or handle PDF document analysis. |
| **trustgraph-bedrock** | AWS Bedrock AI services integration | • AWS Bedrock model access<br>• Cloud-based AI inference<br>• Lightweight AWS-specific integration | Deploy when using AWS Bedrock as your AI provider. Provides dedicated integration without the overhead of other AI providers. |
| **trustgraph-vertexai** | Google Vertex AI integration | • Google Cloud Vertex AI model access<br>• Cloud-based AI inference<br>• Google AI Platform SDK integration | Deploy when using Google Vertex AI as your AI provider. Provides dedicated integration for Google's AI/ML platform. |

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
- `trustgraph-base` as a base for extension
- `trustgraph-flow` for the most common AI capabilities
- `trustgraph-mcp` for MCP protocol suppport

**Document Processing**:
- Add `trustgraph-ocr` for document OCR with Tesseract

**Local ML Processing**:
- Add `trustgraph-hf` for local model inference without external APIs

**Cloud AI Integration**:
- Add `trustgraph-bedrock` for AWS Bedrock
- Add `trustgraph-vertexai` for Google Vertex AI (Google AIStudio is supported
  in `trustgraph-flow`.

## Container Dependencies

```
trustgraph-base (foundation)
├── trustgraph-flow (most of the capability is here)
├── trustgraph-hf (HuggingFace, local ML, transformers model)
├── trustgraph-ocr (tesseract)
├── trustgraph-bedrock (AWS Bedrock)
└── trustgraph-vertexai (Google AI with VertexAI libraries)
trustgraph-mcp (MCP protocol server)
```

Most containers depend on `trustgraph-base` for core functionality, while specialized containers can be deployed independently based on your specific requirements.
