---
title: Introduction
nav_order: 0
parent: Overview
review_date: 2026-08-01
guide_category:
  - Concepts
guide_category_order: 1
guide_description: What is TrustGraph and how does it transform AI agents into contextually-aware systems?
guide_difficulty: beginner
guide_time: 5 min
guide_emoji: 🎯
guide_banner: introduction.jpg
guide_labels:
  - GraphRAG
  - Knowledge Graphs
  - Core Concepts
---

# Introduction to TrustGraph

TrustGraph is an **Open Source Agent Intelligence Platform** that transforms
AI agents from simple task executors into intelligent, contextually-aware
systems. Unlike traditional AI approaches that work with isolated data points,
TrustGraph creates interconnected knowledge structures that enable agents to
understand relationships and context.





## What Makes TrustGraph Different?

### Context Graph Technologies

- Context Graph Factory - Transforms fragmented data into interconnected "Context Graphs" rather than relying on simple vector search, enabling superior reasoning through graph-based context
- Reduced AI hallucinations - Grounds LLMs with accurate, contextual information through intelligent context grounding rather than just retrieval
- Context Cores - Reusable, modular context bases that can be dynamically loaded and removed at runtime
- GraphRAG integration - Combines knowledge graphs with vector search for enhanced retrieval-augmented generation

### Deployment & Architecture

Single-command deployment — Launch entire agentic infrastructure with docker compose up -d
Fully containerized & modular — Transparent, open-source design with end-to-end context management
Run anywhere — Local, on-premise, or multi-cloud (AWS, Azure, GCP, OVHcloud, Scaleway, Kubernetes)

### Flexibility & Integrations

40+ LLM providers — Works with Anthropic, OpenAI, Google VertexAI, AWS Bedrock, and more
Multiple graph store options — Neo4j, Apache Cassandra, Memgraph, FalkorDB
Multiple vector DB options — Qdrant, Pinecone, Milvus
MCP (Model Context Protocol) interoperability — Native integration for external tool connections

Enterprise Features:

Data sovereignty — Keep data in your chosen region or on-premise
Native multi-tenancy — Isolated namespaces with security boundaries per tenant
Open source transparency — Full source code access for security audits






## Stuff needs to be edited




### Knowledge Packages

**Knowledge Packages** combine the best of both worlds:
- **Knowledge Graphs**: For structured relationships and context
- **Vector Embeddings**: For semantic similarity search
- **Unified Access**: Single interface for complex knowledge retrieval

This hybrid approach enables both precise relationship-based queries and flexible semantic search.

## Structured Query Processing

TrustGraph provides powerful capabilities for working with structured data extracted from documents:

### NLP Query

Converts natural language questions into structured GraphQL queries:
- Transform "Show me all products over $100" into precise database queries
- Generate GraphQL from conversational language
- Support complex filtering and aggregation requests

### Object Storage

Manages structured entities extracted from unstructured text:
- Store products, customers, financials as queryable objects
- Maintain schema validation and relationships
- Enable rapid structured data analysis

### Structured Query

Executes queries against extracted structured data:
- Query objects extracted from documents using natural language
- Execute GraphQL queries directly against your data
- Return results in multiple formats (JSON, CSV, tables)

## AI Agent Intelligence

TrustGraph enables AI agents to:
- **Reason about relationships**: Understand how different facts connect
- **Provide contextual responses**: Draw insights from interconnected knowledge
- **Reduce hallucinations**: Ground responses in structured knowledge
- **Learn continuously**: Build and refine knowledge over time

## Architecture Overview

### Knowledge Graph Builder

Extracts entities and relationships from your enterprise data:
- **Document Processing**: Analyzes text, PDFs, and other formats
- **Entity Extraction**: Identifies key concepts and objects
- **Relationship Mapping**: Discovers how entities connect
- **Graph Construction**: Builds interconnected knowledge structures

### Vector Embedding Engine

Creates semantic representations of knowledge elements:
- **Semantic Encoding**: Converts text into mathematical representations
- **Similarity Mapping**: Enables finding related concepts
- **Hybrid Search**: Combines with graph structure for powerful queries

### GraphRAG Processor

Combines graph and vector search for contextual retrieval:
- **Relationship-Aware Retrieval**: Finds information based on connections
- **Context Assembly**: Builds comprehensive context for AI responses
- **Multi-Hop Reasoning**: Follows relationship chains for deeper insights

### AI Agent Runtime

Executes intelligent agents with access to knowledge graphs:
- **Contextual Understanding**: Agents know how information relates
- **Grounded Responses**: Answers based on structured knowledge
- **Transparent Reasoning**: Clear path from question to answer

### Integration Layer

Connects with existing enterprise infrastructure:
- **LLM Integration**: Works with multiple AI models
- **Data Connectors**: Integrates with databases, documents, APIs
- **API Gateway**: Provides unified access to all capabilities

## How TrustGraph Works

### 1. Knowledge Ingestion
```
Documents → Entity Extraction → Relationship Discovery → Knowledge Graph
```

### 2. Query Processing
```
User Question → GraphRAG → Contextual Retrieval → AI Response
```

### 3. Continuous Learning
```
New Data → Graph Updates → Enhanced Knowledge → Better Responses
```

## Key Benefits

### Reduced Hallucinations
By grounding AI responses in structured knowledge graphs, TrustGraph significantly reduces the likelihood of AI generating false or misleading information.

### Contextual Intelligence
Agents understand not just what information exists, but how different pieces of information relate to each other.

### Enterprise Integration
Unifies fragmented organizational knowledge into coherent, queryable knowledge systems.

### Transparency
Full visibility into how data is processed and how AI agents arrive at their responses.

### Flexibility
Open-source architecture prevents vendor lock-in and enables customization.

## Next Steps

- **Understand the Platform**: Read [Architecture](architecture) for technical details
- **See Use Cases**: Explore [Use Cases](use-cases) for applications
- **Get Started**: Try the [Quickstart Guide](../getting-started/quickstart)
- **Deploy**: Review [Deployment Options](../deployment/) for your environment
