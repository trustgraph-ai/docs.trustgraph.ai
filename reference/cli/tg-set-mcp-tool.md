---
title: tg-set-mcp-tool
layout: default
parent: CLI
---

# tg-set-mcp-tool

## Synopsis

```
tg-set-mcp-tool [OPTIONS] --id ID --tool-url URL
```

## Description

The `tg-set-mcp-tool` command configures and registers MCP (Model Context Protocol) tools in the TrustGraph system. MCP tools are external services that follow the Model Context Protocol specification and can be integrated with TrustGraph agents.

This command stores MCP tool configurations in the 'mcp' configuration group with:
- **id**: Unique identifier for the tool
- **remote-name**: Name used by the MCP server (defaults to id if not specified)
- **url**: MCP server endpoint URL

Once configured, MCP tools can be referenced by agent tools using the 'mcp-tool' type via the `tg-set-tool` command.

## Options

- `-u, --api-url URL`
  - TrustGraph API URL to connect to
  - Default: `http://localhost:8088/` (or `TRUSTGRAPH_URL` environment variable)
  - Should point to a running TrustGraph API instance

- `-i, --id ID`
  - **Required**: Unique identifier for the MCP tool
  - Used to reference the tool in agent configurations
  - Must be unique within the MCP tool namespace

- `-r, --remote-name NAME`
  - Optional: Name used by the MCP server
  - Defaults to the value of `--id` if not specified
  - Useful when the MCP server expects a different name than the local identifier

- `--tool-url URL`
  - **Required**: MCP server endpoint URL
  - Should point to a running MCP server that implements the Model Context Protocol
  - Must be a valid HTTP/HTTPS URL

- `-h, --help`
  - Show help message and exit

## Examples

### Basic MCP Tool Configuration

Register a weather MCP tool:
```bash
tg-set-mcp-tool --id weather --tool-url "http://localhost:3000/weather"
```

### MCP Tool with Custom Remote Name

Register a calculator tool with a different remote name:
```bash
tg-set-mcp-tool --id calculator --remote-name calc-service --tool-url "http://mcp-tools.example.com/calc"
```

### Custom API URL

Configure MCP tool on a specific TrustGraph instance:
```bash
tg-set-mcp-tool -u http://trustgraph.example.com:8088/ \
  --id file-reader --tool-url "http://localhost:4000/files"
```

### Remote MCP Server

Configure tool pointing to a remote MCP server:
```bash
tg-set-mcp-tool --id search-engine \
  --tool-url "https://mcp-services.example.com/search" \
  --remote-name web-search
```

## Integration with Agent Tools

After configuring an MCP tool, it can be used by agents through the `tg-set-tool` command:

```bash
# First, configure the MCP tool
tg-set-mcp-tool --id weather --tool-url "http://localhost:3000/weather"

# Then, create an agent tool that uses the MCP tool
tg-set-tool --id weather-lookup --name "Weather Lookup" \
  --type mcp-tool --mcp-tool weather \
  --description "Get weather information for a location" \
  --argument location:string:"Location to query" \
  --argument units:string:"Temperature units (C/F)"
```

## Configuration Storage

MCP tool configurations are stored in the TrustGraph configuration system under the 'mcp' type with the following JSON structure:

```json
{
  "remote-name": "weather-service",
  "url": "http://localhost:3000/weather"
}
```

## MCP Protocol Requirements

The MCP tool URL should point to a server that implements the Model Context Protocol specification. The server should:

1. Accept HTTP POST requests with MCP-compliant message format
2. Return responses in the expected MCP format
3. Handle authentication and authorization as needed
4. Provide proper error handling and status codes

## Error Handling

The command handles various error conditions:

- **Invalid URL format**: If the tool URL is malformed
- **API connection errors**: If the TrustGraph API is unavailable
- **Authentication errors**: If API access is denied
- **Configuration errors**: If the tool configuration cannot be stored

Common error scenarios:
```bash
# Invalid tool URL
tg-set-mcp-tool --id test --tool-url "not-a-valid-url"
# Output: Exception: [URL validation error]

# API not available
tg-set-mcp-tool --id test --tool-url "http://localhost:3000" -u http://invalid-host:8088/
# Output: Exception: [Connection error details]

# Missing required arguments
tg-set-mcp-tool --id test
# Output: Exception: Must specify --tool-url for MCP tool
```

## Verification

After configuring an MCP tool, verify it was stored correctly:

```bash
# List all MCP tools
tg-show-mcp-tools

# Check if specific tool exists
tg-show-mcp-tools | grep -A 5 "weather"
```

## Best Practices

1. **Use descriptive IDs**: Choose clear, descriptive identifiers for MCP tools
2. **Test connectivity**: Verify the MCP server is accessible before configuration
3. **Document tools**: Keep track of MCP tool purposes and configurations
4. **Monitor health**: Regularly check that MCP servers are responding correctly
5. **Version control**: Track MCP tool configuration changes

## Security Considerations

- Ensure MCP server URLs use HTTPS in production environments
- Validate that MCP servers implement proper authentication
- Review MCP tool permissions and capabilities
- Monitor MCP tool usage and access patterns

## Related Commands

- [`tg-show-mcp-tools`](tg-show-mcp-tools) - Display configured MCP tools
- [`tg-delete-mcp-tool`](tg-delete-mcp-tool) - Remove MCP tool configuration
- [`tg-invoke-mcp-tool`](tg-invoke-mcp-tool) - Test MCP tool functionality
- [`tg-set-tool`](tg-set-tool) - Configure agent tools that use MCP tools
- [`tg-show-tools`](tg-show-tools) - Display all agent tools

## See Also

- Model Context Protocol Specification
- TrustGraph Agent Tool Configuration
- MCP Integration Guide