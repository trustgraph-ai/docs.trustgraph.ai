---
title: APIs
layout: default
nav_order: 1
has_children: true
parent: Reference
---

# TrustGraph APIs

## Overview

If you want to interact with TrustGraph through APIs, there are 4
forms of API which may be of interest to you. All four mechanisms
invoke the same underlying TrustGraph functionality but are made
available for integration in different ways:

### Pulsar APIs

Apache Pulsar is a pub/sub system used to deliver messages between TrustGraph
components. Using Pulsar, you can communicate with TrustGraph components.

Pros:
  - Provides complete access to all TrustGraph functionality
  - Simple integration with metrics and observability

Cons:
  - Integration is non-trivial, requires a special-purpose Pulsar client
    library
  - The Pulsar interfaces are likely something that you would not want to
    expose outside of the processing cluster in a production or well-secured
    deployment
    
### REST APIs

A component, `api-gateway`, provides a bridge between Pulsar internals and
the REST API which allows many services to be invoked using REST APIs.

Pros:
  - Uses standard REST approach can be easily integrated into many kinds
    of technology
  - Can be easily protected with authentication and TLS for production-grade
    or secure deployments

Cons:
  - For a complex application, a long series of REST invocations has
    latency and performance overheads - HTTP has limits on the number
    of concurrent service invocations
  - Lower coverage of functionality - service interfaces need to be added to
    `api-gateway` to permit REST invocation

### Websocket API

The `api-gateway` component also provides access to services through a
websocket API.

Pros:
  - Usable through a standard websocket library
  - Can be easily protected with authentication and TLS for production-grade
    or secure deployments
  - Supports concurrent service invocations

Cons:
  - Websocket service invocation is a little more complex to develop than
    using a basic REST API, particular if you want to cover all of the error
    scenarios well

### Python SDK API

The `trustgraph-base` package provides a Python SDK that wraps the underlying
service invocations in a convenient Python API.

Pros:
  - Native Python integration with type hints and documentation
  - Simplified service invocation without manual message handling
  - Built-in error handling and response parsing
  - Convenient for Python-based applications and scripts

Cons:
  - Python-specific, not available for other programming languages
  - Requires Python environment and trustgraph-base package installation
  - Less control over low-level message handling

## Flow-hosted APIs

There are two types of APIs: Flow-hosted which need a flow to be running
to operate.  Non-flow-hosted which are core to the system, and can
be seen as 'global' - they are not dependent on a flow to be running.

Knowledge, Librarian, Config and Flow APIs fall into the latter
category.

## API Conventions

### Field Naming

TrustGraph APIs consistently use **kebab-case** for field names in JSON payloads. This applies to all REST and Websocket APIs.

Examples:
- `document-metadata` (not `document_metadata` or `documentMetadata`)
- `flow-id` (not `flow_id` or `flowId`)
- `class-name` (not `class_name` or `className`)

### RDF Triple Representation

Knowledge graphs in TrustGraph use RDF triples to represent edges/relationships. In the APIs, triples are represented with a specific JSON structure:

```json
{
    "s": {"v": "http://example.com/persons/Person1", "e": true},
    "p": {"v": "http://schema.org/name", "e": true},
    "o": {"v": "John Doe", "e": false}
}
```

Where:
- **`s`**: Subject - the entity the statement is about
- **`p`**: Predicate - the property or relationship
- **`o`**: Object - the value or target entity

Each component has two fields:
- **`v`**: The value (must be a full URI when `e` is true)
- **`e`**: Boolean indicating if this is an entity/URI (true) or literal value (false)

### Value Types

When `e: true`:
- The `v` field must contain a full URI (e.g., `http://example.com/entity`)
- Prefixed shortcuts like `dc:title` are not supported - use full URIs like `http://purl.org/dc/terms/title`

When `e: false`:
- The `v` field contains a literal value (string, number, etc.)
- Examples: "John Doe", "42", "2024-01-01"

### Operation Naming

Most APIs use lowercase operation names, often with hyphens for multi-word operations:
- Simple operations: `get`, `put`, `list`, `delete`
- Compound operations: `add-document`, `get-kg-core`, `list-processing`

## See also

- [TrustGraph websocket overview](websocket)
- [TrustGraph Pulsar overview](pulsar)
- API details
  - [Text completion](api-text-completion)
  - [Prompt completion](api-prompt)
  - [Graph RAG](api-graph-rag)
  - [Document RAG](api-document-rag)
  - [Agent](api-agent)
  - [Embeddings](api-embeddings)
  - [Graph embeddings](api-graph-embeddings)
  - [Document embeddings](api-document-embeddings)
  - [Entity contexts](api-entity-contexts)
  - [Triples query](api-triples-query)
  - [Document load](api-document-load)
  - [Text load](api-text-load)
  - [Config](api-config)
  - [Flow](api-flow)
  - [Librarian](api-librarian)
  - [Knowledge](api-knowledge)
  - [Metrics](api-metrics)
  - [Core import/export](api-core-import-export)

