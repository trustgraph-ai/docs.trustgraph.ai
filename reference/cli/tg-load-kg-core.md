---
title: tg-load-kg-core
parent: CLI
review_date: 2026-05-15
---

# tg-load-kg-core

Loads a stored knowledge core into a processing flow for active use.

## Synopsis

```bash
tg-load-kg-core --id CORE_ID [options]
```

## Description

The `tg-load-kg-core` command loads a previously stored knowledge core into an active processing flow, making the knowledge available for queries, reasoning, and AI operations. Once loaded, the RDF triples and graph embeddings become available for Graph RAG queries and agent reasoning within the flow.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--id, --identifier CORE_ID` | Identifier of the knowledge core to load |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-f, --flow-id FLOW` | `default` | Flow ID to load knowledge into |
| `-c, --collection COLLECTION` | `default` | Collection identifier |

## Examples

### Load into Default Flow
```bash
tg-load-kg-core --id "research-knowledge-v1"
```

### Load into Specific Flow
```bash
tg-load-kg-core \
  --id "medical-knowledge" \
  --flow-id "medical-analysis" \
  --user researcher
```

### Load with Custom Collection
```bash
tg-load-kg-core \
  --id "legal-documents" \
  --flow-id "legal-flow" \
  --collection "law-firm-data"
```

### Using Custom API
```bash
tg-load-kg-core \
  --id "production-knowledge" \
  --flow-id "prod-flow" \
  -u http://production:8088/
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-get-kg-core`](tg-get-kg-core) - Export knowledge core to MessagePack file
- [`tg-unload-kg-core`](tg-unload-kg-core) - Remove knowledge core from flow
- [`tg-show-kg-cores`](tg-show-kg-cores) - List available knowledge cores

## API Integration

This command uses the Knowledge API to load stored knowledge cores into flow contexts for active querying and reasoning.
