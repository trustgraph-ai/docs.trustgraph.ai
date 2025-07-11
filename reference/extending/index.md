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

TrustGraph provides two main base classes for building extension services:

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

## Choosing the Right Base Class

| Use Case | AsyncProcessor | FlowProcessor |
|----------|---------------|---------------|
| Global services | ✓ | |
| Flow-based processing | | ✓ |
| Request/response patterns | ✓ | ✓ |
| Multiple concurrent flows | | ✓ |
| Dynamic flow configuration | | ✓ |
| Simple message handling | ✓ | |
| Complex pipeline integration | | ✓ |

## Getting Started

1. **Choose your base class** based on your service requirements
2. **Implement the required methods** for message handling and lifecycle management
3. **Register specifications** (for FlowProcessor) or set up consumers/producers (for AsyncProcessor)
4. **Add command-line arguments** for configuration
5. **Create an entry point** for your service

Both base classes handle the underlying infrastructure including Pulsar messaging, configuration management, metrics collection, and error handling, allowing you to focus on your service's core logic.
