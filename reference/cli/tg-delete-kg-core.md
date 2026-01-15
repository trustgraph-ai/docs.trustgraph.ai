---
title: tg-delete-kg-core
parent: CLI
review_date: 2026-03-08
---

# tg-delete-kg-core

Permanently removes a knowledge core from the TrustGraph system.

## Synopsis

```bash
tg-delete-kg-core --id CORE_ID [options]
```

## Description

The `tg-delete-kg-core` command permanently removes a stored knowledge core from TrustGraph. This operation is irreversible and deletes all RDF triples, graph embeddings, and metadata associated with the knowledge core.

**Warning**: This operation permanently deletes data. Ensure you have backups if needed.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--id, --identifier CORE_ID` | Identifier of the knowledge core to delete |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-U, --user USER` | `trustgraph` | User identifier |

## Examples

### Delete Knowledge Core
```bash
tg-delete-kg-core --id "old-research-data"
```

### Delete with Specific User
```bash
tg-delete-kg-core --id "test-knowledge" -U developer
```

### Using Custom API
```bash
tg-delete-kg-core --id "obsolete-core" -u http://production:8088/
```

### Backup Before Deletion
```bash
# Export knowledge core before deletion
tg-get-kg-core --id "important-core" -o backup.msgpack

# Then proceed with deletion
tg-delete-kg-core --id "important-core"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-get-kg-core`](tg-get-kg-core) - Export knowledge core for backup
- [`tg-unload-kg-core`](tg-unload-kg-core) - Unload from flow without deleting
- [`tg-show-kg-cores`](tg-show-kg-cores) - List available knowledge cores

## API Integration

This command uses the Knowledge API to permanently delete knowledge cores and all associated data.
