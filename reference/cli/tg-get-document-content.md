---
title: tg-get-document-content
parent: CLI
review_date: 2027-01-01
---

# tg-get-document-content

Retrieves document content from the library by document ID.

## Synopsis

```bash
tg-get-document-content DOCUMENT_ID [options]
```

## Description

Fetches the raw content of a document stored in the library. Can output to a file or stdout. Handles both text and binary content.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `DOCUMENT_ID` | Document IRI to retrieve |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-o, --output FILE` | stdout | Output file path |

## Examples

```bash
# Display document content
tg-get-document-content "urn:trustgraph:doc:abc123"

# Save to file
tg-get-document-content -o document.pdf "urn:trustgraph:doc:abc123"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-library-documents`](tg-show-library-documents) - List documents in library
- [`tg-show-extraction-provenance`](tg-show-extraction-provenance) - Show document provenance hierarchy
