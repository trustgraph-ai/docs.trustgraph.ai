---
layout: default
title: tg-invoke-nlp-query
parent: CLI
---

# tg-invoke-nlp-query

Convert natural language questions to GraphQL queries using the NLP Query service.

## Synopsis

```bash
tg-invoke-nlp-query -q QUESTION [OPTIONS]
```

## Description

The `tg-invoke-nlp-query` command uses AI to convert natural language questions into GraphQL queries that can be executed against your structured data schemas. This tool is useful for:

- Generating GraphQL queries without knowing GraphQL syntax
- Testing query generation capabilities
- Building queries for use with the Structured Query service
- Exploring available schemas through natural language

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `-q`, `--question QUESTION` | Natural language question to convert | Required |
| `-u`, `--url URL` | TrustGraph API URL | `http://localhost:8088/` |
| `-f`, `--flow-id ID` | Flow ID to use | `default` |
| `-m`, `--max-results N` | Maximum number of results | `100` |
| `--format FORMAT` | Output format: `summary`, `json`, `graphql` | `summary` |
| `-h`, `--help` | Show help message | - |

## Output Formats

### Summary Format (Default)

Human-readable output showing the generated query and metadata:

```bash
$ tg-invoke-nlp-query -q "Show all products over $100"

Generated GraphQL Query:
----------------------------------------
query { products(where: {price: {_gt: 100}}) { id name price category } }
----------------------------------------
Detected Schemas: Product
Confidence: 85.00%
```

### GraphQL Format

Outputs only the generated GraphQL query:

```bash
$ tg-invoke-nlp-query -q "List customers from London" --format graphql

query { customers(where: {city: {_eq: "London"}}) { id name email city } }
```

### JSON Format

Complete response in JSON format:

```bash
$ tg-invoke-nlp-query -q "Count orders by status" --format json

{
  "graphql_query": "query { orders_aggregate(groupBy: [status]) { group { status } aggregate { count } } }",
  "detected_schemas": ["Order"],
  "confidence": 0.92,
  "variables": {}
}
```

## Examples

### Basic Query Generation

```bash
# Simple selection query
tg-invoke-nlp-query -q "Show all products"

# Filtered query
tg-invoke-nlp-query -q "Find orders placed in January 2024"

# Query with relationships
tg-invoke-nlp-query -q "List customers who bought electronics"
```

### Using with Structured Query

Generate a query and execute it:

```bash
# Generate the GraphQL query
QUERY=$(tg-invoke-nlp-query -q "Products under $50" --format graphql)

# Execute the query
echo "$QUERY" | tg-invoke-structured-query -q -
```

### Limiting Results

```bash
# Limit to 10 results
tg-invoke-nlp-query -q "Recent orders" -m 10

# The generated query will include: first: 10
```

### Custom Flow ID

```bash
# Use a specific flow configuration
tg-invoke-nlp-query -f production -q "Active users"
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `TRUSTGRAPH_URL` | Default API URL | `http://localhost:8088/` |

## Exit Codes

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | Error (invalid query, service error, etc.) |

## Common Use Cases

### Exploring Available Data

```bash
# See what types of data are available
tg-invoke-nlp-query -q "Show me everything about customers"
```

### Building Complex Queries

```bash
# Aggregation query
tg-invoke-nlp-query -q "What's the average order value by month?"

# Multi-table join
tg-invoke-nlp-query -q "Which products have never been ordered?"
```

### Testing Schema Detection

```bash
# Check if schemas are properly detected
tg-invoke-nlp-query -q "Products, orders, and customers" --format json | jq .detected_schemas
```

## Troubleshooting

### No GraphQL Query Generated

If the service cannot generate a query:
- Check that relevant schemas are loaded
- Verify the question references valid entities
- Try rephrasing the question more explicitly

### Low Confidence Scores

Confidence scores below 0.5 may indicate:
- Ambiguous question phrasing
- Missing schema information
- Complex queries that need simplification

### Service Unavailable

If the service is not responding:
- Verify TrustGraph is running: `docker ps`
- Check the API URL is correct
- Ensure the flow ID exists

## See Also

- [tg-invoke-structured-query](tg-invoke-structured-query) - Execute queries against structured data
- [NLP Query API](../apis/api-nlp-query) - API documentation
- [Structured Query API](../apis/api-structured-query) - Query execution API
