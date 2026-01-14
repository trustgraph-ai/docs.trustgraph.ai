---
title: tg-list-config-items
parent: CLI
review_date: 2026-05-23
---

# tg-list-config-items

List all configuration items stored in the TrustGraph configuration service.

## Synopsis

```bash
tg-list-config-items [OPTIONS]
```

## Description

The `tg-list-config-items` command retrieves and displays a list of all configuration items currently stored in the TrustGraph configuration service. This provides an overview of available configuration keys that can be retrieved or modified.

Configuration items include:
- Flow definitions
- Prompt templates
- Token cost configurations
- Service-specific settings
- Custom application configurations

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `-u`, `--url URL` | TrustGraph API URL | `http://localhost:8088/` |
| `--format FORMAT` | Output format: `table`, `json`, `list` | `table` |
| `--filter PATTERN` | Filter items by pattern (regex) | None |
| `--category CATEGORY` | Filter by category: `flow`, `prompt`, `token-cost`, `settings` | All |
| `-h`, `--help` | Show help message | - |

## Output Formats

### Table Format (Default)

Displays configuration items in a formatted table:

```bash
$ tg-list-config-items

+---------------------------+----------+----------------------------------------+
| Key                       | Category | Description                            |
+---------------------------+----------+----------------------------------------+
| flow.default              | flow     | Default processing flow configuration  |
| flow.production           | flow     | Production flow configuration          |
| prompt.system             | prompt   | System prompt template                 |
| prompt.graph-rag          | prompt   | Graph RAG prompt template             |
| token-cost.gpt-4          | cost     | GPT-4 token pricing                  |
| token-cost.claude-3       | cost     | Claude 3 token pricing                |
| settings.max-tokens       | settings | Maximum tokens per request            |
| settings.temperature      | settings | Default temperature setting           |
+---------------------------+----------+----------------------------------------+
```

### List Format

Simple list of configuration keys:

```bash
$ tg-list-config-items --format list

flow.default
flow.production
prompt.system
prompt.graph-rag
token-cost.gpt-4
token-cost.claude-3
settings.max-tokens
settings.temperature
```

### JSON Format

Complete JSON response with metadata:

```bash
$ tg-list-config-items --format json

{
  "config_items": [
    {
      "key": "flow.default",
      "category": "flow",
      "description": "Default processing flow configuration",
      "modified": "2024-01-15T10:30:00Z",
      "version": 3
    },
    {
      "key": "prompt.system",
      "category": "prompt",
      "description": "System prompt template",
      "modified": "2024-01-10T14:20:00Z",
      "version": 1
    }
  ],
  "total": 8
}
```

## Examples

### Basic Usage

```bash
# List all configuration items
tg-list-config-items

# List in simple format
tg-list-config-items --format list
```

### Filtering

```bash
# Filter by pattern
tg-list-config-items --filter "flow.*"

# Filter by category
tg-list-config-items --category prompt

# Complex regex filter
tg-list-config-items --filter "^(flow|prompt)\..*"
```

### Export and Processing

```bash
# Export to file
tg-list-config-items --format json > config-items.json

# Get just the keys
tg-list-config-items --format list > config-keys.txt

# Count items by category
tg-list-config-items --format json | jq '.config_items | group_by(.category) | map({category: .[0].category, count: length})'
```

### Integration with Other Commands

```bash
# List all items, then get details for each
for key in $(tg-list-config-items --format list); do
  echo "=== $key ==="
  tg-get-config-item -k "$key"
done

# Backup all configuration items
tg-list-config-items --format list | while read key; do
  tg-get-config-item -k "$key" --format json > "backup-$key.json"
done
```

## Configuration Categories

### Flow
Flow-related configurations:
- `flow.<flow-id>` - Individual flow definitions
- `flow-blueprint.<blueprint-name>` - Flow blueprint templates

### Prompt
AI prompt templates:
- `prompt.system` - System-wide prompts
- `prompt.<service>` - Service-specific prompts

### Token Cost
Model pricing configurations:
- `token-cost.<model>` - Per-model token costs

### Settings
General system settings:
- `settings.<parameter>` - Various system parameters

### Custom
User-defined configurations:
- `custom.<namespace>.<key>` - Application-specific settings

## Filtering Patterns

The `--filter` option accepts regular expressions:

```bash
# All flow configurations
tg-list-config-items --filter "^flow\."

# Items containing 'rag'
tg-list-config-items --filter ".*rag.*"

# Exclude test items
tg-list-config-items --filter "^(?!.*test).*"
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `TRUSTGRAPH_URL` | Default API URL | `http://localhost:8088/` |

## Exit Codes

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | Error (connection error, service error, etc.) |

## Error Handling

Common errors and solutions:

### Connection Refused
```bash
Error: Unable to connect to configuration service
```
**Solution**: Verify TrustGraph is running and the URL is correct.

### Empty Results
```bash
No configuration items found
```
**Solution**: Check filter pattern or verify configuration service has data.

## Performance Considerations

- The command retrieves all configuration keys in a single request
- For large deployments with many configurations, consider using filters
- Results are cached briefly to improve performance for sequential operations

## Troubleshooting

### No Items Listed

If no configuration items appear:
1. Verify the configuration service is running
2. Check that configurations have been initialized
3. Ensure proper permissions to access configuration

### Filter Not Working

If filtering returns unexpected results:
1. Test the regex pattern separately
2. Use simpler patterns first
3. Check for special character escaping

## See Also

- [tg-get-config-item](tg-get-config-item) - Retrieve specific configuration item
- [tg-put-config-item](tg-put-config-item) - Update configuration item
- [tg-show-config](tg-show-config) - Display complete system configuration
- [Config API](../apis/api-config) - Configuration service API documentation
