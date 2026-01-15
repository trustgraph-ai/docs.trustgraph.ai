---
title: tg-put-kg-core
parent: CLI
review_date: 2026-05-26
---

# tg-put-kg-core

Stores a knowledge core in TrustGraph from MessagePack format.

## Synopsis

```bash
tg-put-kg-core --id CORE_ID -i INPUT_FILE [options]
```

## Description

The `tg-put-kg-core` command loads a knowledge core from a MessagePack file and stores it in TrustGraph. Knowledge cores contain RDF triples and graph embeddings that can be loaded into flows for processing.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--id, --identifier CORE_ID` | Unique identifier for the knowledge core |
| `-i, --input INPUT_FILE` | Path to MessagePack input file |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `ws://localhost:8088/` | TrustGraph API URL (WebSocket) |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-U, --user USER` | `trustgraph` | User identifier |

## Examples

### Store Knowledge Core
```bash
tg-put-kg-core --id "research-core-v1" -i knowledge.msgpack
```

### With Custom User
```bash
tg-put-kg-core \
  --id "medical-knowledge" \
  -i medical-data.msgpack \
  -U researcher
```

### Using Custom API
```bash
tg-put-kg-core \
  --id "production-core" \
  -i prod-knowledge.msgpack \
  -u ws://production:8088/
```

## Input File Format

The input file must be MessagePack format containing:
- **Triples**: RDF subject-predicate-object relationships
- **Graph Embeddings**: Vector representations for semantic search

Files are typically created using `tg-get-kg-core` or external knowledge processing tools.

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL (automatically converted to WebSocket format)
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-get-kg-core`](tg-get-kg-core) - Export knowledge core to MessagePack
- [`tg-load-kg-core`](tg-load-kg-core) - Load knowledge core into flow
- [`tg-show-kg-cores`](tg-show-kg-cores) - List available knowledge cores

## API Integration

This command uses the Knowledge API via WebSocket connection to stream knowledge data into storage.
