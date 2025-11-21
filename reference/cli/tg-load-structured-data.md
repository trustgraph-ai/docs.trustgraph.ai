---
title: tg-load-structured-data
parent: CLI
review_date: 2025-11-21
---

# tg-load-structured-data

Load structured data (CSV, JSON, XML) into TrustGraph for querying and analysis.

> **Note**: This is an emerging utility that may change as structured data capabilities become more integrated into the TrustGraph platform.

## Synopsis

```bash
tg-load-structured-data -f FILE -s SCHEMA [OPTIONS]
```

## Description

The `tg-load-structured-data` command loads structured data files into TrustGraph, making them available for GraphQL queries, natural language queries, and agent-based extraction. It supports various formats including CSV, JSON, and XML, with automatic or manual schema detection.

This tool bridges the gap between traditional structured data and TrustGraph's knowledge graph capabilities, enabling:
- Direct querying of structured data via GraphQL
- Natural language queries against tabular data
- Integration with document-based knowledge
- Agent-based data enrichment

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `-f`, `--file FILE` | Data file to load (CSV, JSON, XML) | Required |
| `-s`, `--schema SCHEMA` | Schema definition file or auto-detect | `auto` |
| `-c`, `--collection COLLECTION` | Target collection name | From filename |
| `-t`, `--type TYPE` | Object type name | From schema |
| `-u`, `--url URL` | TrustGraph API URL | `http://localhost:8088/` |
| `--format FORMAT` | Force input format: `csv`, `json`, `xml` | Auto-detect |
| `--delimiter DELIM` | CSV delimiter character | `,` |
| `--has-header` | CSV has header row | true |
| `--batch-size N` | Records per batch | `1000` |
| `--validate` | Validate data before loading | false |
| `--update` | Update existing records | false |
| `--dry-run` | Preview without loading | false |
| `-h`, `--help` | Show help message | - |

## Supported Formats

### CSV Files

```bash
# Load CSV with auto-detected schema
tg-load-structured-data -f customers.csv -s auto

# Custom delimiter
tg-load-structured-data -f data.tsv --delimiter '\t'

# No header row
tg-load-structured-data -f data.csv --has-header false
```

### JSON Files

```bash
# Load JSON array
tg-load-structured-data -f products.json

# Load newline-delimited JSON
tg-load-structured-data -f events.jsonl

# Nested JSON with schema
tg-load-structured-data -f complex.json -s schema.json
```

### XML Files

```bash
# Load XML with schema
tg-load-structured-data -f catalog.xml -s catalog-schema.xsd

# Auto-detect XML structure
tg-load-structured-data -f data.xml -s auto
```

## Schema Definition

### Auto-Detection

The tool can automatically detect schemas:

```bash
# Auto-detect from CSV headers
tg-load-structured-data -f sales.csv -s auto

# Preview detected schema
tg-load-structured-data -f data.csv -s auto --dry-run
```

### Manual Schema Files

Define schemas in JSON format:

```json
{
  "name": "Product",
  "fields": [
    {"name": "id", "type": "string", "required": true},
    {"name": "name", "type": "string", "required": true},
    {"name": "price", "type": "number", "required": false},
    {"name": "category", "type": "string", "required": false},
    {"name": "in_stock", "type": "boolean", "default": true}
  ],
  "indexes": ["id", "category"]
}
```

Load with schema:

```bash
tg-load-structured-data -f products.csv -s product-schema.json
```

## Examples

### Basic Data Loading

```bash
# Load customer data
tg-load-structured-data -f customers.csv -c customers

# Load with specific type
tg-load-structured-data -f employees.csv -t Employee

# Load to custom collection
tg-load-structured-data -f q1-sales.csv -c sales-2024-q1
```

### Data Validation

```bash
# Validate before loading
tg-load-structured-data -f data.csv --validate

# Dry run to preview
tg-load-structured-data -f large-dataset.csv --dry-run

# Show validation errors
tg-load-structured-data -f data.csv --validate 2> errors.log
```

### Batch Processing

```bash
# Load large file in batches
tg-load-structured-data -f huge-dataset.csv --batch-size 5000

# Process directory of files
for file in data/*.csv; do
  tg-load-structured-data -f "$file" -c "$(basename $file .csv)"
done
```

### Update Operations

```bash
# Update existing records
tg-load-structured-data -f updated-products.csv --update

# Replace entire collection
tg-invoke-objects-query -c products --delete-all
tg-load-structured-data -f new-products.csv -c products
```

## Integration with Queries

After loading data, query it using:

### GraphQL Queries
```bash
# Query loaded data
tg-invoke-structured-query -q 'query { products { id name price } }'
```

### Natural Language Queries
```bash
# Ask questions about the data
tg-invoke-nlp-query -q "Show all products under $50"
```

### Object Queries
```bash
# Direct object queries
tg-invoke-objects-query -c products -t Product
```

## Advanced Features

### Data Transformation

```bash
# Apply transformations during load
tg-load-structured-data -f raw-data.csv \
  --transform "price:number,date:datetime"

# Custom field mapping
tg-load-structured-data -f legacy.csv \
  --field-map "ProductID:id,ProductName:name"
```

### Relationship Detection

```bash
# Auto-detect foreign keys
tg-load-structured-data -f orders.csv \
  --detect-relations

# Specify relationships
tg-load-structured-data -f orders.csv \
  --relation "customer_id:customers.id"
```

### Incremental Loading

```bash
# Load only new records
tg-load-structured-data -f daily-data.csv \
  --incremental --key-field id

# Timestamp-based loading
tg-load-structured-data -f events.csv \
  --incremental --timestamp-field created_at \
  --since "2024-01-01"
```

## Data Types

Supported data types for schema fields:

| Type | Description | Example |
|------|-------------|---------|
| `string` | Text data | "Product Name" |
| `number` | Numeric values | 42.99 |
| `integer` | Whole numbers | 100 |
| `boolean` | True/false | true |
| `date` | Date only | "2024-01-15" |
| `datetime` | Date and time | "2024-01-15T10:30:00Z" |
| `array` | List of values | ["tag1", "tag2"] |
| `object` | Nested structure | {"address": {...}} |

## Performance Considerations

### Large Files

For files over 100MB:

```bash
# Use larger batch sizes
tg-load-structured-data -f large.csv --batch-size 10000

# Enable compression if supported
gzip -c data.csv | tg-load-structured-data -f - --format csv

# Split into chunks
split -l 100000 huge.csv chunk_
for chunk in chunk_*; do
  tg-load-structured-data -f "$chunk"
done
```

### Optimization Tips

1. **Index key fields** for faster queries
2. **Use appropriate batch sizes** based on record size
3. **Validate locally** before loading large datasets
4. **Consider partitioning** very large datasets
5. **Use incremental loading** for regular updates

## Error Handling

### Validation Errors

```bash
$ tg-load-structured-data -f data.csv --validate

Validation Errors:
  Row 10: Invalid date format in field 'created_date'
  Row 25: Missing required field 'id'
  Row 30: Type mismatch in field 'price' (expected number, got string)
```

### Recovery Options

```bash
# Skip invalid records
tg-load-structured-data -f data.csv --skip-errors

# Log errors and continue
tg-load-structured-data -f data.csv \
  --on-error continue \
  --error-log errors.txt

# Stop on first error (default)
tg-load-structured-data -f data.csv --on-error stop
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `TRUSTGRAPH_URL` | Default API URL | `http://localhost:8088/` |
| `TRUSTGRAPH_BATCH_SIZE` | Default batch size | `1000` |
| `TRUSTGRAPH_TEMP_DIR` | Temporary file directory | `/tmp` |

## Exit Codes

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | Error (validation, loading, etc.) |
| 2 | Partial success (some records failed) |

## Limitations

Current limitations (may change in future versions):

- Maximum file size: 2GB (uncompressed)
- Maximum records per collection: 10 million
- Maximum field count: 1000 per schema
- Nested depth limit: 10 levels for JSON/XML

## Troubleshooting

### Schema Detection Issues

If auto-detection fails:
- Ensure consistent data types in columns
- Check for special characters in headers
- Consider creating manual schema

### Memory Issues

For memory errors with large files:
- Reduce batch size
- Process file in chunks
- Increase available memory

### Slow Loading

If loading is slow:
- Increase batch size for small records
- Disable validation for trusted data
- Use parallel loading for multiple files

## Future Enhancements

Planned improvements for this utility:

- Direct database connections (PostgreSQL, MySQL)
- Real-time streaming data support
- Advanced transformation pipelines
- Automatic relationship discovery
- Data quality profiling

## See Also

- [tg-invoke-structured-query](tg-invoke-structured-query) - Query loaded structured data
- [tg-invoke-objects-query](tg-invoke-objects-query) - Query objects in collections
- [tg-invoke-nlp-query](tg-invoke-nlp-query) - Natural language queries
- [Structured Processing Guide](../../guides/structured-processing/) - Complete guide to structured data
