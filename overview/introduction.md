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

<div class="feature-cards" markdown="0">

<div class="feature-card">
<div class="feature-card-heading" style="background-image: url('feature-context-graph.jpg');">
<div class="feature-icon">🧠</div>
<h3>Context Graph Technologies</h3>
</div>
<div class="feature-card-content">
<ul>
<li><strong>Context Graph Factory</strong> — Transforms fragmented data into interconnected "Context Graphs" rather than relying on simple vector search, enabling superior reasoning through graph-based context</li>
<li><strong>Reduced AI hallucinations</strong> — Grounds LLMs with accurate, contextual information through intelligent context grounding rather than just retrieval</li>
<li><strong>Context Cores</strong> — Reusable, modular context bases that can be dynamically loaded and removed at runtime</li>
<li><strong>GraphRAG integration</strong> — Combines knowledge graphs with vector search for enhanced retrieval-augmented generation</li>
</ul>
</div>
</div>

<div class="feature-card">
<div class="feature-card-heading" style="background-image: url('feature-deployment.jpg');">
<div class="feature-icon">🚀</div>
<h3>Deployment & Architecture</h3>
</div>
<div class="feature-card-content">
<ul>
<li><strong>Single-command deployment</strong> — Launch entire agentic infrastructure with <code>docker compose up -d</code></li>
<li><strong>Fully containerized & modular</strong> — Transparent, open-source design with end-to-end context management</li>
<li><strong>Run anywhere</strong> — Local, on-premise, or multi-cloud (AWS, Azure, GCP, OVHcloud, Scaleway, Kubernetes)</li>
</ul>
</div>
</div>

<div class="feature-card">
<div class="feature-card-heading" style="background-image: url('feature-integrations.jpg');">
<div class="feature-icon">🔌</div>
<h3>Flexibility & Integrations</h3>
</div>
<div class="feature-card-content">
<ul>
<li><strong>40+ LLM providers</strong> — Works with Anthropic, OpenAI, Google VertexAI, AWS Bedrock, and more</li>
<li><strong>Multiple graph store options</strong> — Neo4j, Apache Cassandra, Memgraph, FalkorDB</li>
<li><strong>Multiple vector DB options</strong> — Qdrant, Pinecone, Milvus</li>
<li><strong>MCP interoperability</strong> — Native Model Context Protocol integration for external tool connections</li>
</ul>
</div>
</div>

<div class="feature-card">
<div class="feature-card-heading" style="background-image: url('feature-enterprise.jpg');">
<div class="feature-icon">🏢</div>
<h3>Enterprise Features</h3>
</div>
<div class="feature-card-content">
<ul>
<li><strong>Data sovereignty</strong> — Keep data in your chosen region or on-premise</li>
<li><strong>Native multi-tenancy</strong> — Isolated namespaces with security boundaries per tenant</li>
<li><strong>Open source transparency</strong> — Full source code access for security audits</li>
</ul>
</div>
</div>

</div>






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
