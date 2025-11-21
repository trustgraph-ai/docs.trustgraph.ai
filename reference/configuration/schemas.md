---
title: Schemas
parent: Configuration
grand_parent: Reference
nav_order: 2
permalink: /reference/configuration/schemas
review_date: 2026-08-01
---

# Schema Configuration

Schemas define the structure and properties of structured data objects in TrustGraph. They are used for object extraction, structured data import, and querying with GraphQL and natural language interfaces.

## Overview

Schemas serve as blueprints for structured data in TrustGraph. Each schema defines:
- **Object structure** - The fields and their data types
- **Primary keys** - Fields that uniquely identify objects
- **Required fields** - Fields that must have values
- **Indexes** - Fields optimized for querying
- **Validation rules** - Data quality constraints

Schemas are stored in TrustGraph's configuration system with the configuration type `schema` and are managed through the standard configuration CLI commands.

## Schema Structure

Every schema definition has the following structure:

```json
{
  "name": "Schema Display Name",
  "description": "Human-readable description of what this schema represents",
  "fields": [
    {
      "id": "unique-field-id",
      "name": "field_name",
      "type": "data_type",
      "primary_key": true/false,
      "required": true/false
    }
  ],
  "indexes": ["field1", "field2"]
}
```

### Top-level Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Display name for the schema |
| `description` | string | Yes | Detailed description of the schema's purpose |
| `fields` | array | Yes | Array of field definitions |
| `indexes` | array | No | List of field names to index for faster queries |

### Field Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the field (UUID format) |
| `name` | string | Yes | Field name used in queries and data |
| `type` | string | Yes | Data type (see supported types below) |
| `primary_key` | boolean | Yes | Whether this field is part of the primary key |
| `required` | boolean | Yes | Whether this field must have a value |

### Supported Data Types

| Type | Description | Example Values |
|------|-------------|---------------|
| `string` | Text data | `"Paris"`, `"product-123"` |
| `integer` | Whole numbers | `42`, `-10`, `0` |
| `float` | Decimal numbers | `3.14`, `-2.5`, `100.0` |
| `boolean` | True/false values | `true`, `false` |
| `date` | Date values | `"2024-01-15"` |
| `datetime` | Date and time | `"2024-01-15T10:30:00Z"` |

## Complete Example

Here's a complete schema definition for pie data:

```json
{
  "name": "Pies",
  "description": "Pie measurements including dimensions, weight, pricing, and regional characteristics for various pie types",
  "fields": [
    {
      "id": "0000c3d4-5e6f-7890-abcd-ef1234567890",
      "name": "pie_type",
      "type": "string",
      "primary_key": true,
      "required": true
    },
    {
      "id": "0000d4e5-6f78-9012-bcde-f23456789012",
      "name": "region",
      "type": "string",
      "primary_key": true,
      "required": true
    },
    {
      "id": "0000e5f6-7890-1234-cdef-345678901234",
      "name": "diameter_cm",
      "type": "float",
      "primary_key": false,
      "required": true
    },
    {
      "id": "0000f6a7-8901-2345-def0-456789012345",
      "name": "height_cm",
      "type": "float",
      "primary_key": false,
      "required": true
    },
    {
      "id": "0000a7b8-9012-3456-ef01-567890123456",
      "name": "weight_grams",
      "type": "float",
      "primary_key": false,
      "required": true
    },
    {
      "id": "0000b8c9-0123-4567-f012-678901234567",
      "name": "crust_type",
      "type": "string",
      "primary_key": false,
      "required": true
    },
    {
      "id": "0000c9d0-1234-5678-0123-789012345678",
      "name": "filling_category",
      "type": "string",
      "primary_key": false,
      "required": true
    },
    {
      "id": "0000d0e1-2345-6789-1234-890123456789",
      "name": "price",
      "type": "float",
      "primary_key": false,
      "required": true
    },
    {
      "id": "0000e1f2-3456-7890-2345-901234567890",
      "name": "currency",
      "type": "string",
      "primary_key": false,
      "required": true
    },
    {
      "id": "0000f2a3-4567-8901-3456-012345678901",
      "name": "bakery_type",
      "type": "string",
      "primary_key": false,
      "required": true
    }
  ],
  "indexes": ["filling_category", "currency", "region", "bakery_type"]
}
```

## Managing Schemas

### Creating Schemas

Use `tg-put-config-item` to create a new schema:

```bash
tg-put-config-item --type schema --key pies --value '{
  "name": "Pies",
  "description": "Pie data schema",
  "fields": [
    {
      "id": "0000c3d4-5e6f-7890-abcd-ef1234567890",
      "name": "pie_type",
      "type": "string",
      "primary_key": true,
      "required": true
    },
    {
      "id": "0000d4e5-6f78-9012-bcde-f23456789012",
      "name": "region",
      "type": "string",
      "primary_key": true,
      "required": true
    }
  ],
  "indexes": ["region"]
}'
```

### Retrieving Schemas

List all schemas:
```bash
tg-list-config-items --type schema
```

Get a specific schema:
```bash
tg-get-config-item --type schema --key pies
```

### Updating Schemas

Update an existing schema:
```bash
tg-put-config-item --type schema --key pies --value '{
  "name": "Enhanced Pies",
  "description": "Updated pie data schema with additional fields",
  "fields": [
    // ... updated field definitions
  ],
  "indexes": ["region", "filling_category"]
}'
```

### Deleting Schemas

Remove a schema:
```bash
tg-delete-config-item --type schema --key pies
```

## Primary Keys

Primary keys uniquely identify objects within a collection. You can define composite primary keys using multiple fields:

### Single Primary Key
```json
{
  "fields": [
    {
      "name": "product_id",
      "type": "string",
      "primary_key": true,
      "required": true
    }
  ]
}
```

### Composite Primary Key
```json
{
  "fields": [
    {
      "name": "pie_type",
      "type": "string", 
      "primary_key": true,
      "required": true
    },
    {
      "name": "region",
      "type": "string",
      "primary_key": true,
      "required": true
    }
  ]
}
```

## Indexes

Indexes improve query performance for frequently accessed fields:

```json
{
  "indexes": ["category", "price", "created_date"]
}
```

**Guidelines:**
- Index fields used in `WHERE` clauses
- Index fields used for sorting (`ORDER BY`)
- Index fields used in joins and relationships
- Avoid indexing fields that change frequently
- Balance query performance with storage overhead

## Field IDs

Each field must have a unique UUID identifier:

```json
{
  "id": "0000c3d4-5e6f-7890-abcd-ef1234567890",
  "name": "field_name"
}
```

**Requirements:**
- Must be a valid UUID format
- Must be unique within the schema
- Should be generated once and never changed
- Used internally by TrustGraph for field mapping

## Using Schemas

### Object Extraction

Schemas guide agent-based object extraction from documents:

```bash
# Extract objects using a schema
tg-start-flow --id extraction-flow --class object-extract

# Process document with schema guidance
tg-add-library-document document.pdf
```

### Structured Data Import

Load structured data using schemas:

```bash
# Load CSV data with schema validation
tg-load-structured-data -f data.csv -s pies -c pies-collection

# Auto-generate schema from data
tg-load-structured-data -f data.csv -s auto -c pies-collection
```

### Querying

Query objects using the schema structure:

```bash
# Natural language query
tg-invoke-structured-query -q "Show all pies from France"

# GraphQL query
tg-invoke-structured-query -q 'query { 
  pies(where: {region: {_eq: "France"}}) { 
    pie_type 
    price 
  } 
}'

# Object query
tg-invoke-objects-query -c pies-collection -t Pie
```

## Schema Validation

Schemas enforce data quality through:

### Required Fields
```json
{
  "name": "email",
  "type": "string",
  "required": true
}
```

### Type Validation
- String fields reject non-text values
- Numeric fields reject non-numeric values
- Boolean fields only accept true/false
- Date fields validate date formats

### Primary Key Constraints
- Primary key fields cannot be null
- Composite primary keys must be unique together
- Primary key values identify unique objects

## Best Practices

### Schema Design

1. **Start Simple**
   - Begin with essential fields
   - Add complexity incrementally
   - Test with sample data

2. **Use Descriptive Names**
   - Clear field names improve query readability
   - Include units in field names (`diameter_cm`, `weight_kg`)
   - Use consistent naming conventions

3. **Plan Primary Keys**
   - Choose stable, unique identifiers
   - Consider composite keys for multi-dimensional data
   - Avoid using auto-generated IDs when natural keys exist

4. **Strategic Indexing**
   - Index frequently queried fields
   - Index fields used in WHERE clauses
   - Balance performance with storage costs

### Field Design

1. **Choose Appropriate Types**
   - Use `integer` for whole numbers
   - Use `float` for measurements and calculations
   - Use `string` for text and categorical data
   - Use `date`/`datetime` for temporal data

2. **Required vs Optional**
   - Mark essential fields as required
   - Allow optional fields for incomplete data
   - Consider default values for optional fields

3. **Consistent UUIDs**
   - Generate UUIDs once and never change them
   - Use a UUID generator tool
   - Document field ID mappings

### Schema Evolution

1. **Backward Compatibility**
   - Add new optional fields
   - Avoid removing existing fields
   - Change field types carefully

2. **Versioning**
   - Version your schemas
   - Document changes between versions
   - Plan migration strategies

3. **Testing**
   - Test schema changes with sample data
   - Validate queries still work
   - Check application integrations

## Common Patterns

### Product Catalog
```json
{
  "name": "Products",
  "fields": [
    {"name": "sku", "type": "string", "primary_key": true},
    {"name": "name", "type": "string", "required": true},
    {"name": "category", "type": "string", "required": true},
    {"name": "price", "type": "float", "required": true},
    {"name": "in_stock", "type": "boolean", "required": true}
  ],
  "indexes": ["category", "price"]
}
```

### Customer Records
```json
{
  "name": "Customers",
  "fields": [
    {"name": "customer_id", "type": "string", "primary_key": true},
    {"name": "email", "type": "string", "required": true},
    {"name": "name", "type": "string", "required": true},
    {"name": "country", "type": "string", "required": false},
    {"name": "signup_date", "type": "date", "required": true}
  ],
  "indexes": ["email", "country", "signup_date"]
}
```

### Financial Data
```json
{
  "name": "Transactions",
  "fields": [
    {"name": "transaction_id", "type": "string", "primary_key": true},
    {"name": "amount", "type": "float", "required": true},
    {"name": "currency", "type": "string", "required": true},
    {"name": "date", "type": "datetime", "required": true},
    {"name": "category", "type": "string", "required": true}
  ],
  "indexes": ["date", "category", "currency"]
}
```

## See Also

- [tg-put-config-item](../cli/tg-put-config-item) - Create and update schemas
- [tg-get-config-item](../cli/tg-get-config-item) - Retrieve schema definitions
- [tg-list-config-items](../cli/tg-list-config-items) - List all schemas
- [tg-load-structured-data](../cli/tg-load-structured-data) - Import data using schemas
- [Structured Data Processing](../../guides/structured-processing/) - Complete tutorial
- [Structure Descriptor Language (SDL)](../sdl) - Advanced data transformation
