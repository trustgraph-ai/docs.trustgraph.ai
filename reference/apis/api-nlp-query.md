---
layout: default
title: NLP Query API
nav_order: 2
parent: APIs
grand_parent: Reference
permalink: /reference/apis/nlp-query
---

# NLP Query API

The NLP Query service converts natural language questions into GraphQL queries that can be executed against your structured data schemas. This service uses AI to understand the intent of your question and generate appropriate GraphQL syntax.

## Overview

The NLP Query service:
- Accepts natural language questions in plain English
- Analyzes available GraphQL schemas in your knowledge graph
- Generates syntactically correct GraphQL queries
- Returns confidence scores and detected schemas
- Supports limiting result counts

## REST API

### Endpoint

```
POST /api/v1/flow/{flow-id}/nlp-query
```

### Request Format

```json
{
  "question": "What products have a price greater than 50?",
  "max_results": 100
}
```

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `question` | string | Yes | The natural language question to convert to GraphQL |
| `max_results` | integer | No | Maximum number of results to return (default: 100) |

### Response Format

```json
{
  "graphql_query": "query { products(where: {price: {_gt: 50}}) { id name price category } }",
  "detected_schemas": ["Product", "Category"],
  "confidence": 0.85,
  "variables": {},
  "error": null
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `graphql_query` | string | The generated GraphQL query |
| `detected_schemas` | array | List of schema types detected in the question |
| `confidence` | float | Confidence score (0-1) of the query generation |
| `variables` | object | GraphQL variables if the query uses them |
| `error` | object | Error details if generation failed |

## Python API

### Using the API Client

```python
from trustgraph.api import Api

# Initialize API client
api = Api("http://localhost:8088/").flow().id("default")

# Convert natural language to GraphQL
response = api.nlp_query(
    question="Show me all customers from London",
    max_results=50
)

# Extract the GraphQL query
graphql_query = response["graphql_query"]
print(f"Generated query: {graphql_query}")
```

### Error Handling

```python
try:
    response = api.nlp_query(
        question="What are the top selling products?"
    )
    
    if "error" in response and response["error"]:
        print(f"Error: {response['error']['message']}")
    else:
        query = response["graphql_query"]
        # Execute the query using structured_query API
        
except Exception as e:
    print(f"API call failed: {e}")
```

## Examples

### Simple Query

**Input:**
```json
{
  "question": "List all products",
  "max_results": 10
}
```

**Output:**
```json
{
  "graphql_query": "query { products(first: 10) { id name price } }",
  "detected_schemas": ["Product"],
  "confidence": 0.95
}
```

### Filtered Query with Relationships

**Input:**
```json
{
  "question": "Find orders from customer John Smith with total over 1000",
  "max_results": 20
}
```

**Output:**
```json
{
  "graphql_query": "query { orders(where: {customer: {name: {_eq: \"John Smith\"}}, total: {_gt: 1000}}, first: 20) { id orderDate total customer { name email } items { product { name } quantity } } }",
  "detected_schemas": ["Order", "Customer", "Product"],
  "confidence": 0.82
}
```

### Aggregation Query

**Input:**
```json
{
  "question": "What is the average price of products in the electronics category?"
}
```

**Output:**
```json
{
  "graphql_query": "query { products_aggregate(where: {category: {_eq: \"electronics\"}}) { aggregate { avg { price } } } }",
  "detected_schemas": ["Product"],
  "confidence": 0.88
}
```

## Integration with Structured Query

The NLP Query service is designed to work seamlessly with the [Structured Query API](api-structured-query). A typical workflow:

1. Use NLP Query to convert natural language to GraphQL
2. Pass the generated GraphQL to Structured Query for execution
3. Receive the actual data results

```python
# Step 1: Convert to GraphQL
nlp_response = api.nlp_query(question="Show recent orders")
graphql = nlp_response["graphql_query"]

# Step 2: Execute the query
data_response = api.structured_query(question=graphql)
results = data_response["data"]
```

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid request format or missing required fields |
| 404 | Flow ID not found |
| 422 | Question cannot be parsed or no schemas detected |
| 500 | Internal service error |
| 503 | Service temporarily unavailable |

## See Also

- [Structured Query API](api-structured-query) - Execute queries against structured data
- [Agent API](api-agent) - Advanced agent-based query processing
- [tg-invoke-nlp-query](../cli/tg-invoke-nlp-query) - Command-line tool