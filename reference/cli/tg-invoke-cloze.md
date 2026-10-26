---
title: tg-invoke-cloze
parent: CLI
review_date: 2027-10-26
---

# tg-invoke-cloze

Classify text using a trained cloze model instance.

## Synopsis

```bash
tg-invoke-cloze -m MODEL QUERY [options]
```

## Description

Sends a query to a trained cloze model instance and returns the predicted label with a confidence score. The model must have been previously trained from labeled examples stored in the workspace configuration.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-m, --model MODEL` | Name of the trained cloze model instance |
| `QUERY` (positional) | Query text to classify |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8888/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | `$TRUSTGRAPH_WORKSPACE` or `default` | Workspace identifier |
| `-f, --flow-id FLOW` | `default` | Flow ID |

## Examples

```bash
# Classify a support ticket
tg-invoke-cloze -m ticket-classifier "My account has been locked"

# Classify with a specific workspace
tg-invoke-cloze -w production -m sentiment "Great product, love it!"
```

## Output

```
Label: billing
Confidence: 94.2%
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-list-cloze-models`](tg-list-cloze-models) - List available cloze model instances
- [`tg-invoke-decision-scoring`](tg-invoke-decision-scoring) - Structured decision scoring
