---
title: tg-get-de-core
parent: CLI
review_date: 2027-05-21
---

# tg-get-de-core

Fetches a document embeddings core from the knowledge service and saves it to a local file.

## Synopsis

```bash
tg-get-de-core --id CORE_ID -o OUTPUT_FILE [options]
```

## Description

The `tg-get-de-core` command retrieves a stored document embeddings core from TrustGraph and saves it to a local file in MessagePack format. The exported file contains document chunk embeddings suitable for backup, transfer between systems, or offline analysis.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--id, --identifier CORE_ID` | Identifier of the document embeddings core to fetch |
| `-o, --output OUTPUT_FILE` | Path for the output MessagePack file |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-w, --workspace WORKSPACE` | `$TRUSTGRAPH_WORKSPACE` or `default` | Workspace identifier |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Basic Export
```bash
tg-get-de-core --id "research-embeddings" -o research-de.msgpack
```

### Export with Timestamped Filename
```bash
tg-get-de-core \
  --id "production-embeddings" \
  -o "production-de-$(date +%Y%m%d-%H%M%S).msgpack"
```

### Export from a Specific Workspace
```bash
tg-get-de-core \
  --id "project-embeddings" \
  -o project-de.msgpack \
  -w my-workspace \
  -u http://production:8088/
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-put-de-core`](tg-put-de-core) - Import document embeddings core from MessagePack file
- [`tg-get-kg-core`](tg-get-kg-core) - Export knowledge graph core
- [`tg-put-kg-core`](tg-put-kg-core) - Import knowledge graph core
- [`tg-show-kg-cores`](tg-show-kg-cores) - List available knowledge cores
