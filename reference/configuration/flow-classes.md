---
layout: default
title: Flow Classes
parent: Configuration
grand_parent: Reference
nav_order: 1
permalink: /reference/configuration/flow-classes
---

# Flow Class Configuration

Flow classes define complete dataflow pattern templates in TrustGraph. When instantiated, they create interconnected networks of processors that handle data ingestion, processing, storage, and querying as a unified system.

## Overview

A flow class serves as a blueprint for creating flow instances. Each flow class defines:
- **Shared services** that are used by all flow instances of the same class
- **Flow-specific processors** that are unique to each flow instance
- **Interfaces** that define how external systems interact with the flow
- **Queue patterns** that route messages between processors

Flow classes are stored in TrustGraph's configuration system with the configuration type `flow-classes` and are managed through dedicated CLI commands.

## Structure

Every flow class definition has four main sections:

### 1. Class Section

Defines shared service processors that are instantiated once per flow class. These processors handle requests from all flow instances of this class.

```json
{
  "class": {
    "embeddings:{class}": {
      "request": "non-persistent://tg/request/embeddings:{class}",
      "response": "non-persistent://tg/response/embeddings:{class}"
    },
    "text-completion:{class}": {
      "request": "non-persistent://tg/request/text-completion:{class}",
      "response": "non-persistent://tg/response/text-completion:{class}"
    }
  }
}
```

**Characteristics:**
- Shared across all flow instances of the same class
- Typically expensive or stateless services (LLMs, embedding models)
- Use `{class}` template variable for queue naming
- Examples: `embeddings:{class}`, `text-completion:{class}`, `graph-rag:{class}`

### 2. Flow Section

Defines flow-specific processors that are instantiated for each individual flow instance. Each flow gets its own isolated set of these processors.

```json
{
  "flow": {
    "chunker:{id}": {
      "input": "persistent://tg/flow/chunk:{id}",
      "output": "persistent://tg/flow/chunk-load:{id}"
    },
    "pdf-decoder:{id}": {
      "input": "persistent://tg/flow/document-load:{id}",
      "output": "persistent://tg/flow/chunk:{id}"
    }
  }
}
```

**Characteristics:**
- Unique instance per flow
- Handle flow-specific data and state
- Use `{id}` template variable for queue naming
- Examples: `chunker:{id}`, `pdf-decoder:{id}`, `kg-extract-relationships:{id}`

### 3. Interfaces Section

Defines the entry points and interaction contracts for the flow. These form the API surface for external systems and internal component communication.

Interfaces can take two forms:

**Fire-and-Forget Pattern** (single queue):
```json
{
  "interfaces": {
    "document-load": "persistent://tg/flow/document-load:{id}",
    "triples-store": "persistent://tg/flow/triples-store:{id}"
  }
}
```

**Request/Response Pattern** (object with request/response fields):
```json
{
  "interfaces": {
    "embeddings": {
      "request": "non-persistent://tg/request/embeddings:{class}",
      "response": "non-persistent://tg/response/embeddings:{class}"
    },
    "text-completion": {
      "request": "non-persistent://tg/request/text-completion:{class}",
      "response": "non-persistent://tg/response/text-completion:{class}"
    }
  }
}
```

**Types of Interfaces:**
- **Entry Points**: Where external systems inject data (`document-load`, `agent`)
- **Service Interfaces**: Request/response patterns for services (`embeddings`, `text-completion`)
- **Data Interfaces**: Fire-and-forget data flow connection points (`triples-store`, `entity-contexts-load`)

### 4. Metadata

Additional information about the flow class:

```json
{
  "description": "Standard RAG pipeline with document processing and query capabilities",
  "tags": ["rag", "document-processing", "embeddings", "graph-query"]
}
```

## Template Variables

Flow class definitions use template variables that are replaced when flow instances are created:

### {id}
- **Purpose**: Creates isolated resources for each flow instance
- **Usage**: Flow-specific processors and data pathways
- **Example**: `persistent://tg/flow/chunk-load:{id}` becomes `persistent://tg/flow/chunk-load:customer-A-flow`

### {class}
- **Purpose**: Creates shared resources across flows of the same class
- **Usage**: Shared services and expensive processors
- **Example**: `non-persistent://tg/request/embeddings:{class}` becomes `non-persistent://tg/request/embeddings:standard-rag`

## Queue Patterns

Flow classes use Apache Pulsar for messaging. Queue names follow the Pulsar format:

```
<persistence>://<tenant>/<namespace>/<topic>
```

### Queue Components

| Component | Description | Examples |
|-----------|-------------|----------|
| **persistence** | Pulsar persistence mode | `persistent`, `non-persistent` |
| **tenant** | Organization identifier | `tg` (TrustGraph) |
| **namespace** | Messaging pattern | `flow`, `request`, `response` |
| **topic** | Queue/topic name | `chunk-load:{id}`, `embeddings:{class}` |

### Persistent Queues

Used for fire-and-forget services and durable data flow:

```
persistent://tg/flow/<topic>:{id}
```

**Characteristics:**
- Data persists in Pulsar storage across restarts
- Used for document processing pipelines
- Ensures data durability and reliability
- Examples: `persistent://tg/flow/chunk-load:{id}`, `persistent://tg/flow/triples-store:{id}`

### Non-Persistent Queues

Used for request/response messaging patterns:

```
non-persistent://tg/request/<topic>:{class}
non-persistent://tg/response/<topic>:{class}
```

**Characteristics:**
- Ephemeral, not persisted to disk
- Lower latency, suitable for RPC-style communication
- Used for shared services like embeddings and LLM calls
- Examples: `non-persistent://tg/request/embeddings:{class}`, `non-persistent://tg/response/text-completion:{class}`

## Complete Example

Here's a simplified flow class definition for a standard RAG pipeline:

```json
{
  "description": "Standard RAG pipeline with document processing and query capabilities",
  "tags": ["rag", "document-processing", "embeddings"],
  
  "class": {
    "embeddings:{class}": {
      "request": "non-persistent://tg/request/embeddings:{class}",
      "response": "non-persistent://tg/response/embeddings:{class}"
    },
    "text-completion:{class}": {
      "request": "non-persistent://tg/request/text-completion:{class}",
      "response": "non-persistent://tg/response/text-completion:{class}"
    }
  },
  
  "flow": {
    "pdf-decoder:{id}": {
      "input": "persistent://tg/flow/document-load:{id}",
      "output": "persistent://tg/flow/chunk:{id}"
    },
    "chunker:{id}": {
      "input": "persistent://tg/flow/chunk:{id}",
      "output": "persistent://tg/flow/chunk-load:{id}"
    },
    "vectorizer:{id}": {
      "input": "persistent://tg/flow/chunk-load:{id}",
      "output": "persistent://tg/flow/doc-embeds-store:{id}"
    }
  },
  
  "interfaces": {
    "document-load": "persistent://tg/flow/document-load:{id}",
    "embeddings": {
      "request": "non-persistent://tg/request/embeddings:{class}",
      "response": "non-persistent://tg/response/embeddings:{class}"
    },
    "text-completion": {
      "request": "non-persistent://tg/request/text-completion:{class}",
      "response": "non-persistent://tg/response/text-completion:{class}"
    }
  }
}
```

## Flow Instantiation

When a flow instance is created from this class:

**Given:**
- Flow Instance ID: `customer-A-flow`
- Flow Class: `standard-rag`

**Template Expansions:**
- `persistent://tg/flow/chunk-load:{id}` → `persistent://tg/flow/chunk-load:customer-A-flow`
- `non-persistent://tg/request/embeddings:{class}` → `non-persistent://tg/request/embeddings:standard-rag`

**Result:**
- Isolated document processing pipeline for `customer-A-flow`
- Shared embedding service for all `standard-rag` flows
- Complete dataflow from document ingestion through querying

## Dataflow Architecture

Flow classes create unified dataflows where:

1. **Document Processing Pipeline**: Flows from ingestion through transformation to storage
2. **Query Services**: Integrated processors that query the same data stores and services
3. **Shared Services**: Centralized processors that all flows can utilize
4. **Storage Writers**: Persist processed data to appropriate stores

All processors (both `{id}` and `{class}`) work together as a cohesive dataflow graph, not as separate systems.

## Benefits

### Resource Efficiency
- Expensive services (LLMs, embedding models) are shared across flows
- Reduces computational costs and resource usage

### Flow Isolation
- Each flow has its own data processing pipeline
- Prevents data mixing between different flows

### Scalability
- Can instantiate multiple flows from the same template
- Horizontal scaling by adding more flow instances

### Modularity
- Clear separation between shared and flow-specific components
- Easy to modify and extend flow capabilities

### Unified Architecture
- Query and processing are part of the same dataflow
- Consistent data handling across ingestion and retrieval

## Common Patterns

### Standard RAG Flow
- Document ingestion → chunking → embedding → storage
- Query interface for retrieval and generation

### Knowledge Graph Flow
- Document ingestion → entity extraction → relationship extraction → graph storage
- Query interface for graph traversal and reasoning

### Object Extraction Flow
- Document ingestion → structured data extraction → object storage
- Query interface for structured data retrieval

## Best Practices

### Queue Design
- Use persistent queues for data that must survive restarts
- Use non-persistent queues for fast request/response patterns
- Include template variables in queue names for proper isolation

### Service Sharing
- Share expensive services (LLMs, embeddings) at the class level
- Keep data processing isolated at the flow level

### Interface Design
- Provide clear entry points for external systems
- Use request/response patterns for synchronous operations
- Use fire-and-forget patterns for asynchronous data flow

### Template Variables
- Use `{id}` for flow-specific resources
- Use `{class}` for shared resources
- Be consistent with naming conventions

## See Also

- [tg-put-flow-class](../cli/tg-put-flow-class) - Create or update flow classes
- [tg-get-flow-class](../cli/tg-get-flow-class) - Retrieve flow class definitions
- [tg-show-flow-classes](../cli/tg-show-flow-classes) - List available flow classes
- [Flow Processor Reference](../extending/flow-processor) - Building custom processors
- [Pulsar Configuration](pulsar) - Message queue configuration