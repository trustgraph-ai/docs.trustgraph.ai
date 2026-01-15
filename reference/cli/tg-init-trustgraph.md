---
title: tg-init-trustgraph
parent: CLI
review_date: 2026-04-16
---

# tg-init-trustgraph

Initializes Pulsar with TrustGraph tenant, namespaces, and configuration settings.

## Synopsis

```bash
tg-init-trustgraph [options]
```

## Description

The `tg-init-trustgraph` command initializes the Apache Pulsar messaging system with the required tenant, namespaces, policies, and configuration needed for TrustGraph operation. This is a foundational setup command that must be run before TrustGraph can operate properly.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-p, --pulsar-admin-url URL` | `http://pulsar:8080` | Pulsar admin URL |
| `--pulsar-host HOST` | `pulsar://pulsar:6650` | Pulsar host for client connections |
| `--pulsar-api-key KEY` | (none) | Pulsar API key for authentication |
| `-c, --config CONFIG` | (none) | Initial configuration JSON to load |
| `-t, --tenant TENANT` | `tg` | Tenant name |

## Examples

### Basic Initialization
```bash
tg-init-trustgraph
```

### Custom Pulsar Configuration
```bash
tg-init-trustgraph \
  --pulsar-admin-url http://localhost:8080 \
  --pulsar-host pulsar://localhost:6650
```

### With Initial Configuration
```bash
tg-init-trustgraph \
  --config '{"prompt": {"system": "You are a helpful AI assistant"}}'
```

### Custom Tenant
```bash
tg-init-trustgraph --tenant production-tg
```

## What It Creates

The command creates a TrustGraph tenant with the following namespaces:

- **`tg/flow`**: Processing workflows and flow definitions
- **`tg/request`**: Incoming API requests and commands
- **`tg/response`**: API responses and results
- **`tg/metrics`**: System metrics and monitoring data
- **`tg/config`**: Configuration storage

Each namespace is configured with appropriate retention policies for TrustGraph operation.

## Prerequisites

- Apache Pulsar must be running and accessible
- Pulsar admin tools must be available
- Network connectivity to Pulsar admin and client ports

## Notes

This command is typically run once during initial TrustGraph deployment. Re-running the command is safe and will update existing configurations without data loss.

## Related Commands

- [`tg-init-pulsar-manager`](tg-init-pulsar-manager) - Initialize Pulsar Manager

## API Integration

This command uses Pulsar Admin API to create tenants, namespaces, and policies.
