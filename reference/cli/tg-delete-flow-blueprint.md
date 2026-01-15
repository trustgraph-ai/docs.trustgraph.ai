---
title: tg-delete-flow-blueprint
parent: CLI
review_date: 2026-05-01
---

# tg-delete-flow-blueprint

Permanently deletes a flow blueprint definition from TrustGraph.

## Synopsis

```bash
tg-delete-flow-blueprint -n BLUEPRINT_NAME [options]
```

## Description

The `tg-delete-flow-blueprint` command permanently removes a flow blueprint definition from TrustGraph. This operation cannot be undone.

**Warning**: Deleting a flow blueprint that has active flow instances may cause those instances to become unusable.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-n, --blueprint-name NAME` | Name of the flow blueprint to delete |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Delete Flow Blueprint
```bash
tg-delete-flow-blueprint -n "old-processing-flow"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-flow-blueprints`](tg-show-flow-blueprints) - List all blueprints
- [`tg-get-flow-blueprint`](tg-get-flow-blueprint) - Retrieve blueprint
- [`tg-put-flow-blueprint`](tg-put-flow-blueprint) - Create or update blueprint

## API Integration

This command uses the [Flow Blueprint API](../apis/api-flow-blueprint) to delete blueprint definitions.
