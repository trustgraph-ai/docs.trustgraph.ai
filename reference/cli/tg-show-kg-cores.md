---
title: tg-show-kg-cores
parent: CLI
review_date: 2026-05-07
---

# tg-show-kg-cores

Shows available knowledge cores in TrustGraph.

## Synopsis

```bash
tg-show-kg-cores [options]
```

## Description

The `tg-show-kg-cores` command lists all knowledge cores available for a specific user. Knowledge cores contain structured knowledge (RDF triples and graph embeddings) that can be loaded into flows.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-U, --user USER` | `trustgraph` | User identifier |

## Examples

### List All Knowledge Cores
```bash
tg-show-kg-cores
```

### List Cores for Specific User
```bash
tg-show-kg-cores -U researcher
```

### Using Custom API URL
```bash
tg-show-kg-cores -u http://production:8088/
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-get-kg-core`](tg-get-kg-core) - Export knowledge core to MessagePack
- [`tg-put-kg-core`](tg-put-kg-core) - Import knowledge core from MessagePack
- [`tg-load-kg-core`](tg-load-kg-core) - Load knowledge core into flow

## API Integration

This command uses the Knowledge API to list available knowledge core identifiers.
