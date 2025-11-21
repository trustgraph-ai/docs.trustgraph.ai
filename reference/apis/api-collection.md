---
title: Collection Management API
parent: APIs
review_date: 2025-11-21
---

# TrustGraph Collection Management API

This API provides collection management for TrustGraph, allowing users to create, list, update, and delete collections. Collections are used to organize and isolate data within TrustGraph, enabling multi-tenancy and project separation.

## Overview

Collections provide a mechanism for organizing TrustGraph data by user and project. Each collection can store documents, embeddings, knowledge graph data, and structured objects in isolation from other collections.

## Request/response

### Request

The request contains the following fields:
- `operation`: The operation to perform (see operations below)
- `user`: User ID who owns the collection
- `collection`: Collection identifier
- `name`: Human-readable collection name (optional)
- `description`: Detailed description of collection purpose (optional)
- `tags`: Array of tags for categorization (optional)
- `tag_filter`: Array of tags for filtering list operations (optional)
- `limit`: Maximum number of results to return (optional)

### Response

The response contains the following fields:
- `collections`: Array of collection metadata objects
- `timestamp`: Response timestamp
- `error`: Error information if operation fails

### Collection Metadata

Each collection object contains:
- `user`: User ID who owns the collection
- `collection`: Unique collection identifier
- `name`: Human-readable name
- `description`: Detailed description
- `tags`: Array of tags
- `created_at`: ISO timestamp when created
- `updated_at`: ISO timestamp when last updated

## Operations

### LIST-COLLECTIONS - List Collections for User

List all collections for a specific user, with optional tag filtering.

Request:
```json
{
    "operation": "list-collections",
    "user": "alice"
}
```

Response:
```json
{
    "collections": [
        {
            "user": "alice",
            "collection": "research",
            "name": "Research Project",
            "description": "Medical research document analysis",
            "tags": ["research", "medical"],
            "created_at": "2024-01-15T10:30:00Z",
            "updated_at": "2024-01-20T14:45:00Z"
        },
        {
            "user": "alice",
            "collection": "archive",
            "name": "Archive",
            "description": "Archived documents",
            "tags": ["archive"],
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        }
    ],
    "timestamp": "2024-01-20T15:00:00Z"
}
```

#### With Tag Filter

Request:
```json
{
    "operation": "list-collections",
    "user": "alice",
    "tag_filter": ["research"]
}
```

Response returns only collections with matching tags.

### UPDATE-COLLECTION - Create or Update Collection

Create a new collection or update metadata of an existing collection.

Request:
```json
{
    "operation": "update-collection",
    "user": "alice",
    "collection": "research",
    "name": "Research Project",
    "description": "Medical research document analysis",
    "tags": ["research", "medical", "priority"]
}
```

Response:
```json
{
    "collections": [
        {
            "user": "alice",
            "collection": "research",
            "name": "Research Project",
            "description": "Medical research document analysis",
            "tags": ["research", "medical", "priority"],
            "created_at": "2024-01-15T10:30:00Z",
            "updated_at": "2024-01-20T15:05:00Z"
        }
    ],
    "timestamp": "2024-01-20T15:05:00Z"
}
```

**Notes:**
- If collection doesn't exist, it will be created
- Only specified fields are updated; others remain unchanged
- All metadata fields (name, description, tags) are optional

### DELETE-COLLECTION - Delete Collection and Data

Permanently delete a collection and all associated data.

Request:
```json
{
    "operation": "delete-collection",
    "user": "alice",
    "collection": "old-research"
}
```

Response:
```json
{
    "timestamp": "2024-01-20T15:10:00Z"
}
```

**Warning**: This operation is irreversible. All data in the collection will be permanently deleted, including:
- Collection metadata
- Documents and embeddings
- Knowledge graph triples
- Structured data objects
- Processing history

## REST Service

The REST service is available at `/api/v1/collection-management` and accepts the above request formats.

## Websocket

Requests have a `request` object containing the operation fields.
Responses have a `response` object containing the response fields.

Request:
```json
{
    "id": "unique-request-id",
    "service": "collection-management",
    "request": {
        "operation": "list-collections",
        "user": "alice"
    }
}
```

Response:
```json
{
    "id": "unique-request-id",
    "response": {
        "collections": [
            {
                "user": "alice",
                "collection": "research",
                "name": "Research Project",
                "description": "Medical research document analysis",
                "tags": ["research", "medical"],
                "created_at": "2024-01-15T10:30:00Z",
                "updated_at": "2024-01-20T14:45:00Z"
            }
        ],
        "timestamp": "2024-01-20T15:00:00Z"
    },
    "complete": true
}
```

## Pulsar

The Pulsar schema for the Collection Management API is defined in Python code here:

https://github.com/trustgraph-ai/trustgraph/blob/master/trustgraph-base/trustgraph/schema/services/collection.py

Default request queue:
`non-persistent://tg/request/collection`

Default response queue:
`non-persistent://tg/response/collection`

Request schema:
`trustgraph.schema.CollectionManagementRequest`

Response schema:
`trustgraph.schema.CollectionManagementResponse`

### Request Schema Fields

```python
class CollectionManagementRequest(Record):
    operation = String()        # Operation to perform
    user = String()            # User ID
    collection = String()      # Collection ID
    timestamp = String()       # Request timestamp (ISO)
    name = String()            # Collection name
    description = String()     # Collection description
    tags = Array(String())     # Collection tags
    created_at = String()      # Created timestamp (ISO)
    updated_at = String()      # Updated timestamp (ISO)
    tag_filter = Array(String())  # Tag filter for list operations
    limit = Integer()          # Result limit
```

### Response Schema Fields

```python
class CollectionManagementResponse(Record):
    error = Error()                        # Error information
    timestamp = String()                   # Response timestamp (ISO)
    collections = Array(CollectionMetadata())  # Collection metadata array
```

### Collection Metadata Schema

```python
class CollectionMetadata(Record):
    user = String()           # User ID
    collection = String()     # Collection ID
    name = String()           # Collection name
    description = String()    # Collection description
    tags = Array(String())    # Collection tags
    created_at = String()     # Created timestamp (ISO)
    updated_at = String()     # Updated timestamp (ISO)
```

## Python SDK

The Python SDK provides convenient access to the Collection Management API:

```python
from trustgraph.api import Api

api = Api("http://localhost:8088/")
collection_api = api.collection()

# List collections
collections = collection_api.list_collections(user="alice")
for collection in collections:
    print(f"{collection.collection}: {collection.name}")

# List collections with tag filter
research_collections = collection_api.list_collections(
    user="alice",
    tag_filter=["research"]
)

# Create or update collection
collection_api.update_collection(
    user="alice",
    collection="research",
    name="Research Project",
    description="Medical research document analysis",
    tags=["research", "medical"]
)

# Delete collection
collection_api.delete_collection(user="alice", collection="old-research")
```

## Features

- **Multi-Tenancy**: Separate collections per user
- **Organization**: Tag-based categorization and filtering
- **Metadata Management**: Rich metadata with names and descriptions
- **Data Isolation**: Complete isolation between collections
- **Lifecycle Management**: Create, update, and delete operations
- **Atomic Operations**: Collection operations are atomic

## Use Cases

### Project Organization
```python
# Create collections for different projects
api.collection().update_collection(
    user="research-team",
    collection="project-alpha",
    name="Project Alpha",
    description="Alpha project knowledge base",
    tags=["research", "active", "2024"]
)
```

### Multi-Tenant Applications
```python
# Set up collections for different customers
for customer_id in customer_ids:
    api.collection().update_collection(
        user=customer_id,
        collection="main",
        name=f"{customer_id} Main Collection",
        description=f"Primary collection for {customer_id}",
        tags=["customer", "production"]
    )
```

### Data Lifecycle Management
```python
# Archive old collections
old_collections = api.collection().list_collections(
    user="archive-team",
    tag_filter=["archive"]
)
for collection in old_collections:
    # Export data, then delete
    api.collection().delete_collection(
        user="archive-team",
        collection=collection.collection
    )
```

## Error Handling

Errors are returned in the response `error` field:

```json
{
    "error": {
        "type": "CollectionNotFound",
        "message": "Collection 'invalid-name' not found"
    },
    "timestamp": "2024-01-20T15:00:00Z"
}
```

Common error types:
- `CollectionNotFound`: Collection doesn't exist
- `PermissionDenied`: User lacks permissions
- `InvalidRequest`: Malformed request
- `InternalError`: Server-side error

## Related APIs

- [Flow API](api-flow) - Manage processing flows
- [Knowledge API](api-knowledge) - Knowledge graph operations
- [Librarian API](api-librarian) - Document management

## CLI Tools

- [`tg-list-collections`](../cli/tg-list-collections) - List collections
- [`tg-set-collection`](../cli/tg-set-collection) - Create/update collections
- [`tg-delete-collection`](../cli/tg-delete-collection) - Delete collections
