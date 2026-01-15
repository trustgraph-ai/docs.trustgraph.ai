---
title: tg-show-flow-blueprints
parent: CLI
review_date: 2026-03-11
---

# tg-show-flow-blueprints

Lists all defined flow blueprints in TrustGraph with their descriptions and tags.

## Synopsis

```bash
tg-show-flow-blueprints [options]
```

## Description

The `tg-show-flow-blueprints` command displays a formatted table of all flow blueprint definitions currently stored in TrustGraph. Each flow blueprint is shown with its name, description, and associated tags.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### List All Flow Blueprints
```bash
tg-show-flow-blueprints
```

## Output Format

The command displays blueprints in a formatted table showing name, description, and tags for each blueprint.

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-get-flow-blueprint`](tg-get-flow-blueprint) - Retrieve specific blueprint
- [`tg-put-flow-blueprint`](tg-put-flow-blueprint) - Create or update blueprint
- [`tg-delete-flow-blueprint`](tg-delete-flow-blueprint) - Delete blueprint

## API Integration

This command uses the [Flow Blueprint API](../apis/api-flow-blueprint) to list blueprints.
