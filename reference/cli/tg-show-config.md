---
title: tg-show-config
parent: CLI
review_date: 2026-06-01
---

# tg-show-config

Displays the current TrustGraph system configuration.

## Synopsis

```bash
tg-show-config [options]
```

## Description

The `tg-show-config` command retrieves and displays the complete TrustGraph system configuration in JSON format, including flow definitions, service configurations, and system settings.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Display Complete Configuration
```bash
tg-show-config
```

### Using Custom API URL
```bash
tg-show-config -u http://production:8088/
```

### Save Configuration to File
```bash
tg-show-config > config-backup.json
```

## Output Format

The command outputs a JSON document containing:
- Flow definitions and interfaces
- Service configurations
- Pulsar queue names
- System settings

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-get-config-item`](tg-get-config-item) - Retrieve specific configuration
- [`tg-list-config-items`](tg-list-config-items) - List configuration keys
- [`tg-show-flows`](tg-show-flows) - List running flows

## API Integration

This command uses the Configuration API to retrieve the complete system configuration.
