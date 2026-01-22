---
title: tg-get-flow-blueprint
parent: CLI
review_date: 2026-12-24
---

# tg-get-flow-blueprint

Retrieves and displays a flow blueprint definition in JSON format.

## Synopsis

```bash
tg-get-flow-blueprint -n BLUEPRINT_NAME [options]
```

## Description

The `tg-get-flow-blueprint` command retrieves a stored flow blueprint definition from TrustGraph and displays it in formatted JSON. This is useful for examining configurations, creating backups, or preparing to modify existing blueprints.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-n, --blueprint-name NAME` | Name of the flow blueprint to retrieve |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Display Flow Blueprint
```bash
tg-get-flow-blueprint -n "document-processing"
```

### Save to File
```bash
tg-get-flow-blueprint -n "production-flow" > production-flow-backup.json
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-put-flow-blueprint`](tg-put-flow-blueprint) - Create or update blueprint
- [`tg-show-flow-blueprints`](tg-show-flow-blueprints) - List all blueprints
- [`tg-delete-flow-blueprint`](tg-delete-flow-blueprint) - Delete blueprint

## API Integration

This command uses the [Flow Blueprint API](../apis/api-flow-blueprint) to retrieve blueprint definitions.
