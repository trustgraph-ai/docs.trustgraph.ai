---
title: tg-show-flows
parent: CLI
review_date: 2026-06-16
---

# tg-show-flows

Shows configured flows with their interfaces and queue information.

## Synopsis

```bash
tg-show-flows [options]
```

## Description

The `tg-show-flows` command displays all currently configured flow instances, including identifiers, blueprint names, descriptions, and available service interfaces with corresponding Pulsar queue names.

**New in v1.4**: Displays flow parameter settings with human-readable descriptions.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Show All Flows
```bash
tg-show-flows
```

### Using Custom API URL
```bash
tg-show-flows -u http://production:8088/
```

## Output Format

Each flow is displayed in a table showing:
- **id**: Flow instance identifier
- **class**: Flow blueprint name
- **desc**: Human-readable description
- **parameters**: Configured parameter values (v1.4+)
- **queue**: Service interface endpoints and Pulsar queue names

Example output:
```
+-------------+---------------------------+
| id          | research-flow             |
| class       | document-rag+graph-rag    |
| desc        | Research document pipeline |
| parameters  | • LLM model: GPT-4        |
|             | • Temperature: 0.7        |
| queue       | agent request: non-persistent://tg/request/agent:default |
|             | graph-rag request: non-persistent://tg/request/graph-rag:... |
+-------------+---------------------------+
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-start-flow`](tg-start-flow) - Start a processing flow
- [`tg-stop-flow`](tg-stop-flow) - Stop a running flow
- [`tg-show-flow-state`](tg-show-flow-state) - Check flow status

## API Integration

This command uses the Flow Management API to retrieve flow configurations and interface endpoints.
