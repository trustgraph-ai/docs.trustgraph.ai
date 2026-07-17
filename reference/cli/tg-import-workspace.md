---
title: tg-import-workspace
parent: CLI
review_date: 2027-07-17
---

# tg-import-workspace

Imports a workspace bundle (`.tgx`) into a TrustGraph deployment.

## Synopsis

```bash
tg-import-workspace -i INPUT_FILE [options]
```

## Description

The `tg-import-workspace` command imports a `.tgx` bundle produced by `tg-export-workspace` into a TrustGraph deployment. The target workspace defaults to the name recorded in the bundle's manifest and can be renamed with `--workspace`.

Configuration import is additive by default: existing config keys are left untouched and only missing keys are added. Pass `--overwrite` to replace every imported key. Knowledge import (triples and library documents) is also additive — triples are streamed into the target collection and documents are added to the library. Re-importing the same bundle twice will duplicate knowledge, not merge it.

Use `--dry-run` to preview what would be written, `--config-only` to skip knowledge, and `--process` to re-run imported documents through a flow (which regenerates embeddings, since bundles do not carry vectors).

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-i, --input INPUT_FILE` | Input bundle path, e.g. `workspace-default.tgx` |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | (from bundle manifest) | Target workspace — overrides the workspace recorded in the bundle |
| `-f, --flow-id FLOW` | `default` | Flow to import triples through and process documents with |
| `--overwrite` | | Replace existing config keys in the target workspace |
| `--config-only` | | Import only configuration, skipping any knowledge data in the bundle |
| `--process` | | Re-process imported documents through the flow after import (regenerates extraction output and embeddings) |
| `--process-collection COLLECTION` | `default` | Collection that `--process` targets |
| `--dry-run` | | Show what would be imported without writing anything |

## Examples

### Basic Import
```bash
tg-import-workspace -i my-workspace.tgx
```

### Import into a Different Workspace
```bash
tg-import-workspace -i production-backup.tgx -w staging
```

### Preview Import
```bash
tg-import-workspace -i my-workspace.tgx --dry-run
```

### Import and Regenerate Embeddings
```bash
tg-import-workspace -i my-workspace.tgx --process
```

### Import Config Only, Overwriting Existing Keys
```bash
tg-import-workspace -i my-workspace.tgx --config-only --overwrite
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-export-workspace`](tg-export-workspace) - Export a workspace as a `.tgx` bundle
- [`tg-show-config`](tg-show-config) - Display current workspace configuration
- [`tg-load-kg-core`](tg-load-kg-core) - Import knowledge core from MessagePack file
