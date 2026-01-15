---
title: tg-invoke-nlp-query
parent: CLI
review_date: 2026-02-15
---

# tg-invoke-nlp-query

Converts natural language questions to GraphQL queries using NLP.

## Synopsis

```bash
tg-invoke-nlp-query -q QUESTION [options]
```

## Description

The `tg-invoke-nlp-query` command uses AI to convert natural language questions into GraphQL queries for structured data schemas. Useful for generating queries without knowing GraphQL syntax.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-q, --question QUESTION` | Natural language question to convert |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id FLOW` | `default` | Flow ID to use |
| `-m, --max-results N` | `100` | Maximum number of results |
| `--format FORMAT` | `summary` | Output format: `summary`, `json`, or `graphql` |

## Examples

### Convert Question to GraphQL
```bash
tg-invoke-nlp-query -q "Show all products under $50"
```

### GraphQL Output Format
```bash
tg-invoke-nlp-query -q "List customers from London" --format graphql
```

### JSON Format
```bash
tg-invoke-nlp-query -q "Show sales for Q1 2024" --format json
```

## Output Formats

| Format | Description |
|--------|-------------|
| `summary` | Human-readable summary with generated query |
| `json` | Complete JSON response with query and metadata |
| `graphql` | Generated GraphQL query only |

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-structured-query`](tg-invoke-structured-query) - Execute queries
- [`tg-load-structured-data`](tg-load-structured-data) - Import structured data

## API Integration

This command uses the NLP Query API to convert natural language to GraphQL queries.
