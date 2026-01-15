---
title: tg-put-config-item
parent: CLI
review_date: 2026-01-30
---

# tg-put-config-item

Creates or updates a configuration item in the TrustGraph configuration service.

## Synopsis

```bash
tg-put-config-item -k KEY -v VALUE [options]
tg-put-config-item -k KEY -f FILE [options]
```

## Description

The `tg-put-config-item` command creates or updates configuration items in TrustGraph. Configuration values can be provided directly on the command line, from a file, or via stdin. Supports JSON, YAML, and text formats.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-k, --key KEY` | Configuration key to set |

### Input Options (one required)

| Option | Description |
|--------|-------------|
| `-v, --value VALUE` | Configuration value (JSON string) |
| `-f, --file FILE` | Read value from file |
| `--stdin` | Read value from stdin |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `--format FORMAT` | `json` | Input format: `json`, `yaml`, or `text` |

## Examples

### Direct Value
```bash
tg-put-config-item -k settings.max-tokens -v 4096
```

### JSON Object
```bash
tg-put-config-item -k settings.limits -v '{"max_tokens": 4096, "timeout": 30}'
```

### From File
```bash
tg-put-config-item -k flows.production -f production-flow.json
```

### Text Format
```bash
tg-put-config-item -k prompts.system -f system-prompt.txt --format text
```

### From Stdin
```bash
echo '{"temperature": 0.7}' | tg-put-config-item -k settings.llm --stdin
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-get-config-item`](tg-get-config-item) - Retrieve configuration item
- [`tg-show-config`](tg-show-config) - Display system configuration

## API Integration

This command uses the Configuration API to store configuration items with version tracking.
