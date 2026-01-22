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

### Processing Chains in Action

The following examples show how processors chain together to perform tasks. Processors interact in two ways: **flow** interactions use fire-and-forget messaging where data moves from one processor to the next without waiting for acknowledgement — this powers processing chains. **Request/response** interactions place a request and wait for a response (which may be an error) — this is used when a result is needed before proceeding.

**Knowledge extraction from documents:**

```
pdf-decoder → chunker → kg-extract-relationships → triple-store
```

A PDF is decoded to text, split into chunks, entities and relationships are extracted by an LLM, and the resulting triples are written to the graph store.

**GraphRAG query:**

```
api-gateway → graph-rag → prompt → text-completion
```

A query arrives at the API gateway, GraphRAG retrieves relevant context from the knowledge graph, a prompt is constructed with the context, and the LLM generates a grounded response.

*Note: Both examples are simplified illustrations of single flows within more complex pipelines. The extraction example omits graph embeddings and other extraction processes. The GraphRAG example omits the knowledge graph traversal steps that occur between retrieval and prompt construction.*

### Platform

TrustGraph supports two deployment models:

- **Podman / Docker** — Deploy using `podman-compose` or `docker-compose` for development, evaluation, and smaller-scale production workloads
- **Kubernetes** — Deploy on managed Kubernetes services (GKE, AKS, EKS) or self-managed clusters (Scaleway, OVHcloud, on-premises) for production-scale deployments

See [Deployment](../deployment/) for platform-specific guides.

### Software Packaging

The core TrustGraph system is built into [Python packages](../reference/python-packages) published on PyPI. The build pipeline then packages these into [container images](../reference/containers) published to Docker Hub. Deployment engineers typically work with deployment packages that describe how the system is deployed, rather than interacting directly with Python packages or container images.

