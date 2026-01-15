---
title: tg-stop-library-processing
parent: CLI
review_date: 2026-05-24
---

# tg-stop-library-processing

Removes a library document processing record from TrustGraph.

## Synopsis

```bash
tg-stop-library-processing --id PROCESSING_ID [options]
```

## Description

The `tg-stop-library-processing` command removes a document processing record from TrustGraph's library processing system.

**Important**: This removes the processing record. Presently this doesn't affect the processing in any way. This functionality is here to support a to-be-developed use-case.

The processing ID must be a URI. While the value isn't presently used, a future use-case will use this identifier in the knowledge graph.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--id, --processing-id ID` | Processing ID to remove (must be a URI) |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-U, --user USER` | `trustgraph` | User ID |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Remove a Processing Record
```bash
tg-stop-library-processing --id "urn:trustgraph:processing:123456789"
```

### Remove with Custom User
```bash
tg-stop-library-processing --id "urn:trustgraph:processing:research-001" -U "research-team"
```

## Notes

This command is currently a placeholder for future functionality. Removing a processing record has no effect on actual processing operations at this time. The command exists to establish the interface for a to-be-developed use-case where processing IDs will be tracked in the knowledge graph.

Use [`tg-show-library-processing`](tg-show-library-processing) to view current processing records.

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-start-library-processing`](tg-start-library-processing) - Start document processing
- [`tg-show-library-processing`](tg-show-library-processing) - View processing status
- [`tg-show-library-documents`](tg-show-library-documents) - List library documents
- [`tg-show-flows`](tg-show-flows) - Monitor active flows

## API Integration

This command uses the [Library API](../apis/api-librarian) to remove processing records.
