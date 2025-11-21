---
title: Object Extraction Process
parent: Guides
nav_order: 8
permalink: /guides/object-extraction
review_date: 2025-11-21
---

# Object Extraction Process

The object extraction process focuses specifically on extracting well-structured data objects from unstructured text. Unlike general knowledge graph extraction, object extraction creates discrete, schema-conformant entities that can be stored, indexed, and queried as structured data.

## Overview

Object extraction transforms unstructured text into structured objects by:
1. Identifying discrete entities within text
2. Extracting their properties and attributes
3. Validating against predefined schemas
4. Storing objects in the object storage system
5. Making objects queryable via structured query APIs

## Object vs. Knowledge Graph Extraction

| Aspect | Object Extraction | Knowledge Graph Extraction |
|--------|------------------|---------------------------|
| **Output** | Structured objects | RDF triples |
| **Format** | JSON/Schema-based | Subject-Predicate-Object |
| **Storage** | Object storage | Graph database |
| **Query** | GraphQL/SQL-like | SPARQL |
| **Use Case** | Structured data analysis | Relationship discovery |

## Basic Object Extraction

### Simple Object Extraction

```python
from trustgraph.api import Api

api = Api("http://localhost:8088/").flow().id("default")

# Define target schema
product_schema = {
    "name": "Product",
    "fields": {
        "id": {"type": "string", "required": True},
        "name": {"type": "string", "required": True},
        "price": {"type": "number", "required": True},
        "category": {"type": "string"},
        "description": {"type": "text"},
        "features": {"type": "array", "items": {"type": "string"}},
        "manufacturer": {"type": "string"},
        "model": {"type": "string"}
    }
}

# Text containing product information
catalog_text = """
The new MacBook Pro 16" features an M3 Pro chip and starts at $2,499. 
It includes 18GB unified memory and a Liquid Retina XDR display. 
Available in Space Gray and Silver.

The iPhone 15 Pro Max comes with a titanium design and A17 Pro chip. 
Pricing starts at $1,199 for the 256GB model. Features include 
Action Button, USB-C connectivity, and Pro camera system.
"""

# Extract objects
response = api.extract_objects(
    text=catalog_text,
    schema=product_schema,
    extraction_type="products"
)

print(f"Extracted {len(response['objects'])} product objects")
```

### Extracted Object Example

```json
{
  "objects": [
    {
      "id": "macbook-pro-16-m3",
      "name": "MacBook Pro 16\"",
      "price": 2499.00,
      "category": "Laptop",
      "description": "Features M3 Pro chip with 18GB unified memory",
      "features": ["M3 Pro chip", "18GB unified memory", "Liquid Retina XDR display"],
      "manufacturer": "Apple",
      "model": "MacBook Pro 16\" M3"
    },
    {
      "id": "iphone-15-pro-max",
      "name": "iPhone 15 Pro Max",
      "price": 1199.00,
      "category": "Smartphone",
      "description": "Titanium design with A17 Pro chip",
      "features": ["Titanium design", "A17 Pro chip", "Action Button", "USB-C", "Pro camera system"],
      "manufacturer": "Apple",
      "model": "iPhone 15 Pro Max"
    }
  ],
  "extraction_id": "ext_12345",
  "schema_name": "Product"
}
```

## Schema-Based Extraction

### Defining Extraction Schemas

```python
# Customer schema
customer_schema = {
    "name": "Customer",
    "fields": {
        "id": {"type": "string", "required": True},
        "name": {"type": "string", "required": True},
        "email": {"type": "email"},
        "phone": {"type": "string"},
        "address": {"type": "object", "properties": {
            "street": {"type": "string"},
            "city": {"type": "string"},
            "state": {"type": "string"},
            "zip": {"type": "string"}
        }},
        "company": {"type": "string"},
        "industry": {"type": "string"},
        "status": {"type": "enum", "values": ["active", "inactive", "prospect"]}
    },
    "validation_rules": {
        "email_format": "valid_email",
        "phone_format": "us_phone"
    }
}

# Financial data schema
financial_schema = {
    "name": "FinancialReport",
    "fields": {
        "id": {"type": "string", "required": True},
        "company": {"type": "string", "required": True},
        "period": {"type": "string", "required": True},
        "revenue": {"type": "number"},
        "profit": {"type": "number"},
        "expenses": {"type": "number"},
        "growth_rate": {"type": "number"},
        "metrics": {"type": "object", "properties": {
            "ebitda": {"type": "number"},
            "margin": {"type": "number"},
            "eps": {"type": "number"}
        }},
        "currency": {"type": "string", "default": "USD"}
    }
}
```

### Multi-Schema Extraction

Extract multiple object types from the same text:

```python
# Define multiple schemas
schemas = [customer_schema, financial_schema, product_schema]

# Business document with mixed content
business_text = """
Q4 2024 Report for TechCorp Inc.

Company Overview:
TechCorp Inc., headquartered at 123 Tech Drive, San Francisco, CA 94105, 
reported strong Q4 2024 results. CEO Sarah Johnson (sarah@techcorp.com) 
announced record revenue.

Financial Performance:
- Revenue: $125.5 million (up 23% YoY)
- Net Profit: $31.2 million
- EBITDA: $45.8 million
- Gross Margin: 68%

Product Line:
Our flagship CloudSync Pro platform generated $85M in revenue.
The new DataViz Analytics tool launched in Q4 contributed $12M.
"""

# Extract all object types
response = api.extract_objects(
    text=business_text,
    schemas=schemas,
    extraction_type="comprehensive"
)

# Results organized by schema
for schema_name, objects in response["objects_by_schema"].items():
    print(f"{schema_name}: {len(objects)} objects")
```

## Advanced Object Extraction

### Contextual Extraction

Use context from previous extractions:

```python
# First pass: extract companies
companies_response = api.extract_objects(
    text=business_text,
    schema=company_schema,
    extraction_type="companies"
)

# Second pass: extract financial data with company context
financial_response = api.extract_objects(
    text=business_text,
    schema=financial_schema,
    extraction_type="financial",
    context={
        "companies": companies_response["objects"],
        "focus": "financial_metrics"
    }
)

# Context helps link financial data to specific companies
```

### Relationship Extraction

Extract objects and their relationships:

```python
# Schema with relationships
order_schema = {
    "name": "Order",
    "fields": {
        "id": {"type": "string", "required": True},
        "customer_id": {"type": "string", "required": True},
        "product_ids": {"type": "array", "items": {"type": "string"}},
        "order_date": {"type": "date"},
        "total": {"type": "number"},
        "status": {"type": "enum", "values": ["pending", "shipped", "delivered", "cancelled"]}
    },
    "relationships": {
        "customer": {"type": "Customer", "field": "customer_id"},
        "products": {"type": "Product", "field": "product_ids"}
    }
}

# Extract with relationship resolution
response = api.extract_objects(
    text=order_text,
    schema=order_schema,
    resolve_relationships=True
)

# Objects include resolved relationship data
```

### Hierarchical Object Extraction

Extract nested and hierarchical structures:

```python
# Organization schema with hierarchy
org_schema = {
    "name": "Organization",
    "fields": {
        "id": {"type": "string", "required": True},
        "name": {"type": "string", "required": True},
        "type": {"type": "enum", "values": ["company", "division", "department", "team"]},
        "parent_id": {"type": "string"},
        "employees": {"type": "array", "items": {"type": "object", "properties": {
            "name": {"type": "string"},
            "title": {"type": "string"},
            "email": {"type": "email"}
        }}},
        "location": {"type": "object"},
        "budget": {"type": "number"}
    }
}

# Extract hierarchical organization data
org_text = """
TechCorp Inc. is organized into three main divisions:

Engineering Division (San Francisco):
- Led by VP Sarah Chen (sarah.chen@techcorp.com)
- Software Development Team: 45 engineers
- QA Team: 12 testers
- Budget: $8.5M

Sales Division (New York):
- Led by VP Mike Rodriguez (mike.r@techcorp.com)  
- Enterprise Sales: 20 reps
- SMB Sales: 15 reps
- Budget: $12.2M

Marketing Division (Austin):
- Led by Director Lisa Park (lisa.park@techcorp.com)
- Digital Marketing: 8 specialists
- Content Team: 5 writers
- Budget: $4.8M
"""

response = api.extract_objects(
    text=org_text,
    schema=org_schema,
    extraction_type="hierarchical"
)
```

## Validation and Quality Control

### Schema Validation

```python
# Extract with strict validation
response = api.extract_objects(
    text=catalog_text,
    schema=product_schema,
    validation_mode="strict",  # Options: strict, lenient, custom
    quality_threshold=0.8
)

# Check validation results
for obj in response["objects"]:
    if obj.get("validation_errors"):
        print(f"Object {obj['id']} has validation errors:")
        for error in obj["validation_errors"]:
            print(f"  - {error}")
```

### Custom Validation Rules

```python
# Define custom validation
custom_rules = {
    "price_validation": {
        "field": "price",
        "rule": "greater_than_zero",
        "error_message": "Price must be positive"
    },
    "email_validation": {
        "field": "email",
        "rule": "valid_email_format",
        "error_message": "Invalid email format"
    },
    "date_validation": {
        "field": "date",
        "rule": "valid_date_range",
        "params": {"min_date": "2020-01-01", "max_date": "2030-12-31"}
    }
}

response = api.extract_objects(
    text=input_text,
    schema=schema,
    validation_rules=custom_rules
)
```

## Batch Object Extraction

### Processing Multiple Documents

```python
documents = [
    {"id": "doc1", "path": "catalog1.pdf", "type": "product_catalog"},
    {"id": "doc2", "path": "catalog2.pdf", "type": "product_catalog"},
    {"id": "doc3", "path": "financials.pdf", "type": "financial_report"}
]

all_objects = {}

for doc in documents:
    with open(doc["path"], 'r') as f:
        text = f.read()
    
    # Choose schema based on document type
    schema = product_schema if doc["type"] == "product_catalog" else financial_schema
    
    response = api.extract_objects(
        text=text,
        schema=schema,
        metadata={
            "source_document": doc["id"],
            "document_type": doc["type"]
        }
    )
    
    all_objects[doc["id"]] = response["objects"]

# Combine and deduplicate objects
combined_objects = []
for doc_objects in all_objects.values():
    combined_objects.extend(doc_objects)
```

### Incremental Extraction

Process large documents incrementally:

```python
def extract_objects_incrementally(large_text, schema, chunk_size=5000):
    chunks = [large_text[i:i+chunk_size] for i in range(0, len(large_text), chunk_size)]
    all_objects = []
    context = {}
    
    for i, chunk in enumerate(chunks):
        response = api.extract_objects(
            text=chunk,
            schema=schema,
            context=context,
            chunk_info={
                "chunk_number": i,
                "total_chunks": len(chunks)
            }
        )
        
        all_objects.extend(response["objects"])
        
        # Update context with extracted objects for next chunk
        context["previous_objects"] = response["objects"]
    
    return all_objects
```

## Storage and Retrieval

### Automatic Storage

Extracted objects are automatically stored:

```python
response = api.extract_objects(
    text=catalog_text,
    schema=product_schema,
    auto_store=True  # Objects stored automatically
)

extraction_id = response["extraction_id"]

# Objects are immediately queryable
products = api.structured_query(
    question="Show all products extracted today"
)
```

### Manual Storage Control

```python
# Extract without storing
response = api.extract_objects(
    text=catalog_text,
    schema=product_schema,
    auto_store=False
)

# Review and filter objects
valid_objects = [
    obj for obj in response["objects"]
    if obj.get("confidence", 0) > 0.8
]

# Store only valid objects
if valid_objects:
    api.store_objects(
        objects=valid_objects,
        schema_name=product_schema["name"],
        metadata={
            "extraction_id": response["extraction_id"],
            "validation_passed": True
        }
    )
```

## Querying Extracted Objects

### Basic Queries

```python
# Query by schema type
products = api.query_objects(
    schema_name="Product",
    limit=10
)

# Query with filters
expensive_products = api.query_objects(
    schema_name="Product",
    filters={"price": {"$gt": 1000}},
    sort={"price": "desc"}
)
```

### Advanced Queries

```python
# Natural language queries
results = api.structured_query(
    question="Show products extracted from catalogs this week"
)

# GraphQL queries
graphql_query = """
query {
  products(
    where: {
      _metadata: {extraction_date: {_gte: "2024-01-01"}},
      category: {_eq: "Electronics"}
    }
  ) {
    id
    name
    price
    features
    _metadata {
      extraction_id
      confidence
    }
  }
}
"""

results = api.structured_query(question=graphql_query)
```

## Monitoring and Analytics

### Extraction Metrics

```python
# Get extraction statistics
stats = api.get_extraction_stats(
    schema_name="Product",
    date_range={"start": "2024-01-01", "end": "2024-01-31"}
)

print(f"Objects extracted: {stats['total_objects']}")
print(f"Average confidence: {stats['avg_confidence']}")
print(f"Validation pass rate: {stats['validation_pass_rate']}")
```

### Quality Monitoring

```python
# Monitor extraction quality
quality_report = api.get_quality_report(
    extraction_id=response["extraction_id"]
)

print("Quality Metrics:")
print(f"- Completeness: {quality_report['completeness']}")
print(f"- Accuracy: {quality_report['accuracy']}")  
print(f"- Consistency: {quality_report['consistency']}")
```

## Best Practices

### 1. Schema Design

```python
# Good: Clear, specific schemas
good_schema = {
    "name": "Product",
    "description": "E-commerce product information",
    "fields": {
        "sku": {"type": "string", "required": True, "pattern": "^[A-Z]{3}-\\d{6}$"},
        "name": {"type": "string", "required": True, "min_length": 1},
        "price": {"type": "number", "required": True, "minimum": 0},
        "category": {"type": "enum", "values": ["Electronics", "Clothing", "Books"]}
    }
}

# Avoid: Vague, overly flexible schemas
avoid_schema = {
    "name": "Thing",
    "fields": {
        "data": {"type": "object"},  # Too generic
        "value": {"type": "string"}   # Unclear purpose
    }
}
```

### 2. Validation Strategy

```python
# Implement progressive validation
validation_levels = {
    "basic": {"required_fields": True, "type_checking": True},
    "standard": {"format_validation": True, "range_checking": True},
    "strict": {"custom_rules": True, "cross_reference": True}
}

# Start with basic validation, escalate as needed
```

### 3. Error Handling

```python
try:
    response = api.extract_objects(text=text, schema=schema)
except ExtractionError as e:
    if e.error_type == "schema_validation":
        # Retry with more lenient validation
        response = api.extract_objects(
            text=text, 
            schema=schema, 
            validation_mode="lenient"
        )
    else:
        # Log error for investigation
        logger.error(f"Extraction failed: {e}")
        raise
```

## See Also

- [Agent Extraction Process](agent-extraction) - Comprehensive extraction workflows
- [Object Storage API](../reference/apis/api-object-storage) - Storage and retrieval
- [Structured Query Integration](structured-query-integration) - Query extracted objects
- [Schema Management](../reference/extending/schemas) - Define and manage schemas