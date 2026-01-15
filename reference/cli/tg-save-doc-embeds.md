---
title: tg-save-doc-embeds
parent: CLI
review_date: 2026-02-05
---

# tg-save-doc-embeds

Saves document embeddings from TrustGraph processing streams to MessagePack format files.

## Synopsis

```bash
tg-save-doc-embeds -o OUTPUT_FILE [options]
```

## Description

The `tg-save-doc-embeds` command connects to TrustGraph's document embeddings export stream and saves the embeddings to a file in MessagePack format. This is useful for creating backups, exporting data for analysis, or preparing data for migration between systems.

The command should typically be started before document processing begins to capture all embeddings as they are generated.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-o, --output-file FILE` | Output file for saved embeddings |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_API` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow instance ID to monitor |
| `--format FORMAT` | `msgpack` | Output format - `msgpack` or `json` |
| `--user USER` | (none) | Filter by user ID |
| `--collection COLLECTION` | (none) | Filter by collection ID |

## Examples

### Save Document Embeddings
```bash
tg-save-doc-embeds -o document-embeddings.msgpack
```

### Save from Specific Flow
```bash
tg-save-doc-embeds \
  -o research-embeddings.msgpack \
  -f "research-processing-flow"
```

### Filter by Collection
```bash
tg-save-doc-embeds \
  -o filtered-embeddings.msgpack \
  --collection "research-docs"
```

### Export to JSON Format
```bash
tg-save-doc-embeds \
  -o embeddings.json \
  --format json
```

## Output Format

### MessagePack Structure
Document embeddings are saved as MessagePack records:

```json
["de", {
  "m": {
    "i": "document-id",
    "u": "user-id",
    "c": "collection-id"
  },
  "c": [{
    "c": "text chunk content",
    "v": [0.1, 0.2, 0.3, ...]
  }]
}]
```

Components:
- **Record Type**: `"de"` indicates document embeddings
- **Metadata** (`m`): Document information and context
- **Chunks** (`c`): Text chunks with their vector embeddings

## Environment Variables

- `TRUSTGRAPH_API`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-load-doc-embeds`](tg-load-doc-embeds) - Load document embeddings
- [`tg-dump-msgpack`](tg-dump-msgpack) - Inspect MessagePack files
- [`tg-save-graph-embeds`](tg-save-graph-embeds) - Save graph embeddings

## API Integration

This command uses the [Document Embeddings Export API](../apis/api-document-embeddings) to stream embeddings data.
