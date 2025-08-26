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

**Note**: At the time of writing, this feature is partially complete. The structured data loading and extraction functionality is working and available in version 1.2. The query interface for agents is still a work in progress. Currently, you can access the extracted data directly through Cassandra queries, with full agent query capabilities coming in a future release.

This guide walks through defining extraction schemas, processing documents, and querying the extracted data using Cassandra Query Language (CQL).

## What You'll Learn

- How to define a custom extraction schema
- How to load test data into TrustGraph
- How to start an object extraction flow
- How to process documents through the extraction pipeline
- How to query extracted data using Cassandra

## Prerequisites

Before starting this guide, ensure you have:

- A running TrustGraph instance version 1.2 or later (see [Installation Guide](../../getting-started/installation))
- Python 3.8 or later with the TrustGraph CLI tools installed (`pip install trustgraph-cli`)
- Sample documents to process
- Access to the Cassandra database (for querying extracted data)

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

4. **Configure Basic Schema Information**
   - **Schema ID**: Enter a unique identifier (e.g., `cities`)
   - **Name**: Enter a display name (e.g., `Cities`)
   - **Description**: Add a description of what data this schema captures (e.g., `City demographics including population, currency, climate and language for the most populous cities`)

5. **Add Schema Fields**
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

6. **Configure Indexes**
   In the Indexes section, click **"Add Index"** and add:
   - `primary_language`
   - `currency`
   
   Structured data does not support extra index fields at the moment.

7. **Save the Schema**
   Click **"Create"** to save your schema.

<a href="create-schema.png">
  <img src="create-schema.png" alt="Schema creation dialog in TrustGraph workbench">
</a>

### Option B: Using the Command Line

You can also create a schema using the CLI with the `tg-put-config` command:

```bash
tg-put-config-item --type schema --key cities2 --value '{
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

## Step 2: Load Test Data

Now we'll load some test documents that contain information matching our schema. TrustGraph can process various document formats including PDFs, Word documents, and text files.

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

## Step 5: Query Data Using Cassandra

Since the agent query interface is still under development, we'll use Cassandra Query Language (CQL) directly to examine the extracted data.

### Access Cassandra Shell

Connect to the Cassandra database.  The easiest way is to execute
the `cqlsh` command line utility inside the running Cassandra container.

Find out the Cassandra container name:
```bash
docker ps -a | grep -i cassandra
```

The first field is the container ID, and the last field is a stable name
for the container.  Use either container ID or container name
(say it's `tg_cassandra_1` I can attach to the container and run the `cqlsh`
command:

```bash
docker exec -it tr_cassandra_1 cqlsh
```

### Explore the Data Structure

First, let's understand the database structure:

```sql
-- List all keyspaces
DESCRIBE KEYSPACES;

-- Use the TrustGraph keyspace
USE trustgraph;

-- List all tables
DESCRIBE TABLES;
```

You should see a table based on the name of your schema.  If you used
`cities` that would be `o_cities`.

### Query Extracted Entities

Query the extracted company entities:

```sql
-- Show table structure
DESCRIBE o_cities;
```

```sql
-- Find all extracted companies
SELECT * FROM o_cities;
```

And you should see extracted objects:

```text
cqlsh:trustgraph> select * from o_cities;

 collection | city      | country    | climate              | currency         | population | primary_language
------------+-----------+------------+----------------------+------------------+------------+------------------
    default | São Paulo |     Brazil | subtropical highland |   Brazilian Real |   22800000 |       Portuguese
    default |     Tokyo |      Japan |    humid subtropical |     Japanese Yen |   37400000 |         Japanese
    default |  Shanghai |      China |    humid subtropical |     Chinese Yuan |   28500000 | Mandarin Chinese
    default |     Delhi |      India |            semi-arid |     Indian Rupee |   32900000 |            Hindi
    default |     Dhaka | Bangladesh |     tropical monsoon | Bangladeshi Taka |   22400000 |          Bengali
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

While waiting for the full agent query capabilities to be released, you can:

1. **Experiment with different schemas** - Try creating schemas for different domains
2. **Build data pipelines** - Export extracted data for use in other systems
3. **Create validation scripts** - Write scripts to validate extraction quality
4. **Prepare for agent integration** - Design queries that agents will eventually use

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

- [Cassandra Query Language Guide](https://cassandra.apache.org/doc/latest/cql/)
- [TrustGraph CLI Reference](../../reference/cli/)

