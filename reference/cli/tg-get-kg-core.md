---
title: tg-get-kg-core
parent: CLI
review_date: 2026-03-21
---

# tg-get-kg-core

Exports a knowledge core from TrustGraph to a MessagePack file.

## Synopsis

```bash
tg-get-kg-core --id CORE_ID -o OUTPUT_FILE [options]
```

## Description

The `tg-get-kg-core` command retrieves a stored knowledge core from TrustGraph and exports it to MessagePack format. The exported file contains both RDF triples and graph embeddings, suitable for backup, transfer between systems, or offline analysis.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--id, --identifier CORE_ID` | Identifier of the knowledge core to export |
| `-o, --output OUTPUT_FILE` | Path for the output MessagePack file |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `ws://localhost:8088/` | TrustGraph API URL (WebSocket) |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-U, --user USER` | `trustgraph` | User identifier |

## Examples

### Basic Export
```bash
tg-get-kg-core --id "research-knowledge" -o research-backup.msgpack
```

### Export with Timestamped Filename
```bash
tg-get-kg-core \
  --id "production-core" \
  -o "production-backup-$(date +%Y%m%d-%H%M%S).msgpack"
```

### Export and Compress
```bash
tg-get-kg-core --id "large-core" -o large-core.msgpack
gzip large-core.msgpack
```

### Custom User and API
```bash
tg-get-kg-core \
  --id "remote-core" \
  -o remote-backup.msgpack \
  -u ws://production:8088/ \
  -U medical-team
```

## Output Format

The MessagePack file contains two types of messages:

| Type | Description | Content |
|------|-------------|---------|
| Triple (`"t"`) | RDF triples (facts and relationships) | Subject, predicate, object triples |
| Graph Embedding (`"ge"`) | Vector embeddings for entities | Entity vectors for semantic search |

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL (automatically converted to WebSocket format)
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-load-kg-core`](tg-load-kg-core) - Import knowledge core from MessagePack file
- [`tg-show-kg-cores`](tg-show-kg-cores) - List available knowledge cores
- [`tg-delete-kg-core`](tg-delete-kg-core) - Delete knowledge core
- [`tg-dump-msgpack`](tg-dump-msgpack) - Examine MessagePack file contents

## API Integration

This command uses the Knowledge API via WebSocket connection with `get-kg-core` operations to stream knowledge data.
