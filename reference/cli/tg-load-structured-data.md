---
title: tg-load-structured-data
parent: CLI
review_date: 2026-05-23
---

# tg-load-structured-data
{: .no_toc }

Load structured data (CSV, JSON, XML) into TrustGraph using AI-assisted schema discovery and descriptor-based transformation.

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Quick Start

```bash
# Fully automatic: Discover schema, generate descriptor, and import data
tg-load-structured-data -i customers.csv --auto

# Preview before importing
tg-load-structured-data -i data.csv --auto --dry-run
```

For more control over the process, see [Manual Workflow](#manual-workflow-step-by-step).

---

## Synopsis

```bash
# Automatic mode
tg-load-structured-data -i INPUT --auto [OPTIONS]

# Manual mode (step-by-step)
tg-load-structured-data -i INPUT --discover-schema [OPTIONS]
tg-load-structured-data -i INPUT --generate-descriptor --schema-name SCHEMA [OPTIONS]
tg-load-structured-data -i INPUT --descriptor FILE --parse-only [OPTIONS]
tg-load-structured-data -i INPUT --descriptor FILE --load [OPTIONS]
```

---

## Description

The `tg-load-structured-data` command loads structured data files into TrustGraph using a multi-phase pipeline that combines AI-assisted schema discovery with descriptor-based data transformation.

### Two Approaches

This tool supports two distinct workflows:

**1. Automated Mode (`--auto`)**:
- One command does everything
- AI discovers the best matching schema
- Automatically generates descriptor configuration
- Parses and imports data
- Best for: Quick imports, prototyping, trusted data sources

**2. Manual Mode (Step-by-Step)**:
- Run each phase individually
- Review and modify generated configurations
- Validate data before importing
- Fine-tune transformations and mappings
- Best for: Production workflows, complex data, quality validation

### The Four Phases

Every data load goes through these phases (automatically or manually):

1. **Discover Schema** - AI analyzes your data sample and identifies the best matching TrustGraph schema
2. **Generate Descriptor** - AI creates a descriptor configuration (JSON) that maps your data fields to the schema
3. **Parse Data** - Apply the descriptor to transform and validate your data
4. **Load Data** - Import the transformed data into TrustGraph

---

## Workflow Modes

### Automated Mode

Run the entire pipeline with a single command:

```bash
tg-load-structured-data -i customers.csv --auto
```

What happens:
1. AI analyzes data sample (500 chars by default)
2. Discovers best matching schema from TrustGraph config
3. Generates descriptor configuration automatically
4. Parses and validates a preview of the data
5. Imports all data to TrustGraph

**Use automated mode when:**
- You want to import data quickly
- Your data structure is straightforward
- You trust the AI's schema selection
- You're prototyping or exploring

**Add `--dry-run` to preview without importing:**
```bash
tg-load-structured-data -i data.csv --auto --dry-run
```

### Manual Mode (Step-by-Step)

Run each phase individually for maximum control:

#### Phase 1: Discover Schema
```bash
tg-load-structured-data -i customers.csv --discover-schema
```

**What it does**: Analyzes your data and recommends which TrustGraph schema best matches

**When to use**: Before generation to understand schema options, or to verify automatic selection

**Output**: Schema name recommendation

#### Phase 2: Generate Descriptor
```bash
tg-load-structured-data -i customers.csv \
  --generate-descriptor \
  --schema-name customer \
  -o descriptor.json
```

**What it does**: Creates a descriptor configuration file that maps your data fields to the target schema

**When to use**: To create a reusable configuration, or to review/modify field mappings before import

**Output**: Descriptor JSON file (save with `-o` or view in console)

#### Phase 3: Parse Data
```bash
tg-load-structured-data -i customers.csv \
  -d descriptor.json \
  --parse-only
```

**What it does**: Applies the descriptor to transform your data without importing

**When to use**: To validate that data transformation works correctly before importing

**Output**: Preview of transformed data

#### Phase 4: Load Data
```bash
tg-load-structured-data -i customers.csv \
  -d descriptor.json \
  --load
```

**What it does**: Transforms and imports data to TrustGraph

**When to use**: After validating with `--parse-only`

**Output**: Import confirmation with record count

**Use manual mode when:**
- You need to review AI-generated configurations
- You want to modify field mappings
- You're setting up production pipelines
- You need to reuse descriptors across similar files
- You require quality validation before import

---

## Options

### Operation Modes (Mutually Exclusive)

| Option | Type | Description | Required |
|--------|------|-------------|----------|
| `--auto` | bool | Run full automatic pipeline | No |
| `--discover-schema` | bool | Analyze data and discover matching schemas | No |
| `--generate-descriptor` | bool | Generate descriptor from data sample | No |
| `--parse-only` | bool | Parse data without importing | No |
| `--load` | bool | Import data using existing descriptor | No |

**Note**: You must specify exactly one operation mode.

### Required Arguments

| Option | Type | Description | Default |
|--------|------|-------------|---------|
| `-i`, `--input` | string | Path to input data file (CSV, JSON, XML) | Required |

### Optional Arguments

| Option | Type | Description | Default |
|--------|------|-------------|---------|
| `-d`, `--descriptor` | string | Path to descriptor JSON file | None (required for `--parse-only` and `--load`) |
| `-o`, `--output` | string | Output file for descriptor or parsed data | None (prints to console) |
| `--schema-name` | string | Target schema for descriptor generation | Auto-discovered |
| `-u`, `--api-url` | string | TrustGraph API URL | `http://localhost:8088/` or `$TRUSTGRAPH_URL` |
| `-f`, `--flow` | string | TrustGraph flow name for prompts | `default` |
| `--user` | string | User name for metadata | `trustgraph` |
| `--collection` | string | Collection name for metadata | `default` |
| `--dry-run` | bool | Preview without importing (auto mode only) | `false` |
| `-v`, `--verbose` | bool | Enable verbose logging | `false` |
| `-t`, `--token` | string | Authentication token | `$TRUSTGRAPH_TOKEN` |

### Sampling Options

| Option | Type | Description | Default | Used In |
|--------|------|-------------|---------|---------|
| `--sample-chars` | int | Max characters to read for AI analysis | 500 | `--discover-schema`, `--generate-descriptor`, `--auto` |
| `--sample-size` | int | Number of records to process | 100 | `--parse-only` |

### Advanced Options

| Option | Type | Description | Default |
|--------|------|-------------|---------|
| `--batch-size` | int | Records per batch during import | 1000 |
| `--max-errors` | int | Maximum errors before stopping | 100 |
| `--error-file` | string | Path to write error records | None |

---

## Examples

### Automated Workflow

#### Basic Automatic Import
```bash
# Fully automatic - discover, generate, and import
tg-load-structured-data -i customers.csv --auto
```

#### Preview Before Importing
```bash
# Dry run to validate without importing
tg-load-structured-data -i large-dataset.csv --auto --dry-run
```

#### Automatic Import with Custom Flow
```bash
# Use specific flow for prompts and import
tg-load-structured-data -i products.json \
  --auto \
  --flow production \
  --collection products-2024
```

#### Larger Sample for Better Analysis
```bash
# Use more data for schema discovery and descriptor generation
tg-load-structured-data -i complex-data.csv \
  --auto \
  --sample-chars 2000
```

### Manual Workflow Examples

#### Complete Manual Workflow
```bash
# Step 1: Discover which schema matches your data
tg-load-structured-data -i customers.csv --discover-schema

# Output: Best matching schema: customer

# Step 2: Generate descriptor configuration
tg-load-structured-data -i customers.csv \
  --generate-descriptor \
  --schema-name customer \
  -o customer-descriptor.json

# Step 3: Preview parsed data
tg-load-structured-data -i customers.csv \
  -d customer-descriptor.json \
  --parse-only

# Step 4: Import to TrustGraph
tg-load-structured-data -i customers.csv \
  -d customer-descriptor.json \
  --load
```

#### Just Discover Schema
```bash
# Find out which schema matches without generating descriptor
tg-load-structured-data -i mystery-data.csv --discover-schema

# Use larger sample for better matching
tg-load-structured-data -i complex.xml \
  --discover-schema \
  --sample-chars 1000
```

#### Generate and Save Descriptor
```bash
# Generate descriptor and save for reuse
tg-load-structured-data -i sample.csv \
  --generate-descriptor \
  --schema-name product \
  -o product-descriptor.json

# View descriptor instead of saving
tg-load-structured-data -i sample.csv \
  --generate-descriptor \
  --schema-name product
```

#### Parse Without Importing
```bash
# Validate transformation with small sample
tg-load-structured-data -i data.csv \
  -d descriptor.json \
  --parse-only \
  --sample-size 50

# Save parsed output for inspection
tg-load-structured-data -i data.csv \
  -d descriptor.json \
  --parse-only \
  -o parsed-output.json
```

### Format-Specific Examples

#### CSV Files
```bash
# Standard CSV with header row
tg-load-structured-data -i customers.csv --auto

# The descriptor handles delimiter, encoding, header detection
# No need to specify these manually - AI figures it out
```

#### JSON Files
```bash
# JSON array
tg-load-structured-data -i products.json --auto

# Newline-delimited JSON (JSONL)
tg-load-structured-data -i events.jsonl --auto
```

#### XML Files
```bash
# XML with repeating record elements
tg-load-structured-data -i catalog.xml --auto

# Complex XML structure
tg-load-structured-data -i data.xml \
  --generate-descriptor \
  --schema-name record \
  -o xml-descriptor.json
```

### Production Workflows

#### Reusable Descriptor
```bash
# Create descriptor once
tg-load-structured-data -i sample-customers.csv \
  --generate-descriptor \
  --schema-name customer \
  -o customer-descriptor.json

# Reuse for multiple files
for file in daily-exports/*.csv; do
  tg-load-structured-data -i "$file" \
    -d customer-descriptor.json \
    --load
done
```

#### Validate Before Import
```bash
# Always validate first in production
tg-load-structured-data -i production-data.csv \
  -d descriptor.json \
  --parse-only

# Review output, then import
tg-load-structured-data -i production-data.csv \
  -d descriptor.json \
  --load
```

#### Custom Collection and User
```bash
# Import to specific collection with metadata
tg-load-structured-data -i quarterly-sales.csv \
  --auto \
  --collection sales-q1-2024 \
  --user analytics-team \
  --flow production
```

---

## Descriptor Files

Descriptor files are JSON configurations that define how to transform your data. They are automatically generated by the `--generate-descriptor` phase but can be manually edited for custom transformations.

### Descriptor Structure

```json
{
  "format": {
    "type": "csv",
    "encoding": "utf-8",
    "options": {
      "delimiter": ",",
      "has_header": true
    }
  },
  "mappings": [
    {
      "source_field": "customer_id",
      "target_field": "id",
      "transforms": [
        {"type": "trim"}
      ]
    },
    {
      "source_field": "customer_name",
      "target_field": "name",
      "transforms": [
        {"type": "trim"},
        {"type": "title_case"}
      ]
    },
    {
      "source_field": "total_purchases",
      "target_field": "purchase_count",
      "transforms": [
        {"type": "to_int"}
      ]
    }
  ],
  "output": {
    "schema_name": "customer",
    "options": {
      "batch_size": 1000,
      "confidence": 0.9
    }
  }
}
```

### Format Section

Defines the input file format:

**CSV Options:**
```json
{
  "format": {
    "type": "csv",
    "encoding": "utf-8",
    "options": {
      "delimiter": ",",
      "has_header": true
    }
  }
}
```

**JSON Options:**
```json
{
  "format": {
    "type": "json",
    "encoding": "utf-8",
    "options": {
      "root_path": "$.data"
    }
  }
}
```

**XML Options:**
```json
{
  "format": {
    "type": "xml",
    "encoding": "utf-8",
    "options": {
      "record_path": "//record",
      "field_attribute": "name"
    }
  }
}
```

### Mappings Section

Defines how source fields map to target fields:

```json
{
  "source_field": "input_column_name",
  "target_field": "schema_field_name",
  "transforms": [
    {"type": "transform_type"}
  ]
}
```

**Available Transforms:**
- `trim` - Remove leading/trailing whitespace
- `upper` - Convert to uppercase
- `lower` - Convert to lowercase
- `title_case` - Convert to title case
- `to_int` - Convert to integer
- `to_float` - Convert to float

### Output Section

Defines the target schema and import options:

```json
{
  "output": {
    "schema_name": "customer",
    "options": {
      "batch_size": 1000,
      "confidence": 0.9
    }
  }
}
```

### Editing Descriptors

You can manually edit generated descriptors to:
- Change field mappings
- Add or remove transformations
- Adjust batch size
- Modify confidence scores
- Fine-tune format parsing options

```bash
# Generate descriptor
tg-load-structured-data -i data.csv \
  --generate-descriptor \
  --schema-name customer \
  -o descriptor.json

# Edit descriptor.json manually to customize transformations

# Test your changes
tg-load-structured-data -i data.csv \
  -d descriptor.json \
  --parse-only

# Import with customized descriptor
tg-load-structured-data -i data.csv \
  -d descriptor.json \
  --load
```

---

## Decision Guide: Automated vs Manual Mode

### When to Use Automated Mode

✅ **Use `--auto` when:**
- Data structure is straightforward
- You're exploring or prototyping
- Quick import is more important than customization
- You trust AI-generated configurations
- Data source is trusted and consistent

### When to Use Manual Mode

✅ **Use step-by-step when:**
- You need to review AI-generated configurations
- Data requires custom transformations
- Setting up production data pipelines
- Multiple files share the same structure (reuse descriptor)
- Quality validation is critical
- You want to understand the transformation process
- Data has unusual formatting or structure

### Workflow Comparison

| Feature | Automated (`--auto`) | Manual (Step-by-Step) |
|---------|---------------------|----------------------|
| **Commands** | 1 command | 4 commands (or fewer) |
| **Control** | Minimal | Maximum |
| **Speed** | Fastest | Slower but thorough |
| **Validation** | Preview only (with `--dry-run`) | Validate each phase |
| **Customization** | None | Full descriptor editing |
| **Reusability** | None | Save and reuse descriptors |
| **Best for** | Prototyping, exploration | Production, quality control |

---

## Output Format

### Discover Schema Output

```
Best matching schema: customer
```

Or for multiple matches:
```
Multiple schemas found:
  - customer
  - person
  - contact
```

### Generate Descriptor Output

JSON descriptor configuration (to console or file via `-o`):
```json
{
  "format": {...},
  "mappings": [...],
  "output": {...}
}
```

### Parse-Only Output

Preview of transformed data:
```
Parsed Data Preview:
==================================================
Record 1:
{
  "metadata": {...},
  "schema_name": "customer",
  "values": {
    "id": "C001",
    "name": "John Doe",
    "email": "john@example.com"
  },
  "confidence": 0.9
}

... and 97 more records
Total records processed: 100

Parsing Summary:
- Input format: csv
- Records processed: 100
- Target schema: customer
- Field mappings: 3
```

### Load Output

Import confirmation:
```
🚀 Importing 1000 records to TrustGraph...

📊 Import Summary:
- Total records: 1000
- Successfully imported: 1000
✅ All records imported successfully!

🎉 Load Complete!
- Input format: csv
- Target schema: customer
- Records imported: 1000
- Flow used: default
```

### Auto Mode Output

Complete pipeline output:
```
🚀 Starting automatic pipeline for customers.csv...
Step 1: Analyzing data to discover best matching schema...
🎯 Auto-selected schema: customer

Step 2: Generating descriptor configuration...
📝 Generated descriptor configuration

Step 3: Parsing and validating data...
📊 Data Preview (first few records):
==================================================
Record 1: {'id': 'C001', 'name': 'John Doe'}
Record 2: {'id': 'C002', 'name': 'Jane Smith'}
Record 3: {'id': 'C003', 'name': 'Bob Johnson'}
==================================================

Step 4: Importing data to TrustGraph...
🚀 Importing data to TrustGraph...

📊 Import Summary:
- Total records: 1000
- Successfully imported: 1000
✅ All records imported successfully!

🎉 Auto-Import Complete!
- Input format: csv
- Target schema: customer
- Records imported: 1000
- Flow used: default
```

---

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `TRUSTGRAPH_URL` | Default API URL | `http://localhost:8088/` |
| `TRUSTGRAPH_TOKEN` | Authentication token | None |

**Example:**
```bash
export TRUSTGRAPH_URL=https://trustgraph.example.com
export TRUSTGRAPH_TOKEN=your-auth-token

tg-load-structured-data -i data.csv --auto
```

---

## Exit Codes

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | Error (file not found, invalid descriptor, import failed, etc.) |

---

## Error Handling

### Common Errors

#### Input File Not Found
```
Error: Input file not found: customers.csv
```

**Solution:** Verify file path exists

#### Descriptor Required
```
Error: --descriptor is required when using --parse-only
```

**Solution:** Provide descriptor file with `-d descriptor.json`

#### Operation Mode Required
```
Error: Must specify an operation mode
Available modes:
  --auto                 : Discover schema + generate descriptor + import
  --discover-schema       : Analyze data and discover schemas
  --generate-descriptor  : Generate descriptor from data
  --parse-only          : Parse data without importing
  --load                : Import data using existing descriptor
```

**Solution:** Choose one operation mode

#### Schema Discovery Failed
```
❌ Could not automatically determine the best schema for your data.
💡 Try running with --discover-schema first to see available options.
```

**Solution:**
- Verify schemas exist: `tg-list-config-items schema`
- Try larger sample: `--sample-chars 2000`
- Manually specify schema: `--schema-name customer`

#### Descriptor Generation Failed
```
Error: Could not determine schema automatically.
Please specify a schema using --schema-name or run --discover-schema first.
```

**Solution:** Run `--discover-schema` first or specify `--schema-name`

#### Invalid JSON Descriptor
```
Error: Invalid JSON in descriptor - Expecting value: line 1 column 1 (char 0)
```

**Solution:** Validate descriptor JSON syntax

#### Import Failed
```
Import failed: Connection refused
```

**Solution:** Verify TrustGraph API is running at specified URL

---

## Best Practices

### 1. Always Validate in Production

```bash
# Don't do this in production:
tg-load-structured-data -i production.csv --auto

# Do this instead:
tg-load-structured-data -i production.csv --auto --dry-run
# Review output, then:
tg-load-structured-data -i production.csv --auto
```

### 2. Reuse Descriptors for Consistency

```bash
# Create descriptor from sample
tg-load-structured-data -i sample.csv \
  --generate-descriptor \
  --schema-name customer \
  -o customer-descriptor.json

# Reuse for all similar files
tg-load-structured-data -i daily-import.csv -d customer-descriptor.json --load
```

### 3. Use Manual Mode for Production Pipelines

```bash
# Production workflow
tg-load-structured-data -i data.csv --discover-schema
tg-load-structured-data -i data.csv --generate-descriptor --schema-name X -o desc.json
# Edit desc.json if needed
tg-load-structured-data -i data.csv -d desc.json --parse-only
tg-load-structured-data -i data.csv -d desc.json --load
```

### 4. Use Larger Samples for Complex Data

```bash
# Default sample may not capture complexity
tg-load-structured-data -i complex.csv --auto --sample-chars 500

# Better for complex data
tg-load-structured-data -i complex.csv --auto --sample-chars 5000
```

### 5. Organize Descriptors

```bash
# Keep descriptors in version control
mkdir -p config/descriptors
tg-load-structured-data -i sample.csv \
  --generate-descriptor \
  --schema-name customer \
  -o config/descriptors/customer-v1.json
```

### 6. Use Verbose Mode for Debugging

```bash
# Add -v to see detailed logging
tg-load-structured-data -i data.csv --auto -v
```

---

## Performance Characteristics

### Sample Size Impact

- **`--sample-chars`**: Affects AI analysis quality and speed
  - Smaller (500): Faster, may miss patterns
  - Larger (5000): Slower, better pattern detection
  - Used in: `--discover-schema`, `--generate-descriptor`, `--auto`

- **`--sample-size`**: Affects parse preview size
  - Only used in `--parse-only` mode
  - Does not affect import (`--load` processes all records)

### Import Performance

- Default batch size: 1000 records
- Configurable in descriptor: `output.options.batch_size`
- Larger batches: Faster import, more memory
- Smaller batches: Slower import, less memory

### File Size Considerations

- **Small files (<1MB)**: Use `--auto` for convenience
- **Medium files (1-100MB)**: Use `--auto` with `--dry-run` first
- **Large files (>100MB)**: Use manual mode with validation

---

## Related Commands

- [`tg-list-config-items`](tg-list-config-items) - List available schemas
- [`tg-put-config-item`](tg-put-config-item) - Add custom schemas
- [`tg-show-config`](tg-show-config) - View TrustGraph configuration

---

## API Integration

This command uses the following TrustGraph APIs:

- **Config API** - Retrieve and validate schemas
- **Flow/Prompt API** - AI-powered schema discovery and descriptor generation
- **Bulk Import API** - Import transformed data

Prompts used:
- `schema-selection` - Discovers matching schemas
- `diagnose-structured-data` - Generates descriptor configurations

---

## Notes

### Supported Formats

- **CSV**: Comma-separated values with customizable delimiters
- **JSON**: JSON arrays, single objects, or newline-delimited JSON
- **XML**: XML with repeating record elements

### AI-Powered Features

Schema discovery and descriptor generation use AI prompts configured in your TrustGraph flow. Results depend on:
- Available schemas in TrustGraph config
- Quality and size of data sample
- Prompt configuration in the flow

### Data Transformation

All transformations happen via the descriptor file. The tool:
1. Parses raw data according to format specification
2. Applies field mappings and transformations
3. Converts to TrustGraph `ExtractedObject` format
4. Imports via bulk API

### Limitations

- Schema must exist in TrustGraph config before import
- All field values converted to strings in `ExtractedObject.values`
- Transformations are basic; complex logic requires custom preprocessing
- XML parsing uses ElementTree (limited XPath support)

---

## See Also

For more information on structured data processing:
- [Structured Data Guide](../../guides/structured-processing/) - Complete guide
- [Descriptor Format Specification](../../tech-specs/structured-data-descriptor) - Detailed descriptor reference
