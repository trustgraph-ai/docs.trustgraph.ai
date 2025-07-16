---
title: tg-delete-tool
layout: default
parent: CLI
---

# tg-delete-tool

## Synopsis

```
tg-delete-tool [OPTIONS] --id ID
```

## Description

The `tg-delete-tool` command removes tool configurations from the TrustGraph system. This command deletes agent tool configurations by ID from the 'tool' configuration group, effectively removing tools from the system.

Once deleted, the tool will no longer be available for use by agents. The command includes safety checks to verify the tool exists before attempting deletion and provides clear feedback on the operation status.

Tools can be of various types including:
- **knowledge-query**: Tools that query knowledge bases
- **text-completion**: Tools for text generation
- **mcp-tool**: References to MCP (Model Context Protocol) tools
- **prompt**: Tools that execute prompt templates

## Options

- `-u, --api-url URL`
  - TrustGraph API URL to connect to
  - Default: `http://localhost:8088/` (or `TRUSTGRAPH_URL` environment variable)
  - Should point to a running TrustGraph API instance

- `--id ID`
  - **Required**: ID of the tool to delete
  - Must match an existing tool identifier
  - Case-sensitive

- `-h, --help`
  - Show help message and exit

## Examples

### Basic Tool Deletion

Remove a weather lookup tool:
```bash
tg-delete-tool --id weather
```

### Custom API URL

Delete tool from a specific TrustGraph instance:
```bash
tg-delete-tool --api-url http://localhost:9000/ --id calculator
```

### Remote Instance

Remove tool from a remote TrustGraph deployment:
```bash
tg-delete-tool -u http://trustgraph.example.com:8088/ --id file-reader
```

## Safety and Verification

The command includes built-in safety features:

### Pre-deletion Check
Before deletion, the command verifies the tool exists:
```bash
tg-delete-tool --id nonexistent-tool
# Output: Tool configuration for 'nonexistent-tool' not found.
```

### Successful Deletion Confirmation
When deletion succeeds:
```bash
tg-delete-tool --id weather
# Output: Tool 'weather' deleted successfully.
```

### Verification After Deletion
Confirm the tool was removed:
```bash
# List remaining tools
tg-show-tools

# Verify specific tool is gone
tg-show-tools | grep "weather" || echo "Tool successfully removed"
```

## Tool Type Considerations

### MCP Tools vs MCP Tool References

Be aware of the distinction between:
- **MCP tools**: Configured via `tg-set-mcp-tool` (stored in 'mcp' configuration group)
- **Agent tools**: May reference MCP tools (stored in 'tool' configuration group)

```bash
# This deletes an agent tool that references an MCP tool
tg-delete-tool --id weather-lookup

# This deletes the underlying MCP tool configuration
tg-delete-mcp-tool --id weather
```

### Cleanup Order

When removing MCP-based tools, consider the cleanup order:
```bash
# 1. First remove agent tools that reference MCP tools
tg-delete-tool --id weather-lookup

# 2. Then remove the underlying MCP tool if no longer needed
tg-delete-mcp-tool --id weather
```

## Batch Operations

### Delete Multiple Tools
```bash
#!/bin/bash
TOOLS=("weather" "calculator" "file-reader")

for tool in "${TOOLS[@]}"; do
    echo "Deleting tool: $tool"
    tg-delete-tool --id "$tool"
done
```

### Conditional Deletion
```bash
#!/bin/bash
# Delete tool only if it exists
if tg-show-tools | grep -q "weather"; then
    tg-delete-tool --id weather
    echo "Weather tool deleted"
else
    echo "Weather tool not found"
fi
```

### Type-based Cleanup
```bash
#!/bin/bash
echo "Removing all MCP-type tools..."

# Get list of MCP-type tools
mcp_tools=$(tg-show-tools | grep -B 3 "mcp-tool" | grep "id" | cut -d'|' -f3 | tr -d ' ')

for tool in $mcp_tools; do
    echo "Removing MCP tool: $tool"
    tg-delete-tool --id "$tool"
done
```

## Error Handling

The command handles various error conditions gracefully:

### Tool Not Found
```bash
tg-delete-tool --id nonexistent
# Output: Tool configuration for 'nonexistent' not found.
```

### API Connection Issues
```bash
tg-delete-tool --id weather -u http://invalid-host:8088/
# Output: Exception: [Connection error details]
```

### Permission Errors
```bash
# If API access is denied
# Output: Error deleting tool 'weather': [Permission error details]
```

### Network Timeouts
```bash
# If API request times out
# Output: Error deleting tool 'weather': [Timeout error details]
```

## Impact Assessment

Before deleting tools, assess their usage:

### Check Agent Dependencies
```bash
# Review agent configurations that might reference the tool
tg-show-config | grep -A 5 -B 5 "weather"
```

### Flow Usage Analysis
```bash
# Check if any flows are currently using the tool
tg-show-flows
tg-show-flow-state -f flow-id
```

### Historical Usage
```bash
# If logging is enabled, check tool usage history
# This would depend on your specific logging setup
grep "weather" /var/log/trustgraph/agent.log
```

## Workflow Integration

### Environment Cleanup
```bash
#!/bin/bash
echo "=== Cleaning up test tools ==="

# List all tools starting with 'test-'
test_tools=$(tg-show-tools | grep -E "test-" | grep "id" | cut -d'|' -f3 | tr -d ' ')

for tool in $test_tools; do
    echo "Removing test tool: $tool"
    tg-delete-tool --id "$tool"
done

echo "Test cleanup complete"
```

### Migration Script
```bash
#!/bin/bash
echo "=== Tool Configuration Migration ==="

# Export current tool configuration
tg-show-tools > old_tools_config.txt

# Remove deprecated tools
deprecated_tools=("old-weather" "legacy-calculator")
for tool in "${deprecated_tools[@]}"; do
    echo "Removing deprecated tool: $tool"
    tg-delete-tool --id "$tool"
done

# Add new tools (this would use tg-set-tool)
echo "Adding updated tools..."
# ... add new tool configurations ...

echo "Migration complete"
```

### Audit and Cleanup
```bash
#!/bin/bash
echo "=== Tool Audit and Cleanup ==="

# Count tools by type
echo "Tool inventory by type:"
for type in "knowledge-query" "text-completion" "mcp-tool" "prompt"; do
    count=$(tg-show-tools | grep -c "$type")
    echo "$type: $count tools"
done

# Find unused tools (this is a simplified example)
echo "Checking for potentially unused tools..."
tg-show-tools | grep "id" | while read line; do
    tool_id=$(echo "$line" | cut -d'|' -f3 | tr -d ' ')
    # This would need additional logic to check actual usage
    echo "Tool: $tool_id (usage check needed)"
done
```

## Recovery

If you accidentally delete a tool:

### Re-create from Documentation
If you have the tool configuration documented:
```bash
# Example recreation of a weather tool
tg-set-tool --id weather --name "Weather Lookup" \
  --type knowledge-query \
  --description "Get weather information for locations" \
  --collection weather-data \
  --argument location:string:"Location to query" \
  --argument units:string:"Temperature units (C/F)"
```

### Restore from Backup
```bash
# If you have configuration backups
# This would involve parsing backup files and recreating tools
source restore_tools.sh weather
```

### Recovery from Version Control
```bash
# If tool configurations are version controlled
git checkout HEAD~1 -- tools_config.json
# Then reimport tool configurations
```

## Best Practices

1. **Document configurations**: Keep records of tool configurations before deletion
2. **Check dependencies**: Verify no agents or flows depend on the tool
3. **Staged deletion**: Remove tools from test environments first
4. **Backup first**: Export tool configurations before major cleanup operations
5. **Monitor impact**: Check system functionality after tool removal

## Monitoring and Auditing

### Deletion Audit Trail
```bash
#!/bin/bash
tool_id="$1"
echo "Tool Deletion Audit - $(date)" >> tool_audit.log
echo "User: $(whoami)" >> tool_audit.log
echo "Tool ID: $tool_id" >> tool_audit.log
echo "Before deletion:" >> tool_audit.log
tg-show-tools | grep -A 10 "$tool_id" >> tool_audit.log
echo "Executing deletion..." >> tool_audit.log
tg-delete-tool --id "$tool_id" 2>&1 | tee -a tool_audit.log
```

### System Health Check
```bash
#!/bin/bash
echo "=== Post-deletion Health Check ==="
echo "Remaining tools:"
tool_count=$(tg-show-tools | grep -c "id.*|")
echo "Total tools: $tool_count"

echo "Tools by type:"
for type in "knowledge-query" "text-completion" "mcp-tool" "prompt"; do
    count=$(tg-show-tools | grep -c "$type")
    echo "  $type: $count"
done
```

## Advanced Usage

### Selective Cleanup by Type
```bash
#!/bin/bash
tool_type="$1"
echo "Removing all tools of type: $tool_type"

# This requires parsing the tool output to identify tools by type
# Implementation would depend on exact output format
tg-show-tools | grep -B 5 "$tool_type" | grep "id" | while read line; do
    tool_id=$(echo "$line" | cut -d'|' -f3 | tr -d ' ')
    echo "Removing $tool_type tool: $tool_id"
    tg-delete-tool --id "$tool_id"
done
```

### Configuration Validation
```bash
#!/bin/bash
echo "Validating tool configuration after cleanup..."

# Check that remaining tools are properly configured
tg-show-tools > current_tools.txt

# Validate each tool (simplified example)
echo "Checking tool integrity..."
if tg-show-tools > /dev/null 2>&1; then
    echo "✓ Tool configuration is valid"
else
    echo "✗ Tool configuration has issues"
fi
```

## Related Commands

- [`tg-set-tool`](tg-set-tool) - Configure agent tools
- [`tg-show-tools`](tg-show-tools) - Display all agent tools
- [`tg-delete-mcp-tool`](tg-delete-mcp-tool) - Remove MCP tool configurations
- [`tg-set-mcp-tool`](tg-set-mcp-tool) - Configure MCP tools
- [`tg-show-mcp-tools`](tg-show-mcp-tools) - Display MCP tool configurations

## See Also

- Agent Tool Configuration Guide
- MCP Tool Management
- TrustGraph Configuration Management
- Tool Development Guide