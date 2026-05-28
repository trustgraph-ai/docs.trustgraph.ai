---
title: tg-put-de-core
parent: CLI
review_date: 2027-05-21
---

# tg-put-de-core

Puts a document embeddings core into the knowledge manager from a local MessagePack file.

## Synopsis

```bash
tg-put-de-core --id CORE_ID -i INPUT_FILE [options]
```

## Description

The `tg-put-de-core` command loads a document embeddings core from a local MessagePack file into TrustGraph via the API socket. This is used to restore previously exported document embeddings or to transfer them between TrustGraph instances.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--id, --identifier CORE_ID` | Identifier for the document embeddings core |
| `-i, --input INPUT_FILE` | Path to the input MessagePack file |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-w, --workspace WORKSPACE` | `$TRUSTGRAPH_WORKSPACE` or `default` | Workspace identifier |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Basic Import
```bash
tg-put-de-core --id "research-embeddings" -i research-de.msgpack
```

### Import to a Specific Workspace
```bash
tg-put-de-core \
  --id "project-embeddings" \
  -i project-de.msgpack \
  -w my-workspace \
  -u http://production:8088/
```

### Restore from Backup
```bash
tg-put-de-core \
  --id "production-embeddings" \
  -i production-de-20260101-120000.msgpack
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-get-de-core`](tg-get-de-core) - Export document embeddings core to MessagePack file
- [`tg-get-kg-core`](tg-get-kg-core) - Export knowledge graph core
- [`tg-put-kg-core`](tg-put-kg-core) - Import knowledge graph core
- [`tg-show-kg-cores`](tg-show-kg-cores) - List available knowledge cores
