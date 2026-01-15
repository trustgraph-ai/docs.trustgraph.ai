---
title: tg-show-library-processing
parent: CLI
review_date: 2026-03-12
---

# tg-show-library-processing

Displays all active library document processing records and their details.

## Synopsis

```bash
tg-show-library-processing [options]
```

## Description

The `tg-show-library-processing` command lists all library document processing records, showing the status and details of document processing jobs that have been initiated through the library system.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-U, --user USER` | `trustgraph` | User ID to filter processing records |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Show All Processing Records
```bash
tg-show-library-processing
```

### Show Processing for Specific User
```bash
tg-show-library-processing -U "research-team"
```

## Output Format

The command displays processing records in formatted tables:

```
+----------------+----------------------------------+
| id             | urn:trustgraph:processing:001    |
| document-id    | doc_123456789                    |
| time           | 2023-12-15 14:30:22             |
| flow           | research-processing              |
| collection     | research-docs                    |
| tags           | nlp, research, automated         |
+----------------+----------------------------------+
```

### Field Details

- **id**: Unique processing record identifier (URI)
- **document-id**: ID of the document being processed
- **time**: Timestamp when processing was initiated
- **flow**: Flow instance used for processing
- **collection**: Target collection for processed data
- **tags**: Associated tags for categorization

If no processing records exist, the output is:
```
No processing objects.
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-start-library-processing`](tg-start-library-processing) - Start document processing
- [`tg-stop-library-processing`](tg-stop-library-processing) - Remove processing record
- [`tg-show-library-documents`](tg-show-library-documents) - List library documents
- [`tg-show-flows`](tg-show-flows) - Monitor active flows

## API Integration

This command uses the [Library API](../apis/api-librarian) to retrieve processing records.
