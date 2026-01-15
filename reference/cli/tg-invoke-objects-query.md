---
title: tg-invoke-objects-query
parent: CLI
review_date: 2026-03-05
---

# tg-invoke-objects-query

Query and retrieve objects stored in the TrustGraph object storage system.

## Synopsis

```bash
tg-invoke-objects-query -c COLLECTION [options]
```

## Description

The `tg-invoke-objects-query` command queries objects stored in TrustGraph's object storage. Objects are structured data entities extracted from documents or imported directly. Supports filtering, pagination, and multiple output formats.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-c, --collection COLLECTION` | Collection name to query |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-T, --type TYPE` | All types | Filter by object type |
| `-q, --query QUERY` | None | Query filter (JSON format) |
| `-l, --limit N` | `100` | Maximum number of results |
| `-o, --offset N` | `0` | Skip first N results |
| `--format FORMAT` | `table` | Output format: `table`, `json`, `jsonl` |
| `--fields FIELDS` | All fields | Comma-separated list of fields to include |

## Examples

### Basic Query
```bash
tg-invoke-objects-query -c products
```

### Filter by Type
```bash
tg-invoke-objects-query -c customers --type Customer
```

### JSON Output
```bash
tg-invoke-objects-query -c orders --format json
```

### With Pagination
```bash
tg-invoke-objects-query -c products --limit 50 --offset 100
```

### Specific Fields
```bash
tg-invoke-objects-query -c customers --fields "id,name,email" --format table
```

## Output Formats

| Format | Description | Use Case |
|--------|-------------|----------|
| `table` | Formatted table (default) | Human-readable viewing |
| `json` | Complete JSON response | API integration, analysis |
| `jsonl` | One object per line | Streaming, large datasets |

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-load-structured-data`](tg-load-structured-data) - Import structured data as objects
- [`tg-set-collection`](tg-set-collection) - Create or configure collections

## API Integration

This command uses the Objects Query API to retrieve structured data entities from TrustGraph collections.
