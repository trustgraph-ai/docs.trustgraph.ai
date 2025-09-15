---
layout: default
title: Object Storage API
parent: APIs
permalink: /reference/apis/object-storage
---

# Object Storage API

The Object Storage service provides a persistent store for structured objects extracted from documents or created through agent workflows. It supports schema-based storage, querying, and import/export of structured data.

## Overview

The Object Storage service:
- Stores structured objects with defined schemas
- Supports bulk import of objects
- Enables querying objects by schema type
- Integrates with extraction workflows
- Maintains metadata and relationships

## REST API

### Object Import Endpoint

Import structured objects into the knowledge graph.

```
POST /api/v1/flow/{flow-id}/objects/import
```

#### Request Format

```json
{
  "metadata": {
    "id": "import-001",
    "user": "system",
    "collection": "products",
    "metadata": {
      "source": "catalog.pdf",
      "extraction_date": "2024-01-15"
    }
  },
  "schema_name": "Product",
  "values": [
    {
      "id": "prod-1",
      "name": "Laptop",
      "price": 1299.99,
      "category": "Electronics",
      "description": "High-performance laptop"
    },
    {
      "id": "prod-2",
      "name": "Mouse",
      "price": 29.99,
      "category": "Electronics",
      "description": "Wireless mouse"
    }
  ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `metadata` | object | Yes | Import metadata including ID, user, and collection |
| `metadata.id` | string | Yes | Unique identifier for this import batch |
| `metadata.user` | string | Yes | User or system initiating the import |
| `metadata.collection` | string | Yes | Target collection name |
| `metadata.metadata` | object | No | Additional metadata (source, date, etc.) |
| `schema_name` | string | Yes | Name of the schema these objects conform to |
| `values` | array | Yes | Array of objects to import |

### Object Query Endpoint

Query stored objects by schema and filters.

```
POST /api/v1/flow/{flow-id}/objects/query
```

#### Request Format

```json
{
  "schema_name": "Product",
  "filters": {
    "category": "Electronics",
    "price": {"$gt": 100}
  },
  "limit": 50,
  "offset": 0
}
```

#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `schema_name` | string | Yes | Schema type to query |
| `filters` | object | No | Filter criteria |
| `limit` | integer | No | Maximum results (default: 100) |
| `offset` | integer | No | Pagination offset (default: 0) |

#### Response Format

```json
{
  "objects": [
    {
      "id": "prod-1",
      "name": "Laptop",
      "price": 1299.99,
      "category": "Electronics",
      "description": "High-performance laptop",
      "_metadata": {
        "created_at": "2024-01-15T10:30:00Z",
        "updated_at": "2024-01-15T10:30:00Z",
        "collection": "products"
      }
    }
  ],
  "total": 25,
  "limit": 50,
  "offset": 0
}
```

## Python API

### Importing Objects

```python
from trustgraph.api import Api

api = Api("http://localhost:8088/").flow().id("default")

# Import product data
products = [
    {
        "id": "p1",
        "name": "Laptop",
        "price": 1299.99,
        "category": "Electronics"
    },
    {
        "id": "p2",
        "name": "Chair",
        "price": 199.99,
        "category": "Furniture"
    }
]

response = api.import_objects(
    metadata={
        "id": "batch-001",
        "user": "admin",
        "collection": "products"
    },
    schema_name="Product",
    values=products
)

print(f"Imported {len(products)} products")
```

### Querying Objects

```python
# Query products by category
response = api.query_objects(
    schema_name="Product",
    filters={"category": "Electronics"},
    limit=10
)

products = response["objects"]
for product in products:
    print(f"{product['name']}: ${product['price']}")
```

### Bulk Import from Files

```python
import json

# Load data from JSON file
with open("products.json", "r") as f:
    product_data = json.load(f)

# Import in batches
batch_size = 100
for i in range(0, len(product_data), batch_size):
    batch = product_data[i:i+batch_size]
    
    api.import_objects(
        metadata={
            "id": f"batch-{i//batch_size}",
            "user": "import-script",
            "collection": "products",
            "metadata": {
                "source": "products.json",
                "batch_number": i//batch_size
            }
        },
        schema_name="Product",
        values=batch
    )
```

## Integration with Extraction Workflows

The Object Storage service integrates seamlessly with extraction workflows:

### Agent-Based Extraction

```python
# Agent extracts structured data from document
agent_response = api.invoke_agent(
    prompt="Extract product information as structured data",
    text=document_text
)

# Extracted objects are automatically stored
extracted_objects = agent_response["extracted_objects"]

# Query the stored objects
products = api.query_objects(
    schema_name="Product",
    filters={"_metadata.extraction_id": agent_response["extraction_id"]}
)
```

### Object Extraction Process

```python
# Configure extraction with schema
extraction_config = {
    "schema": "Product",
    "fields": ["name", "price", "category", "description"],
    "extraction_rules": {
        "price": {"type": "number", "format": "currency"},
        "category": {"type": "enum", "values": ["Electronics", "Furniture", "Clothing"]}
    }
}

# Extract and store objects
response = api.extract_objects(
    document=document_text,
    config=extraction_config
)

# Objects are automatically stored and queryable
object_ids = response["stored_object_ids"]
```

## Schema Management

### Defining Schemas

```python
# Define a product schema
product_schema = {
    "name": "Product",
    "fields": {
        "id": {"type": "string", "required": True},
        "name": {"type": "string", "required": True},
        "price": {"type": "number", "required": True},
        "category": {"type": "string"},
        "description": {"type": "text"},
        "tags": {"type": "array", "items": {"type": "string"}}
    },
    "indexes": ["category", "price"]
}

api.create_schema(product_schema)
```

### Schema Validation

Objects are validated against their schema during import:

```python
try:
    api.import_objects(
        metadata={...},
        schema_name="Product",
        values=[
            {"name": "Invalid Product"}  # Missing required 'id' and 'price'
        ]
    )
except ValidationError as e:
    print(f"Validation failed: {e.errors}")
    # Output: Missing required fields: id, price
```

## Metadata Management

Each stored object includes system metadata:

| Field | Description |
|-------|-------------|
| `_id` | Unique object identifier |
| `_schema` | Schema name |
| `_created_at` | Creation timestamp |
| `_updated_at` | Last update timestamp |
| `_collection` | Collection name |
| `_user` | User who created/imported |
| `_metadata` | Custom metadata |

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid request format or schema validation failure |
| 404 | Schema or collection not found |
| 409 | Duplicate object ID |
| 413 | Import batch too large |
| 500 | Internal storage error |
| 503 | Storage service unavailable |

## Best Practices

1. **Batch Imports**: Import objects in batches of 100-1000 for optimal performance
2. **Schema Design**: Define clear schemas before importing data
3. **Unique IDs**: Ensure object IDs are unique within a collection
4. **Metadata**: Include source and timestamp metadata for traceability
5. **Indexing**: Define indexes on frequently queried fields

## See Also

- [Structured Query API](api-structured-query) - Query stored objects
- [Agent API](api-agent) - Extract objects from documents
- [Knowledge API](api-knowledge) - Knowledge graph operations
- [Import/Export API](api-core-import-export) - Bulk data operations
