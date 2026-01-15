---
title: tg-show-processor-state
parent: CLI
review_date: 2025-12-07
---

# tg-show-processor-state

Displays the current state of TrustGraph processors.

## Synopsis

```bash
tg-show-processor-state [options]
```

## Description

The `tg-show-processor-state` command displays the current state of TrustGraph processors by querying the metrics endpoint. Shows active processors with visual status indicators, useful for monitoring health and troubleshooting connectivity.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-m, --metrics-url URL` | `http://localhost:8088/api/metrics` | Metrics endpoint URL |

## Examples

### Display Processor States
```bash
tg-show-processor-state
```

### Custom Metrics URL
```bash
tg-show-processor-state -m http://metrics.example.com:8088/api/metrics
```

## Output Format

The command displays processors with status indicators:

```
✓ text-completion-processor
✓ document-rag-processor
✓ graph-rag-processor
✓ knowledge-processor
✗ inactive-processor
```

Where:
- ✓ indicates an active, healthy processor
- ✗ indicates an inactive or unreachable processor

## Related Commands

- [`tg-show-token-rate`](tg-show-token-rate) - Monitor token usage rates
- [`tg-show-flows`](tg-show-flows) - List running flows

## API Integration

This command queries the Prometheus-compatible metrics endpoint for processor health information.
