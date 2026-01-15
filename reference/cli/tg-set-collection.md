---
title: tg-set-collection
parent: CLI
review_date: 2026-03-07
---

# tg-set-collection

Creates or updates collection metadata.

## Synopsis

```bash
tg-set-collection COLLECTION [options]
```

## Description

The `tg-set-collection` command creates a new collection or updates metadata of an existing collection. Collections organize and isolate data within TrustGraph, allowing multiple users and projects to maintain separate data spaces.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `COLLECTION` | Collection ID to create or update |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-U, --user USER` | `trustgraph` | User ID |
| `-n, --name NAME` | None | Human-readable collection name |
| `-d, --description DESC` | None | Detailed description |
| `-T, --tag TAG` | None | Collection tag (can specify multiple times) |

## Examples

### Create New Collection
```bash
tg-set-collection research-2024 \
  -n "2024 Research" \
  -d "Research documents and data for 2024" \
  -T research -T academic
```

### Update Existing Collection
```bash
tg-set-collection existing-collection -d "Updated description"
```

### Create Collection for Specific User
```bash
tg-set-collection medical-data -U researcher -n "Medical Research Data"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-list-collections`](tg-list-collections) - List all collections
- [`tg-delete-collection`](tg-delete-collection) - Delete collection

## API Integration

This command uses the Collection Management API to create or update collection metadata.
