---
title: tg-invoke-structured-query
parent: CLI
review_date: 2026-04-10
---

# tg-invoke-structured-query

Executes natural language questions or GraphQL queries against structured data.

## Synopsis

```bash
tg-invoke-structured-query -q QUESTION [options]
```

## Description

The `tg-invoke-structured-query` command executes queries against structured data, accepting either natural language questions (automatically converted to GraphQL) or GraphQL queries directly. This is the primary command-line tool for retrieving structured data.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-q, --question QUESTION` | Natural language question or GraphQL query |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id FLOW` | `default` | Flow ID to use |
| `--format FORMAT` | `table` | Output format: `table`, `json`, or `csv` |

## Examples

### Natural Language Query
```bash
tg-invoke-structured-query -q "Show all products under $50"
```

### JSON Output
```bash
tg-invoke-structured-query -q "List customers from London" --format json
```

### CSV Export
```bash
tg-invoke-structured-query -q "Show sales for Q1 2024" --format csv > sales-q1.csv
```

### GraphQL Query
```bash
tg-invoke-structured-query -q '{
  products(filter: {price: {lt: 50}}) {
    id
    name
    price
  }
}'
```

### Specific Flow
```bash
tg-invoke-structured-query \
  -f analytics-flow \
  -q "Show revenue by product category"
```

## Output Formats

| Format | Description | Use Case |
|--------|-------------|----------|
| `table` | Formatted ASCII table | Human-readable viewing |
| `json` | Complete JSON response | API integration, further processing |
| `csv` | Comma-separated values | Spreadsheet import, data export |

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-objects-query`](tg-invoke-objects-query) - Query objects with filters
- [`tg-load-structured-data`](tg-load-structured-data) - Import structured data

## API Integration

This command uses the Structured Query API to execute queries against loaded structured data collections.
