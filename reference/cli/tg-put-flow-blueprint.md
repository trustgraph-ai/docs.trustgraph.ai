---
title: tg-put-flow-blueprint
parent: CLI
review_date: 2026-05-20
---

# tg-put-flow-blueprint

Uploads or updates a flow blueprint definition in TrustGraph.

## Synopsis

```bash
tg-put-flow-blueprint -n BLUEPRINT_NAME -c CONFIG_JSON [options]
```

## Description

The `tg-put-flow-blueprint` command creates or updates a flow blueprint definition in TrustGraph. Flow blueprints are templates that define processing pipeline configurations, service interfaces, and resource requirements. These blueprints are used by `tg-start-flow` to create running flow instances.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-n, --blueprint-name NAME` | Name for the flow blueprint |
| `-c, --config CONFIG_JSON` | Flow blueprint configuration as raw JSON string |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Create Flow Blueprint
```bash
tg-put-flow-blueprint \
  -n "simple-processing" \
  -c '{"description": "Simple text processing flow", "interfaces": {"text-completion": {"request": "non-persistent://tg/request/text-completion:simple", "response": "non-persistent://tg/response/text-completion:simple"}}}'
```

### Load from File
```bash
tg-put-flow-blueprint \
  -n "document-analysis" \
  -c "$(cat flow-config.json)"
```

### Update Existing Blueprint
```bash
tg-put-flow-blueprint \
  -n "production-flow" \
  -c "$(cat updated-config.json)"
```

## Configuration Format

Flow blueprint configurations are JSON objects defining:
- **description**: Human-readable description
- **interfaces**: Service endpoint definitions with Pulsar topic mappings
- **resources**: Optional resource requirements
- **settings**: Optional configuration parameters

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-get-flow-blueprint`](tg-get-flow-blueprint) - Retrieve flow blueprint
- [`tg-show-flow-blueprints`](tg-show-flow-blueprints) - List all blueprints
- [`tg-delete-flow-blueprint`](tg-delete-flow-blueprint) - Delete blueprint
- [`tg-start-flow`](tg-start-flow) - Start flow from blueprint

## API Integration

This command uses the [Flow Blueprint API](../apis/api-flow-blueprint) to store blueprint definitions.
