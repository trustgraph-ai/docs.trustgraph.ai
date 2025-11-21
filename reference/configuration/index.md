---
title: Configuration
parent: Reference
has_children: true
nav_order: 7
review_date: 2026-08-01
---

# Configuration Schemas

Reference documentation for TrustGraph configuration file formats and data structures.

## Configuration Types

### Flow Configuration
- **[Flow Classes](flow-classes)** - Define dataflow pattern templates and processor networks

### Data Configuration
- **Structure Descriptor Language (SDL)** - For structured data import (see [SDL Reference](../sdl))

### System Configuration
- **Pulsar Configuration** - Message queue and topic configuration (see [Pulsar API](../apis/pulsar))

## Overview

TrustGraph uses various configuration schemas to define:
- How data flows through the system
- How processors are connected and configured
- How external systems integrate with TrustGraph
- How data is transformed and stored

These configuration files are typically stored in JSON format and can be managed through the CLI tools or the web interface.

## Common Patterns

### Template Variables
Many configuration schemas support template variables for dynamic naming:
- `{id}` - Replaced with instance identifiers
- `{class}` - Replaced with class names
- `{collection}` - Replaced with collection names

### JSON Schema Validation
Configuration files are validated against JSON schemas to ensure correctness before deployment.

### Versioning
Configuration schemas support versioning to maintain backward compatibility as the system evolves.

## See Also

- [CLI Reference](../cli/) - Commands for managing configurations
- [API Reference](../apis/) - REST APIs for configuration management
- [Extension Reference](../extending/) - Creating custom configurations
