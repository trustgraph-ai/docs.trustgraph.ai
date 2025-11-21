---
title: tg-invoke-objects-query
parent: CLI
review_date: 2026-03-05
---

# tg-invoke-objects-query

Query and retrieve objects stored in the TrustGraph object storage system.

## Synopsis

```bash
tg-invoke-objects-query -c COLLECTION [OPTIONS]
```

## Description

The `tg-invoke-objects-query` command queries objects stored in TrustGraph's object storage system. Objects are structured data entities that have been extracted from documents or imported directly. This tool allows you to:

- Query objects by collection
- Filter objects by type or properties
- Retrieve specific object details
- Export object data for analysis

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `-c`, `--collection COLLECTION` | Collection name to query | Required |
| `-t`, `--type TYPE` | Filter by object type | All types |
| `-q`, `--query QUERY` | Query filter (JSON format) | None |
| `-l`, `--limit N` | Maximum number of results | `100` |
| `-o`, `--offset N` | Skip first N results | `0` |
| `-u`, `--url URL` | TrustGraph API URL | `http://localhost:8088/` |
| `--format FORMAT` | Output format: `table`, `json`, `jsonl` | `table` |
| `--fields FIELDS` | Comma-separated list of fields to include | All fields |
| `-h`, `--help` | Show help message | - |

## Output Formats

### Table Format (Default)

Displays objects in a formatted table:

```bash
$ tg-invoke-objects-query -c products

+------+------------------+----------+-------+-------------+
| id   | name             | type     | price | category    |
+------+------------------+----------+-------+-------------+
| p001 | Wireless Mouse   | Product  | 29.99 | Electronics |
| p002 | USB Cable        | Product  | 9.99  | Electronics |
| p003 | Notebook         | Product  | 4.99  | Stationery  |
+------+------------------+----------+-------+-------------+
```

### JSON Format

Returns complete JSON response:

```bash
$ tg-invoke-objects-query -c customers --format json

{
  "objects": [
    {
      "id": "c001",
      "type": "Customer",
      "properties": {
        "name": "John Smith",
        "email": "john@example.com",
        "city": "London",
        "created": "2024-01-15T10:30:00Z"
      }
    },
    {
      "id": "c002",
      "type": "Customer",
      "properties": {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "city": "Paris",
        "created": "2024-01-16T14:20:00Z"
      }
    }
  ],
  "total": 2,
  "hasMore": false
}
```

### JSON Lines Format

Outputs one object per line for streaming processing:

```bash
$ tg-invoke-objects-query -c orders --format jsonl

{"id":"o001","type":"Order","properties":{"date":"2024-01-15","total":599.99}}
{"id":"o002","type":"Order","properties":{"date":"2024-01-16","total":1299.99}}
{"id":"o003","type":"Order","properties":{"date":"2024-01-17","total":89.99}}
```

## Examples

### Basic Queries

```bash
# Query all objects in a collection
tg-invoke-objects-query -c products

# Query with type filter
tg-invoke-objects-query -c entities -t Person

# Limit results
tg-invoke-objects-query -c documents -l 10
```

### Using Query Filters

```bash
# Filter by property value (JSON query)
tg-invoke-objects-query -c products -q '{"category": "Electronics"}'

# Complex filter with multiple conditions
tg-invoke-objects-query -c orders -q '{"total": {"$gt": 100}, "status": "pending"}'

# Filter by date range
tg-invoke-objects-query -c events -q '{"date": {"$gte": "2024-01-01", "$lt": "2024-02-01"}}'
```

### Field Selection

```bash
# Select specific fields only
tg-invoke-objects-query -c customers --fields id,name,email

# Exclude sensitive fields
tg-invoke-objects-query -c users --fields id,username,created_at
```

### Pagination

```bash
# First page of results
tg-invoke-objects-query -c products -l 20

# Second page
tg-invoke-objects-query -c products -l 20 -o 20

# Third page
tg-invoke-objects-query -c products -l 20 -o 40
```

### Export Operations

```bash
# Export to JSON file
tg-invoke-objects-query -c customers --format json > customers.json

# Export as JSON lines for streaming
tg-invoke-objects-query -c orders --format jsonl > orders.jsonl

# Process with jq
tg-invoke-objects-query -c products --format json | jq '.objects[] | select(.price < 50)'
```

## Working with Different Object Types

### Extracted Entities

Query entities extracted from documents:

```bash
# Query person entities
tg-invoke-objects-query -c entities -t Person

# Query organization entities
tg-invoke-objects-query -c entities -t Organization

# Query location entities
tg-invoke-objects-query -c entities -t Location
```

### Document Metadata

Query document metadata objects:

```bash
# Query all documents
tg-invoke-objects-query -c documents

# Filter by document type
tg-invoke-objects-query -c documents -q '{"mime_type": "application/pdf"}'
```

### Custom Objects

Query custom imported objects:

```bash
# Query product catalog
tg-invoke-objects-query -c products -t Product

# Query customer database
tg-invoke-objects-query -c customers -t Customer
```

## Advanced Usage

### Complex Queries

```bash
# Combine multiple filters
tg-invoke-objects-query -c orders \
  -q '{"$and": [{"total": {"$gte": 100}}, {"status": "completed"}]}'

# OR conditions
tg-invoke-objects-query -c products \
  -q '{"$or": [{"category": "Electronics"}, {"price": {"$lt": 20}}]}'

# Nested object queries
tg-invoke-objects-query -c customers \
  -q '{"address.city": "London"}'
```

### Integration with Other Tools

```bash
# Count objects
tg-invoke-objects-query -c products --format json | jq '.total'

# Calculate sum
tg-invoke-objects-query -c orders --format jsonl | \
  jq -s 'map(.properties.total) | add'

# Find unique values
tg-invoke-objects-query -c customers --format jsonl | \
  jq -r '.properties.city' | sort -u
```

### Monitoring Collections

```bash
# Check collection size
tg-invoke-objects-query -c products -l 1 --format json | jq '.total'

# List all object types in collection
tg-invoke-objects-query -c entities --format jsonl | \
  jq -r '.type' | sort -u

# Find recently added objects
tg-invoke-objects-query -c documents \
  -q '{"created": {"$gte": "2024-01-01T00:00:00Z"}}'
```

## Query Operators

Supported query operators:

| Operator | Description | Example |
|----------|-------------|---------|
| `$eq` | Equals | `{"status": {"$eq": "active"}}` |
| `$ne` | Not equals | `{"status": {"$ne": "deleted"}}` |
| `$gt` | Greater than | `{"price": {"$gt": 100}}` |
| `$gte` | Greater than or equal | `{"age": {"$gte": 18}}` |
| `$lt` | Less than | `{"stock": {"$lt": 10}}` |
| `$lte` | Less than or equal | `{"priority": {"$lte": 5}}` |
| `$in` | In array | `{"category": {"$in": ["Electronics", "Books"]}}` |
| `$nin` | Not in array | `{"status": {"$nin": ["deleted", "archived"]}}` |
| `$and` | Logical AND | `{"$and": [condition1, condition2]}` |
| `$or` | Logical OR | `{"$or": [condition1, condition2]}` |

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
$ tg-invoke-objects-query -c nonexistent

Error: Collection 'nonexistent' not found
```

## Performance Tips

1. **Use pagination**: For large collections, paginate results
2. **Select specific fields**: Reduce data transfer by selecting only needed fields
3. **Use indexes**: Query on indexed fields for better performance
4. **Apply filters early**: Filter at query time rather than post-processing

## Troubleshooting

### Empty Results

If queries return no objects:
- Verify collection name is correct
- Check that objects exist in the collection
- Review query filters for typos

### Slow Queries

For performance issues:
- Add pagination with `-l` and `-o`
- Reduce number of fields with `--fields`
- Use more specific filters

### Connection Errors

If unable to connect:
- Verify TrustGraph is running
- Check API URL is correct
- Ensure network connectivity

## See Also

- [tg-invoke-structured-query](tg-invoke-structured-query) - Query structured data with GraphQL
- [tg-invoke-nlp-query](tg-invoke-nlp-query) - Convert natural language to queries
- [Object Storage API](../apis/api-object-storage) - API documentation
- [tg-load-structured-data](tg-load-structured-data) - Load structured data into object storage
