---
title: tg-unload-kg-core
parent: CLI
review_date: 2026-04-06
---

# tg-unload-kg-core

Removes a knowledge core from an active flow without deleting the stored core.

## Synopsis

```bash
tg-unload-kg-core --id CORE_ID [options]
```

## Description

The `tg-unload-kg-core` command removes a previously loaded knowledge core from an active processing flow, making that knowledge unavailable for queries within the flow. The knowledge core remains stored in the system and can be loaded again later.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--id, --identifier CORE_ID` | Identifier of the knowledge core to unload |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-f, --flow-id FLOW` | `default` | Flow ID to unload knowledge from |

## Examples

### Unload from Default Flow
```bash
tg-unload-kg-core --id "research-knowledge"
```

### Unload from Specific Flow
```bash
tg-unload-kg-core \
  --id "medical-knowledge" \
  --flow-id "medical-analysis" \
  -U medical-team
```

### Using Custom API
```bash
tg-unload-kg-core \
  --id "production-knowledge" \
  --flow-id "prod-flow" \
  -u http://production:8088/
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-load-kg-core`](tg-load-kg-core) - Load knowledge core into flow
- [`tg-delete-kg-core`](tg-delete-kg-core) - Permanently delete knowledge core
- [`tg-show-kg-cores`](tg-show-kg-cores) - List available knowledge cores

## API Integration

This command uses the Knowledge API to remove knowledge cores from flow contexts while preserving the stored data.
