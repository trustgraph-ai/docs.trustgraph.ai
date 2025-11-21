---
title: Ontology RAG
nav_order: 11
parent: How-to Guides
grand_parent: TrustGraph Documentation
review_date: 2025-11-21
---

# Ontology RAG Guide

**Query structured data using schema-based extraction and typed entities**

Ontology RAG (also called "Structured RAG" or "Schema-based RAG") uses predefined schemas to extract and query typed, structured data from unstructured documents. Unlike basic RAG which retrieves text chunks, Ontology RAG extracts structured objects that conform to your defined schema.

## What is Ontology RAG?

Ontology RAG works by:
1. **Defining schemas** for entity types (products, people, events, etc.)
2. **Extracting objects** that match schema definitions
3. **Storing typed entities** with validated structure
4. **Querying structured data** using natural language or GraphQL
5. **Returning typed results** in structured formats

### How Ontology RAG Works

```
Schema Definition → Document Processing → Entity Extraction → Validation → Storage → Structured Query
```

1. **Define schema**: Specify entity types, fields, and relationships
2. **Process documents**: Extract entities matching schema
3. **Validate data**: Ensure extracted data conforms to schema
4. **Store objects**: Save typed entities in object store
5. **Query**: Use natural language queries or GraphQL
6. **Return**: Get structured JSON/CSV results

### Ontology RAG vs. Other Approaches

| Aspect | Document RAG | Graph RAG | Ontology RAG |
|--------|--------------|-----------|--------------|
| **Output** | Text chunks | Relationships | Structured objects |
| **Schema** | None | Implicit | **Explicit types** |
| **Validation** | None | Minimal | **Type-checked** |
| **Query** | Semantic | Relationships | **Structured** |
| **Format** | Text | Triples | **JSON/CSV** |
| **Best for** | Reading | Connections | **Data extraction** |

## When to Use Ontology RAG

✅ **Use Ontology RAG when**:
- You need structured, typed data extraction
- Output should be in database/spreadsheet format
- You want type validation and consistency
- Need to extract specific entity types (products, people, financial data)
- Building data pipelines or integration workflows
- Require queryable structured data

⚠️ **Consider alternatives when**:
- Just need semantic search → Use [Document RAG](document-rag)
- Need relationship understanding → Use [Graph RAG](graph-rag)
- Documents don't have structured data to extract

## Prerequisites

Before starting:
- ✅ TrustGraph deployed ([Quick Start](../getting-started/quickstart))
- ✅ Understanding of [structured processing](structured-processing/)
- ✅ SDL (Schema Definition Language) basics
- ✅ Documents with extractable structured data

## Step-by-Step Guide

### Step 1: Define Your Schema

Create a schema using SDL (Schema Definition Language):

**Example: Product schema**
```sdl
type Product {
  name: String!
  price: Float
  category: String
  manufacturer: String
  description: String
}
```

**Example: Person schema**
```sdl
type Person {
  name: String!
  title: String
  organization: String
  email: String
  location: String
}
```

**Example: Financial data schema**
```sdl
type FinancialRecord {
  company: String!
  revenue: Float
  profit: Float
  quarter: String
  year: Int
}
```

**Schema guidelines**:
- Use `!` for required fields
- Choose appropriate types: String, Float, Int, Boolean
- Keep schemas focused (one entity type per schema)
- Use clear, descriptive field names

See [Schema Guide](structured-processing/schemas) for complete syntax.

### Step 2: Configure Extraction Flow

Set up a flow with your schema:

**Using CLI**:
```bash
# Set the schema
tg-set-schema product-schema products.sdl

# Configure flow to use schema
tg-put-flow-class product-extraction \
  --schema product-schema \
  --collection products
```

**Schema location**: Store schemas in a dedicated directory:
```
schemas/
  ├── products.sdl
  ├── people.sdl
  └── financials.sdl
```

### Step 3: Load and Process Documents

**Load documents for extraction**:
```bash
# Load a single document
tg-load-doc --schema product-schema --collection products catalog.pdf

# Load multiple documents
for file in catalogs/*.pdf; do
  tg-load-doc --schema product-schema --collection products "$file"
done
```

**Monitor processing**:
```bash
# Check processing status
tg-show-processor-state

# View extracted objects
tg-invoke-objects-query --collection products "Show all products"
```

### Step 4: Query Structured Data

#### Natural Language Queries

**Using NLP Query** (converts natural language to GraphQL):
```bash
# Simple query
tg-invoke-nlp-query --collection products "Show all products"

# Filtered query
tg-invoke-nlp-query --collection products "Products over $100"

# Aggregation
tg-invoke-nlp-query --collection products "Average price by category"

# Sorting
tg-invoke-nlp-query --collection products "Top 10 most expensive products"
```

#### Direct GraphQL Queries

**Using Objects Query**:
```bash
# Get all products
tg-invoke-objects-query --collection products "{ products { name price } }"

# Filter by criteria
tg-invoke-objects-query --collection products \
  "{ products(where: { price: { gt: 100 } }) { name price } }"

# Complex query
tg-invoke-objects-query --collection products \
  "{ products(where: { category: \"Electronics\" }, orderBy: price_DESC, limit: 10) { name price manufacturer } }"
```

#### API Method

**Endpoint**: `/api/nlp-query` or `/api/objects-query`

**NLP Query Request**:
```json
{
  "query": "Show all products over $100",
  "collection": "products",
  "format": "json"
}
```

**GraphQL Request**:
```json
{
  "query": "{ products(where: { price: { gt: 100 } }) { name price } }",
  "collection": "products"
}
```

**Response**:
```json
{
  "data": {
    "products": [
      {
        "name": "Product A",
        "price": 150.00
      },
      {
        "name": "Product B",
        "price": 200.00
      }
    ]
  }
}
```

### Step 5: Export Structured Data

**Export to JSON**:
```bash
tg-invoke-objects-query --collection products \
  --format json "{ products { name price } }" > products.json
```

**Export to CSV**:
```bash
tg-invoke-objects-query --collection products \
  --format csv "{ products { name price } }"
```

**Export for analysis**:
```bash
# Get all data
tg-invoke-objects-query --collection products \
  "{ products { name price category manufacturer } }" | jq '.' > all_products.json

# Load into pandas, Excel, or database
```

## Common Patterns

### Product Catalog Extraction

**Schema**:
```sdl
type Product {
  name: String!
  sku: String
  price: Float
  category: String
  inStock: Boolean
}
```

**Queries**:
```bash
# All products
tg-invoke-nlp-query "Show all products"

# Out of stock
tg-invoke-nlp-query "Products that are out of stock"

# Price range
tg-invoke-nlp-query "Products between $50 and $200"
```

### Financial Data Extraction

**Schema**:
```sdl
type FinancialRecord {
  company: String!
  revenue: Float
  profit: Float
  quarter: String
  year: Int
}
```

**Queries**:
```bash
# Q4 results
tg-invoke-nlp-query "Q4 2024 financial results"

# Profitable companies
tg-invoke-nlp-query "Companies with profit over 1 million"

# Revenue comparison
tg-invoke-nlp-query "Compare revenue across companies"
```

### People/Contact Extraction

**Schema**:
```sdl
type Person {
  name: String!
  title: String
  organization: String
  email: String
  phone: String
}
```

**Queries**:
```bash
# All contacts
tg-invoke-nlp-query "Show all people"

# By organization
tg-invoke-nlp-query "People at Acme Corp"

# By title
tg-invoke-nlp-query "All CEOs"
```

### Event/Meeting Extraction

**Schema**:
```sdl
type Meeting {
  title: String!
  date: String
  attendees: [String]
  location: String
  agenda: String
}
```

**Queries**:
```bash
# Upcoming meetings
tg-invoke-nlp-query "Meetings in December"

# By attendee
tg-invoke-nlp-query "Meetings with John Smith"
```

## Advanced Usage

### Complex Schemas

**Nested objects**:
```sdl
type Company {
  name: String!
  headquarters: Address
  revenue: Float
}

type Address {
  street: String
  city: String
  country: String
}
```

**Arrays**:
```sdl
type Product {
  name: String!
  categories: [String]
  tags: [String]
  prices: [PricePoint]
}

type PricePoint {
  amount: Float!
  currency: String!
  date: String
}
```

### Combining with Other RAG Types

**Use Ontology RAG + Graph RAG**:
```bash
# Extract structured data
tg-invoke-nlp-query "All products"

# Understand relationships
tg-invoke-graph-rag "How are products related to manufacturers?"
```

**Use Ontology RAG + Document RAG**:
```bash
# Get structured data
tg-invoke-nlp-query "Q4 revenue by company"

# Get context/explanation
tg-invoke-document-rag "Why did Q4 revenue increase?"
```

### Validation and Quality Control

**Check extraction quality**:
```bash
# Count extracted objects
tg-invoke-objects-query "{ products { count } }"

# Sample extracted data
tg-invoke-objects-query "{ products(limit: 10) { name price } }"

# Check for missing fields
tg-invoke-nlp-query "Products without prices"
```

**Improve extraction**:
- Refine schema definitions
- Improve extraction prompts
- Add validation rules
- Use better source documents

## Troubleshooting

### No Objects Extracted

**Problem**: Schema defined but no objects extracted

**Solutions**:
- Verify schema is loaded: `tg-show-schemas`
- Check processing status: `tg-show-processor-state`
- Review extraction prompt configuration
- Ensure documents contain relevant data
- Check logs for extraction errors

### Incorrect Field Values

**Problem**: Extracted data has wrong types or values

**Solutions**:
- Refine schema field types
- Add field descriptions to guide extraction
- Improve source document quality
- Adjust extraction prompt
- Add validation rules

### Query Returns No Results

**Problem**: NLP queries return empty results

**Solutions**:
- Verify objects exist: `tg-invoke-objects-query "{ products { count } }"`
- Check collection name is correct
- Try direct GraphQL query first
- Simplify natural language query
- Check field names match schema

### Poor NLP Query Translation

**Problem**: Natural language doesn't convert to correct GraphQL

**Solutions**:
- Use more explicit field names in query
- Try direct GraphQL query instead
- Add more context to natural language
- Use simpler query structure
- Check NLP query examples

## Schema Best Practices

### Schema Design

**Keep schemas focused**:
- ✅ One entity type per schema
- ✅ Clear, descriptive field names
- ✅ Appropriate data types
- ✅ Required fields marked with `!`

**Avoid**:
- ❌ Overly complex nested structures
- ❌ Ambiguous field names
- ❌ Too many optional fields
- ❌ Mixing multiple entity types

### Field Naming

**Good names**:
- ✅ `firstName` and `lastName` (specific)
- ✅ `priceUSD` (includes unit)
- ✅ `publishedDate` (clear type)
- ✅ `isActive` (boolean convention)

**Poor names**:
- ❌ `data` (too generic)
- ❌ `value` (ambiguous)
- ❌ `field1` (meaningless)
- ❌ `info` (vague)

### Type Selection

| Data | SDL Type | Example |
|------|----------|---------|
| Text | `String` | "Product Name" |
| Number (int) | `Int` | 42 |
| Number (decimal) | `Float` | 19.99 |
| True/False | `Boolean` | true |
| List | `[String]` | ["tag1", "tag2"] |
| Date | `String` | "2024-12-01" |

## Comparing Approaches

### When to Use Each

| Need | Use This |
|------|----------|
| Semantic search | Document RAG |
| Relationship queries | Graph RAG |
| **Structured extraction** | **Ontology RAG** |
| "Tell me about X" | Document RAG |
| "How is X related to Y" | Graph RAG |
| **"Extract all X entities"** | **Ontology RAG** |
| Text summaries | Document RAG |
| Connected information | Graph RAG |
| **Database-like queries** | **Ontology RAG** |

### Combined Workflow

```bash
# 1. Extract structured data (Ontology RAG)
tg-invoke-nlp-query "All products over $100" > products.json

# 2. Understand relationships (Graph RAG)
tg-invoke-graph-rag "How are these products related to manufacturers?"

# 3. Get detailed context (Document RAG)
tg-invoke-document-rag "Detailed specifications for product X"
```

## Next Steps

### Explore Related Guides

- **[Schema Definition](structured-processing/schemas)** - Complete SDL syntax
- **[Document RAG](document-rag)** - Semantic search basics
- **[Graph RAG](graph-rag)** - Relationship-aware retrieval

### Advanced Features

- **[Agent Extraction](agent-extraction)** - AI-powered extraction workflows
- **[Object Extraction](object-extraction)** - Domain-specific extraction patterns
- **[Structured Processing](structured-processing/)** - Complete structured data workflow

### API Integration

- **[NLP Query API](../reference/apis/api-nlp-query)** - Natural language query API
- **[Objects Query API](../reference/apis/api-objects-query)** - GraphQL query API
- **[CLI Reference](../reference/cli/)** - Command-line tools

## Related Resources

- **[SDL Reference](../reference/sdl)** - Schema definition language
- **[Structured Query](../getting-started/concepts#structured-queries)** - Query concepts
- **[Examples](../examples/)** - Code samples
- **[Troubleshooting](../deployment/troubleshooting)** - Common issues
