---
title: tg-list-collections
parent: CLI
review_date: 2026-12-20
---

# tg-list-collections

Lists collections for a user with their metadata.

## Synopsis

```bash
tg-list-collections [options]
```

## Description

The `tg-list-collections` command displays all collections associated with a user, showing metadata including names, descriptions, tags, and timestamps. Collections organize and isolate data within TrustGraph.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-U, --user USER` | `trustgraph` | User ID |
| `-T, --tag-filter TAG` | None | Filter by tags (can specify multiple times) |

## Examples

### List All Collections
```bash
tg-list-collections
```

### List for Specific User
```bash
tg-list-collections -U alice
```

### Filter by Tag
```bash
tg-list-collections -T research
```

### Multiple Tag Filters
```bash
tg-list-collections -T research -T academic
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-set-collection`](tg-set-collection) - Create or update collection
- [`tg-delete-collection`](tg-delete-collection) - Delete collection

## API Integration

This command uses the Collection Management API to retrieve collection metadata for the specified user.
