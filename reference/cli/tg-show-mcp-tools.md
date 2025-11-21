---
title: tg-show-mcp-tools
parent: CLI
review_date: 2026-04-28
---

# tg-show-mcp-tools

## Synopsis

```
tg-show-mcp-tools [OPTIONS]
```

## Description

The `tg-show-mcp-tools` command displays the current MCP (Model Context Protocol) tool configuration from TrustGraph. It retrieves and presents detailed information about all configured MCP tools, including their identifiers, remote names, and endpoint URLs.

This command is useful for:
- Understanding available MCP tools and their configurations
- Debugging MCP tool connectivity issues
- Documenting the current MCP tool set
- Verifying MCP tool definitions and endpoints
- Auditing MCP tool configurations

The command queries the TrustGraph API to fetch all MCP tool configurations from the 'mcp' configuration group and presents them in a formatted table for easy reading.

## Options

- `-u, --api-url URL`
  - TrustGraph API URL to query for MCP tool configuration
  - Default: `http://localhost:8088/` (or `TRUSTGRAPH_URL` environment variable)
  - Should point to a running TrustGraph API instance

- `-h, --help`
  - Show help message and exit

## Examples

### Basic Usage

Display all configured MCP tools using the default API URL:
```bash
tg-show-mcp-tools
```

### Custom API URL

Display MCP tools from a specific TrustGraph instance:
```bash
tg-show-mcp-tools -u http://trustgraph.example.com:8088/
```

### Remote Instance

Query MCP tools from a remote TrustGraph deployment:
```bash
tg-show-mcp-tools --api-url http://10.0.1.100:8088/
```

### Using Environment Variable

Set the API URL via environment variable:
```bash
export TRUSTGRAPH_URL=http://production.trustgraph.com:8088/
tg-show-mcp-tools
```

## Output Format

The command displays each MCP tool in a detailed table format:

```
+-------------+----------------------------------------------------------------------+
| id          | weather                                                              |
+-------------+----------------------------------------------------------------------+
| remote-name | weather-service                                                      |
+-------------+----------------------------------------------------------------------+
| url         | http://localhost:3000/weather                                        |
+-------------+----------------------------------------------------------------------+


+-------------+----------------------------------------------------------------------+
| id          | calculator                                                           |
+-------------+----------------------------------------------------------------------+
| remote-name | calc-service                                                         |
+-------------+----------------------------------------------------------------------+
| url         | https://mcp-tools.example.com/calc                                   |
+-------------+----------------------------------------------------------------------+
```

For each MCP tool, the output includes:
- **id**: Unique identifier used locally to reference the tool
- **remote-name**: Name used by the MCP server (may differ from local id)
- **url**: MCP server endpoint URL where the tool can be accessed

## Advanced Usage

### MCP Tool Inventory

Create a complete inventory of available MCP tools:
```bash
#!/bin/bash
echo "=== TrustGraph MCP Tools Inventory ==="
echo "Generated on: $(date)"
echo
tg-show-mcp-tools > mcp_tools_inventory.txt
echo "MCP tools inventory saved to mcp_tools_inventory.txt"
```

### MCP Tool Comparison

Compare MCP tools across different environments:
```bash
#!/bin/bash
echo "=== Development MCP Tools ==="
tg-show-mcp-tools -u http://dev.trustgraph.com:8088/ > dev_mcp_tools.txt
echo
echo "=== Production MCP Tools ==="
tg-show-mcp-tools -u http://prod.trustgraph.com:8088/ > prod_mcp_tools.txt
echo
echo "=== Differences ==="
diff dev_mcp_tools.txt prod_mcp_tools.txt
```

### Health Check Script

Verify MCP tool configurations and connectivity:
```bash
#!/bin/bash
echo "=== MCP Tools Health Check ==="
tg-show-mcp-tools | grep -E "^\| url" | sed 's/^| url *| //' | sed 's/ *|$//' | while read url; do
    if curl -s --max-time 5 "$url" > /dev/null; then
        echo "✓ $url - Accessible"
    else
        echo "✗ $url - Not accessible"
    fi
done
```

### MCP Tool Documentation

Generate documentation for MCP tools:
```bash
#!/bin/bash
echo "# Available MCP Tools" > MCP_TOOLS.md
echo "" >> MCP_TOOLS.md
echo "Generated on: $(date)" >> MCP_TOOLS.md
echo "" >> MCP_TOOLS.md
echo '```' >> MCP_TOOLS.md
tg-show-mcp-tools >> MCP_TOOLS.md
echo '```' >> MCP_TOOLS.md
```

## Integration Examples

### With Agent Tool Analysis

Show MCP tools alongside their usage in agent tools:
```bash
#!/bin/bash
echo "=== MCP Tools Configuration ==="
tg-show-mcp-tools
echo
echo "=== Agent Tools Using MCP ==="
tg-show-tools | grep -A 5 "mcp-tool"
```

### Configuration Validation

Validate MCP tool configuration consistency:
```bash
#!/bin/bash
echo "Validating MCP tool configuration..."

# Get list of MCP tool IDs
mcp_ids=$(tg-show-mcp-tools | grep -E "^\| id" | sed 's/^| id *| //' | sed 's/ *|$//')

# Check if they're referenced by agent tools
for id in $mcp_ids; do
    if tg-show-tools | grep -q "mcp-tool.*$id"; then
        echo "✓ MCP tool '$id' is referenced by agent tools"
    else
        echo "⚠ MCP tool '$id' is not referenced by any agent tools"
    fi
done
```

### Backup Configuration

Create a backup of MCP tool configurations:
```bash
#!/bin/bash
backup_dir="mcp_backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$backup_dir"

echo "Backing up MCP tool configurations..."
tg-show-mcp-tools > "$backup_dir/mcp_tools.txt"

# Extract individual tool configurations
tg-show-mcp-tools | grep -E "^\| id" | sed 's/^| id *| //' | sed 's/ *|$//' | while read id; do
    echo "Backing up MCP tool: $id"
    # Note: This would need additional logic to extract individual tool configs
done

echo "Backup completed in: $backup_dir"
```

## Error Handling

The command handles various error conditions:

- **API connection errors**: If the TrustGraph API is unavailable
- **Authentication errors**: If API access is denied
- **Configuration errors**: If MCP tool configuration is malformed
- **Network timeouts**: If API requests time out

Common error scenarios:
```bash
# API not available
tg-show-mcp-tools -u http://invalid-host:8088/
# Output: Exception: [Connection error details]

# Invalid API URL
tg-show-mcp-tools --api-url "not-a-url"
# Output: Exception: [URL parsing error]

# No MCP tools configured
# Output: (empty output - no tables displayed)
```

## Monitoring and Maintenance

### Regular Health Checks

Monitor MCP tool availability:
```bash
#!/bin/bash
echo "=== MCP Tools Status Check - $(date) ==="

# Check if any MCP tools are configured
if tg-show-mcp-tools | grep -q "id"; then
    echo "✓ MCP tools are configured"
    tool_count=$(tg-show-mcp-tools | grep -c "^\| id")
    echo "✓ Found $tool_count MCP tools"
else
    echo "⚠ No MCP tools configured"
fi
```

### Configuration Drift Detection

Monitor for configuration changes:
```bash
#!/bin/bash
current_config="current_mcp_config.txt"
previous_config="previous_mcp_config.txt"

# Save current configuration
tg-show-mcp-tools > "$current_config"

# Compare with previous if it exists
if [ -f "$previous_config" ]; then
    if diff -q "$current_config" "$previous_config" > /dev/null; then
        echo "✓ MCP configuration unchanged"
    else
        echo "⚠ MCP configuration has changed:"
        diff "$previous_config" "$current_config"
    fi
fi

# Update previous configuration
cp "$current_config" "$previous_config"
```

## Troubleshooting

### No MCP Tools Displayed

If no MCP tools are shown:
1. Verify the TrustGraph API is running and accessible
2. Check that MCP tool configurations have been properly set
3. Ensure the API URL is correct
4. Verify network connectivity

### Incomplete MCP Tool Information

If MCP tool information is missing or incomplete:
1. Check the MCP tool configuration files
2. Verify the configuration was stored correctly
3. Ensure MCP tool definitions are valid JSON
4. Check for configuration loading errors

### MCP Tool Connectivity Issues

If MCP tools are not responding:
1. Verify MCP server URLs are accessible
2. Check MCP server health and status
3. Validate network connectivity to MCP endpoints
4. Review MCP server logs for errors

## Best Practices

1. **Regular monitoring**: Check MCP tool configurations regularly
2. **Documentation**: Keep MCP tool configurations documented
3. **Health checks**: Monitor MCP server availability
4. **Version control**: Track MCP tool configuration changes
5. **Security**: Review MCP tool endpoints and access patterns

## Related Commands

- [`tg-set-mcp-tool`](tg-set-mcp-tool) - Configure MCP tools
- [`tg-delete-mcp-tool`](tg-delete-mcp-tool) - Remove MCP tool configuration
- [`tg-invoke-mcp-tool`](tg-invoke-mcp-tool) - Test MCP tool functionality
- [`tg-show-tools`](tg-show-tools) - Display all agent tools
- [`tg-show-config`](tg-show-config) - Show TrustGraph configuration

## See Also

- Model Context Protocol Documentation
- TrustGraph MCP Integration Guide
- Agent Tool Configuration Guide