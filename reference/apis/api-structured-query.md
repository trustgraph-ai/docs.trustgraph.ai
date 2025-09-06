---
layout: default
title: Structured Query API
nav_order: 3
parent: APIs
grand_parent: Reference
permalink: /reference/apis/structured-query
---

# Structured Query API

The Structured Query service executes natural language questions or GraphQL queries against your structured data schemas, returning the actual data results. It works seamlessly with the NLP Query service or can accept direct GraphQL queries.

## Overview

The Structured Query service:
- Executes natural language questions against structured data
- Accepts GraphQL queries directly
- Returns data in multiple formats (JSON, table, CSV)
- Integrates with agent-based extraction workflows
- Supports complex filtering and relationships

## REST API

### Endpoint

```
POST /api/v1/flow/{flow-id}/structured-query
```

### Request Format

```json
{
  "question": "Show all products with price > 100"
}
```

Or with a GraphQL query:

```json
{
  "question": "query { products(where: {price: {_gt: 100}}) { id name price category } }"
}
```

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `question` | string | Yes | Natural language question or GraphQL query |

### Response Format

```json
{
  "data": {
    "products": [
      {
        "id": "1",
        "name": "Laptop",
        "price": 1299.99,
        "category": "Electronics"
      },
      {
        "id": "2", 
        "name": "Smartphone",
        "price": 899.00,
        "category": "Electronics"
      }
    ]
  },
  "errors": []
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `data` | object | Query results organized by entity type |
| `errors` | array | List of any errors encountered during execution |

## Python API

### Basic Usage

```python
from trustgraph.api import Api

# Initialize API client
api = Api("http://localhost:8088/").flow().id("default")

# Execute a natural language query
response = api.structured_query(
    question="List all customers from London"
)

# Access the results
if "data" in response:
    customers = response["data"].get("customers", [])
    for customer in customers:
        print(f"{customer['name']} - {customer['email']}")
```

### Using with NLP Query

```python
# Step 1: Convert natural language to GraphQL
nlp_response = api.nlp_query(
    question="What are the top 5 most expensive products?"
)

# Step 2: Execute the generated query
query_response = api.structured_query(
    question=nlp_response["graphql_query"]
)

# Step 3: Process results
products = query_response["data"]["products"]
for product in products:
    print(f"{product['name']}: ${product['price']}")
```

### Direct GraphQL Execution

```python
# Execute a GraphQL query directly
graphql_query = """
query {
  orders(
    where: {
      orderDate: {_gte: "2024-01-01"},
      total: {_gt: 500}
    },
    orderBy: {orderDate: desc},
    first: 10
  ) {
    id
    orderDate
    total
    customer {
      name
      email
    }
    items {
      product {
        name
      }
      quantity
      price
    }
  }
}
"""

response = api.structured_query(question=graphql_query)
orders = response["data"]["orders"]
```

## Query Examples

### Simple Selection

**Natural Language:**
```json
{
  "question": "Show all products"
}
```

**Response:**
```json
{
  "data": {
    "products": [
      {"id": "1", "name": "Laptop", "price": 1299.99},
      {"id": "2", "name": "Mouse", "price": 29.99}
    ]
  }
}
```

### Filtered Query

**Natural Language:**
```json
{
  "question": "Find customers who placed orders in 2024"
}
```

**Response:**
```json
{
  "data": {
    "customers": [
      {
        "id": "c1",
        "name": "John Smith",
        "orders": [
          {"id": "o1", "orderDate": "2024-01-15", "total": 599.99}
        ]
      }
    ]
  }
}
```

### Aggregation Query

**GraphQL:**
```json
{
  "question": "query { products_aggregate(where: {category: {_eq: \"Electronics\"}}) { aggregate { count avg { price } max { price } min { price } } } }"
}
```

**Response:**
```json
{
  "data": {
    "products_aggregate": {
      "aggregate": {
        "count": 25,
        "avg": {"price": 499.99},
        "max": {"price": 2999.99},
        "min": {"price": 29.99}
      }
    }
  }
}
```

## Integration with Agent Workflows

The Structured Query service integrates with agent-based extraction:

```python
# Agent extracts structured data from documents
agent_response = api.invoke_agent(
    prompt="Extract product information from this catalog",
    text=catalog_text
)

# Query the extracted structured data
query_response = api.structured_query(
    question="What products cost less than $50?"
)

# Results include freshly extracted data
products = query_response["data"]["products"]
```

## Output Formats

The service supports multiple output formats through the CLI:

### Table Format (Default)
```
+----+------------+--------+-------------+
| id | name       | price  | category    |
+----+------------+--------+-------------+
| 1  | Laptop     | 1299.99| Electronics |
| 2  | Mouse      | 29.99  | Electronics |
+----+------------+--------+-------------+
```

### CSV Format
```csv
id,name,price,category
1,Laptop,1299.99,Electronics
2,Mouse,29.99,Electronics
```

### JSON Format
```json
{
  "products": [
    {"id": "1", "name": "Laptop", "price": 1299.99, "category": "Electronics"},
    {"id": "2", "name": "Mouse", "price": 29.99, "category": "Electronics"}
  ]
}
```

## Error Handling

```python
response = api.structured_query(question="Show invalid data")

if "errors" in response and response["errors"]:
    for error in response["errors"]:
        print(f"Error: {error}")
    
# Partial results may still be available
if "data" in response:
    # Process any successful results
    pass
```

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid request format |
| 404 | Flow ID or schema not found |
| 422 | Invalid GraphQL syntax or unrecognized entities |
| 500 | Internal service error |
| 503 | Service temporarily unavailable |

## Supported GraphQL Features

- **Filtering**: `where` clauses with comparison operators
- **Ordering**: `orderBy` with asc/desc
- **Pagination**: `first`, `last`, `offset`
- **Relationships**: Nested entity queries
- **Aggregations**: `count`, `sum`, `avg`, `min`, `max`
- **Grouping**: `groupBy` operations

## See Also

- [NLP Query API](api-nlp-query) - Convert natural language to GraphQL
- [Agent API](api-agent) - Agent-based data extraction
- [Object Storage API](api-object-storage) - Store and retrieve structured objects
- [tg-invoke-structured-query](../cli/tg-invoke-structured-query) - Command-line tool