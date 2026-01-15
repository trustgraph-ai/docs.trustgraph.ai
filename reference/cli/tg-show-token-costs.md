---
title: tg-show-token-costs
parent: CLI
review_date: 2026-03-10
---

# tg-show-token-costs

Displays token cost configuration for language models in TrustGraph.

## Synopsis

```bash
tg-show-token-costs [options]
```

## Description

The `tg-show-token-costs` command displays the configured token pricing for all language models in TrustGraph. This information shows input and output costs per million tokens, used for cost tracking, billing, and resource management.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Display All Token Costs
```bash
tg-show-token-costs
```

### Using Custom API URL
```bash
tg-show-token-costs -u http://production:8088/
```

## Output Format

The command displays costs in a formatted table:

```
+----------------+-------------+--------------+
| model          | input, $/Mt | output, $/Mt |
+----------------+-------------+--------------+
| gpt-4          |      30.000 |       60.000 |
| gpt-3.5-turbo  |       0.500 |        1.500 |
| claude-3-sonnet|       3.000 |       15.000 |
| claude-3-haiku |       0.250 |        1.250 |
| local-model    |       0.000 |        0.000 |
+----------------+-------------+--------------+
```

### Column Details

- **model**: Language model identifier
- **input, $/Mt**: Cost per million input tokens in USD
- **output, $/Mt**: Cost per million output tokens in USD

Models with incomplete cost configuration show `-` for missing values.

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-set-token-costs`](tg-set-token-costs) - Configure token costs
- [`tg-show-token-rate`](tg-show-token-rate) - View token usage rates

## API Integration

This command uses the [Configuration API](../apis/api-config) to retrieve token cost information.
