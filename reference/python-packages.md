---
title: Python packages
nav_order: 4
parent: Reference
review_date: 2026-02-01
---

# Python Packages

TrustGraph is distributed as a collection of Python packages available on PyPI. Each package provides specific functionality while maintaining minimal dependencies to avoid large installation footprints.

## Installation

All packages are available on PyPI and can be installed using pip:

```bash
pip install trustgraph-base
pip install trustgraph-flow
pip install trustgraph-cli
# ... and so on
```

Note that all packages depend on `trustgraph-base` as a dependency so
there is no need to install it unless you are using that package in
isolation.

## Version strategy

The TrustGraph release process creates containers and packages with the
same version number.  For best results, match the container and package
version numbers.

## Package Structure

| Package | Description | Major Dependencies | Scripts |
|---------|-------------|-------------------|---------|
| `trustgraph-base` | Minimal base classes and API support | `pulsar-client`, `prometheus-client` | None |
| `trustgraph-flow` | Core AI processing pipeline capabilities | `anthropic`, `openai`, `langchain`, `neo4j`, `milvus`, `pinecone`, `qdrant`, `fastembed`, `ollama`, `cohere`, `mistralai` | 60+ processing scripts |
| `trustgraph-cli` | Command-line interface for client-side operations | `requests`, `aiohttp`, `rdflib`, `tabulate`, `websockets` | 49 `tg-*` CLI commands |
| `trustgraph-embeddings-hf` | HuggingFace embeddings support | `torch`, `transformers`, `sentence-transformers`, `huggingface-hub` | `embeddings-hf` |
| `trustgraph-bedrock` | AWS Bedrock integration | `boto3` | `text-completion-bedrock` |
| `trustgraph-vertexai` | Google Vertex AI integration | `google-cloud-aiplatform` | `text-completion-vertexai` |
| `trustgraph-ocr` | OCR processing capabilities | `boto3`, `pdf2image`, `pytesseract` | `pdf-ocr` |
| `trustgraph-mcp` | Model Context Protocol server | `mcp`, `websockets` | `mcp-server` |

## Package Dependencies

### Core Dependencies
- **trustgraph-base**: Minimal foundation with messaging and metrics
- **trustgraph-flow**: Full AI pipeline with extensive ML/AI library support
- **trustgraph-cli**: Client tools with web and RDF support

### Specialized Dependencies
- **embeddings-hf**: PyTorch and HuggingFace ecosystem
- **bedrock/vertexai**: Cloud provider SDKs
- **ocr**: Image processing and OCR libraries
- **mcp**: Model Context Protocol implementation

## Python Requirements

All packages require Python {{site.data.software.python-min-version}} or
higher and are licensed under GPLv3+.

## Architecture

The modular design allows users to install only the components they need:
- Install `trustgraph-base` for basic API integration
- Add `trustgraph-flow` for full AI processing capabilities
- Include `trustgraph-cli` for command-line management
- Add specialized packages (embeddings, cloud providers, OCR) as needed
