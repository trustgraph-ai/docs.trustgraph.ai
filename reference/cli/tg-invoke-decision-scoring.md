---
title: tg-invoke-decision-scoring
parent: CLI
review_date: 2027-10-26
---

# tg-invoke-decision-scoring

Score structured decisions using the Laya decision model.

## Synopsis

```bash
tg-invoke-decision-scoring -s STATE -q QUESTIONS [options]
```

## Description

Sends state and question specifications to the decision-scoring service and returns scored answers. Supports three output types per request: choice (select from options), score (probability distribution over ordered levels), and noul (binary yes/no confidence). Multiple questions can be evaluated in a single call against the same input state.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-s, --state STATE` | State as a JSON string or `@filename` (`@-` for stdin) |
| `-q, --questions QUESTIONS` | Questions specification as a JSON string or `@filename` |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8888/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | `$TRUSTGRAPH_WORKSPACE` or `default` | Workspace identifier |
| `-f, --flow-id FLOW` | `default` | Flow ID |

## Question Types

### Choice
Select from a list of options with per-option probabilities:
```json
{"department": {"type": "choice", "criteria": ["sales", "support", "billing"], "instructions": "Which department?"}}
```

### Score
Probability distribution over ordered levels:
```json
{"urgency": {"type": "score", "criteria": ["low", "medium", "high", "critical"], "instructions": "How urgent?"}}
```

### Noul
Binary yes/no confidence:
```json
{"refund_requested": {"type": "noul", "instructions": "Is the customer requesting a refund?"}}
```

## Examples

```bash
# Evaluate a customer service request
tg-invoke-decision-scoring \
  -s '{"category": "billing", "message": "I was overcharged last month"}' \
  -q '{"department": {"type": "choice", "criteria": ["sales", "support", "billing"], "instructions": "Which department should handle this?"}}'

# Load state from a file
tg-invoke-decision-scoring -s @state.json -q @questions.json
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-invoke-cloze`](tg-invoke-cloze) - Cloze model classification
- [`tg-invoke-llm`](tg-invoke-llm) - Direct LLM text completion
