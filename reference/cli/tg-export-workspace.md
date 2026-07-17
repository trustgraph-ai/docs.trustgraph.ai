---
title: tg-export-workspace
parent: CLI
review_date: 2027-07-17
---

# tg-export-workspace

Exports a workspace's full state as a portable `.tgx` bundle for backup, migration, or sharing.

## Synopsis

```bash
tg-export-workspace -o OUTPUT_FILE [options]
```

## Description

The `tg-export-workspace` command exports a workspace as a gzipped tar archive (`.tgx` bundle). The bundle contains the workspace configuration (one pretty-printed JSON file per config key) and, by default, its knowledge: per-collection triples as N-Quads and the document library (metadata plus content). Embedding vectors are not exported — re-processing imported documents through a flow regenerates them.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-o, --output OUTPUT_FILE` | Output bundle path, e.g. `workspace-default.tgx` |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | `$TRUSTGRAPH_WORKSPACE` or `default` | Workspace to export |
| `-c, --collection COLLECTION` | (auto-detected) | Additionally export this collection even if not registered in collection management (repeatable) |
| `-f, --flow-id FLOW` | `default` | Flow to query triples through |
| `--config-only` | | Export only configuration, skipping knowledge (triples and library documents) |
| `--triples-limit LIMIT` | `1000000` | Maximum triples to export per collection |

## Examples

### Basic Export
```bash
tg-export-workspace -o my-workspace.tgx
```

### Export Configuration Only
```bash
tg-export-workspace -o my-config.tgx --config-only
```

### Export a Specific Workspace
```bash
tg-export-workspace -w research -o research-backup.tgx
```

### Export with Additional Collections
```bash
tg-export-workspace -o full-export.tgx -c extra-collection -c another-collection
```

## Output Format

The `.tgx` bundle is a gzipped tar archive containing:

| Path | Description |
|------|-------------|
| `manifest.json` | Bundle metadata (format version, source workspace, timestamp) |
| `config/<type>/<key>.json` | One JSON file per config entry with `type`, `key`, and `value` fields |
| `knowledge/<collection>/triples.nq` | N-Quads file per collection containing RDF triples |
| `library/` | Document library metadata and content |

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-import-workspace`](tg-import-workspace) - Import a `.tgx` bundle into a deployment
- [`tg-show-config`](tg-show-config) - Display current workspace configuration
- [`tg-get-kg-core`](tg-get-kg-core) - Export knowledge core as MessagePack (single collection)
