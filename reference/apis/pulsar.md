---
title: Pub/Sub Messaging
nav_order: 1
parent: APIs
review_date: 2027-01-01
---

# Pub/Sub Messaging

TrustGraph components communicate via a pub/sub messaging fabric. The
messaging layer is abstracted behind a backend-neutral interface,
allowing different messaging systems to be used without changing
application code.

## Supported Backends

| Backend | Selection | Status |
|---------|-----------|--------|
| Apache Pulsar | `PUBSUB_BACKEND=pulsar` (default) | Production |
| RabbitMQ | `PUBSUB_BACKEND=rabbitmq` | Production |

The backend is selected via the `PUBSUB_BACKEND` environment variable
or the `--pubsub-backend` CLI argument.

## Queue Naming

TrustGraph uses a generic queue naming format that is independent of the
underlying messaging backend:

```
<class>:<namespace>:<topic>
```

| Component | Description | Examples |
|-----------|-------------|----------|
| `class` | Determines operational characteristics (persistence, TTL) | `flow`, `request`, `response` |
| `namespace` | Deployment isolation prefix | `tg` |
| `topic` | Logical queue name | `config`, `graph-rag`, `text-completion` |

### Queue Classes

| Class | Characteristics | Usage |
|-------|-----------------|-------|
| `flow` | Persistent processing pipeline queue | Data processing, document chunking, config push signals |
| `request` | Non-persistent, short TTL | Service request messages |
| `response` | Non-persistent, short TTL | Service response messages |

### Examples

```
request:tg:config          # Config service requests
response:tg:config         # Config service responses
flow:tg:text-document-load # Document loading pipeline
request:tg:graph-rag       # Graph RAG requests
response:tg:graph-rag      # Graph RAG responses
```

Each backend maps these generic queue names to its own native
addressing scheme. Application code works only with the generic format.

## Service Types

TrustGraph uses two categories of service with different queue patterns:

### Global Services

Fixed queue names, not dependent on flows:

| Service | Request Queue | Response Queue |
|---------|---------------|----------------|
| Config | `request:tg:config` | `response:tg:config` |
| Flow | `request:tg:flow` | `response:tg:flow` |
| Knowledge | `request:tg:knowledge` | `response:tg:knowledge` |
| Librarian | `request:tg:librarian` | `response:tg:librarian` |
| Collection Management | `request:tg:collection-management` | `response:tg:collection-management` |

### Flow-Hosted Services

Queue names that incorporate the flow identifier:

- Agent, Graph RAG, Document RAG, Text Completion, Prompt
- Embeddings, Graph Embeddings, Document Embeddings
- Triples, SPARQL Query, Row Embeddings, NLP Query, Structured Query
- Text Load, Document Load, MCP Tool

## Discovering Flow-Hosted Queue Names

Flow-hosted service queue names are determined by the flow configuration.
Use the CLI to inspect them:

```bash
tg-show-flows
```

Or query the config service for a specific flow's interface definitions.

## Flow Interface Types

### Request/Response Interfaces

Services that accept a request and return a response:

```json
{
    "graph-rag": {
        "request": "request:tg:graph-rag",
        "response": "response:tg:graph-rag"
    }
}
```

### Fire-and-Forget Interfaces

Services that accept data without returning a response:

```json
{
    "text-load": "flow:tg:text-document-load"
}
```

## Backend Configuration

### Pulsar

| Environment Variable | Default | Description |
|---------------------|---------|-------------|
| `PULSAR_HOST` | `pulsar://pulsar:6650` | Pulsar broker URL |
| `PULSAR_API_KEY` | (none) | API key for authentication |

### RabbitMQ

| Environment Variable | Default | Description |
|---------------------|---------|-------------|
| `RABBITMQ_HOST` | `rabbitmq` | RabbitMQ hostname |
| `RABBITMQ_PORT` | `5672` | RabbitMQ port |
| `RABBITMQ_USERNAME` | `guest` | Authentication username |
| `RABBITMQ_PASSWORD` | `guest` | Authentication password |
| `RABBITMQ_VHOST` | `/` | Virtual host |

## Best Practices

1. **Use the Python SDK or REST/WebSocket APIs** for application
   integration rather than connecting to the messaging fabric directly
2. **Query flow configuration** to discover queue names for flow-hosted
   services — do not hard-code them
3. **Choose the appropriate backend** for your deployment: Pulsar for
   large-scale deployments, RabbitMQ for lower resource requirements

## See Also

- [REST API](rest) - REST API reference
- [WebSocket API](websocket) - WebSocket API reference
- [Python API](python) - Python SDK reference
- [Flow Blueprints](../configuration/flow-blueprints) - Flow configuration
- [Parameter Types](../configuration/parameters) - Flow parameter definitions
