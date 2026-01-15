---
title: tg-load-structured-data
parent: CLI
review_date: 2026-05-23
---

# tg-load-structured-data

Load structured data (CSV, JSON, XML) into TrustGraph using AI-assisted schema discovery and descriptor-based transformation.

## Synopsis

```bash
# Automatic mode
tg-load-structured-data -i INPUT --auto [options]

# Manual mode (step-by-step)
tg-load-structured-data -i INPUT --discover-schema [options]
tg-load-structured-data -i INPUT --generate-descriptor --schema-name SCHEMA [options]
tg-load-structured-data -i INPUT --descriptor FILE --parse-only [options]
tg-load-structured-data -i INPUT --descriptor FILE --load [options]
```

## Description

The `tg-load-structured-data` command loads structured data files into TrustGraph using a multi-phase pipeline that combines AI-assisted schema discovery with descriptor-based data transformation.

### Workflow Modes

**Automated Mode (`--auto`)**:
- One command does everything
- AI discovers the best matching schema
- Automatically generates descriptor configuration
- Parses and imports data

**Manual Mode (Step-by-Step)**:
- Run each phase individually
- Review and modify generated configurations
- Validate data before importing
- Fine-tune transformations and mappings

### The Four Phases

1. **Discover Schema** - AI analyzes data and identifies the best matching TrustGraph schema
2. **Generate Descriptor** - Creates descriptor configuration (JSON) that maps data fields to schema
3. **Parse Data** - Applies descriptor to transform and validate data
4. **Load Data** - Imports transformed data into TrustGraph

## Options

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --input FILE` | Input data file (CSV, JSON, XML) |
| `-u, --url URL` | TrustGraph API URL (default: `$TRUSTGRAPH_URL` or `http://localhost:8088/`) |
| `-t, --token TOKEN` | Authentication token (default: `$TRUSTGRAPH_TOKEN`) |
| `-f, --flow-id ID` | Flow instance ID (default: `default`) |
| `-U, --user USER` | User ID (default: `trustgraph`) |
| `-C, --collection COLLECTION` | Collection to assign data (default: `default`) |

### Mode-Specific Options

| Option | Description |
|--------|-------------|
| `--auto` | Automatic mode - run all phases |
| `--discover-schema` | Phase 1: Discover best schema |
| `--generate-descriptor` | Phase 2: Generate descriptor |
| `--parse-only` | Phase 3: Parse data without importing |
| `--load` | Phase 4: Load data into TrustGraph |
| `--dry-run` | Preview without importing |
| `-d, --descriptor FILE` | Descriptor configuration file |
| `--schema-name NAME` | Schema name to use |
| `-o, --output FILE` | Output file for descriptor |
| `--sample-size SIZE` | Data sample size for analysis (default: 500) |

## Examples

### Automated Mode

```bash
# Fully automatic import
tg-load-structured-data -i customers.csv --auto

# Preview before importing
tg-load-structured-data -i data.csv --auto --dry-run

# Auto with custom collection
tg-load-structured-data -i products.json --auto -C "products"
```

### Manual Mode

```bash
# Phase 1: Discover schema
tg-load-structured-data -i customers.csv --discover-schema

# Phase 2: Generate descriptor
tg-load-structured-data -i customers.csv \
  --generate-descriptor \
  --schema-name customer \
  -o descriptor.json

# Phase 3: Parse and validate
tg-load-structured-data -i customers.csv \
  -d descriptor.json \
  --parse-only

# Phase 4: Load data
tg-load-structured-data -i customers.csv \
  -d descriptor.json \
  --load
```

### Supported File Formats

```bash
# CSV
tg-load-structured-data -i data.csv --auto

# JSON (array of objects)
tg-load-structured-data -i data.json --auto

# XML
tg-load-structured-data -i data.xml --auto
```

## Descriptor Configuration

The descriptor is a JSON configuration that defines how to map your data to a TrustGraph schema:

```json
{
  "schema": "customer",
  "fields": {
    "name": "customer_name",
    "email": "contact_email",
    "phone": "phone_number"
  },
  "transformations": {
    "phone": "normalize_phone"
  }
}
```

You can generate descriptors automatically or create them manually for complex mappings.

## Workflow Decision Guide

**Use Automatic Mode When:**
- Quick imports needed
- Straightforward data structure
- Prototyping or exploring
- Trust AI schema selection

**Use Manual Mode When:**
- Production workflows
- Complex data requiring validation
- Need to review/modify mappings
- Custom transformation logic needed
- Quality assurance required

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-load-knowledge`](tg-load-knowledge) - Load RDF triples
- [`tg-load-pdf`](tg-load-pdf) - Load PDF documents
- [`tg-show-parameter-types`](tg-show-parameter-types) - View available schemas

## API Integration

This command uses the [Structured Data Load API](../apis/api-text-load) and [NLP Query API](../apis/api-nlp-query) for schema discovery and data transformation.
