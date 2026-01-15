---
title: tg-list-config-items
parent: CLI
review_date: 2026-05-23
---

# tg-list-config-items

Lists all configuration items stored in TrustGraph.

## Synopsis

```bash
tg-list-config-items [options]
```

## Description

The `tg-list-config-items` command retrieves and displays all configuration items currently stored in TrustGraph. Configuration items include flow definitions, prompt templates, token costs, and service settings.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `--format FORMAT` | `table` | Output format: `table`, `json`, or `list` |
| `--filter PATTERN` | None | Filter items by regex pattern |
| `--category CATEGORY` | All | Filter by category: `flow`, `prompt`, `token-cost`, `settings` |

## Examples

### List All Configuration Items
```bash
tg-list-config-items
```

### JSON Output
```bash
tg-list-config-items --format json
```

### Simple List Format
```bash
tg-list-config-items --format list
```

### Filter by Pattern
```bash
tg-list-config-items --filter "^prompt\."
```

### Filter by Category
```bash
tg-list-config-items --category flow
```

## Output Formats

| Format | Description | Use Case |
|--------|-------------|----------|
| `table` | Formatted table with key, category, description | Human-readable viewing |
| `json` | Complete JSON response | API integration |
| `list` | Simple list of keys | Scripting, piping |

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-get-config-item`](tg-get-config-item) - Retrieve specific configuration
- [`tg-put-config-item`](tg-put-config-item) - Create or update configuration
- [`tg-show-config`](tg-show-config) - Display complete system configuration

## API Integration

This command uses the Configuration API to list all stored configuration item keys.
