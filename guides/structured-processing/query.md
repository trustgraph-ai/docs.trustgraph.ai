---
title: Querying structured data
layout: default
parent: Structured data processing
nav_order: 4
---

# Querying Structured Data

Learn how to process documents and extract structured data using TrustGraph's schema-based extraction capabilities.

This feature was introduced in TrustGraph 1.3.

## Overview

TrustGraph provides capabilities for querying structured data using defined
schema

**Note**: TrustGraph 1.3 introduces fully integrated query capabilities for structured data. You can now query extracted data using natural language, GraphQL, or direct object queries through the CLI commands.

This guide walks through defining extraction schemas, loading structured data, processing documents, and querying the extracted data using TrustGraph's integrated query tools.

## What You'll Learn

- How to query extracted data using natural language, GraphQL, and object queries

## Prerequisites

Before starting this guide, ensure you have:

- A running TrustGraph instance version 1.3 or later (see [Installation Guide](../../getting-started/installation))
- Python 3.10 or later with the TrustGraph CLI tools installed (`pip install trustgraph-cli`)
- Sample documents or structured data files to process

## NLP query operation

This operation takes a natural language query, and uses an LLM prompt
to convert to a GraphQL query.  This uses defined schema, so you need
to have the pies schema loaded:

```
tg-invoke-nlp-query -f obj-ex \
  -q 'Which pies have more than 20cm diameter?'
```

If successful the output is something like...

```
Generated GraphQL Query:
----------------------------------------
query { pies(where: {diameter_cm: {gt: 20}}) { pie_type region diameter_cm } }
----------------------------------------
Detected Schemas: pies
Confidence: 95.00%
```

## Objects query operation

This operation takes a GraphQL query, and executes it on the object
store.

```
tg-invoke-objects-query -f obj-ex \
  --collection uk-pies \
  -q '
{
  pies (where: {diameter_cm: {gt: 20}})
  { pie_type region diameter_cm }
}'
```

If successful the output is something like...

```
+-------------------+-----------+-------------+
|     pie_type      |  region   | diameter_cm |
+-------------------+-----------+-------------+
| Veggie Wellington |  London   |    25.0     |
| Toad in the Hole  | Yorkshire |    22.0     |
+-------------------+-----------+-------------+
```

You can use `--format` to request CSV or JSON output.

## Structured query operation

This is an API which uses the above two operations in sequence.

```
tg-invoke-structured-query -f obj-ex \
  --collection uk-pies \
  -q 'Which pies have more than 20cm diameter?'
```

If successful the output is something like...

```
+-------------------+-----------+-------------+
|     pie_type      |  region   | diameter_cm |
+-------------------+-----------+-------------+
| Veggie Wellington |  London   |    25.0     |
| Toad in the Hole  | Yorkshire |    22.0     |
+-------------------+-----------+-------------+
```

You can use `--format` to request CSV or JSON output.

## With collections

```
tg-invoke-structured-query -f obj-ex \
  --collection fr-pies \
  -q 'Which pies have more than 20cm diameter?'
```

```
+-----------------------+------------+-------------+
|       pie_type        |   region   | diameter_cm |
+-----------------------+------------+-------------+
|     Tarte Flambée     |   Alsace   |    28.0     |
|   Tarte Alsacienne    |   Alsace   |    20.5     |
|    Quiche Lorraine    |  Lorraine  |    22.0     |
|     Pissaladière      |  Provence  |    25.0     |
|   Galette des Rois    | Nationwide |    21.0     |
| Flamiche aux Poireaux |  Picardy   |    22.5     |
+-----------------------+------------+-------------+
```

```
tg-invoke-structured-query -f obj-ex \
  --collection uk-pies \
  -q 'Which pies have more than 20cm diameter?'
```

```
+-------------------+-----------+-------------+
|     pie_type      |  region   | diameter_cm |
+-------------------+-----------+-------------+
| Veggie Wellington |  London   |    25.0     |
| Toad in the Hole  | Yorkshire |    22.0     |
+-------------------+-----------+-------------+
```

## Best Practices

### Schema Design

- Keep schemas focused on specific domains
- Use clear, descriptive property names
- Include helpful descriptions for each property
- Start simple and iterate

## Further Reading

- [tg-invoke-structured-query](../../reference/cli/tg-invoke-structured-query) - Execute GraphQL queries
- [tg-invoke-nlp-query](../../reference/cli/tg-invoke-nlp-query) - Convert natural language to GraphQL
- [tg-invoke-objects-query](../../reference/cli/tg-invoke-objects-query) - Query objects in collections
- [TrustGraph CLI Reference](../../reference/cli/) - Complete CLI documentation

