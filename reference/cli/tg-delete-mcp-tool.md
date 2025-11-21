---
title: tg-delete-mcp-tool
parent: CLI
review_date: 2025-11-21
---

# tg-delete-mcp-tool

## Synopsis

```
tg-delete-mcp-tool [OPTIONS] --id ID
```

## Description

The `tg-delete-mcp-tool` command removes MCP (Model Context Protocol) tool configurations from the TrustGraph system. This command deletes MCP tool configurations by ID from the 'mcp' configuration group.

Once deleted, the MCP tool will no longer be available for use by agent tools. Any agent tools that reference the deleted MCP tool will need to be updated or removed.

The command includes safety checks to verify the tool exists before attempting deletion and provides clear feedback on the operation status.

## Options

- `-u, --api-url URL`
  - TrustGraph API URL to connect to
  - Default: `http://localhost:8088/` (or `TRUSTGRAPH_URL` environment variable)
  - Should point to a running TrustGraph API instance

- `--id ID`
  - **Required**: ID of the MCP tool to delete
  - Must match an existing MCP tool identifier
  - Case-sensitive

- `-h, --help`
  - Show help message and exit

## Examples

### Basic MCP Tool Deletion

Remove a weather MCP tool:
```bash
tg-delete-mcp-tool --id weather
```

### Custom API URL

Delete MCP tool from a specific TrustGraph instance:
```bash
tg-delete-mcp-tool --api-url http://localhost:9000/ --id calculator
```

### Remote Instance

Remove MCP tool from a remote TrustGraph deployment:
```bash
tg-delete-mcp-tool -u http://trustgraph.example.com:8088/ --id file-reader
```

## Safety and Verification

The command includes built-in safety features:

### Pre-deletion Check
Before deletion, the command verifies the MCP tool exists:
```bash
tg-delete-mcp-tool --id nonexistent-tool
# Output: MCP tool 'nonexistent-tool' not found.
```

### Successful Deletion Confirmation
When deletion succeeds:
```bash
tg-delete-mcp-tool --id weather
# Output: MCP tool 'weather' deleted successfully.
```

### Verification After Deletion
Confirm the tool was removed:
```bash
# List remaining MCP tools
tg-show-mcp-tools

# Verify specific tool is gone
tg-show-mcp-tools | grep "weather" || echo "Tool successfully removed"
```

## Impact on Dependent Agent Tools

Before deleting an MCP tool, consider its usage by agent tools:

### Check for Dependencies
```bash
# Show all agent tools and check for MCP tool references
tg-show-tools | grep -A 10 -B 5 "mcp-tool.*weather"
```

### Clean Up Dependent Tools
If agent tools reference the MCP tool being deleted:
```bash
# Remove dependent agent tools first
tg-delete-tool --id weather-lookup

# Then remove the MCP tool
tg-delete-mcp-tool --id weather
```

## Batch Operations

### Delete Multiple MCP Tools
```bash
#!/bin/bash
MCP_TOOLS=("weather" "calculator" "file-reader")

for tool in "${MCP_TOOLS[@]}"; do
    echo "Deleting MCP tool: $tool"
    tg-delete-mcp-tool --id "$tool"
done
```

### Conditional Deletion
```bash
#!/bin/bash
# Delete MCP tool only if it exists
if tg-show-mcp-tools | grep -q "weather"; then
    tg-delete-mcp-tool --id weather
    echo "Weather MCP tool deleted"
else
    echo "Weather MCP tool not found"
fi
```

## Error Handling

The command handles various error conditions gracefully:

### Tool Not Found
```bash
tg-delete-mcp-tool --id nonexistent
# Output: MCP tool 'nonexistent' not found.
```

### API Connection Issues
```bash
tg-delete-mcp-tool --id weather -u http://invalid-host:8088/
# Output: Exception: [Connection error details]
```

### Permission Errors
```bash
# If API access is denied
# Output: Error deleting MCP tool 'weather': [Permission error details]
```

### Network Timeouts
```bash
# If API request times out
# Output: Error deleting MCP tool 'weather': [Timeout error details]
```

## Workflow Integration

### Environment Cleanup
```bash
#!/bin/bash
echo "=== Cleaning up test MCP tools ==="

# List all MCP tools starting with 'test-'
test_tools=$(tg-show-mcp-tools | grep -E "^test-" | cut -d: -f1)

for tool in $test_tools; do
    echo "Removing test MCP tool: $tool"
    tg-delete-mcp-tool --id "$tool"
done

echo "Test cleanup complete"
```

### Configuration Migration
```bash
#!/bin/bash
echo "=== Migrating MCP tool configuration ==="

# Export current configuration
tg-show-mcp-tools > old_mcp_config.txt

# Remove old tools
tg-delete-mcp-tool --id old-weather-service

# Add new tools
tg-set-mcp-tool --id weather --tool-url "http://new-weather-api:3000"

echo "Migration complete"
```

## Recovery

If you accidentally delete an MCP tool:

### Re-create from Documentation
```bash
# If you have the configuration documented
tg-set-mcp-tool --id weather \
  --tool-url "http://localhost:3000/weather" \
  --remote-name weather-service
```

### Restore from Backup
```bash
# If you have configuration backups
# Parse backup file and recreate tools
source restore_mcp_tools.sh
```

## Best Practices

1. **Verify dependencies**: Check for agent tools using the MCP tool before deletion
2. **Backup configurations**: Keep records of MCP tool configurations
3. **Clean up dependencies**: Remove dependent agent tools first
4. **Test after deletion**: Verify system functionality after removing tools
5. **Document changes**: Record why MCP tools were removed

## Monitoring

### Audit Trail
```bash
#!/bin/bash
echo "MCP Tool Deletion Audit - $(date)" >> mcp_audit.log
echo "Deleting MCP tool: $1" >> mcp_audit.log
tg-delete-mcp-tool --id "$1" 2>&1 | tee -a mcp_audit.log
```

### System Health Check
```bash
#!/bin/bash
echo "=== Post-deletion Health Check ==="
echo "Remaining MCP tools:"
tg-show-mcp-tools

echo "Agent tools status:"
tg-show-tools | grep -c "mcp-tool" || echo "No MCP-based agent tools found"
```

## Related Commands

- [`tg-set-mcp-tool`](tg-set-mcp-tool) - Configure MCP tools
- [`tg-show-mcp-tools`](tg-show-mcp-tools) - Display MCP tool configurations
- [`tg-invoke-mcp-tool`](tg-invoke-mcp-tool) - Test MCP tool functionality
- [`tg-delete-tool`](tg-delete-tool) - Remove agent tools
- [`tg-show-tools`](tg-show-tools) - Display all agent tools

## See Also

- MCP Tool Configuration Guide
- Agent Tool Management
- TrustGraph Configuration Management