---
title: tg-show-flow-state
parent: CLI
review_date: 2026-03-23
---

# tg-show-flow-state

Displays the processor states for a specific flow and its associated flow blueprint.

## Synopsis

```bash
tg-show-flow-state [options]
```

## Description

The `tg-show-flow-state` command shows the current state of processors within a specific TrustGraph flow instance and its corresponding flow blueprint. It queries the metrics system to determine which processing components are running and displays their status with visual indicators.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-f, --flow-id ID` | `default` | Flow instance ID to examine |
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-m, --metrics-url URL` | `http://localhost:8088/api/metrics` | Metrics API URL |

## Examples

### Check Default Flow State
```bash
tg-show-flow-state
```

### Check Specific Flow
```bash
tg-show-flow-state -f "production-flow"
```

### Use Custom Metrics URL
```bash
tg-show-flow-state \
  -f "research-flow" \
  -m "http://metrics-server:8088/api/metrics"
```

## Output Format

The command displays processor states for both the flow instance and its flow blueprint:

```
Flow production-flow
- pdf-processor                💚
- text-extractor              💚
- embeddings-generator        💚
- knowledge-builder           ❌
- document-indexer            💚

Class document-processing-v2
- base-pdf-processor          💚
- base-text-extractor         💚
- base-embeddings-generator   💚
- base-knowledge-builder      💚
- base-document-indexer       💚
```

### Status Indicators
- **💚 (Green Heart)**: Processor is running and healthy
- **❌ (Red X)**: Processor is not running or unhealthy

## Notes

The command queries the metrics system to determine processor health. A processor showing ❌ indicates it may have crashed, not started, or encountered an error.

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-flows`](tg-show-flows) - List all flows
- [`tg-start-flow`](tg-start-flow) - Start a flow
- [`tg-stop-flow`](tg-stop-flow) - Stop a flow
- [`tg-show-processor-state`](tg-show-processor-state) - Show processor details

## API Integration

This command uses the [Metrics API](../apis/api-metrics) to retrieve processor state information.
