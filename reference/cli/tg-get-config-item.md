---
title: tg-get-config-item
parent: CLI
review_date: 2026-12-27
---

# tg-get-config-item

Retrieves a specific configuration item from TrustGraph.

## Synopsis

```bash
tg-get-config-item -k KEY [options]
```

## Description

The `tg-get-config-item` command retrieves and displays the value of a specific configuration item from TrustGraph. Supports multiple output formats for different use cases.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-k, --key KEY` | Configuration key to retrieve |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `--format FORMAT` | `json` | Output format: `json`, `yaml`, or `raw` |
| `--version VERSION` | Latest | Retrieve specific version |
| `-o, --output FILE` | stdout | Write output to file |

## Examples

### Retrieve Configuration
```bash
tg-get-config-item -k flows.default
```

### YAML Format
```bash
tg-get-config-item -k prompts.system --format yaml
```

### Raw Value Only
```bash
tg-get-config-item -k settings.temperature --format raw
```

### Save to File
```bash
tg-get-config-item -k flows.production -o production-flow.json
```

### Specific Version
```bash
tg-get-config-item -k prompts.system --version 2
```

## Output Formats

| Format | Description | Use Case |
|--------|-------------|----------|
| `json` | Pretty-printed JSON with metadata | Default, human-readable |
| `yaml` | YAML format with metadata | Configuration editing |
| `raw` | Value only, no metadata | Piping to other commands |

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-put-config-item`](tg-put-config-item) - Create or update configuration
- [`tg-list-config-items`](tg-list-config-items) - List all configuration keys
- [`tg-show-config`](tg-show-config) - Display complete system configuration

## API Integration

This command uses the Configuration API to retrieve individual configuration items with version history support.
