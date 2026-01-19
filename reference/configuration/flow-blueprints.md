---
title: Flow Blueprints
parent: Configuration
grand_parent: Reference
nav_order: 1
permalink: /reference/configuration/flow-blueprints
review_date: 2026-08-01
---

# Flow Blueprint Configuration

Flow blueprints define complete dataflow pattern templates in TrustGraph. When instantiated, they create interconnected networks of processors that handle data ingestion, processing, storage, and querying as a unified system.

## Overview

A flow blueprint serves as a template for creating flow instances. Each flow blueprint defines:
- **Shared services** that are used by all flow instances of the same blueprint
- **Flow-specific processors** that are unique to each flow instance
- **Interfaces** that define how external systems interact with the flow
- **Queue patterns** that route messages between processors

Flow blueprints are stored in TrustGraph's configuration system with the configuration type `flow` and are managed through dedicated CLI commands.

## Structure

Every flow blueprint definition has four main sections:

### 1. Blueprint Section

Defines shared service processors that are instantiated once per flow blueprint. These processors handle requests from all flow instances of this blueprint.

```json
{
  "blueprint": {
    "embeddings:{blueprint}": {
      "request": "non-persistent://tg/request/embeddings:{blueprint}",
      "response": "non-persistent://tg/response/embeddings:{blueprint}"
    },
    "text-completion:{blueprint}": {
      "request": "non-persistent://tg/request/text-completion:{blueprint}",
      "response": "non-persistent://tg/response/text-completion:{blueprint}"
    }
  }
}
```

**Characteristics:**
- Shared across all flow instances of the same blueprint
- Typically expensive or stateless services (LLMs, embedding models)
- Use `{blueprint}` template variable for queue naming
- Examples: `embeddings:{blueprint}`, `text-completion:{blueprint}`, `graph-rag:{blueprint}`

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
      "request": "non-persistent://tg/request/embeddings:{blueprint}",
      "response": "non-persistent://tg/response/embeddings:{blueprint}"
    },
    "text-completion": {
      "request": "non-persistent://tg/request/text-completion:{blueprint}",
      "response": "non-persistent://tg/response/text-completion:{blueprint}"
    }
  }
}
```

**Types of Interfaces:**
- **Entry Points**: Where external systems inject data (`document-load`, `agent`)
- **Service Interfaces**: Request/response patterns for services (`embeddings`, `text-completion`)
- **Data Interfaces**: Fire-and-forget data flow connection points (`triples-store`, `entity-contexts-load`)

### 4. Metadata

Additional information about the flow blueprint:

```json
{
  "description": "Standard RAG pipeline with document processing and query capabilities",
  "tags": ["rag", "document-processing", "embeddings", "graph-query"]
}
```

## Parameters

**New in v1.4**: Flow blueprints can define configurable parameters that allow customization of flow behavior without modifying the flow blueprint definition. Parameters enable users to select different LLM models, adjust processing settings, and control flow behavior when starting flow instances.

### Parameter Definition Schema

Parameters are defined in the flow blueprint definition using this structure:

```json
{
  "description": "Flow blueprint description",
  "tags": ["tag1", "tag2"],
  "parameters": {
    "param-name": {
      "type": "parameter-type-ref",
      "description": "Human-readable description",
      "order": 1,
      "controlled-by": "other-param-name"
    }
  },
  "blueprint": { ... },
  "flow": { ... },
  "interfaces": { ... }
}
```

### Parameter Fields

#### type (required)

Reference to a parameter type definition stored in the configuration system. Parameter types define the schema, validation rules, default values, and allowed values.

**Example:**
```json
"parameters": {
  "model": {
    "type": "llm-model"
  }
}
```

The `llm-model` type is looked up in the parameter type configuration, which defines valid models, defaults, and constraints.

#### description (optional)

Human-readable description of what this parameter controls in the context of this flow. Overrides or supplements the parameter type's description.

**Example:**
```json
"parameters": {
  "model": {
    "type": "llm-model",
    "description": "LLM model for document analysis and extraction"
  }
}
```

#### order (optional)

Display order for the parameter in user interfaces and CLI output. Parameters are shown in ascending order.

**Example:**
```json
"parameters": {
  "model": {
    "type": "llm-model",
    "order": 1
  },
  "temperature": {
    "type": "temperature",
    "order": 2
  },
  "chunk-size": {
    "type": "chunk-size",
    "order": 3
  }
}
```

#### controlled-by (optional)

Indicates that this parameter's value is automatically inherited from another parameter. Used when multiple services in a flow should use the same setting.

**Example:**
```json
"parameters": {
  "llm-model": {
    "type": "llm-model",
    "description": "Primary LLM model",
    "order": 1
  },
  "rag-model": {
    "type": "llm-model",
    "description": "Model for RAG queries",
    "order": 2,
    "controlled-by": "llm-model"
  }
}
```

When `controlled-by` is specified:
- The parameter inherits the value from the controlling parameter
- Users can optionally override the inherited value
- UI can display the inheritance relationship

### Complete Parameter Example

```json
{
  "description": "Customizable RAG pipeline with LLM selection",
  "tags": ["rag", "configurable"],
  "parameters": {
    "llm-model": {
      "type": "llm-model",
      "description": "Primary language model for processing",
      "order": 1
    },
    "rag-model": {
      "type": "llm-model",
      "description": "Model for RAG query generation",
      "order": 2,
      "controlled-by": "llm-model"
    },
    "temperature": {
      "type": "temperature",
      "description": "Response randomness (0.0 = deterministic, 2.0 = very random)",
      "order": 3
    },
    "chunk-size": {
      "type": "chunk-size",
      "description": "Maximum text chunk size for processing",
      "order": 4
    },
    "embedding-model": {
      "type": "embedding-model",
      "description": "Model for generating document embeddings",
      "order": 5
    }
  },
  "blueprint": { ... },
  "flow": { ... },
  "interfaces": { ... }
}
```

### Parameter Types

Parameter types are centrally defined in the configuration system with type `parameter-type`. Each parameter type specifies:

- **Data type**: string, number, integer, boolean, array, object
- **Default value**: Value used when not specified by user
- **Enum values**: List of allowed values with descriptions
- **Constraints**: Validation rules (min/max, length, pattern, required)

Common parameter types include:

| Type | Description | Example Values |
|------|-------------|----------------|
| `llm-model` | LLM model selection | `gpt-4`, `claude-3-opus`, `mistral-large` |
| `temperature` | LLM temperature | `0.0` to `2.0` (default: `0.7`) |
| `chunk-size` | Text chunking size | `100` to `10000` (default: `1000`) |
| `embedding-model` | Embedding model | `text-embedding-ada-002`, `text-embedding-3-large` |

See [Parameter Types](parameters) for complete parameter type documentation.

### Parameter Resolution

When a flow instance is started, parameters are resolved in this order:

1. **User-provided values**: Explicit values from `tg-start-flow --param` or API
2. **Default values**: From parameter type definitions
3. **Controlled-by relationships**: Inherited from controlling parameters
4. **Required validation**: Error if required parameters are missing

**Example:**

Given parameter definitions with defaults:
- `llm-model`: default `gpt-4`
- `temperature`: default `0.7`
- `chunk-size`: default `1000`

Starting a flow with:
```bash
tg-start-flow -n my-flow -i flow1 -d "Test" --param llm-model=claude-3-opus
```

Results in:
- `llm-model`: `claude-3-opus` (user-provided)
- `temperature`: `0.7` (default)
- `chunk-size`: `1000` (default)

### Using Parameters in Flow Definitions

Parameters can be referenced in flow blueprint definitions using the `{param:name}` syntax. This allows queue names, processor configurations, and other settings to be parameterized.

**Example:**
```json
{
  "parameters": {
    "model": {
      "type": "llm-model",
      "order": 1
    }
  },
  "blueprint": {
    "text-completion:{blueprint}": {
      "request": "non-persistent://tg/request/text-completion:{blueprint}",
      "response": "non-persistent://tg/response/text-completion:{blueprint}",
      "config": {
        "model": "{param:model}"
      }
    }
  }
}
```

When the flow is started with `--param model=gpt-4`, the configuration becomes:
```json
{
  "config": {
    "model": "gpt-4"
  }
}
```

### Parameter Storage

All parameter values are stored as strings internally, regardless of their input format. When starting flows:

- Numbers: `--param temperature=0.7` → stored as `"0.7"`
- Booleans: `--param enabled=true` → stored as `"true"`
- Strings: `--param model=gpt-4` → stored as `"gpt-4"`

Processors are responsible for converting string values to appropriate types based on parameter type definitions.

### Benefits of Parameters

1. **Flexibility**: Customize flow behavior without modifying flow blueprints
2. **Reusability**: Single flow blueprint supports multiple configurations
3. **Consistency**: Centralized parameter type definitions ensure validation
4. **Discoverability**: Users can see available parameters with `tg-show-flow-blueprints`
5. **Documentation**: Parameter types include descriptions and constraints

## Template Variables

Flow blueprint definitions use template variables that are replaced when flow instances are created:

### {id}
- **Purpose**: Creates isolated resources for each flow instance
- **Usage**: Flow-specific processors and data pathways
- **Example**: `persistent://tg/flow/chunk-load:{id}` becomes `persistent://tg/flow/chunk-load:customer-A-flow`

### {blueprint}
- **Purpose**: Creates shared resources across flows of the same blueprint
- **Usage**: Shared services and expensive processors
- **Example**: `non-persistent://tg/request/embeddings:{blueprint}` becomes `non-persistent://tg/request/embeddings:standard-rag`

## Queue Patterns

Flow blueprints use Apache Pulsar for messaging. Queue names follow the Pulsar format:

```
<persistence>://<tenant>/<namespace>/<topic>
```

### Queue Components

| Component | Description | Examples |
|-----------|-------------|----------|
| **persistence** | Pulsar persistence mode | `persistent`, `non-persistent` |
| **tenant** | Organization identifier | `tg` (TrustGraph) |
| **namespace** | Messaging pattern | `flow`, `request`, `response` |
| **topic** | Queue/topic name | `chunk-load:{id}`, `embeddings:{blueprint}` |

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
non-persistent://tg/request/<topic>:{blueprint}
non-persistent://tg/response/<topic>:{blueprint}
```

**Characteristics:**
- Ephemeral, not persisted to disk
- Lower latency, suitable for RPC-style communication
- Used for shared services like embeddings and LLM calls
- Examples: `non-persistent://tg/request/embeddings:{blueprint}`, `non-persistent://tg/response/text-completion:{blueprint}`

## Complete Example

Here's a simplified flow blueprint definition for a standard RAG pipeline:

```json
{
  "description": "Standard RAG pipeline with document processing and query capabilities",
  "tags": ["rag", "document-processing", "embeddings"],
  
  "blueprint": {
    "embeddings:{blueprint}": {
      "request": "non-persistent://tg/request/embeddings:{blueprint}",
      "response": "non-persistent://tg/response/embeddings:{blueprint}"
    },
    "text-completion:{blueprint}": {
      "request": "non-persistent://tg/request/text-completion:{blueprint}",
      "response": "non-persistent://tg/response/text-completion:{blueprint}"
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
      "request": "non-persistent://tg/request/embeddings:{blueprint}",
      "response": "non-persistent://tg/response/embeddings:{blueprint}"
    },
    "text-completion": {
      "request": "non-persistent://tg/request/text-completion:{blueprint}",
      "response": "non-persistent://tg/response/text-completion:{blueprint}"
    }
  }
}
```

## Flow Instantiation

When a flow instance is created from this blueprint:

**Given:**
- Flow Instance ID: `customer-A-flow`
- Flow Blueprint: `standard-rag`

**Template Expansions:**
- `persistent://tg/flow/chunk-load:{id}` → `persistent://tg/flow/chunk-load:customer-A-flow`
- `non-persistent://tg/request/embeddings:{blueprint}` → `non-persistent://tg/request/embeddings:standard-rag`

**Result:**
- Isolated document processing pipeline for `customer-A-flow`
- Shared embedding service for all `standard-rag` flows
- Complete dataflow from document ingestion through querying

## Dataflow Architecture

Flow blueprints create unified dataflows where:

1. **Document Processing Pipeline**: Flows from ingestion through transformation to storage
2. **Query Services**: Integrated processors that query the same data stores and services
3. **Shared Services**: Centralized processors that all flows can utilize
4. **Storage Writers**: Persist processed data to appropriate stores

All processors (both `{id}` and `{blueprint}`) work together as a cohesive dataflow graph, not as separate systems.

## Benefits

### Resource Efficiency
- Expensive services (LLMs, embedding models) are shared across flows
- Reduces computational costs and resource usage

### Flow Isolation
- Each flow has its own data processing pipeline
- Prevents data mixing between different flows

### Scalability
- Can instantiate multiple flows from the same blueprint
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
- Share expensive services (LLMs, embeddings) at the blueprint level
- Keep data processing isolated at the flow level

### Interface Design
- Provide clear entry points for external systems
- Use request/response patterns for synchronous operations
- Use fire-and-forget patterns for asynchronous data flow

### Template Variables
- Use `{id}` for flow-specific resources
- Use `{blueprint}` for shared resources
- Be consistent with naming conventions

## See Also

- [tg-put-flow-blueprint](../cli/tg-put-flow-blueprint) - Create or update flow blueprints
- [tg-get-flow-blueprint](../cli/tg-get-flow-blueprint) - Retrieve flow blueprint definitions
- [tg-show-flow-blueprints](../cli/tg-show-flow-blueprints) - List available flow blueprints and parameters
- [tg-start-flow](../cli/tg-start-flow) - Start flows with parameter values
- [tg-show-parameter-types](../cli/tg-show-parameter-types) - View parameter type definitions
- [Parameter Types](parameters) - Parameter type configuration reference
- [Flow Processor Reference](../extending/flow-processor) - Building custom processors
- [Pulsar Configuration](pulsar) - Message queue configuration
