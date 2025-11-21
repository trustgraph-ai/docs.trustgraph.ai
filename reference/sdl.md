---
title: Structure Descriptor Language (SDL)
parent: Reference
nav_order: 6
permalink: /reference/sdl
review_date: 2026-02-01
---

# Structure Descriptor Language (SDL)

The TrustGraph Structure Descriptor Language (SDL) is a JSON-based configuration language that describes how to parse, transform, and import structured data into TrustGraph. It provides a declarative approach to data ingestion, supporting multiple input formats and complex transformation pipelines without requiring custom code.

## Overview

SDL enables you to:
- **Import multiple formats** - CSV, JSON, XML, Excel, Parquet, and fixed-width files
- **Transform data** - Clean, normalize, and convert data types during import
- **Validate data** - Apply quality checks and constraints
- **Handle errors** - Configure how to deal with invalid data
- **Enrich data** - Use lookup tables and calculated fields

## Basic Structure

Every SDL configuration has this top-level structure:

```json
{
  "version": "1.0",
  "metadata": { ... },
  "format": { ... },
  "globals": { ... },
  "preprocessing": [ ... ],
  "mappings": [ ... ],
  "postprocessing": [ ... ],
  "output": { ... }
}
```

### Required Sections

| Section | Description |
|---------|-------------|
| `version` | SDL specification version (currently "1.0") |
| `format` | Input data format and parsing options |
| `mappings` | Field-by-field mapping from source to target |
| `output` | Output configuration for TrustGraph |

### Optional Sections

| Section | Description |
|---------|-------------|
| `metadata` | Configuration information (name, author, etc.) |
| `globals` | Variables, constants, and lookup tables |
| `preprocessing` | Operations applied before field mapping |
| `postprocessing` | Operations applied after field mapping |

## Format Definition

The `format` section describes the input data format and parsing options:

```json
{
  "format": {
    "type": "csv|json|xml|fixed-width|excel|parquet",
    "encoding": "utf-8",
    "options": {
      // Format-specific options
    }
  }
}
```

### CSV Format

```json
{
  "format": {
    "type": "csv",
    "encoding": "utf-8",
    "options": {
      "delimiter": ",",
      "quote_char": "\"",
      "escape_char": "\\",
      "skip_rows": 1,
      "has_header": true,
      "null_values": ["", "NULL", "null", "N/A"]
    }
  }
}
```

**CSV Options:**

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `delimiter` | string | `","` | Field separator character |
| `quote_char` | string | `"\""` | Character used to quote fields |
| `escape_char` | string | `"\\"` | Character used to escape quotes |
| `skip_rows` | integer | `0` | Number of rows to skip at start |
| `has_header` | boolean | `true` | First row contains column names |
| `null_values` | array | `[""]` | Values to treat as null |

### JSON Format

```json
{
  "format": {
    "type": "json",
    "options": {
      "root_path": "$.data",
      "array_mode": "records",
      "flatten": false
    }
  }
}
```

**JSON Options:**

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `root_path` | string | `"$"` | JSONPath to array of records |
| `array_mode` | string | `"records"` | How to handle arrays: `records` or `single` |
| `flatten` | boolean | `false` | Flatten nested objects |

### XML Format

```json
{
  "format": {
    "type": "xml",
    "options": {
      "root_element": "//records/record",
      "namespaces": {
        "ns": "http://example.com/namespace"
      }
    }
  }
}
```

**XML Options:**

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `root_element` | string | Required | XPath to record elements |
| `namespaces` | object | `{}` | Namespace prefixes and URIs |

## Global Settings

The `globals` section defines lookup tables, variables, and constants used throughout the configuration:

```json
{
  "globals": {
    "variables": {
      "current_date": "2024-01-01",
      "batch_id": "BATCH_001",
      "default_confidence": 0.8
    },
    "lookup_tables": {
      "country_codes": {
        "US": "United States",
        "UK": "United Kingdom",
        "CA": "Canada"
      },
      "status_mapping": {
        "1": "active",
        "0": "inactive"
      }
    },
    "constants": {
      "source_system": "legacy_crm",
      "import_type": "full"
    }
  }
}
```

**Usage in expressions:**
- Variables: `${current_date}`
- Constants: `${source_system}`
- Lookup tables: Used with `lookup` transform

## Field Mappings

The `mappings` section defines how source data maps to target fields:

```json
{
  "mappings": [
    {
      "target_field": "person_name",
      "source": "$.name",
      "transforms": [
        {"type": "trim"},
        {"type": "title_case"},
        {"type": "required"}
      ],
      "validation": [
        {"type": "min_length", "value": 2},
        {"type": "max_length", "value": 100}
      ]
    }
  ]
}
```

### Mapping Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `target_field` | string | Yes | Name of the target field |
| `source` | string | Yes | Source path expression |
| `transforms` | array | No | List of transformations to apply |
| `validation` | array | No | List of validation rules |

### Source Path Expressions

Different formats use different path expression languages:

| Format | Example | Description |
|--------|---------|-------------|
| CSV | `"customer_name"` or `"[2]"` | Column name or index |
| JSON | `"$.user.profile.email"` | JSONPath expression |
| XML | `"//product[@id='123']/price"` | XPath expression |
| Fixed-width | `"customer_name"` | Field name from definition |

## Transformations

Transforms are applied to field values in the order specified:

### String Transforms

```json
{"type": "trim"}                                    // Remove whitespace
{"type": "upper"}                                   // Convert to uppercase
{"type": "lower"}                                   // Convert to lowercase  
{"type": "title_case"}                              // Title Case Format
{"type": "replace", "pattern": "old", "replacement": "new"}
{"type": "regex_replace", "pattern": "\\d+", "replacement": "XXX"}
{"type": "substring", "start": 0, "end": 10}       // Extract substring
{"type": "pad_left", "length": 10, "char": "0"}    // Pad with characters
```

### Type Conversions

```json
{"type": "to_string"}                               // Convert to string
{"type": "to_int"}                                  // Convert to integer
{"type": "to_float"}                                // Convert to float
{"type": "to_bool"}                                 // Convert to boolean
{"type": "to_date", "format": "YYYY-MM-DD"}        // Parse date
{"type": "parse_json"}                              // Parse JSON string
```

### Data Operations

```json
{"type": "default", "value": "default_value"}      // Set default if null
{"type": "lookup", "table": "table_name"}          // Lookup in table
{"type": "concat", "values": ["field1", " - ", "field2"]}
{"type": "calculate", "expression": "${field1} + ${field2}"}
{"type": "conditional", 
 "condition": "${age} > 18", 
 "true_value": "adult", 
 "false_value": "minor"}
```

### Expression Syntax

Expressions use `${}` syntax to reference:
- Current field value: `${.}`
- Other fields: `${field_name}`
- Variables: `${variable_name}`

**Examples:**
```json
{"type": "calculate", "expression": "${price} * 1.1"}
{"type": "conditional", "condition": "${status} == 'active'", "true_value": "yes", "false_value": "no"}
```

## Validation Rules

Validation rules check data quality and can trigger error handling:

### Basic Validations

```json
{"type": "required"}                                // Field must have value
{"type": "not_null"}                               // Field cannot be null
{"type": "min_length", "value": 5}                // Minimum string length
{"type": "max_length", "value": 100}              // Maximum string length
{"type": "range", "min": 0, "max": 1000}          // Numeric range
{"type": "pattern", "value": "^[A-Z]{2,3}$"}      // Regex pattern
{"type": "in_list", "values": ["active", "inactive", "pending"]}
```

### Custom Validations

```json
{
  "type": "custom",
  "expression": "${age} >= 18 && ${country} == 'US'",
  "message": "Must be 18+ and in US"
}
```

```json
{
  "type": "cross_field",
  "fields": ["start_date", "end_date"],
  "expression": "${start_date} < ${end_date}",
  "message": "Start date must be before end date"
}
```

## Preprocessing and Postprocessing

### Preprocessing

Operations applied to all records before field mapping:

```json
{
  "preprocessing": [
    {
      "type": "filter",
      "condition": "${status} != 'deleted'"
    },
    {
      "type": "sort",
      "field": "created_date",
      "order": "asc"
    }
  ]
}
```

### Postprocessing

Operations applied to all records after field mapping:

```json
{
  "postprocessing": [
    {
      "type": "deduplicate",
      "key_fields": ["email", "phone"]
    },
    {
      "type": "aggregate",
      "group_by": ["country"],
      "functions": {
        "total_count": {"type": "count"},
        "avg_age": {"type": "avg", "field": "age"}
      }
    }
  ]
}
```

## Output Configuration

The `output` section configures how processed data is saved:

```json
{
  "output": {
    "format": "trustgraph-objects",
    "schema_name": "person",
    "options": {
      "batch_size": 1000,
      "confidence": 0.9,
      "source_span_field": "raw_text",
      "metadata": {
        "source": "crm_import",
        "version": "1.0"
      }
    },
    "error_handling": {
      "on_validation_error": "skip",
      "on_transform_error": "default",
      "max_errors": 100,
      "error_output": "errors.json"
    }
  }
}
```

### Output Options

| Option | Type | Description |
|--------|------|-------------|
| `format` | string | Always "trustgraph-objects" |
| `schema_name` | string | Target schema name |
| `batch_size` | integer | Records per batch |
| `confidence` | float | Confidence score (0.0-1.0) |
| `metadata` | object | Additional metadata to include |

### Error Handling

| Option | Values | Description |
|--------|--------|-------------|
| `on_validation_error` | `skip`, `fail`, `log` | What to do when validation fails |
| `on_transform_error` | `skip`, `fail`, `default` | What to do when transform fails |
| `max_errors` | integer | Maximum errors before stopping |
| `error_output` | string | File to write error details |

## Complete Example

Here's a complete SDL configuration for importing customer data from CSV:

```json
{
  "version": "1.0",
  "metadata": {
    "name": "Customer Import from CRM CSV",
    "description": "Imports customer data from legacy CRM system",
    "author": "Data Team",
    "created": "2024-01-01T00:00:00Z"
  },
  "format": {
    "type": "csv",
    "encoding": "utf-8",
    "options": {
      "delimiter": ",",
      "has_header": true,
      "skip_rows": 1,
      "null_values": ["", "NULL", "N/A"]
    }
  },
  "globals": {
    "variables": {
      "import_date": "2024-01-01",
      "default_confidence": 0.85
    },
    "lookup_tables": {
      "country_codes": {
        "US": "United States",
        "CA": "Canada", 
        "UK": "United Kingdom"
      },
      "status_codes": {
        "1": "active",
        "0": "inactive"
      }
    }
  },
  "preprocessing": [
    {
      "type": "filter",
      "condition": "${status} != ''"
    }
  ],
  "mappings": [
    {
      "target_field": "full_name",
      "source": "customer_name",
      "transforms": [
        {"type": "trim"},
        {"type": "title_case"}
      ],
      "validation": [
        {"type": "required"},
        {"type": "min_length", "value": 2},
        {"type": "max_length", "value": 100}
      ]
    },
    {
      "target_field": "email",
      "source": "email_address", 
      "transforms": [
        {"type": "trim"},
        {"type": "lower"}
      ],
      "validation": [
        {"type": "pattern", "value": "^[\\w.-]+@[\\w.-]+\\.[a-zA-Z]{2,}$"}
      ]
    },
    {
      "target_field": "age",
      "source": "age",
      "transforms": [
        {"type": "to_int"},
        {"type": "default", "value": 0}
      ],
      "validation": [
        {"type": "range", "min": 0, "max": 120}
      ]
    },
    {
      "target_field": "country",
      "source": "country_code",
      "transforms": [
        {"type": "lookup", "table": "country_codes"},
        {"type": "default", "value": "Unknown"}
      ]
    },
    {
      "target_field": "status",
      "source": "status",
      "transforms": [
        {"type": "lookup", "table": "status_codes"},
        {"type": "default", "value": "unknown"}
      ]
    }
  ],
  "postprocessing": [
    {
      "type": "deduplicate",
      "key_fields": ["email"]
    }
  ],
  "output": {
    "format": "trustgraph-objects",
    "schema_name": "customer",
    "options": {
      "confidence": "${default_confidence}",
      "batch_size": 500,
      "metadata": {
        "import_date": "${import_date}",
        "source": "legacy_crm"
      }
    },
    "error_handling": {
      "on_validation_error": "log",
      "on_transform_error": "default",
      "max_errors": 50,
      "error_output": "customer_import_errors.json"
    }
  }
}
```

## Usage with TrustGraph

SDL configurations are used with the `tg-load-structured-data` command:

```bash
# Use SDL configuration file
tg-load-structured-data -f data.csv -d config.json -c customers

# Generate SDL from sample data
tg-load-structured-data -f data.csv -s auto -c customers --save-config config.json
```

## Best Practices

### 1. Start Simple

Begin with basic field mappings and add complexity incrementally:

```json
{
  "mappings": [
    {
      "target_field": "name",
      "source": "customer_name",
      "transforms": [{"type": "trim"}]
    }
  ]
}
```

### 2. Use Descriptive Names

Choose clear names for target fields and include metadata:

```json
{
  "metadata": {
    "name": "Customer Import - Legacy CRM System",
    "description": "Imports customer records from CSV export of legacy CRM",
    "version": "1.2"
  }
}
```

### 3. Handle Data Quality

Include validation and error handling:

```json
{
  "validation": [
    {"type": "required"},
    {"type": "pattern", "value": "^[\\w.-]+@[\\w.-]+\\.[a-zA-Z]{2,}$"}
  ]
}
```

### 4. Use Lookup Tables

Define lookup tables for code-to-value mappings:

```json
{
  "globals": {
    "lookup_tables": {
      "department_codes": {
        "ENG": "Engineering",
        "SALES": "Sales",
        "MKT": "Marketing"
      }
    }
  }
}
```

### 5. Test with Small Datasets

Validate your configuration with a small sample before processing large files.

### 6. Document Complex Logic

Use comments in metadata to explain complex transformations:

```json
{
  "metadata": {
    "description": "Age calculation: Uses birth_date if available, otherwise uses age_years field with ${current_date} as reference"
  }
}
```

## Error Handling

SDL provides several levels of error handling:

### Transform Errors
When a transformation fails (e.g., converting "abc" to integer):
- `skip`: Skip the record entirely
- `fail`: Stop processing with error
- `default`: Use the field's default value

### Validation Errors
When validation rules fail:
- `skip`: Skip the record entirely
- `fail`: Stop processing with error  
- `log`: Log error but continue processing

### Error Output
All errors are logged to the specified error output file with details:
- Record number
- Field name
- Error type and message
- Original value

## See Also

- [tg-load-structured-data](../cli/tg-load-structured-data) - Command-line tool for using SDL
- [Structured Data Processing](../guides/structured-processing/) - Tutorial on working with structured data
- [Object Storage API](../apis/api-object-storage) - API for managing structured objects
