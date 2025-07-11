---
title: Core Concepts
layout: default
nav_order: 1
parent: Getting Started
grand_parent: TrustGraph Documentation
---

# Core Concepts

Understand the fundamental concepts and architecture that make TrustGraph a powerful AI agent intelligence platform.

## What is TrustGraph?

TrustGraph is an **Open Source Agent Intelligence Platform** that transforms AI agents from simple task executors into intelligent, contextually-aware systems. Unlike traditional AI approaches that work with isolated data points, TrustGraph creates interconnected knowledge structures that enable agents to understand relationships and context.

## Core Concepts

### Knowledge Graphs

**Knowledge Graphs** are the foundation of TrustGraph's intelligence. They represent information as interconnected networks of entities and relationships, rather than isolated documents or data points.

- **Entities**: People, places, concepts, or objects in your data
- **Relationships**: How entities connect and relate to each other
- **Context**: The meaning that emerges from understanding these connections

### GraphRAG (Graph Retrieval-Augmented Generation)

**GraphRAG** is TrustGraph's advanced approach to information retrieval that goes beyond traditional RAG systems:

**Traditional RAG:**
- Retrieves similar documents based on vector similarity
- Works with isolated pieces of information
- Limited contextual understanding

**GraphRAG:**
- Understands relationships between different pieces of information
- Retrieves contextually relevant knowledge based on graph structure
- Provides more accurate, nuanced responses
- Significantly reduces AI hallucinations

### Knowledge Packages

**Knowledge Packages** combine the best of both worlds:
- **Knowledge Graphs**: For structured relationships and context
- **Vector Embeddings**: For semantic similarity search
- **Unified Access**: Single interface for complex knowledge retrieval

This hybrid approach enables both precise relationship-based queries and flexible semantic search.

### AI Agent Intelligence

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

## From Your First Steps

When you followed the [First Steps](first-steps) guide, you experienced these concepts in action:

- **Document Loading**: Your PDFs became entities and relationships in a knowledge graph
- **Graph Visualization**: You saw how TrustGraph represents knowledge as interconnected data
- **Vector Search**: You found relevant information using semantic similarity
- **Graph RAG**: You asked questions and received contextually-aware answers

## Essential Terminology

**Knowledge Graph**: Network of interconnected entities and relationships
**GraphRAG**: Graph-enhanced retrieval and generation for AI responses
**Knowledge Package**: Combined graph and vector representation of knowledge
**Entity**: A person, place, concept, or object in your data
**Relationship**: A connection between two entities
**Vector Embedding**: Mathematical representation of text for similarity search
**Agent Intelligence**: AI that understands context and relationships
**N-Triples**: Standard format for representing graph data as subject-predicate-object statements

## Next Steps

Now that you understand TrustGraph's core concepts:
- Explore [Deployment Options](../deployment/) for production use
- Learn about [API Integration](../reference/) for custom applications
- Review [How-to Guides](../guides/) for specific use cases
