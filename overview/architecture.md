---
title: Architecture
nav_order: 2
parent: Overview
review_date: 2026-08-01
guide_category:
  - How does it work?
guide_category_order: 2
guide_description: System design, component relationships, data flow, and integration points
guide_difficulty: advanced
guide_time: 5 min
guide_emoji: 🏗️
guide_banner: architecture.jpg
guide_labels:
  - Architecture
  - Components
  - Technical
---

# Architecture

Learn about TrustGraph's system architecture and design principles for building intelligent AI agent platforms.

## System Overview

TrustGraph is a knowledge and agent substrate that sits alongside your existing data sources and LLM providers — not a monolithic application. It transforms your enterprise data into structured knowledge that agents can reason over, while you retain full control over where data lives and which models you use.

The architecture builds on proven patterns from the knowledge graph and semantic web ecosystem, making concepts familiar to teams with experience in enterprise knowledge management.

**At a glance**: Ingestion & Processing → Knowledge Storage → Agent Runtime → Integration Layer

### High-Level Architecture

<a href="arch-diagram.png">
  <img src="arch-diagram.png" alt="TrustGraph architecture">
</a>

TrustGraph follows a modular, microservices-based architecture built on an event-driven streaming backbone (Apache Pulsar). Components communicate asynchronously, enabling independent scaling and resilient operation.

### Infrastructure

- **Apache Pulsar** — The messaging backbone that underpins all system communication. Every service communicates through Pulsar, enabling decoupled scaling, message replay, and resilient operation
- **Cassandra** — Stores system metadata, processing state, and operational data
- **Garage** — S3-compatible object storage for source documents and artifacts
- **Grafana & Loki** — Monitoring dashboards and log aggregation for observability

### Knowledge Infrastructure

TrustGraph uses pluggable backends for knowledge storage:

- **Graph store** — Stores entities and relationships. Options: Cassandra, Neo4j, Memgraph, FalkorDB
- **Vector store** — Stores embeddings for semantic search. Options: Qdrant, Milvus
- **Structure store** — Stores structured data extracts. Options: Cassandra

### Service Architecture

TrustGraph consists of many independent **processors** — small, focused services that each perform a specific task (parsing documents, extracting entities, generating embeddings, etc.). Processors communicate exclusively through Pulsar, making the system loosely coupled and independently scalable.

- **Processors** — Individual services that subscribe to input queues, perform work, and publish to output queues
- **Flows** — Running dataflow pipelines that chain processors together to accomplish complex tasks
- **Flow blueprints** — Reusable templates that define which processors to invoke and how data moves between them

This architecture allows the system to run many configurable dataflows simultaneously, adapting processing pipelines to different use cases without code changes.

### Core Components

- **Knowledge Graph Builder** — Extracts entities and relationships from enterprise data to construct [Knowledge Cores](../guides/context-cores/)
- **Vector Embedding Engine** — Creates semantic embeddings that enable similarity search as entry points into the graph
- **GraphRAG Processor** — Combines graph traversal with vector search for multi-hop contextual retrieval
- **AI Agent Runtime** — Executes agents and tools with access to Knowledge Cores and external systems
- **Integration Layer** — Connects with external LLMs, databases, and enterprise systems through pluggable adapters

### Data Flow

1. **Ingestion** — Raw data enters from various sources (e.g. product docs from Confluence, tickets from Jira)
2. **Processing** — Entity extraction, relationship identification, and graph construction
3. **Embedding** — Vector representation of knowledge elements for semantic search
4. **Storage** — Persistent storage in graph and vector databases as a Knowledge Core
5. **Query** — Agents query Knowledge Cores via GraphRAG for contextual information
6. **Response** — Grounded responses with reasoning paths traced back to source entities

## Storage Layer

### Knowledge Graph Storage

TrustGraph supports multiple graph database backends as pluggable storage. Stores entities, relationships, and metadata in optimized graph structures.

Supported backends include Cassandra, Neo4j, Memgraph, and FalkorDB. See [Maturity](maturity) for production recommendations.

### Vector Database Integration

Integrates with vector databases for semantic similarity search and hybrid retrieval. Embeddings link to graph entities, enabling vector search to serve as entry points for graph traversal.

Supported backends include Qdrant, Milvus, and Pinecone. See [Maturity](maturity) for production recommendations.

### Knowledge Cores

Combines graph and vector storage into unified [Knowledge Cores](../guides/context-cores/) — the deployable unit that provides both structured relationships and semantic search capabilities. Knowledge Cores can be loaded, unloaded, and versioned independently at runtime.

## Processing & Reasoning Layer

### Entity Extraction Engine

Uses NLP pipelines including entity recognition and relationship extraction to identify entities, relationships, and concepts from unstructured data.

### Relationship Mapping

Constructs relationship maps that capture how entities connect and influence each other, enabling multi-hop reasoning across your knowledge base.

### GraphRAG Processing

Implements [Graph Retrieval-Augmented Generation](../guides/graph-rag/) that leverages both graph structure and vector similarity for enhanced context retrieval.

### AI Agent Orchestration

Manages execution of AI agents with access to shared Knowledge Cores, tool invocation via [MCP](../guides/mcp-integration/), and workflow state management.

## Integration Layer

### LLM Integration

Supports 40+ LLM providers through standardized interfaces, including Anthropic, OpenAI, Google VertexAI, AWS Bedrock, Azure OpenAI, and Ollama.

### Enterprise Data Connectors

Built-in connectors for common enterprise systems including databases, document management systems, and APIs.

### API Gateway

Provides unified access to all TrustGraph capabilities through REST APIs, GraphQL, and WebSocket connections.

## Deployment & Operations

### Containerized Deployment

Fully containerized using Docker with Kubernetes orchestration for scalable, cloud-native deployments.

### Microservices Design

Modular architecture allows independent scaling of different components based on workload requirements.

### Multi-Cloud Support

Runs on any cloud platform (AWS, Azure, GCP, Scaleway, OVHcloud) or on-premises infrastructure. See [Maturity](maturity) for deployment status by platform.

### Observability

- **Metrics** — Prometheus endpoints on all services with pre-built Grafana dashboards
- **Logging** — Structured logs compatible with standard aggregators
- **Cost tracking** — LLM API usage and token consumption metrics

## Security & Multi-Tenancy

### Access Control

API gateway provides the integration point for authentication and authorization. TrustGraph does not include built-in user/token management — integrate with your existing identity provider.

### Multi-Tenancy

Logical isolation through Knowledge Core namespaces, per-namespace resource quotas, and configuration isolation. Tenants share infrastructure while data remains strictly separated.

### Compliance

Audit logging, data encryption at rest and in transit, and support for air-gapped deployments for data sovereignty requirements.

## Scalability & Performance

### Horizontal Scaling

Ingestion, processing, and query paths scale independently based on workload demands.

### Resilient Processing

The Pulsar streaming backbone provides message replay, persistence, and backpressure handling. Services recover state after restarts without data loss.

### Caching & Optimization

Query result caching and optimized graph traversal ensure fast response times even with large Knowledge Cores.
