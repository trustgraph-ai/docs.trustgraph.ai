---
title: tg-set-tool
parent: CLI
review_date: 2025-11-21
---

# tg-set-tool

## Synopsis

```
tg-set-tool [OPTIONS] --id ID --name NAME --type TYPE [--argument ARG...]
```

## Description

The `tg-set-tool` command configures and registers agent tools in the TrustGraph system. This script allows you to define various types of tools that agents can use to perform specific tasks and operations.

Tools are stored in the 'tool' configuration group and can include argument specifications for parameterized execution. The system supports multiple tool types to cover different use cases and integration patterns.

## Tool Types

The system supports the following tool types:

### knowledge-query
Query knowledge bases and graph data structures.
- Used for retrieving information from loaded knowledge cores
- Requires `--collection` parameter to specify the knowledge collection
- Ideal for fact-finding and information retrieval tasks

### text-completion  
Text generation and completion services.
- Used for generating text content using language models
- Typically used for creative writing, summarization, and text transformation
- Can be parameterized for different completion styles and requirements

### mcp-tool
Reference to MCP (Model Context Protocol) tools.
- Links to external MCP-compliant services
- Requires `--mcp-tool` parameter to specify the MCP tool configuration ID
- Enables integration with external tools and services following the MCP standard

### prompt
Prompt template execution tools.
- Executes configured prompt templates with parameters
- Requires `--template` parameter to specify the prompt template ID
- Used for standardized prompt-based operations

## Options

- `-u, --api-url URL`
  - TrustGraph API URL to connect to
  - Default: `http://localhost:8088/` (or `TRUSTGRAPH_URL` environment variable)
  - Should point to a running TrustGraph API instance

- `--id ID`
  - **Required**: Unique tool identifier
  - Used to reference the tool in agent configurations
  - Must be unique within the tool namespace

- `--name NAME`
  - **Required**: Human-readable tool name
  - Displayed in tool listings and agent interfaces
  - Should be descriptive and meaningful

- `--description DESCRIPTION`
  - **Required**: Detailed description of what the tool does
  - Used by agents to understand tool capabilities
  - Should clearly explain the tool's purpose and functionality

- `--type TYPE`
  - **Required**: Tool type
  - Must be one of: `knowledge-query`, `text-completion`, `mcp-tool`, `prompt`
  - Determines how the tool is invoked and what parameters it expects

- `--mcp-tool MCP_TOOL_ID`
  - Required for `mcp-tool` type: ID of MCP tool configuration
  - References an MCP tool configured via `tg-set-mcp-tool`
  - Links the agent tool to the underlying MCP service

- `--collection COLLECTION`
  - Required for `knowledge-query` type: collection to query
  - Specifies which knowledge collection the tool should search
  - Must match an available knowledge collection in the system

- `--template TEMPLATE_ID`
  - Required for `prompt` type: template ID to use
  - References a prompt template configured in the system
  - Enables standardized prompt execution with parameters

- `--argument ARG`
  - Optional: Tool arguments in the form `name:type:description`
  - Can be specified multiple times for multiple arguments
  - Valid types: `string`, `number`
  - Defines the parameters the tool accepts

- `-h, --help`
  - Show help message and exit

## Examples

### Knowledge Query Tool

Create a tool for querying weather information:
```bash
tg-set-tool --id weather --name "Weather Lookup" \
  --type knowledge-query \
  --description "Get weather information for locations" \
  --collection weather-data \
  --argument location:string:"Location to query" \
  --argument units:string:"Temperature units (C/F)"
```

### MCP Tool Integration

Create an agent tool that uses an MCP calculator service:
```bash
# First configure the MCP tool
tg-set-mcp-tool --id calculator --tool-url "http://localhost:3000/calc"

# Then create the agent tool
tg-set-tool --id calculator --name "Calculator" --type mcp-tool \
  --description "Perform mathematical calculations" \
  --mcp-tool calculator \
  --argument expression:string:"Mathematical expression to evaluate"
```

### Text Completion Tool

Create a tool for text generation:
```bash
tg-set-tool --id text-generator --name "Text Generator" \
  --type text-completion \
  --description "Generate text content based on prompts" \
  --argument prompt:string:"Text prompt for generation" \
  --argument max_length:number:"Maximum length of generated text"
```

### Prompt Template Tool

Create a tool that executes a prompt template:
```bash
tg-set-tool --id email-writer --name "Email Writer" \
  --type prompt \
  --description "Generate professional emails using templates" \
  --template email-template \
  --argument recipient:string:"Email recipient name" \
  --argument subject:string:"Email subject" \
  --argument content:string:"Main email content"
```

### Complex Tool with Multiple Arguments

Create a comprehensive document analysis tool:
```bash
tg-set-tool --id document-analyzer --name "Document Analyzer" \
  --type knowledge-query \
  --description "Analyze documents for various insights" \
  --collection document-analysis \
  --argument document_id:string:"Unique document identifier" \
  --argument analysis_type:string:"Type of analysis (sentiment, entities, summary)" \
  --argument confidence_threshold:number:"Minimum confidence for results" \
  --argument max_results:number:"Maximum number of results to return"
```

## Argument Specification

Arguments follow the format: `name:type:description`

### Valid Argument Types

- **string**: Text/string parameter
- **number**: Numeric parameter (integer or decimal)

### Argument Examples

```bash
# String arguments
--argument location:string:"Geographic location"
--argument filename:string:"Name of the file to process"

# Number arguments  
--argument count:number:"Number of items to return"
--argument threshold:number:"Confidence threshold (0.0-1.0)"

# Multiple arguments
--argument query:string:"Search query text" \
--argument limit:number:"Maximum results" \
--argument format:string:"Output format (json, text, xml)"
```

## Integration Workflow

### Complete MCP Tool Setup

1. Configure the MCP tool:
```bash
tg-set-mcp-tool --id weather-service \
  --tool-url "http://weather-api.example.com:3000"
```

2. Create the agent tool:
```bash
tg-set-tool --id weather-lookup --name "Weather Lookup" \
  --type mcp-tool --mcp-tool weather-service \
  --description "Get current weather and forecasts" \
  --argument location:string:"City or coordinates" \
  --argument units:string:"Temperature units (celsius/fahrenheit)"
```

3. Verify the configuration:
```bash
tg-show-tools | grep -A 10 weather-lookup
tg-show-mcp-tools | grep weather-service
```

### Knowledge Query Setup

1. Ensure knowledge collection exists:
```bash
tg-show-kg-cores | grep financial-data
```

2. Create the knowledge query tool:
```bash
tg-set-tool --id financial-query --name "Financial Data Query" \
  --type knowledge-query \
  --description "Query financial market data and analysis" \
  --collection financial-data \
  --argument symbol:string:"Stock or asset symbol" \
  --argument timeframe:string:"Analysis timeframe (1d, 1w, 1m, 1y)"
```

## Validation and Testing

### Configuration Verification

After creating a tool, verify it was configured correctly:
```bash
# List all tools
tg-show-tools

# Check specific tool configuration
tg-show-tools | grep -A 20 "weather-lookup"
```

### Tool Testing

For MCP tools, test the underlying functionality:
```bash
# Test the MCP tool directly
tg-invoke-mcp-tool -n weather-service -P '{"location":"London"}'

# Test through agent if configured
tg-invoke-agent -f test-flow --query "What's the weather in London?"
```

## Error Handling

The command handles various error conditions:

### Missing Required Parameters
```bash
tg-set-tool --id test --name "Test Tool"
# Output: Exception: Must specify --type for tool
```

### Invalid Tool Type
```bash
tg-set-tool --id test --name "Test" --type invalid-type
# Output: Exception: Type must be one of: knowledge-query, text-completion, mcp-tool, prompt
```

### Invalid Argument Format
```bash
tg-set-tool --id test --name "Test" --type knowledge-query \
  --argument "invalid-format"
# Output: Exception: Arguments should be form name:type:description
```

### Invalid Argument Type
```bash
tg-set-tool --id test --name "Test" --type knowledge-query \
  --argument "param:invalid_type:description"
# Output: Exception: Type invalid_type invalid, use: string, number
```

### MCP Tool Reference Missing
```bash
tg-set-tool --id test --name "Test" --type mcp-tool
# Output: Exception: MCP tool type requires --mcp-tool parameter
```

## Best Practices

1. **Descriptive naming**: Use clear, descriptive tool IDs and names
2. **Comprehensive descriptions**: Provide detailed tool descriptions for agents
3. **Parameter validation**: Define appropriate argument types and descriptions
4. **Type consistency**: Choose the most appropriate tool type for the use case
5. **Dependency management**: Ensure MCP tools and collections exist before referencing them

## Tool Management

### Updating Tools

To update a tool configuration, simply run the command again with the same ID:
```bash
# Initial configuration
tg-set-tool --id weather --name "Weather" --type knowledge-query \
  --collection weather-data --description "Basic weather lookup"

# Updated configuration
tg-set-tool --id weather --name "Advanced Weather" --type knowledge-query \
  --collection weather-data --description "Advanced weather analysis with forecasts" \
  --argument location:string:"Location for weather query" \
  --argument days:number:"Number of forecast days"
```

### Tool Removal

Remove tools that are no longer needed:
```bash
tg-delete-tool --id weather
```

### Bulk Configuration

Configure multiple related tools:
```bash
#!/bin/bash
# Configure a suite of analysis tools

tools=(
    "sentiment:Sentiment Analysis:knowledge-query:sentiment-data"
    "entity:Entity Extraction:knowledge-query:entity-data"  
    "summary:Text Summarization:text-completion:"
)

for tool_spec in "${tools[@]}"; do
    IFS=':' read -r id name type collection <<< "$tool_spec"
    
    if [ "$type" = "knowledge-query" ]; then
        tg-set-tool --id "$id" --name "$name" --type "$type" \
          --collection "$collection" \
          --description "Automated $name tool" \
          --argument text:string:"Text to analyze"
    else
        tg-set-tool --id "$id" --name "$name" --type "$type" \
          --description "Automated $name tool" \
          --argument text:string:"Text to process"
    fi
done
```

## Security Considerations

- Validate tool configurations before deployment
- Ensure MCP tools use secure communication protocols
- Review tool permissions and access patterns
- Monitor tool usage for unusual activity
- Implement proper authentication for external tool services

## Related Commands

- [`tg-show-tools`](tg-show-tools) - Display all configured agent tools
- [`tg-delete-tool`](tg-delete-tool) - Remove tool configurations
- [`tg-set-mcp-tool`](tg-set-mcp-tool) - Configure MCP tools
- [`tg-show-mcp-tools`](tg-show-mcp-tools) - Display MCP tool configurations
- [`tg-invoke-agent`](tg-invoke-agent) - Use agents with configured tools

## See Also

- Agent Tool Configuration Guide
- MCP Integration Documentation
- Knowledge Graph Management
- Prompt Template Guide