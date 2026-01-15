---
title: tg-init-pulsar-manager
parent: CLI
review_date: 2026-02-25
---

# tg-init-pulsar-manager

Initializes Pulsar Manager with default superuser credentials for TrustGraph.

## Synopsis

```bash
tg-init-pulsar-manager
```

## Description

The `tg-init-pulsar-manager` command is a setup utility that creates a default superuser account in Pulsar Manager. This is typically run once during initial TrustGraph deployment to establish administrative access to the Pulsar message queue management interface.

## Options

This command takes no arguments or options.

## Examples

### Initialize Pulsar Manager
```bash
tg-init-pulsar-manager
```

## Default Configuration

The command creates a superuser with these default credentials:

- **Username**: `admin`
- **Password**: `apachepulsar`
- **Email**: `username@test.org`

## Prerequisites

- Pulsar Manager must be running and accessible at `http://localhost:7750`
- Network access to the Pulsar Manager API endpoint

## Notes

The command performs these operations:
1. Retrieves a CSRF token from Pulsar Manager
2. Creates the superuser account with administrative privileges
3. Sets the configured credentials

After initialization, you can access Pulsar Manager at `http://localhost:7750/pulsar-manager/` using the default credentials.

## Related Commands

- [`tg-init-trustgraph`](tg-init-trustgraph) - Initialize TrustGraph system

## API Integration

This command uses the Pulsar Manager API to create administrative credentials.
