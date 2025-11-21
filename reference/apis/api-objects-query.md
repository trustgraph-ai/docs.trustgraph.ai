---
title: Objects Query API
parent: APIs
permalink: /reference/apis/objects-query
review_date: 2026-04-28
---

# Objects Query API

The Objects Query service executes GraphQL queries against structured data stored in TrustGraph, providing a flexible and powerful way to retrieve, filter, and traverse relationships in your knowledge graph.

## Overview

The Objects Query service:
- Executes standard GraphQL queries against your data
- Supports complex filtering, sorting, and pagination
- Handles nested relationships and graph traversals
- Returns data in GraphQL-compliant format
- Integrates with the NLP Query service for natural language queries

## REST API

### Endpoint

```
POST /api/v1/flow/{flow-id}/service/objects
```

### Request Format

```json
{
  "user": "trustgraph",
  "collection": "default",
  "query": "query { products { id name price } }",
  "variables": {},
  "operation_name": null
}
```

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user` | string | No | Cassandra keyspace identifier (default: "trustgraph") |
| `collection` | string | No | Data collection identifier (default: "default") |
| `query` | string | Yes | GraphQL query string |
| `variables` | object | No | GraphQL variables for parameterized queries |
| `operation_name` | string | No | Operation to execute for multi-operation documents |

### Response Format

```json
{
  "data": {
    "products": [
      {
        "id": "1",
        "name": "Laptop",
        "price": 1299.99
      }
    ]
  },
  "errors": [],
  "extensions": {}
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `data` | object | Query results following GraphQL specification |
| `errors` | array | GraphQL errors with message, path, and extensions |
| `extensions` | object | Query metadata (execution time, etc.) |
| `error` | object | System-level error (if request failed) |

## Python API

### Basic Usage

```python
from trustgraph.api import Api

# Initialize API client
api = Api("http://localhost:8088/").flow().id("default")

# Execute a GraphQL query
response = api.objects_query(
    query="""
    query {
        customers(where: {city: {_eq: "London"}}) {
            id
            name
            email
            orders {
                id
                total
                orderDate
            }
        }
    }
    """,
    user="trustgraph",
    collection="default"
)

# Process results
if "data" in response:
    customers = response["data"]["customers"]
    for customer in customers:
        print(f"{customer['name']}: {len(customer.get('orders', []))} orders")

# Check for errors
if "errors" in response:
    for error in response["errors"]:
        print(f"Error: {error['message']}")
```

### Using Variables

```python
# Define query with variables
query = """
query GetProductsByCategory($category: String!, $minPrice: Float) {
    products(
        where: {
            category: {_eq: $category},
            price: {_gte: $minPrice}
        }
    ) {
        id
        name
        price
        description
    }
}
"""

# Execute with variables
response = api.objects_query(
    query=query,
    variables={
        "category": "Electronics",
        "minPrice": 100.0
    }
)

products = response["data"]["products"]
```

### Multiple Operations

```python
# Document with multiple operations
query = """
query GetProducts {
    products {
        id
        name
    }
}

query GetCustomers {
    customers {
        id
        name
    }
}
"""

# Execute specific operation
response = api.objects_query(
    query=query,
    operation_name="GetProducts"
)
```

## GraphQL Query Examples

### Simple Selection

```graphql
query {
    products {
        id
        name
        price
        category
    }
}
```

### Filtering with Where Clause

```graphql
query {
    orders(
        where: {
            total: {_gt: 500},
            orderDate: {_gte: "2024-01-01"}
        }
    ) {
        id
        total
        orderDate
    }
}
```

### Nested Relationships

```graphql
query {
    customers {
        id
        name
        orders {
            id
            total
            items {
                product {
                    name
                    price
                }
                quantity
            }
        }
    }
}
```

### Sorting and Pagination

```graphql
query {
    products(
        orderBy: {price: desc},
        first: 10,
        offset: 20
    ) {
        id
        name
        price
    }
}
```

### Aggregations

```graphql
query {
    products_aggregate(
        where: {category: {_eq: "Electronics"}}
    ) {
        aggregate {
            count
            sum {
                price
            }
            avg {
                price
            }
            max {
                price
            }
            min {
                price
            }
        }
    }
}
```

## Supported GraphQL Features

### Filtering Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `_eq` | Equals | `{price: {_eq: 100}}` |
| `_neq` | Not equals | `{status: {_neq: "cancelled"}}` |
| `_gt` | Greater than | `{price: {_gt: 50}}` |
| `_gte` | Greater than or equal | `{age: {_gte: 18}}` |
| `_lt` | Less than | `{quantity: {_lt: 10}}` |
| `_lte` | Less than or equal | `{discount: {_lte: 0.5}}` |
| `_in` | In list | `{category: {_in: ["Electronics", "Books"]}}` |
| `_nin` | Not in list | `{status: {_nin: ["deleted", "archived"]}}` |
| `_like` | Pattern match | `{name: {_like: "%Smith%"}}` |
| `_ilike` | Case-insensitive pattern | `{email: {_ilike: "%@gmail.com"}}` |
| `_is_null` | Check for null | `{deletedAt: {_is_null: true}}` |

### Logical Operators

```graphql
query {
    products(
        where: {
            _and: [
                {category: {_eq: "Electronics"}},
                {price: {_between: [100, 500]}}
            ],
            _or: [
                {inStock: {_eq: true}},
                {preOrder: {_eq: true}}
            ]
        }
    ) {
        id
        name
    }
}
```

### Ordering

```graphql
query {
    products(
        orderBy: [
            {category: asc},
            {price: desc}
        ]
    ) {
        id
        name
        category
        price
    }
}
```

### Pagination

```graphql
query {
    products(
        first: 20,      # Limit results
        offset: 40      # Skip first 40
    ) {
        id
        name
    }
}
```

## Error Handling

### GraphQL Errors

GraphQL errors are returned in the `errors` array:

```python
response = api.objects_query(query="{ invalid }")

if "errors" in response:
    for error in response["errors"]:
        print(f"Message: {error['message']}")
        if "path" in error:
            print(f"Path: {error['path']}")
        if "extensions" in error:
            print(f"Extensions: {error['extensions']}")
```

### System Errors

System-level errors are returned in the `error` field:

```python
response = api.objects_query(query="...")

if "error" in response:
    error = response["error"]
    print(f"Error type: {error['type']}")
    print(f"Error message: {error['message']}")
```

## Error Response Example

```json
{
  "data": null,
  "errors": [
    {
      "message": "Field 'invalidField' doesn't exist on type 'Product'",
      "path": ["products", 0, "invalidField"],
      "extensions": {
        "code": "GRAPHQL_VALIDATION_FAILED"
      }
    }
  ]
}
```

## Performance Considerations

1. **Use field selection** - Only request fields you need
2. **Implement pagination** - Use `first` and `offset` for large result sets
3. **Optimize nested queries** - Limit depth of relationship traversal
4. **Use variables** - Parameterized queries are cached more efficiently
5. **Consider aggregations** - Use `_aggregate` queries for counts and statistics

## Integration with Other Services

### With NLP Query

```python
# Convert natural language to GraphQL
nlp_response = api.nlp_query(
    question="Show me all orders from last month"
)

# Execute the generated GraphQL
objects_response = api.objects_query(
    query=nlp_response["graphql_query"],
    variables=nlp_response.get("variables", {})
)
```

### With Structured Query

The Structured Query service provides a higher-level interface that combines NLP Query and Objects Query:

```python
# One-step natural language query
response = api.structured_query(
    question="What are the top selling products?"
)
```

## See Also

- [NLP Query API](api-nlp-query) - Convert natural language to GraphQL
- [Structured Query API](api-structured-query) - High-level query interface
- [Object Storage API](api-object-storage) - Store and manage objects
- [tg-invoke-objects-query](../cli/tg-invoke-objects-query) - Command-line tool