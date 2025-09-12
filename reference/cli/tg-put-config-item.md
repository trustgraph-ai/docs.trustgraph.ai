---
layout: default
title: tg-put-config-item
parent: CLI
---

# tg-put-config-item

Create or update a configuration item in the TrustGraph configuration service.

## Synopsis

```bash
tg-put-config-item -k KEY -v VALUE [OPTIONS]
tg-put-config-item -k KEY -f FILE [OPTIONS]
```

## Description

The `tg-put-config-item` command creates or updates configuration items in the TrustGraph configuration service. You can provide the configuration value directly on the command line, from a file, or via stdin. The command maintains version history and validates configuration format before storing.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `-k`, `--key KEY` | Configuration key to set | Required |
| `-v`, `--value VALUE` | Configuration value (JSON string) | - |
| `-f`, `--file FILE` | Read value from file | - |
| `--stdin` | Read value from stdin | - |
| `-u`, `--url URL` | TrustGraph API URL | `http://localhost:8088/` |
| `--format FORMAT` | Input format: `json`, `yaml`, `text` | `json` |
| `--force` | Skip validation and confirmation | false |
| `--backup` | Create backup before updating | false |
| `-h`, `--help` | Show help message | - |

## Input Methods

### Direct Value

Provide value directly on command line:

```bash
# Simple value
tg-put-config-item -k settings.max-tokens -v 4096

# JSON value
tg-put-config-item -k settings.limits -v '{"max_tokens": 4096, "timeout": 30}'

# String value
tg-put-config-item -k prompts.greeting -v "Hello, how can I help you today?"
```

### From File

Read configuration from a file:

```bash
# JSON file
tg-put-config-item -k flows.production -f production-flow.json

# YAML file
tg-put-config-item -k flows.staging -f staging-flow.yaml --format yaml

# Text file for prompts
tg-put-config-item -k prompts.system -f system-prompt.txt --format text
```

### From Stdin

Pipe configuration from another command:

```bash
# From echo
echo '{"temperature": 0.7}' | tg-put-config-item -k settings.llm --stdin

# From another command
tg-get-config-item -k flows.default | jq '.value' | tg-put-config-item -k flows.backup --stdin

# From heredoc
tg-put-config-item -k prompts.custom --stdin --format text << EOF
You are an expert assistant.
Always provide accurate information.
EOF
```

## Examples

### Basic Configuration Updates

```bash
# Update a simple setting
tg-put-config-item -k settings.temperature -v 0.8

# Update token costs
tg-put-config-item -k token-costs.gpt-4 -v '{"prompt": 0.03, "completion": 0.06}'

# Set a timeout value
tg-put-config-item -k settings.timeout -v 60
```

### Flow Configuration

```bash
# Create flow configuration file
cat > new-flow.json << EOF
{
  "class-name": "custom-flow",
  "description": "Custom processing flow",
  "interfaces": {
    "agent": {
      "request": "non-persistent://tg/request/agent:custom",
      "response": "non-persistent://tg/response/agent:custom"
    }
  }
}
EOF

# Upload flow configuration
tg-put-config-item -k flows.custom -f new-flow.json
```

### Prompt Management

```bash
# Update system prompt from file
tg-put-config-item -k prompts.system -f system-prompt.txt --format text

# Set inline prompt
tg-put-config-item -k prompts.greeting -v "Welcome! How can I assist you?" --format text

# Complex prompt with formatting
tg-put-config-item -k prompts.analysis --stdin --format text << 'EOF'
Analyze the following text and provide:
1. Main topics discussed
2. Key entities mentioned
3. Sentiment analysis
4. Summary in 2-3 sentences
EOF
```

### Backup and Update

```bash
# Backup current configuration before updating
tg-get-config-item -k flows.production -o backup-production.json
tg-put-config-item -k flows.production -f new-production.json

# Automated backup flag
tg-put-config-item -k flows.production -f updated-flow.json --backup
```

### Batch Updates

```bash
# Update multiple settings
for setting in temperature max_tokens timeout; do
  value=$(jq -r ".$setting" config.json)
  tg-put-config-item -k "settings.$setting" -v "$value"
done

# Import all prompts from directory
for file in prompts/*.txt; do
  key="prompts.$(basename $file .txt)"
  tg-put-config-item -k "$key" -f "$file" --format text
done
```

## Configuration Types

### JSON Objects

```bash
# Complex nested configuration
cat > service-config.json << EOF
{
  "endpoints": {
    "primary": "http://api.example.com",
    "backup": "http://backup.example.com"
  },
  "retry": {
    "attempts": 3,
    "delay": 1000
  }
}
EOF

tg-put-config-item -k settings.service -f service-config.json
```

### Arrays

```bash
# List configuration
tg-put-config-item -k settings.allowed-models -v '["gpt-4", "claude-3", "llama-2"]'

# Complex array
tg-put-config-item -k settings.endpoints -v '[
  {"name": "primary", "url": "http://primary.com"},
  {"name": "secondary", "url": "http://secondary.com"}
]'
```

### Simple Values

```bash
# String
tg-put-config-item -k settings.environment -v "production"

# Number
tg-put-config-item -k settings.max-retries -v 5

# Boolean
tg-put-config-item -k settings.debug -v true
```

## Validation

The command performs validation before storing:

```bash
# Invalid JSON will be rejected
$ tg-put-config-item -k settings.config -v '{invalid json}'
Error: Invalid JSON format

# Type validation for known keys
$ tg-put-config-item -k settings.max-tokens -v "not-a-number"
Error: Expected number for settings.max-tokens

# Skip validation with force flag
$ tg-put-config-item -k experimental.feature -v '{"test": true}' --force
Configuration updated (validation skipped)
```

## Safety Features

### Confirmation Prompts

For critical configurations, confirmation is required:

```bash
$ tg-put-config-item -k flows.production -f new-flow.json

Warning: Updating production flow configuration
Current version: 5
This change will affect running services.
Continue? (y/N):
```

### Backup Creation

```bash
# Automatic backup before update
$ tg-put-config-item -k flows.default -f updated.json --backup

Creating backup: flows.default.backup.20240115-103000
Configuration updated successfully
Previous version backed up to: flows.default.backup.20240115-103000
```

### Version Tracking

Each update creates a new version:

```bash
$ tg-put-config-item -k prompts.system -v "New prompt"

Configuration updated:
  Key: prompts.system
  New version: 4
  Previous version: 3
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `TRUSTGRAPH_URL` | Default API URL | `http://localhost:8088/` |
| `TRUSTGRAPH_CONFIG_BACKUP` | Auto-backup directory | `~/.trustgraph/backups/` |

## Exit Codes

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | Error (validation failed, service error, etc.) |
| 2 | User cancelled operation |

## Error Handling

Common errors and solutions:

### Validation Error
```bash
Error: Configuration validation failed: Missing required field 'interfaces'
```
**Solution**: Check configuration format against schema.

### Permission Denied
```bash
Error: Permission denied for key 'system.core'
```
**Solution**: Some keys may be read-only or require admin access.

### Conflict Error
```bash
Error: Configuration conflict - version mismatch
```
**Solution**: Another process updated the configuration. Retrieve latest and retry.

## Best Practices

1. **Always backup** critical configurations before updating
2. **Validate locally** complex JSON before uploading
3. **Use version control** for configuration files
4. **Test in staging** before updating production configurations
5. **Document changes** in commit messages or logs

## Advanced Usage

### Templating

```bash
# Use environment variables in configuration
cat > config-template.json << EOF
{
  "environment": "$ENVIRONMENT",
  "api_url": "$API_URL",
  "max_tokens": $MAX_TOKENS
}
EOF

# Substitute and upload
envsubst < config-template.json | tg-put-config-item -k settings.app --stdin
```

### Atomic Updates

```bash
# Update multiple related configs atomically
cat > update-script.sh << 'EOF'
#!/bin/bash
set -e  # Exit on any error

tg-put-config-item -k settings.feature-flag -v true
tg-put-config-item -k settings.feature-config -f feature.json
tg-put-config-item -k prompts.feature -f feature-prompt.txt --format text

echo "Feature configuration completed"
EOF

chmod +x update-script.sh
./update-script.sh
```

## Troubleshooting

### Large Configuration Files

For very large configurations:
- Consider splitting into multiple smaller configurations
- Use compression if supported
- Increase timeout values if needed

### Format Detection Issues

If format is not detected correctly:
- Explicitly specify `--format` parameter
- Ensure file extensions match content type
- Validate JSON/YAML syntax before uploading

### Network Issues

For unreliable connections:
- Use `--backup` flag for safety
- Implement retry logic in scripts
- Consider local validation before upload

## See Also

- [tg-get-config-item](tg-get-config-item) - Retrieve configuration item
- [tg-list-config-items](tg-list-config-items) - List all configuration items
- [tg-show-config](tg-show-config) - Display complete system configuration
- [Config API](../apis/api-config) - Configuration service API documentation
