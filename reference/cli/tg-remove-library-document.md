---
title: tg-remove-library-document
parent: CLI
review_date: 2025-12-04
---

# tg-remove-library-document

Removes a document from the TrustGraph document library.

## Synopsis

```bash
tg-remove-library-document --id DOCUMENT_ID [options]
```

## Description

The `tg-remove-library-document` command permanently removes a document from TrustGraph's document library. This operation deletes the document metadata and content.

**Warning**: This operation is permanent and cannot be undone.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--identifier, --id ID` | Document ID to remove |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-U, --user USER` | `trustgraph` | User ID |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Remove a Document
```bash
tg-remove-library-document --id "doc_123456789"
```

### Remove with Custom User
```bash
tg-remove-library-document --id "doc_987654321" -U "research-team"
```

## Notes

Use [`tg-show-library-documents`](tg-show-library-documents) to list documents and find the document ID before removal.

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-library-documents`](tg-show-library-documents) - List library documents
- [`tg-add-library-document`](tg-add-library-document) - Add documents to library
- [`tg-show-library-processing`](tg-show-library-processing) - View processing status

## API Integration

This command uses the [Library API](../apis/api-librarian) to remove documents from the library.
