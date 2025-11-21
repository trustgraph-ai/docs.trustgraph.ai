---
title: Structure data load from a data file
parent: Structured data processing
nav_order: 3
review_date: 2026-02-01
---

# Structured Data Load from a File

In this guide a document containing tabular data will be loaded using a
new schema to load data from XML files.

Learn how to process data files and load structured data using
command-line utilities.

This feature was introduced in TrustGraph 1.3.

## Overview

TrustGraph provides capabilities for extracting structured information from
data files using configurable schemas. This allows you to define custom data
structures and have TrustGraph automatically extract matching information from
your documents.

**Note**: At the time of writing, the automated data diagnosis features
rely on prompts which can be demanding of the LLM and are sensitive to 
LLM training and capabilities.

Expect to see further developments on the structured load capablity
on the roadmap:
- Broader testing with a broader set of LLMs and models.  We're particularly
  interested in allowing these capabilities to be effective on smaller
  models.
- Integration of data diagnosis with TrustGraph services so that they can
  be invoked using APIs and used in the workbench.

## What You'll Learn

- The purpose of a structured data schema.
- How to load structured data directly using `tg-load-structured-data`

## Prerequisites

Before starting this guide, ensure you have:

- A running TrustGraph instance version 1.3 or later (see [Installation Guide](../../getting-started/installation))
- Python 3.10 with the TrustGraph CLI tools installed (`pip install trustgraph-cli`)
- Sample documents or structured data files to process

## Data files you will need:

- [UK pies](https://raw.githubusercontent.com/trustgraph-ai/example-data/main/pies/uk-pies-simplified.xml)
- [French pies](https://raw.githubusercontent.com/trustgraph-ai/example-data/main/pies/fr-pies-simplified.xml)
- [Pies Structured Descriptor Language](https://raw.githubusercontent.com/trustgraph-ai/example-data/main/pies/pies-sdl.json)

## Step 1: Define a Schema

The first step is to define a schema that describes the structured data you want to extract from documents. The schema defines the types of objects and their properties that TrustGraph should look for.

You can create a schema using either the web workbench or the command line interface.

### Option A: Using the Web Workbench


**Add Schema Fields**:

   Click **"Add Field"** for each field you want to include. For our cities example:
   
   **Field 1 - Pie type:**
   - Field Name: `pie_type`
   - Type: `String`
   - ☑ Primary Key
   - ☑ Required
   
   **Field 2 - Region:**
   - Field Name: `region`
   - Type: `String`
   - ☑ Primary Key
   - ☑ Required
   
   **Field 3 - Diameter (cm):**
   - Field Name: `diameter_cm`
   - Type: `float`
   - ☐ Primary Key
   - ☑ Required
   
   **Field 4 - Height (cm):**
   - Field Name: `height_cm`
   - Type: `float`
   - ☐ Primary Key
   - ☑ Required
   
   **Field 5 - Weight (grams):**
   - Field Name: `weight_grams`
   - Type: `float`
   - ☐ Primary Key
   - ☑ Required
   
   **Field 6 - Crust type:**
   - Field Name: `crust_type`
   - Type: `string`
   - ☐ Primary Key
   - ☑ Required
   
   **Field 7 - Filling category:**
   - Field Name: `filling_category`
   - Type: `string`
   - ☐ Primary Key
   - ☑ Required
   
   **Field 8 - Price:**
   - Field Name: `price`
   - Type: `float`
   - ☐ Primary Key
   - ☑ Required
   
   **Field 9 - Currency:**
   - Field Name: `currency`
   - Type: `String`
   - ☐ Primary Key
   - ☑ Required

   **Field 10 - Bakery type:**
   - Field Name: `bakery_type`
   - Type: `String`
   - ☐ Primary Key
   - ☑ Required

7. **Configure Indexes**
   In the Indexes section, click **"Add Index"** and add:
   - `filling_category`
   - `currency`
   - `region`
   - `backery_type`
   
   Note: Structured data does not support extra index fields at the moment.

### Option B: Using the Command Line

You can also create a schema using the CLI with the `tg-put-config` command:

```bash
tg-put-config-item --type schema --key pies --value '{
  "name": "pies",
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
      "name": "region",
      "type": "string",
      "primary_key": true,
      "required": true,
      "id": "0000d4e5-6f78-9012-bcde-f23456789012"
    },
    {
      "name": "diameter_cm",
      "type": "float",
      "primary_key": false,
      "required": true,
      "id": "0000e5f6-7890-1234-cdef-345678901234"
    },
    {
      "name": "height_cm",
      "type": "float",
      "primary_key": false,
      "required": true,
      "id": "0000f6a7-8901-2345-def0-456789012345"
    },
    {
      "name": "weight_grams",
      "type": "float",
      "primary_key": false,
      "required": true,
      "id": "0000a7b8-9012-3456-ef01-567890123456"
    },
    {
      "name": "crust_type",
      "type": "string",
      "primary_key": false,
      "required": true,
      "id": "0000b8c9-0123-4567-f012-678901234567"
    },
    {
      "name": "filling_category",
      "type": "string",
      "primary_key": false,
      "required": true,
      "id": "0000c9d0-1234-5678-0123-789012345678"
    },
    {
      "name": "price",
      "type": "float",
      "primary_key": false,
      "required": true,
      "id": "0000d0e1-2345-6789-1234-890123456789"
    },
    {
      "name": "currency",
      "type": "string",
      "primary_key": false,
      "required": true,
      "id": "0000e1f2-3456-7890-2345-901234567890"
    },
    {
      "name": "bakery_type",
      "type": "string",
      "primary_key": false,
      "required": true,
      "id": "0000f2a3-4567-8901-3456-012345678901"
    }
  ],
  "indexes": ["filling_category", "currency", "region", "bakery_type"]
}'
```

### Verify Schema Creation

Regardless of which method you used, verify the schema was created:

```bash
# List all schemas
tg-list-config-items --type schema

# View specific schema details
tg-get-config-item --type schema --key pies
```

You should see your `cities` schema with all defined fields and indexes.

## Step 2: Load Data into TrustGraph

### Automated load

The script `tg-load-structured-data` is a command-line utility to load
data.  It has a number of modes, the easiest of which is the automated load
mode.

When loading, you to specify the flow you want to load data into, and
you may want to override the collection (`default`).

Here's completely automated mode:

```
tg-load-structured-data -f obj-ex --collection uk-pies --auto \
  -i uk-pies.xml
```

Automated load performs the following steps:
- Examines a sample of the data file with a comparison against defined
  schema, using an LLM to select the best schema for the file.
- Diagnoses the file structure using an LLM to produce a
  Structured Descriptor Language (SDL) for the file format.
- Uses the SDL to process the file, sending objeects to the object storage
  service.

You have two options for getting structured data into TrustGraph:
1. **Direct loading** of structured data files (CSV, JSON, XML) using `tg-load-structured-data`
2. **Document extraction** where TrustGraph extracts structured data from unstructured documents

### Step-by-step load

You have the option of doing all the steps of the automated load one
at a time, in order to verify the output e.g.


#### Schema selection
```
tg-load-structured-data -f obj-ex \
  -i uk-pies.xml \
  --discover-schema
```

You will see some output which can include a schema recommendation:

```
Best matching schema: pies
```

#### Descriptor generation

This step takes as input the selected schema, takes the data file
and tries to create a structured descriptor:

```
tg-load-structured-data -f obj-ex \
  -i uk-pies.xml \
  --schema-name pies \
  --generate-descriptor --output sdl.json
```

If successful you will see output like...

```
INFO:trustgraph.cli.load_structured_data:Sample size: 100 records
INFO:trustgraph.cli.load_structured_data:Sample chars: 500 characters
INFO:trustgraph.cli.load_structured_data:Target schema: pies
Generated descriptor saved to: sdl.json
```

#### Trial parse

This step parses the file using the descriptor, and reports how much
of the data could be processed:

```
tg-load-structured-data -f obj-ex \
  -i uk-pies.xml \
  --schema-name pies \
  --descriptor sdl.json \
  --parse-only
```

If successful you will see output like...

```

... and 22 more records
Total records processed: 25

Parsing Summary:
- Input format: xml
- Records processed: 25
- Target schema: Pies
- Field mappings: 10
```

#### Data load

This step parses the file using the descriptor, and reports how much
of the data could be processed:

```
tg-load-structured-data -f obj-ex \
  -i uk-pies.xml \
  --schema-name pies \
  --descriptor sdl.json \
  --load
```

If successful you will see output like...

```
🎉 Load Complete!
- Input format: xml
- Target schema: pies
- Records imported: 25
- Flow used: obj-ex
```

## Collection management

One of the things you may find useful is loading different datasets into
different collections e.g.

```
tg-load-structured-data -f obj-ex \
  -i uk-pies.xml \
  --collection uk-pies \
  --schema-name pies \
  --descriptor sdl.json \
  --load

tg-load-structured-data -f obj-ex \
  -i fr-pies.xml \
  --collection french-pies \
  --schema-name pies \
  --descriptor sdl.json \
  --load
```

This allows data to be treated separately, but using the same schema
and collection load.

## Notes

- At the time of writing, the prompts work well at XML processing, 
  but we'll be optimising to work with smaller models and provide
  better coverage of other data types.  We recommend you stick with
  XML data for TrustGraph 1.3.
- You may find that the prompts are sensitive to different LLMs, and
  that you may see hallucinations or insensitivity to different data features.
- XPath expressions have some incompatibilities and edge cases with
  incompatibility across different libraries.  In our pie example, the
  expression `/pies/pie` accurately captures every pie record.
  The expression `//pies/pie` is looser binding which _should_ capture the
  same records, but due to ambiguities in the standard is not handled
  the same by all XML processing software.  You may need to modify and
  experiment with the SDL file XPath expressions.
- Be prepared to experiment with the SDL using `--parse-only` mode until
  it works.
- At the moment, you have to create the schema - there's no automated
  process to do that.  This is something we'll add later.

## Further Reading

- [tg-load-structured-data](../../reference/cli/tg-load-structured-data) - Load structured data files
- [Structured Data Definition](../../reference/sdl) - Data definition language
- [TrustGraph CLI Reference](../../reference/cli/) - Complete CLI documentation

