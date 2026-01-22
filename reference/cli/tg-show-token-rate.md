---
title: tg-show-token-rate
parent: CLI
review_date: 2026-12-05
---

# tg-show-token-rate

Displays live stream of token usage rates from TrustGraph processors.

## Synopsis

```bash
tg-show-token-rate [options]
```

## Description

The `tg-show-token-rate` command monitors token usage rates from TrustGraph processors in real-time. Displays input tokens, output tokens, and total token rates (tokens per second), calculated as averages since the command started.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-m, --metrics-url URL` | `http://localhost:8088/api/metrics` | Metrics endpoint URL |
| `-p, --period SECONDS` | `1` | Sampling period between measurements |
| `-n, --number-samples COUNT` | `100` | Number of samples before stopping |

## Examples

### Basic Monitoring
```bash
tg-show-token-rate
```

### Custom Sampling Period
```bash
tg-show-token-rate --period 5
```

### Continuous Monitoring
```bash
tg-show-token-rate -n 1000
```

### Remote Monitoring
```bash
tg-show-token-rate -m http://production:8088/api/metrics
```

### Short-term Monitoring
```bash
tg-show-token-rate -n 10 -p 2
```

## Output Format

The command displays token rates in a continuous stream:

```
Input: 1523.4 tokens/sec | Output: 342.1 tokens/sec | Total: 1865.5 tokens/sec
Input: 1589.2 tokens/sec | Output: 356.8 tokens/sec | Total: 1946.0 tokens/sec
Input: 1612.7 tokens/sec | Output: 361.3 tokens/sec | Total: 1974.0 tokens/sec
```

Rates shown are cumulative averages since monitoring started.

## Related Commands

- [`tg-show-token-costs`](tg-show-token-costs) - Display token cost configurations
- [`tg-set-token-costs`](tg-set-token-costs) - Configure token costs

## API Integration

This command queries the Prometheus-compatible metrics endpoint for token usage statistics.
