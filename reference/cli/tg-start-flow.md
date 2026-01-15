---
title: tg-start-flow
parent: CLI
review_date: 2026-03-16
---

# tg-start-flow

Starts a processing flow using a defined flow blueprint.

## Synopsis

```bash
tg-start-flow -n CLASS_NAME -i FLOW_ID -d DESCRIPTION [options]
```

## Description

The `tg-start-flow` command creates and starts a new processing flow instance based on a predefined flow blueprint. Flow blueprints define the processing pipeline configuration, while flow instances are running implementations with specific identifiers.

**New in v1.4**: Flows can be customized with configurable parameters that control LLM models, chunking behavior, and other processing settings.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-n, --blueprint-name CLASS` | Name of the flow blueprint to instantiate |
| `-i, --flow-id FLOW_ID` | Unique identifier for the new flow instance |
| `-d, --description DESC` | Human-readable description of the flow |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

### Flow Parameters (New in v1.4)

| Option | Description |
|--------|-------------|
| `-p, --parameters JSON` | Flow parameters as JSON string |
| `--parameters-file FILE` | Path to JSON file containing flow parameters |
| `--param KEY=VALUE` | Individual parameter (can be used multiple times) |

**Note**: All parameter values are stored as strings internally.

## Examples

### Start Basic Flow
```bash
tg-start-flow \
  -n "document-rag+graph-rag" \
  -i "research-flow" \
  -d "Research document processing pipeline"
```

### Start with Parameters
```bash
tg-start-flow \
  -n "document-rag+graph-rag" \
  -i "custom-flow" \
  -d "Custom flow with parameters" \
  --param model=gpt-4 \
  --param temperature=0.7 \
  --param chunk-size=512
```

### Using Parameters File
```bash
tg-start-flow \
  -n "medical-analysis" \
  -i "medical-flow" \
  -d "Medical document analysis" \
  --parameters-file flow-config.json
```

### Using JSON Parameters
```bash
tg-start-flow \
  -n "document-processing" \
  -i "prod-flow" \
  -d "Production flow" \
  -p '{"model": "gpt-4", "temp": "0.7"}'
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-stop-flow`](tg-stop-flow) - Stop a running flow
- [`tg-show-flows`](tg-show-flows) - List all running flows
- [`tg-show-flow-blueprints`](tg-show-flow-blueprints) - List available blueprints

## API Integration

This command uses the Flow Management API to create and start flow instances from blueprint definitions.
