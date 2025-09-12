---
layout: default
title: tg-invoke-structured-query
parent: CLI
---

# tg-invoke-structured-query

Execute natural language questions or GraphQL queries against structured data.

## Synopsis

```bash
tg-invoke-structured-query -q QUESTION [OPTIONS]
```

## Description

The `tg-invoke-structured-query` command executes queries against your structured data, returning actual data results. It accepts either:

- Natural language questions (automatically converted to GraphQL)
- GraphQL queries directly

This tool is the primary way to retrieve structured data from the command line.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `-q`, `--question QUESTION` | Natural language question or GraphQL query | Required |
| `-u`, `--url URL` | TrustGraph API URL | `http://localhost:8088/` |
| `-f`, `--flow-id ID` | Flow ID to use | `default` |
| `--format FORMAT` | Output format: `table`, `json`, `csv` | `table` |
| `-h`, `--help` | Show help message | - |

## Output Formats

### Table Format (Default)

Displays results in a formatted ASCII table:

```bash
$ tg-invoke-structured-query -q "Show all products under $50"

+----+----------------+-------+-------------+
| id | name           | price | category    |
+----+----------------+-------+-------------+
| 1  | Wireless Mouse | 29.99 | Electronics |
| 2  | USB Cable      | 9.99  | Electronics |
| 3  | Notebook       | 4.99  | Stationery  |
+----+----------------+-------+-------------+
```

### JSON Format

Returns complete JSON response:

```bash
$ tg-invoke-structured-query -q "List customers from London" --format json

{
  "customers": [
    {
      "id": "c1",
      "name": "John Smith",
      "email": "john@example.com",
      "city": "London"
    },
    {
      "id": "c2",
      "name": "Jane Doe",
      "email": "jane@example.com",
      "city": "London"
    }
  ]
}
```

### CSV Format

Outputs data in CSV format for easy import into spreadsheets:

```bash
$ tg-invoke-structured-query -q "Recent orders" --format csv

id,orderDate,customer,total,status
o1,2024-01-15,John Smith,599.99,completed
o2,2024-01-16,Jane Doe,1299.99,processing
o3,2024-01-17,Bob Wilson,89.99,shipped
```

## Examples

### Natural Language Queries

```bash
# Simple query
tg-invoke-structured-query -q "Show all products"

# Filtered query
tg-invoke-structured-query -q "Find orders over $1000"

# Query with relationships
tg-invoke-structured-query -q "List customers who ordered electronics"

# Aggregation query
tg-invoke-structured-query -q "What's the total revenue by month?"
```

### Direct GraphQL Queries

```bash
# Execute a GraphQL query
tg-invoke-structured-query -q 'query { products(first: 10) { id name price } }'

# Complex GraphQL with filters
tg-invoke-structured-query -q 'query { 
  orders(where: {status: {_eq: "pending"}}) { 
    id 
    customer { name } 
    total 
  } 
}'
```

### Piping Queries

```bash
# Generate query with NLP and execute
tg-invoke-nlp-query -q "Active users" --format graphql | \
  xargs -I {} tg-invoke-structured-query -q '{}'

# Read query from file
cat query.graphql | xargs -I {} tg-invoke-structured-query -q '{}'
```

### Export to Files

```bash
# Export to CSV file
tg-invoke-structured-query -q "All products" --format csv > products.csv

# Export to JSON for processing
tg-invoke-structured-query -q "Customer data" --format json > customers.json

# Process with jq
tg-invoke-structured-query -q "Orders" --format json | jq '.orders[] | .total'
```

## Working with Different Data Types

### Products and Inventory

```bash
# Product queries
tg-invoke-structured-query -q "Products in stock"
tg-invoke-structured-query -q "Low inventory items (quantity < 10)"
```

### Customer Data

```bash
# Customer queries
tg-invoke-structured-query -q "New customers this month"
tg-invoke-structured-query -q "Customers with no orders"
```

### Orders and Transactions

```bash
# Order queries
tg-invoke-structured-query -q "Pending orders"
tg-invoke-structured-query -q "Orders shipped today"
```

## Advanced Usage

### Using Variables in GraphQL

For complex queries with variables, save to a file:

```bash
# query.graphql
cat > query.graphql << 'EOF'
query GetCustomerOrders {
  customers(where: {id: {_eq: "c123"}}) {
    name
    orders(orderBy: {orderDate: desc}, first: 10) {
      id
      orderDate
      total
    }
  }
}
EOF

# Execute the query
cat query.graphql | xargs -I {} tg-invoke-structured-query -q '{}'
```

### Combining with Other Tools

```bash
# Count results
tg-invoke-structured-query -q "All products" --format json | jq '.products | length'

# Sum values
tg-invoke-structured-query -q "Today's orders" --format json | \
  jq '[.orders[].total] | add'

# Filter and format
tg-invoke-structured-query -q "Customers" --format csv | \
  awk -F',' '$3 == "London" {print $2}'
```

## Integration with Agent Extraction

Query data extracted by agents:

```bash
# First, extract data using an agent
tg-invoke-agent -p "Extract product data from catalog" -t catalog.txt

# Then query the extracted data
tg-invoke-structured-query -q "Show extracted products"
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `TRUSTGRAPH_URL` | Default API URL | `http://localhost:8088/` |

## Exit Codes

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | Error (query error, service error, etc.) |

## Error Handling

The tool provides clear error messages:

```bash
$ tg-invoke-structured-query -q "Invalid query syntax"

Query Errors:
  - Syntax error at position 15
  - Unknown entity type: InvalidEntity
```

## Performance Tips

1. **Use specific queries**: More specific queries return faster
2. **Limit results**: Add limits to queries when exploring data
3. **Use indexes**: Query on indexed fields for better performance
4. **Batch operations**: Group related queries together

## Troubleshooting

### No Data Returned

If queries return empty results:
- Verify data has been loaded/imported
- Check schema names match exactly
- Use simpler queries to test connectivity

### Query Timeout

For large datasets:
- Add pagination with `first:` and `offset:`
- Use more specific filters
- Consider aggregation queries instead of full data

### Format Issues

If output format is incorrect:
- Verify the `--format` option is spelled correctly
- Check that data structure matches expected format
- Use JSON format for complex nested data

## See Also

- [tg-invoke-nlp-query](tg-invoke-nlp-query) - Convert natural language to GraphQL
- [Structured Query API](../apis/api-structured-query) - API documentation
- [NLP Query API](../apis/api-nlp-query) - Query generation API
- [Object Storage API](../apis/api-object-storage) - Data storage API
