---
title: tg-invoke-mcp-tool
parent: CLI
review_date: 2026-04-16
---

# tg-invoke-mcp-tool

## Synopsis

```
tg-invoke-mcp-tool [OPTIONS] -n TOOL_NAME [-P PARAMETERS]
```

## Description

The `tg-invoke-mcp-tool` command invokes MCP (Model Context Protocol) tools through the TrustGraph API. This allows you to test MCP tool functionality, debug tool configurations, and execute MCP tools directly from the command line.

The command calls MCP tools by specifying the tool name and providing parameters as a JSON-encoded dictionary. The tool is executed within the context of a specified flow, allowing it to access flow-specific resources and state.

This is particularly useful for:
- Testing MCP tool functionality and connectivity
- Debugging MCP tool configurations
- Prototyping MCP tool integrations
- Manual execution of MCP tools for one-off tasks
- Validating MCP tool responses and behavior

## Options

- `-u, --url URL`
  - TrustGraph API URL to connect to
  - Default: `http://localhost:8088/` (or `TRUSTGRAPH_URL` environment variable)
  - Should point to a running TrustGraph API instance

- `-f, --flow-id FLOW_ID`
  - Flow identifier for the execution context
  - Default: `default`
  - The MCP tool will be executed within this flow's context

- `-n, --name TOOL_NAME`
  - **Required**: Name of the MCP tool to invoke
  - Must match a configured MCP tool identifier
  - Case-sensitive

- `-P, --parameters JSON`
  - Tool parameters as a JSON-encoded dictionary
  - Optional: defaults to empty parameters `{}`
  - Must be valid JSON format

- `-h, --help`
  - Show help message and exit

## Examples

### Basic MCP Tool Invocation

Invoke a simple MCP tool without parameters:
```bash
tg-invoke-mcp-tool -n weather
```

### MCP Tool with Parameters

Invoke a weather tool with location parameter:
```bash
tg-invoke-mcp-tool -n weather -P '{"location": "New York", "units": "celsius"}'
```

### Calculator MCP Tool

Execute a calculation using an MCP calculator tool:
```bash
tg-invoke-mcp-tool -n calculator -P '{"expression": "2 + 2 * 3"}'
```

### Custom Flow Context

Invoke MCP tool within a specific flow:
```bash
tg-invoke-mcp-tool -f my-analysis-flow -n data-processor \
  -P '{"dataset": "sales_data", "operation": "summarize"}'
```

### Complex Parameters

Use complex JSON parameters for advanced MCP tools:
```bash
tg-invoke-mcp-tool -n document-analyzer -P '{
  "document_id": "doc123",
  "analysis_type": "sentiment",
  "options": {
    "include_entities": true,
    "confidence_threshold": 0.8
  }
}'
```

### Remote TrustGraph Instance

Invoke MCP tool on a remote TrustGraph instance:
```bash
tg-invoke-mcp-tool -u http://trustgraph.example.com:8088/ \
  -n search-engine -P '{"query": "machine learning", "limit": 10}'
```

## Parameter Format

Parameters must be provided as valid JSON. Common parameter patterns:

### String Parameters
```bash
tg-invoke-mcp-tool -n text-processor -P '{"text": "Hello, world!"}'
```

### Numeric Parameters
```bash
tg-invoke-mcp-tool -n calculator -P '{"x": 10, "y": 20, "operation": "multiply"}'
```

### Boolean Parameters
```bash
tg-invoke-mcp-tool -n file-processor -P '{"validate": true, "backup": false}'
```

### Array Parameters
```bash
tg-invoke-mcp-tool -n batch-processor -P '{"items": ["item1", "item2", "item3"]}'
```

### Nested Objects
```bash
tg-invoke-mcp-tool -n advanced-tool -P '{
  "config": {
    "mode": "production",
    "settings": {
      "timeout": 30,
      "retries": 3
    }
  }
}'
```

## Output Format

The command displays the MCP tool response in a readable format:

### String Response
```bash
$ tg-invoke-mcp-tool -n weather -P '{"location": "London"}'
Current weather in London: 15°C, partly cloudy with light rain expected.
```

### JSON Response
```bash
$ tg-invoke-mcp-tool -n calculator -P '{"expression": "2 + 2"}'
{
    "result": 4,
    "expression": "2 + 2",
    "type": "arithmetic"
}
```

### Complex Response
```bash
$ tg-invoke-mcp-tool -n search-engine -P '{"query": "AI"}'
{
    "results": [
        {
            "title": "Artificial Intelligence Overview",
            "url": "https://example.com/ai-overview",
            "snippet": "Introduction to AI concepts..."
        }
    ],
    "total_results": 1,
    "query_time": 0.25
}
```

## Testing and Debugging

### MCP Tool Connectivity Test

Test if an MCP tool is responding:
```bash
#!/bin/bash
echo "Testing MCP tool connectivity..."

# Test with minimal parameters
if tg-invoke-mcp-tool -n weather -P '{}' > /dev/null 2>&1; then
    echo "✓ Weather MCP tool is responding"
else
    echo "✗ Weather MCP tool is not responding"
fi
```

### Parameter Validation

Test MCP tool parameter validation:
```bash
#!/bin/bash
echo "Testing MCP tool parameter validation..."

# Test with invalid parameters
echo "Testing invalid parameters..."
tg-invoke-mcp-tool -n calculator -P '{"invalid": "parameter"}'

# Test with missing required parameters
echo "Testing missing parameters..."
tg-invoke-mcp-tool -n calculator -P '{}'

# Test with valid parameters
echo "Testing valid parameters..."
tg-invoke-mcp-tool -n calculator -P '{"expression": "1 + 1"}'
```

### Response Format Testing

Verify MCP tool response formats:
```bash
#!/bin/bash
tools=("weather" "calculator" "search-engine")

for tool in "${tools[@]}"; do
    echo "Testing $tool response format..."
    response=$(tg-invoke-mcp-tool -n "$tool" -P '{}' 2>/dev/null)
    
    if echo "$response" | jq . > /dev/null 2>&1; then
        echo "✓ $tool returns valid JSON"
    else
        echo "ℹ $tool returns plain text"
    fi
done
```

## Error Handling

The command handles various error conditions:

### MCP Tool Not Found
```bash
tg-invoke-mcp-tool -n nonexistent-tool
# Output: Exception: [Tool not found error]
```

### Invalid JSON Parameters
```bash
tg-invoke-mcp-tool -n weather -P "invalid-json"
# Output: Exception: [JSON parsing error]
```

### MCP Server Connection Error
```bash
# If the MCP server is not available
tg-invoke-mcp-tool -n weather -P '{}'
# Output: Exception: [MCP server connection error]
```

### API Connection Issues
```bash
tg-invoke-mcp-tool -n weather -u http://invalid-host:8088/
# Output: Exception: [API connection error]
```

### Missing Required Parameters
```bash
tg-invoke-mcp-tool -n calculator -P '{}'
# Output: Exception: [Missing required parameter error]
```

## Workflow Integration

### Automated Testing

Create automated tests for MCP tools:
```bash
#!/bin/bash
echo "=== MCP Tools Test Suite ==="

test_cases=(
    "weather:{\"location\":\"London\"}"
    "calculator:{\"expression\":\"2+2\"}"
    "search-engine:{\"query\":\"test\"}"
)

for test_case in "${test_cases[@]}"; do
    tool=$(echo "$test_case" | cut -d: -f1)
    params=$(echo "$test_case" | cut -d: -f2-)
    
    echo "Testing $tool..."
    if tg-invoke-mcp-tool -n "$tool" -P "$params" > /dev/null 2>&1; then
        echo "✓ $tool test passed"
    else
        echo "✗ $tool test failed"
    fi
done
```

### Performance Testing

Measure MCP tool response times:
```bash
#!/bin/bash
tool_name="$1"
parameters="$2"

echo "Performance testing MCP tool: $tool_name"

for i in {1..5}; do
    start_time=$(date +%s.%N)
    tg-invoke-mcp-tool -n "$tool_name" -P "$parameters" > /dev/null 2>&1
    end_time=$(date +%s.%N)
    
    duration=$(echo "$end_time - $start_time" | bc)
    echo "Run $i: ${duration}s"
done
```

### Data Pipeline Integration

Use MCP tools in data processing pipelines:
```bash
#!/bin/bash
echo "Processing documents with MCP tools..."

# Get list of documents
documents=$(ls /data/documents/*.txt)

for doc in $documents; do
    echo "Processing: $doc"
    
    # Extract text
    text=$(cat "$doc")
    
    # Analyze with MCP tool
    result=$(tg-invoke-mcp-tool -n document-analyzer \
        -P "{\"text\":\"$text\",\"type\":\"sentiment\"}")
    
    echo "Analysis result: $result"
done
```

## Best Practices

1. **Parameter validation**: Always validate JSON parameters before execution
2. **Error handling**: Implement proper error handling for production use
3. **Testing**: Test MCP tools regularly to ensure availability
4. **Logging**: Log MCP tool invocations for audit and debugging
5. **Security**: Validate and sanitize input parameters

## Security Considerations

- Validate all input parameters to prevent injection attacks
- Ensure MCP tools have appropriate access controls
- Monitor MCP tool usage for unusual patterns
- Use secure communication channels for sensitive data

## Troubleshooting

### Tool Execution Failures

If MCP tool execution fails:
1. Verify the tool exists: `tg-show-mcp-tools | grep tool-name`
2. Check MCP server connectivity
3. Validate parameter format and content
4. Review MCP server logs for errors

### Parameter Issues

If parameters are not accepted:
1. Validate JSON format: `echo '{"param":"value"}' | jq .`
2. Check required parameters in tool documentation
3. Verify parameter types and values
4. Test with minimal parameter set

### Flow Context Issues

If flow-related errors occur:
1. Verify the flow exists: `tg-show-flows`
2. Check flow status: `tg-show-flow-state -f flow-id`
3. Ensure flow has necessary permissions
4. Try with default flow context

## Related Commands

- [`tg-set-mcp-tool`](tg-set-mcp-tool) - Configure MCP tools
- [`tg-show-mcp-tools`](tg-show-mcp-tools) - Display MCP tool configurations
- [`tg-delete-mcp-tool`](tg-delete-mcp-tool) - Remove MCP tool configuration
- [`tg-invoke-agent`](tg-invoke-agent) - Invoke agents that may use MCP tools
- [`tg-show-flows`](tg-show-flows) - Display available flows

## See Also

- Model Context Protocol Specification
- TrustGraph MCP Integration Guide
- Agent Tool Testing Guide