---
title: Agent integration
layout: default
parent: Structured data processing
nav_order: 5
---

# Agent Integration with Structured Queries

Learn how TrustGraph agents can query and interact with structured data stored in the object store.

This feature was introduced in TrustGraph 1.3.

## Overview

TrustGraph agents can directly query structured data using the
`structured-query` tool. This enables agents to:
- Answer questions about tabular data stored in TrustGraph
- Combine structured data queries with document analysis
- Provide intelligent responses based on database content
- Execute complex queries without requiring the user to know GraphQL

## Prerequisites

Before agents can query structured data, you must configure the `structured_query` tool:

```bash
tg-set-tool --id structured_query \
  --name structured_query \
  --description 'Executes a database structured query' \
  --type structured-query \
  --collection <your-collection-name>
```

**Example for pie data:**
```bash
tg-set-tool --id structured_query \
  --name structured_query \
  --description 'Executes a database structured query for pie data' \
  --type structured-query \
  --collection fr-pies
```

**Important**: The `--collection` parameter must match the collection where
your structured data is stored.

## How It Works

When an agent receives a question about structured data:

1. The agent analyzes the question to understand what data is needed
2. The agent uses the `structured_query` tool to query the object store
3. The query is automatically converted from natural language to GraphQL
4. Results are returned to the agent in JSON format
5. The agent interprets the results and formulates a response

## Example Usage

### Basic Query

Here's an example of querying pie data stored in TrustGraph:

```bash
$ tg-invoke-agent -f obj-ex -q 'Which pies are larger than 20cm diameter?'
```

**Agent Response:**
```
❓ Which pies are larger than 20cm diameter?

🤔 The user is asking for pies that are larger than 20cm in diameter. I need
🤔 to query the database to find this information. The `structured_query` tool
🤔 seems appropriate for this. I will ask a question that directly targets
🤔 pies with a diameter greater than 20cm.

💡 {"pies": [{"pie_type": "Tarte Flambée", "diameter_cm": 28.0}, 
💡 {"pie_type": "Tarte Alsacienne", "diameter_cm": 20.5},
💡 {"pie_type": "Quiche Lorraine", "diameter_cm": 22.0}, 
💡 {"pie_type": "Pissaladière", "diameter_cm": 25.0},
💡 {"pie_type": "Galette des Rois", "diameter_cm": 21.0}, 
💡 {"pie_type": "Flamiche aux Poireaux", "diameter_cm": 22.5}]}

🤔 The user is asking for pies larger than 20cm in diameter. The previous
🤔 action returned a list of pies with their diameters. I need to extract the
🤔 pie types from this list where the diameter is greater than 20cm.

Tarte Flambée, Tarte Alsacienne, Quiche Lorraine, Pissaladière, Galette des Rois, 
Flamiche aux Poireaux
```

### Understanding the Process

In the example above:

1. **Question Analysis**: The agent understands the user wants pies with diameter > 20cm
2. **Tool Selection**: The agent identifies `structured_query` as the appropriate tool
3. **Query Execution**: The agent queries the database for pie data
4. **Result Processing**: The agent receives JSON data with pie information
5. **Answer Generation**: The agent filters and formats the results for the user

## Query Capabilities

Agents can handle various types of structured queries, depending on
the capabilities of the LLM in use:

### Filtering
```bash
tg-invoke-agent -f obj-ex -q 'List all products with price over $100'
```

### Sorting
```bash
tg-invoke-agent -f obj-ex -q 'Show the top 5 most expensive items'
```

### Aggregations
```bash
tg-invoke-agent -f obj-ex -q 'What is the total revenue by category?'
```

### Relationships
```bash
tg-invoke-agent -f obj-ex -q 'Which customers ordered products from France?'
```

## Agent Prompting Best Practices

When querying structured data through agents:

### Be Specific
- ✅ "Show pies larger than 20cm diameter"
- ❌ "Show big pies"

### Use Clear Comparisons
- ✅ "Products with price between $50 and $100"
- ❌ "Moderately priced products"

### Specify Fields When Needed
- ✅ "List customer names and email addresses"
- ❌ "Show customer info"

## Combining with Other Agent Capabilities

Agents can combine structured queries with other capabilities:

### Document Analysis + Structured Query
```bash
tg-invoke-agent -f obj-ex -q \
  'Compare the revenue figures in this report with our database records'
```

### Multi-step Reasoning
```bash
tg-invoke-agent -f obj-ex -q \
  'Find the most profitable product category and explain why it performs well'
```

### Data Validation
```bash
tg-invoke-agent -f obj-ex -q \
  'Check if any products have invalid pricing (negative or over $10,000)'
```

## Troubleshooting

### Agent doesn't find data
- Verify data is loaded: `tg-invoke-objects-query -c <collection>`
- Check the flow is configured for object extraction
- Ensure schema matches the data structure
- Check that you're using the right flow - it's important to use a flow
  with the structured data capabilities deployed

### Incorrect results
- Be more specific in your questions
- Use exact field names when known
- Try breaking complex questions into steps

### Performance issues
- Limit result sets with specific filters
- Use aggregations instead of retrieving all records
- Consider indexing frequently queried fields

## See Also

- [Structured data processing overview](.)
- [Load from a data file](load-file)
- [Querying structured data](query)
- [Agent API](../../reference/apis/api-agent)
- [Structured Query API](../../reference/apis/api-structured-query)
