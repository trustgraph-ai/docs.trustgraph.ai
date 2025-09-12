---
title: Structured data processing
layout: default
parent: How-to Guides
grand_parent: TrustGraph Documentation
---

# Structured Data Processing

Learn how to process documents and extract structured data using TrustGraph's schema-based extraction capabilities.

This feature was introduced in TrustGraph 1.2.

## Overview

TrustGraph provides capabilities for extracting structured information from documents using configurable schemas. This allows you to define custom data structures and have TrustGraph automatically extract matching information from your documents.

**Note**: TrustGraph 1.3 introduces fully integrated query capabilities for structured data. You can now query extracted data using natural language, GraphQL, or direct object queries through the CLI commands.

This guide walks through defining extraction schemas, loading structured data, processing documents, and querying the extracted data using TrustGraph's integrated query tools.

## What You'll Learn

- How to define a custom extraction schema
- How to load structured data directly using `tg-load-structured-data`
- How to load test documents into TrustGraph
- How to start an object extraction flow
- How to process documents through the extraction pipeline
- How to query extracted data using natural language, GraphQL, and object queries

## Prerequisites

Before starting this guide, ensure you have:

- A running TrustGraph instance version 1.3 or later (see [Installation Guide](../../getting-started/installation))
- Python 3.8 or later with the TrustGraph CLI tools installed (`pip install trustgraph-cli`)
- Sample documents or structured data files to process

## Step 1: Define a Schema

The first step is to define a schema that describes the structured data you want to extract from documents. The schema defines the types of objects and their properties that TrustGraph should look for.

You can create a schema using either the web workbench or the command line interface.

### Option A: Using the Web Workbench

1. **Access the TrustGraph Workbench**
   Navigate to [http://localhost:8888/](http://localhost:8888/) in your web browser.

2. **Enable Schema Feature**
   Before you can access schemas, ensure the feature is enabled:
   - Go to **Settings** in the navigation menu
   - Find the **Schemas** option and make sure it is checked/enabled
   - Save settings if needed

3. **Open Schema Configuration**
   Once schemas are enabled, click on the **"Schema"** tab in the navigation menu.

4. **Create a New Schema**
   Click the **"Create New Schema"** button to open the schema creation dialog.

5. **Configure Basic Schema Information**
   - **Schema ID**: Enter a unique identifier (e.g., `cities`)
   - **Name**: Enter a display name (e.g., `Cities`)
   - **Description**: Add a description of what data this schema captures (e.g., `City demographics including population, currency, climate and language for the most populous cities`)

6. **Add Schema Fields**
   Click **"Add Field"** for each field you want to include. For our cities example:
   
   **Field 1 - City Name:**
   - Field Name: `city`
   - Type: `String`
   - ☑ Primary Key
   - ☑ Required
   
   **Field 2 - Country:**
   - Field Name: `country`
   - Type: `String`
   - ☑ Primary Key
   - ☑ Required
   
   **Field 3 - Population:**
   - Field Name: `population`
   - Type: `Integer`
   - ☐ Primary Key
   - ☑ Required
   
   **Field 4 - Climate:**
   - Field Name: `climate`
   - Type: `String`
   - ☐ Primary Key
   - ☑ Required
   
   **Field 5 - Primary Language:**
   - Field Name: `primary_language`
   - Type: `String`
   - ☐ Primary Key
   - ☑ Required
   
   **Field 6 - Currency:**
   - Field Name: `currency`
   - Type: `String`
   - ☐ Primary Key
   - ☑ Required

7. **Configure Indexes**
   In the Indexes section, click **"Add Index"** and add:
   - `primary_language`
   - `currency`
   
   Note: Structured data does not support extra index fields at the moment.

8. **Save the Schema**
   Click **"Create"** to save your schema.

<a href="create-schema.png">
  <img src="create-schema.png" alt="Schema creation dialog in TrustGraph workbench">
</a>

### Option B: Using the Command Line

You can also create a schema using the CLI with the `tg-put-config` command:

```bash
tg-put-config-item --type schema --key cities --value '{
  "name": "Cities",
  "description": "City demographics including population, currency, climate and language for the most populous cities",
  "fields": [
    {
      "id": "278f1d70-5000-42ae-b9d5-dea78d0d01a9",
      "name": "city",
      "type": "string",
      "primary_key": true,
      "required": true
    },
    {
      "name": "country",
      "type": "string",
      "primary_key": true,
      "required": true,
      "id": "83b7d911-b086-4614-b44c-74d20d8e8ba8"
    },
    {
      "name": "population",
      "type": "integer",
      "primary_key": false,
      "required": true,
      "id": "00b09134-34ec-46be-a374-4ba2e3cb95e2"
    },
    {
      "name": "climate",
      "type": "string",
      "primary_key": false,
      "required": true,
      "id": "18e434ae-3dbb-4431-a8b5-15a744ad23b2"
    },
    {
      "name": "primary_language",
      "type": "string",
      "primary_key": false,
      "required": true,
      "id": "e4e8ff1f-7605-4a49-aebc-3538d15f52ff"
    },
    {
      "name": "currency",
      "type": "string",
      "primary_key": false,
      "required": true,
      "id": "2d661b00-d3e2-4d6b-b283-8c65220b8d59"
    }
  ],
  "indexes": ["primary_language", "currency"]
}'
```

### Verify Schema Creation

Regardless of which method you used, verify the schema was created:

```bash
# List all schemas
tg-list-config-items --type schema

# View specific schema details
tg-get-config-item --type schema --key cities
```

You should see your `cities` schema with all defined fields and indexes.

## Step 2: Load Data into TrustGraph

You have two options for getting structured data into TrustGraph:
1. **Direct loading** of structured data files (CSV, JSON, XML) using `tg-load-structured-data`
2. **Document extraction** where TrustGraph extracts structured data from unstructured documents

### Option A: Direct Loading of Structured Data (New in 1.3)

> **Note**: The `tg-load-structured-data` command is an emerging utility that may change as structured data capabilities become more integrated into the TrustGraph platform.

If you already have structured data in CSV, JSON, or XML format, you can load it directly:

#### Load CSV Data

Create a CSV file with city data (`cities.csv`):

```csv
city,country,population,climate,primary_language,currency
Tokyo,Japan,37400000,humid subtropical,Japanese,Japanese Yen
Delhi,India,32900000,semi-arid,Hindi,Indian Rupee
Shanghai,China,28500000,humid subtropical,Mandarin Chinese,Chinese Yuan
São Paulo,Brazil,22800000,subtropical highland,Portuguese,Brazilian Real
Dhaka,Bangladesh,22400000,tropical monsoon,Bengali,Bangladeshi Taka
```

Load the CSV file:

```bash
# Load with auto-detected schema
tg-load-structured-data -f cities.csv -s auto -c cities

# Or load with the predefined schema
tg-load-structured-data -f cities.csv -s cities -c cities
```

#### Load JSON Data

Create a JSON file with city data (`cities.json`):

```json
[
  {
    "city": "Tokyo",
    "country": "Japan",
    "population": 37400000,
    "climate": "humid subtropical",
    "primary_language": "Japanese",
    "currency": "Japanese Yen"
  },
  {
    "city": "Delhi",
    "country": "India",
    "population": 32900000,
    "climate": "semi-arid",
    "primary_language": "Hindi",
    "currency": "Indian Rupee"
  }
]
```

Load the JSON file:

```bash
tg-load-structured-data -f cities.json -c cities -t City
```

### Option B: Extract from Documents

If your data is in unstructured documents, you can use TrustGraph's extraction capabilities to process them.

### Prepare Test Documents

For this example, we'll use a sample document containing city demographic data that matches our schema.

1. **Access the Sample Document**
   Open this Google Docs document containing city demographic data:
   [https://docs.google.com/document/d/1_5KfhWL9fN3VuhANIVKuJX6MVBH3vFVW3RiUNYE9jHQ/edit](https://docs.google.com/document/d/1_5KfhWL9fN3VuhANIVKuJX6MVBH3vFVW3RiUNYE9jHQ)

2. **Save as PDF**
   - In Google Docs, click **File** → **Download** → **PDF Document (.pdf)**
   - Save the file as `cities_data.pdf` to your local machine

3. **Alternative: Create Your Own Test Document**
   If you prefer, you can create your own test document with city information. Make sure it includes:
   - City names and their countries
   - Population figures
   - Climate descriptions
   - Primary languages spoken
   - Local currencies

   Example content format:

   ```text
   Tokyo, Japan has a population of 37.4 million people. The climate
   is humid subtropical with hot summers and mild winters. The primary
   language is Japanese and the currency is the Japanese Yen.

   Delhi, India has a population of 32.9 million. The climate is
   semi-arid with extreme summers and cool winters. The primary
   language is Hindi and the currency is the Indian Rupee.

   Shanghai, China has a population of 28.5 million people. The
   climate is humid subtropical with hot, humid summers and cool, damp
   winters. The primary language is Mandarin Chinese and the currency
   is the Chinese Yuan.

   São Paulo, Brazil has a population of 22.8 million people. The
   climate is subtropical highland with warm, rainy summers and mild,
   dry winters. The primary language is Portuguese and the currency is
   the Brazilian Real.

   Dhaka, Bangladesh has a population of 22.4 million people. The
   climate is tropical monsoon with hot, humid summers and mild
   winters. The primary language is Bengali and the currency is the
   Bangladeshi Taka.
  ```

### Load Documents into TrustGraph

You can load documents using either the web workbench or the command line interface.

#### Option A: Using the Web Workbench

1. **Navigate to Library**
   In the TrustGraph workbench, click on **Library** in the navigation menu.

2. **Upload Documents**
   Click **Upload Documents** button.

3. **Configure Document Upload**
   - **Title**: Enter `30 Most Populous Cities`
   - **Document Type**: Select `PDF` from the dropdown
   - **Select Files**: Click **Select PDF files** and choose your `cities_data.pdf` file

4. **Submit Upload**
   Click **Submit** to load the document into the library.

#### Option B: Using the Command Line

Load the document using the `tg-add-library-document` command:

```bash
tg-add-library-document cities_data.pdf \
  --name "30 Most Populous Cities" \
  --kind "application/pdf"
```

## Step 3: Start an Object Extraction Flow

Use the Workbench to create a new flow on the Flows page.

Select 'Create', give your flow an ID e.g. `object-extraction` and
select the `object-extract` flow class.  Give it a helpful description
e.g. `Object extraction`.

## Step 4: Launch Document Processing

On the Library page, select your document containing city information,
click 'Submit' at the bottom of the screen.

Select your new object extraction processing and submit the document.

You can track progress on the Grafana dashboard.  The sample document
provided should process quickly, say under 1 minute.  The processing
makes use of an LLM to perform extraction so there will be time needed
when processing large datasets.

## Step 5: Query Extracted Data

TrustGraph 1.3 provides multiple integrated ways to query your structured data. You can use natural language queries, GraphQL, or direct object queries through the CLI.

### Method 1: Natural Language Queries

Use `tg-invoke-nlp-query` to convert natural language questions into GraphQL queries:

```bash
# Generate a GraphQL query from natural language
tg-invoke-nlp-query -q "Show all cities with population over 30 million"

# Generate and execute in one step
tg-invoke-nlp-query -q "List cities where the primary language is English" --format graphql | \
  xargs -I {} tg-invoke-structured-query -q '{}'
```

### Method 2: Direct GraphQL Queries

Use `tg-invoke-structured-query` to execute GraphQL queries directly:

```bash
# Get all cities
tg-invoke-structured-query -q "Show all cities"

# Filter by population
tg-invoke-structured-query -q "Find cities with population over 25 million"

# Query specific fields
tg-invoke-structured-query -q 'query { cities { city country population currency } }'

# Complex query with filters
tg-invoke-structured-query -q 'query { 
  cities(where: {population: {_gt: 30000000}}) { 
    city 
    country 
    population 
    climate 
  } 
}'
```

Example output:
```
+----------+---------+------------+------------------+
| city     | country | population | climate          |
+----------+---------+------------+------------------+
| Tokyo    | Japan   | 37400000   | humid subtropical|
| Delhi    | India   | 32900000   | semi-arid        |
+----------+---------+------------+------------------+
```

### Method 3: Object Queries

Use `tg-invoke-objects-query` to query objects directly from collections:

```bash
# Query all objects in the cities collection
tg-invoke-objects-query -c cities

# Filter by type
tg-invoke-objects-query -c cities -t City

# Apply filters using JSON query syntax
tg-invoke-objects-query -c cities -q '{"population": {"$gt": 25000000}}'

# Filter by multiple conditions
tg-invoke-objects-query -c cities -q '{"$and": [
  {"population": {"$gte": 20000000}},
  {"primary_language": "Portuguese"}
]}'

# Export to different formats
tg-invoke-objects-query -c cities --format json > cities.json
tg-invoke-objects-query -c cities --format csv > cities.csv
```

Example output:
```
+------+-----------+------------+------------+----------------------+------------------+------------------+
| id   | city      | country    | population | climate              | primary_language | currency         |
+------+-----------+------------+------------+----------------------+------------------+------------------+
| c001 | São Paulo | Brazil     | 22800000   | subtropical highland | Portuguese       | Brazilian Real   |
| c002 | Tokyo     | Japan      | 37400000   | humid subtropical    | Japanese         | Japanese Yen     |
| c003 | Shanghai  | China      | 28500000   | humid subtropical    | Mandarin Chinese | Chinese Yuan     |
| c004 | Delhi     | India      | 32900000   | semi-arid           | Hindi            | Indian Rupee     |
| c005 | Dhaka     | Bangladesh | 22400000   | tropical monsoon    | Bengali          | Bangladeshi Taka |
+------+-----------+------------+------------+----------------------+------------------+------------------+
```

### Advanced Query Examples

#### Aggregations
```bash
# Count cities by primary language
tg-invoke-structured-query -q "What's the count of cities grouped by primary language?"

# Average population by climate type
tg-invoke-structured-query -q "Show average population by climate type"
```

#### Sorting and Limiting
```bash
# Top 3 most populous cities
tg-invoke-objects-query -c cities -l 3 --sort population:desc

# Cities sorted by name
tg-invoke-structured-query -q 'query { cities(orderBy: {city: asc}) { city population } }'
```

#### Export and Processing
```bash
# Export to CSV for analysis
tg-invoke-objects-query -c cities --format csv > cities_data.csv

# Process with jq
tg-invoke-objects-query -c cities --format json | \
  jq '.objects[] | select(.population > 30000000) | .city'

# Calculate total population
tg-invoke-objects-query -c cities --format json | \
  jq '[.objects[].population] | add'
```

### Common Issues and Solutions

**No entities extracted**
- Check that your schema matches the document content
- Verify the document was properly loaded
- Review extraction logs for errors
- Try adjusting the confidence threshold lower
- Check Grafana (http://localhost:3000) to see any indicators of load
  failure.
- Check container logs of `kg-extract-objects` and `store-objects` for
  errors.

## Next Steps

Now that you have structured data loaded and queryable in TrustGraph, you can:

1. **Build complex queries** - Combine natural language and GraphQL for sophisticated data retrieval
2. **Integrate with applications** - Use the query APIs to power data-driven applications
3. **Create data pipelines** - Export and transform data for downstream systems
4. **Experiment with schemas** - Try different schemas for various data domains
5. **Combine with RAG** - Use structured data alongside document RAG for comprehensive knowledge retrieval

## Best Practices

1. **Schema Design**
   - Keep schemas focused on specific domains
   - Use clear, descriptive property names
   - Include helpful descriptions for each property
   - Start simple and iterate

2. **Document Preparation**
   - Ensure documents contain clear, structured information
   - Use consistent formatting and terminology
   - Include relevant context around entities

3. **Extraction Configuration**
   - Start with higher confidence thresholds and adjust down if needed
   - Use appropriate models for your document complexity
   - Monitor extraction quality and iterate on schemas

4. **Data Management**
   - Regularly backup extracted data
   - Implement data validation checks
   - Plan for data versioning as schemas evolve

## Further Reading

- [tg-load-structured-data](../../reference/cli/tg-load-structured-data) - Load structured data files
- [tg-invoke-structured-query](../../reference/cli/tg-invoke-structured-query) - Execute GraphQL queries
- [tg-invoke-nlp-query](../../reference/cli/tg-invoke-nlp-query) - Convert natural language to GraphQL
- [tg-invoke-objects-query](../../reference/cli/tg-invoke-objects-query) - Query objects in collections
- [TrustGraph CLI Reference](../../reference/cli/) - Complete CLI documentation

