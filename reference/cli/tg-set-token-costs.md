---
title: tg-set-token-costs
parent: CLI
review_date: 2026-05-05
---

# tg-set-token-costs

Sets token cost configuration for language models in TrustGraph.

## Synopsis

```bash
tg-set-token-costs --model MODEL_ID -i INPUT_COST -o OUTPUT_COST [options]
```

## Description

The `tg-set-token-costs` command configures the token pricing for language models used by TrustGraph. Token costs are specified in dollars per million tokens and are used for cost tracking, billing, and resource management.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--model MODEL_ID` | Language model identifier |
| `-i, --input-costs COST` | Input token cost in $ per 1M tokens |
| `-o, --output-costs COST` | Output token cost in $ per 1M tokens |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Set Costs for GPT-4
```bash
tg-set-token-costs --model "gpt-4" -i 30.0 -o 60.0
```

### Set Costs for Claude Sonnet
```bash
tg-set-token-costs --model "claude-3-sonnet" -i 3.0 -o 15.0
```

### Set Costs for Local Model (Free)
```bash
tg-set-token-costs --model "llama-2-7b" -i 0.0 -o 0.0
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-token-costs`](tg-show-token-costs) - Display token costs
- [`tg-show-token-rate`](tg-show-token-rate) - View token usage rates

## API Integration

This command uses the [Configuration API](../apis/api-config) to store token cost configuration.
