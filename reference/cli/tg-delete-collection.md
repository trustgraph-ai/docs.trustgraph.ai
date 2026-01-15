---
title: tg-delete-collection
parent: CLI
review_date: 2026-01-19
---

# tg-delete-collection

Deletes a collection and all its data.

## Synopsis

```bash
tg-delete-collection COLLECTION [options]
```

## Description

The `tg-delete-collection` command permanently deletes a collection and all associated data from TrustGraph, including documents, embeddings, knowledge graph triples, and other stored data.

**Warning**: This operation is irreversible. All data in the collection will be permanently lost.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `COLLECTION` | Collection ID to delete |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-U, --user USER` | `trustgraph` | User ID |
| `-y, --yes` | false | Skip confirmation prompt |

## Examples

### Delete with Confirmation
```bash
tg-delete-collection old-research
```

### Delete Without Confirmation
```bash
tg-delete-collection old-research -y
```

### Delete with Specific User
```bash
tg-delete-collection test-data -U developer -y
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-set-collection`](tg-set-collection) - Create or configure collection
- [`tg-list-collections`](tg-list-collections) - List all collections

## API Integration

This command uses the Collection Management API to permanently delete collections and all associated data.
