---
title: tg-stop-flow
parent: CLI
review_date: 2025-12-27
---

# tg-stop-flow

Stops a running processing flow.

## Synopsis

```bash
tg-stop-flow -i FLOW_ID [options]
```

## Description

The `tg-stop-flow` command terminates a running flow instance and releases its associated resources. When stopped, the flow becomes unavailable for processing requests and all service endpoints are shut down.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-i, --flow-id FLOW_ID` | Identifier of the flow to stop |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Stop Specific Flow
```bash
tg-stop-flow -i research-flow
```

### Using Custom API URL
```bash
tg-stop-flow -i production-flow -u http://production:8088/
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-start-flow`](tg-start-flow) - Start a processing flow
- [`tg-show-flows`](tg-show-flows) - List all running flows
- [`tg-show-flow-state`](tg-show-flow-state) - Check flow status

## API Integration

This command uses the Flow Management API to terminate flow instances and release resources.
