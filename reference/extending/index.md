---
title: Extending TrustGraph
layout: default
nav_order: 5
parent: Reference
has_children: true
---

# Extending TrustGraph

Learn how to build custom services and processors for TrustGraph.

## Base Classes

TrustGraph provides multiple levels of abstraction for building extension services:

### [AsyncProcessor](async-processor.md)
For building global services that operate independently of flow management. Best for:
- Core infrastructure services
- Request/response services
- Services that don't participate in processing flows
- Global data stores and managers

### [FlowProcessor](flow-processor.md)
For building flow-aware services that integrate with TrustGraph's processing pipelines. Best for:
- Data processing services
- Services that transform or enrich data
- Services that need dynamic reconfiguration
- Services with multiple input/output streams

### [Service Base Classes](service-base-classes.md)
Pre-built service templates that extend FlowProcessor for common patterns. Best for:
- Standard service types (LLM, embeddings, storage, query)
- Rapid development with minimal boilerplate
- Consistent service patterns across your system
- Built-in error handling and metrics

### [Flow Specifications](flow-specifications.md)
Declarative interfaces for defining how services integrate with flows. Best for:
- Automatic message queue management
- Type-safe service integration
- Request/response client patterns
- Dynamic flow reconfiguration

## Choosing the Right Base Class

| Use Case | AsyncProcessor | FlowProcessor | Service Base Classes |
|----------|---------------|---------------|---------------------|
| Global services | ✓ | | |
| Flow-based processing | | ✓ | ✓ |
| Request/response patterns | ✓ | ✓ | ✓ |
| Multiple concurrent flows | | ✓ | ✓ |
| Dynamic flow configuration | | ✓ | ✓ |
| Simple message handling | ✓ | | |
| Complex pipeline integration | | ✓ | ✓ |
| Standard service patterns | | | ✓ |
| Minimal boilerplate | | | ✓ |
| Built-in error handling | | | ✓ |

## Getting Started

1. **Choose your base class** based on your service requirements:
   - **Service Base Classes**: For standard patterns (LLM, embeddings, storage, etc.)
   - **FlowProcessor**: For custom flow-aware services
   - **AsyncProcessor**: For global services outside the flow system

2. **Implement the required methods**:
   - Service Base Classes: One core method (e.g., `generate_content`, `invoke_tool`)
   - FlowProcessor: Message handlers and flow specifications
   - AsyncProcessor: Consumers, producers, and lifecycle management

3. **Configure your service**:
   - Add command-line arguments for configuration
   - Set up any required dependencies
   - Configure concurrency if supported

4. **Create an entry point** for your service

All base classes handle the underlying infrastructure including Pulsar messaging, configuration management, metrics collection, and error handling, allowing you to focus on your service's core logic.

## Documentation Index

- **[AsyncProcessor](async-processor.md)** - Base class for global services
- **[FlowProcessor](flow-processor.md)** - Base class for flow-aware services  
- **[Service Base Classes](service-base-classes)** - Pre-built service templates
- **[Flow Specifications](flow-specifications)** - Declarative flow integration
