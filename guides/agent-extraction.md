---
title: Agent Extraction Process
parent: Guides
nav_order: 7
permalink: /guides/agent-extraction
review_date: 2026-06-01
---

# Agent Extraction Process

The agent extraction process uses AI agents to automatically extract structured data, knowledge graphs, and objects from unstructured text. This guide explains how the extraction workflow operates and how to configure it for different use cases.

## Overview

Agent extraction is a multi-stage process that:
1. Analyzes unstructured text using LLM-based agents
2. Identifies entities, relationships, and structured data
3. Extracts information according to defined schemas
4. Stores results in the knowledge graph and object storage
5. Makes data queryable through GraphQL and other APIs

## Extraction Workflow

### 1. Document Ingestion

```python
from trustgraph.api import Api

api = Api("http://localhost:8088/").flow().id("default")

# Load document for extraction
document_text = """
Apple Inc. announced its Q4 2024 earnings today. The company reported 
revenue of $89.5 billion, led by strong iPhone 15 sales. CEO Tim Cook 
stated that the new AI features have driven customer upgrades.
"""
```

### 2. Agent Configuration

Agents can be configured with specific extraction instructions:

```python
# Configure extraction agent
extraction_prompt = """
Extract the following information:
1. Company entities (name, executives, products)
2. Financial data (revenue, earnings, metrics)
3. Product information (name, features)
4. Relationships between entities
5. Temporal information (dates, quarters)

Structure the output as:
- Knowledge graph triples
- Structured objects matching defined schemas
"""
```

### 3. Invoke Agent Extraction

```python
# Execute extraction
response = api.invoke_agent(
    prompt=extraction_prompt,
    text=document_text,
    extraction_mode="comprehensive"  # Options: simple, comprehensive, schema-based
)

# Response contains extracted data
print(f"Extracted {len(response['triples'])} knowledge graph triples")
print(f"Extracted {len(response['objects'])} structured objects")
print(f"Extraction ID: {response['extraction_id']}")
```

## Extraction Modes

### Simple Extraction

Basic entity and relationship extraction:

```python
response = api.invoke_agent(
    prompt="Extract key entities and relationships",
    text=document_text,
    extraction_mode="simple"
)

# Results include:
# - Named entities (people, organizations, locations)
# - Basic relationships
# - Key facts
```

### Comprehensive Extraction

Detailed multi-level extraction:

```python
response = api.invoke_agent(
    prompt="Perform comprehensive knowledge extraction",
    text=document_text,
    extraction_mode="comprehensive"
)

# Results include:
# - All entities with properties
# - Complex relationships
# - Temporal information
# - Contextual metadata
# - Inferred relationships
```

### Schema-Based Extraction

Extract data matching specific schemas:

```python
# Define target schema
schema = {
    "Company": {
        "fields": ["name", "ceo", "revenue", "products"],
        "required": ["name"]
    },
    "Product": {
        "fields": ["name", "features", "company"],
        "required": ["name", "company"]
    }
}

response = api.invoke_agent(
    prompt="Extract data according to provided schemas",
    text=document_text,
    extraction_mode="schema-based",
    schemas=schema
)

# Results match the defined schemas exactly
```

## Knowledge Graph Extraction

The agent creates knowledge graph triples in RDF format:

```python
# Example extracted triples
triples = [
    ("Apple_Inc", "rdf:type", "Organization"),
    ("Apple_Inc", "has_ceo", "Tim_Cook"),
    ("Apple_Inc", "reported_revenue", "89.5_billion"),
    ("iPhone_15", "rdf:type", "Product"),
    ("iPhone_15", "manufactured_by", "Apple_Inc"),
    ("iPhone_15", "has_feature", "AI_capabilities"),
    ("Q4_2024", "rdf:type", "TimePeriod"),
    ("89.5_billion", "reported_in", "Q4_2024")
]

# Triples are automatically stored in the knowledge graph
# Query them using SPARQL or GraphQL
```

## Object Extraction

Structured objects are extracted and stored:

```python
# Example extracted objects
objects = [
    {
        "schema": "Company",
        "data": {
            "id": "apple-inc",
            "name": "Apple Inc.",
            "ceo": "Tim Cook",
            "revenue": 89500000000,
            "revenue_period": "Q4 2024",
            "products": ["iPhone 15"]
        }
    },
    {
        "schema": "Product",
        "data": {
            "id": "iphone-15",
            "name": "iPhone 15",
            "company": "apple-inc",
            "features": ["AI capabilities"],
            "category": "Smartphone"
        }
    }
]

# Objects are stored and queryable via Structured Query API
```

## Extraction Pipelines

### Sequential Extraction

Process documents through multiple extraction stages:

```python
# Stage 1: Entity extraction
entities = api.invoke_agent(
    prompt="Extract all named entities",
    text=document_text,
    extraction_mode="simple"
)

# Stage 2: Relationship extraction
relationships = api.invoke_agent(
    prompt=f"Extract relationships between these entities: {entities['entities']}",
    text=document_text,
    extraction_mode="comprehensive"
)

# Stage 3: Property extraction
properties = api.invoke_agent(
    prompt="Extract properties and attributes for each entity",
    text=document_text,
    context=entities
)
```

### Batch Extraction

Process multiple documents:

```python
documents = ["doc1.txt", "doc2.txt", "doc3.txt"]
all_extractions = []

for doc_path in documents:
    with open(doc_path, 'r') as f:
        text = f.read()
    
    response = api.invoke_agent(
        prompt="Extract structured data",
        text=text,
        extraction_mode="comprehensive",
        metadata={"source": doc_path}
    )
    
    all_extractions.append(response)

# Aggregate results
total_triples = sum(len(e['triples']) for e in all_extractions)
total_objects = sum(len(e['objects']) for e in all_extractions)
```

## Querying Extracted Data

### Query Knowledge Graph

```python
# SPARQL query for extracted triples
sparql_query = """
SELECT ?company ?revenue ?period
WHERE {
    ?company rdf:type Organization .
    ?company reported_revenue ?revenue .
    ?revenue reported_in ?period .
}
"""

results = api.query_triples(sparql_query)
```

### Query Structured Objects

```python
# GraphQL query for extracted objects
response = api.structured_query(
    question="Show all companies with revenue over 50 billion"
)

companies = response["data"]["companies"]
```

### Combined Queries

```python
# Natural language query across all extracted data
response = api.structured_query(
    question="What products were mentioned with AI features?"
)
```

## Advanced Configuration

### Custom Extraction Rules

```python
extraction_config = {
    "rules": {
        "financial_data": {
            "patterns": ["revenue", "earnings", "profit", "sales"],
            "extract_as": "FinancialMetric",
            "include_context": True
        },
        "temporal": {
            "patterns": ["Q[1-4] \\d{4}", "\\d{4}"],
            "extract_as": "TimePeriod"
        }
    },
    "confidence_threshold": 0.8,
    "include_metadata": True
}

response = api.invoke_agent(
    prompt="Extract financial information",
    text=document_text,
    config=extraction_config
)
```

### Extraction Validation

```python
# Validate extracted data against schemas
validation_result = api.validate_extraction(
    extraction_id=response["extraction_id"],
    schemas=schema
)

if validation_result["valid"]:
    print("Extraction passed validation")
else:
    print(f"Validation errors: {validation_result['errors']}")
```

## Best Practices

### 1. Clear Extraction Prompts

Provide specific instructions:
```python
# Good: Specific and structured
prompt = """
Extract:
1. Company names and their executives
2. Financial metrics with time periods
3. Product names and features
Format as knowledge graph triples.
"""

# Avoid: Vague instructions
prompt = "Extract important information"
```

### 2. Schema Definition

Define schemas before extraction:
```python
# Define clear schemas
schemas = {
    "Person": ["name", "title", "company"],
    "Company": ["name", "industry", "revenue"],
    "Product": ["name", "category", "features"]
}
```

### 3. Incremental Processing

Process large documents in chunks:
```python
chunks = split_document(large_document, chunk_size=1000)
for chunk in chunks:
    response = api.invoke_agent(
        prompt="Extract entities",
        text=chunk,
        context=previous_extractions
    )
```

### 4. Validation and Quality Control

Always validate critical extractions:
```python
# Set quality thresholds
if response["confidence"] < 0.7:
    # Request human review
    flag_for_review(response["extraction_id"])
```

## Monitoring Extraction

### Check Extraction Status

```python
# Get extraction details
status = api.get_extraction_status(extraction_id)
print(f"Status: {status['state']}")
print(f"Progress: {status['progress']}%")
print(f"Triples extracted: {status['triple_count']}")
print(f"Objects extracted: {status['object_count']}")
```

### View Extraction Logs

```python
# Get detailed logs
logs = api.get_extraction_logs(extraction_id)
for log in logs:
    print(f"{log['timestamp']}: {log['message']}")
```

## Error Handling

```python
try:
    response = api.invoke_agent(
        prompt="Extract data",
        text=document_text
    )
except ExtractionError as e:
    print(f"Extraction failed: {e.message}")
    # Retry with different parameters
    response = api.invoke_agent(
        prompt="Extract basic entities only",
        text=document_text,
        extraction_mode="simple"
    )
```

## See Also

- [Object Extraction Process](object-extraction) - Detailed object extraction
- [Agent API](../reference/apis/api-agent) - Agent API reference
- [Structured Query Integration](structured-query-integration) - Query extracted data
- [Object Storage API](../reference/apis/api-object-storage) - Store extracted objects
