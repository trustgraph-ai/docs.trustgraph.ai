---
title: tg-get-config-item
parent: CLI
review_date: 2025-12-27
---

# tg-get-config-item

Retrieve a specific configuration item from the TrustGraph configuration service.

## Synopsis

```bash
tg-get-config-item -k KEY [OPTIONS]
```

## Description

The `tg-get-config-item` command retrieves and displays the value of a specific configuration item from the TrustGraph configuration service. This allows you to inspect individual configuration settings, flow definitions, prompts, or any other stored configuration data.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `-k`, `--key KEY` | Configuration key to retrieve | Required |
| `-u`, `--url URL` | TrustGraph API URL | `http://localhost:8088/` |
| `--format FORMAT` | Output format: `json`, `yaml`, `raw` | `json` |
| `--version VERSION` | Retrieve specific version | Latest |
| `-o`, `--output FILE` | Write output to file | stdout |
| `-h`, `--help` | Show help message | - |

## Output Formats

### JSON Format (Default)

Pretty-printed JSON output:

```bash
$ tg-get-config-item -k flows.default

{
  "key": "flows.default",
  "value": {
    "blueprint-name": "document-rag+graph-rag",
    "description": "Default processing flow",
    "interfaces": {
      "agent": {
        "request": "non-persistent://tg/request/agent:default",
        "response": "non-persistent://tg/response/agent:default"
      },
      "graph-rag": {
        "request": "non-persistent://tg/request/graph-rag:document-rag+graph-rag",
        "response": "non-persistent://tg/response/graph-rag:document-rag+graph-rag"
      }
    }
  },
  "version": 3,
  "modified": "2024-01-15T10:30:00Z"
}
```

### YAML Format

Human-readable YAML output:

```bash
$ tg-get-config-item -k prompts.system --format yaml

key: prompts.system
value: |
  You are a helpful AI assistant with expertise in knowledge graphs 
  and document analysis. Provide clear, accurate, and concise responses.
version: 1
modified: "2024-01-10T14:20:00Z"
```

### Raw Format

Just the value without metadata:

```bash
$ tg-get-config-item -k settings.max-tokens --format raw

4096
```

## Examples

### Basic Retrieval

```bash
# Get a flow configuration
tg-get-config-item -k flows.default

# Get a prompt template
tg-get-config-item -k prompts.graph-rag

# Get token costs
tg-get-config-item -k token-costs.gpt-4
```

### Different Output Formats

```bash
# Get as YAML for readability
tg-get-config-item -k flows.production --format yaml

# Get raw value only
tg-get-config-item -k settings.temperature --format raw

# Pretty JSON (default)
tg-get-config-item -k prompts.system
```

### Save to File

```bash
# Save configuration to file
tg-get-config-item -k flows.default -o flow-config.json

# Save prompt template
tg-get-config-item -k prompts.system -o system-prompt.txt --format raw

# Backup configuration
tg-get-config-item -k flows.production > backup-production-flow.json
```

### Version Management

```bash
# Get specific version
tg-get-config-item -k flows.default --version 2

# Compare versions
tg-get-config-item -k prompts.system --version 1 > v1.json
tg-get-config-item -k prompts.system --version 2 > v2.json
diff v1.json v2.json
```

### Processing Output

```bash
# Extract specific field with jq
tg-get-config-item -k flows.default | jq '.value.interfaces.agent'

# Get just the description
tg-get-config-item -k flows.production | jq -r '.value.description'

# Check version number
tg-get-config-item -k prompts.system | jq '.version'
```

## Common Configuration Keys

### Flow Configurations
```bash
# Get default flow
tg-get-config-item -k flows.default

# Get specific flow
tg-get-config-item -k flows.production

# Get flow blueprint definition
tg-get-config-item -k flow-blueprintes.document-rag
```

### Prompt Templates
```bash
# System prompt
tg-get-config-item -k prompts.system

# Service-specific prompts
tg-get-config-item -k prompts.graph-rag
tg-get-config-item -k prompts.document-rag
```

### Token Costs
```bash
# Model pricing
tg-get-config-item -k token-costs.gpt-4
tg-get-config-item -k token-costs.claude-3
tg-get-config-item -k token-costs.llama-2
```

### System Settings
```bash
# General settings
tg-get-config-item -k settings.max-tokens
tg-get-config-item -k settings.temperature
tg-get-config-item -k settings.timeout
```

## Integration Examples

### Update Workflow
```bash
# Get current configuration
tg-get-config-item -k flows.default -o current.json

# Edit the configuration
vi current.json

# Update with new configuration
tg-put-config-item -k flows.default -f current.json
```

### Configuration Validation
```bash
# Verify configuration exists
if tg-get-config-item -k flows.production > /dev/null 2>&1; then
  echo "Production flow configured"
else
  echo "Production flow not found"
fi
```

### Backup Script
```bash
#!/bin/bash
# Backup all configurations

for key in $(tg-list-config-items --format list); do
  echo "Backing up $key..."
  tg-get-config-item -k "$key" -o "backup/$key.json"
done
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `TRUSTGRAPH_URL` | Default API URL | `http://localhost:8088/` |

## Exit Codes

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | Error (key not found, service error, etc.) |

## Error Handling

Common errors and solutions:

### Key Not Found
```bash
Error: Configuration key 'flows.nonexistent' not found
```
**Solution**: Use `tg-list-config-items` to see available keys.

### Invalid Format
```bash
Error: Unknown format 'xml'
```
**Solution**: Use one of: `json`, `yaml`, `raw`.

### Connection Error
```bash
Error: Unable to connect to configuration service
```
**Solution**: Verify TrustGraph is running and URL is correct.

## Performance Tips

1. **Use raw format** for simple values to reduce parsing overhead
2. **Cache frequently accessed** configurations locally
3. **Specify version** when you know it to avoid version lookup
4. **Use specific keys** rather than retrieving full configuration

## Troubleshooting

### Empty or Null Values

If a configuration returns null:
- Verify the key name is exact (case-sensitive)
- Check if the configuration has been initialized
- Ensure proper permissions to access the configuration

### Format Issues

If output format is unexpected:
- Complex nested objects may not display well in raw format
- Use JSON or YAML for structured data
- Raw format works best for simple string/number values

### Version Problems

If version retrieval fails:
- Verify the version number exists
- Use latest version (omit --version) as fallback
- Check version history with service logs

## See Also

- [tg-list-config-items](tg-list-config-items) - List all configuration items
- [tg-put-config-item](tg-put-config-item) - Update configuration item
- [tg-show-config](tg-show-config) - Display complete system configuration
- [Config API](../apis/api-config) - Configuration service API documentation
