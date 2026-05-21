---
title: tg-show-library-documents
parent: CLI
review_date: 2027-05-21
---

# tg-show-library-documents

Lists all documents stored in the TrustGraph document library with their metadata.

## Synopsis

```bash
tg-show-library-documents [options]
```

## Description

The `tg-show-library-documents` command displays all documents currently stored in TrustGraph's document library. For each document, it shows metadata including ID, timestamp, title, document type, comments, and tags.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-w, --workspace WORKSPACE` | `$TRUSTGRAPH_WORKSPACE` or `default` | Workspace identifier |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### List All Documents
```bash
tg-show-library-documents
```

### List Documents for Specific Workspace
```bash
tg-show-library-documents -w "research-team"
```

## Output Format

The command displays each document in a formatted table:

```
+-------+----------------------------------+
| id    | doc_123456789                    |
| time  | 2023-12-15 10:30:45             |
| title | Technical Manual v2.1           |
| kind  | PDF                              |
| note  | Updated installation procedures  |
| tags  | technical, manual, v2.1          |
+-------+----------------------------------+
```

### Document Properties

- **id**: Unique document identifier
- **time**: Upload/creation timestamp
- **title**: Document title or name
- **kind**: Document type (PDF, DOCX, TXT, etc.)
- **note**: Comments or description
- **tags**: Comma-separated list of tags

If no documents exist, the output is:
```
No documents.
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-add-library-document`](tg-add-library-document) - Add documents to library
- [`tg-remove-library-document`](tg-remove-library-document) - Remove documents from library
- [`tg-start-library-processing`](tg-start-library-processing) - Start document processing
- [`tg-show-library-processing`](tg-show-library-processing) - View processing status

## API Integration


