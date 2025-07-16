---
title: MCP Integration
layout: default
parent: How-to Guides
grand_parent: TrustGraph Documentation
---

# MCP Integration

Learn how to integrate Model Context Protocol (MCP) servers with TrustGraph to extend your agent workflows with custom tools and capabilities.

This is a feature which began release in TrustGraph 1.1.

## Overview

The Model Context Protocol (MCP) is an open standard that enables seamless integration between AI systems and external tools. TrustGraph supports MCP, allowing you to connect custom tools and services that your agents can use during their workflows.

This guide walks through setting up a simple MCP server and integrating it with TrustGraph's agent framework.

The capability has been released to allow early adopters to get started
with the technology.  MCP is an emerging topic, and a number of areas such
as production deployment and authentication may not be ready for production
use.  Follow the TrustGraph roadmap as we track this emerging and amazing
technology.

## What You'll Learn

- How to create a basic MCP server with custom tools
- How to configure TrustGraph to use MCP services
- How to enable agents to use MCP tools in their workflows
- Best practices for MCP integration

## Prerequisites

Before starting this guide, ensure you have:

- A running TrustGraph instance (see [Installation Guide](../../getting-started/installation))
- Python 3.8 or later with a working development environment
- Basic familiarity with Python programming
- The TrustGraph CLI tools installed (`pip install trustgraph-cli`)

## Quickstart Scenario

In this guide, we'll create an MCP server with three example tools:

1. **`get_current_time`** - Returns the current system time
2. **`get_tesla_list_prices`** - Provides Tesla vehicle pricing information (test data)
3. **`get_bank_balance`** - Returns a user's bank balance (hard-coded for demo)

We'll then configure TrustGraph to use these tools and demonstrate how an agent can leverage them to answer complex questions.

## Step 1: Set Up TrustGraph

If you haven't already, deploy TrustGraph using one of the methods described in the [Installation Guide](../../getting-started/installation).

For this tutorial, we recommend loading a small sample document to enable knowledge-based queries alongside MCP tools:

```bash
tg-load-sample-documents
```

Select a small document like "Beyond State Surveillance" for quick loading.

## Step 2: Create the MCP Server

Create a new file called `server.py` with the following code:

```python
import dataclasses
import datetime

# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo", host="0.0.0.0", port=9870)

@dataclasses.dataclass
class CurrentTime:
    time: str

@mcp.tool()
def get_current_time() -> CurrentTime:
    """Return the current time"""
    return {
        "time": datetime.datetime.now().isoformat()
    }

@mcp.tool()
def get_tesla_list_prices() -> dict:
    """Return Tesla list prices"""
    return {
      "tesla_vehicles": [
        {
          "model": "Model 3",
          "description": "Compact executive sedan with dual motor all-wheel drive",
          "price": "£42,990",
          "note": "Base price for Long Range variant"
        },
        {
          "model": "Model Y",
          "description": "Mid-size electric SUV with 7-seat configuration available",
          "price": "£54,990",
          "note": "Performance variant with enhanced acceleration"
        },
        {
          "model": "Model S",
          "description": "Full-size luxury sedan with tri-motor setup",
          "price": "£89,990",
          "note": "Plaid variant with 1,020 horsepower"
        },
        {
          "model": "Model X",
          "description": "Full-size luxury SUV with falcon wing doors",
          "price": "£99,990",
          "note": "Plaid variant with distinctive gull-wing rear doors"
        },
        {
          "model": "Cybertruck",
          "description": "Angular electric pickup truck with stainless steel exoskeleton",
          "price": "£750,000",
          "note": "It's not road-legal in the UK so you would need to sponsor a major amount of engineering work"
        }
      ]
    }

@mcp.tool()
def get_bank_balance() -> float:
    """Return the value in my current account in UK pounds"""
    return 424.12

mcp.run(transport="streamable-http")
```

### Install Dependencies

Install the MCP library:

```bash
pip install mcp
```

### Start the MCP Server

Run the server:

```bash
python3 server.py
```

You should see output similar to:

```
INFO:     Started server process [457135]
INFO:     Waiting for application startup.
[07/15/25 13:52:21] INFO     StreamableHTTP session manager started         streamable_http_manager.py:111
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9870 (Press CTRL+C to quit)
```

This confirms the server is running on port 9870.

## Step 3: Configure MCP Tools in TrustGraph

### Access the Web Interface

Navigate to the TrustGraph web interface at [http://localhost:8888/](http://localhost:8888/).

### Add MCP Tool Integrations

1. Go to the **MCP Tools** configuration page
2. For each of the three tools, click **"Add MCP Tool Integration"** and configure:

   - **Tool 1**: `get_tesla_list_prices`
   - **Tool 2**: `get_current_time`
   - **Tool 3**: `get_bank_balance`

3. For each tool, set the MCP server address:
   - **Linux with Podman**: `http://host.containers.internal:9870/mcp`
   - **Docker**: `http://host.docker.internal:9870/mcp`

<a href="mcp-tool-config.png">
  <img src="mcp-tool-config.png" alt="MCP tool configuration example">
</a>

> **Note**: Since TrustGraph runs in containers while your MCP server runs on the host machine, you need to use the special hostname that allows containers to access the host.

The finished MCP tool list should appear as below:

<a href="mcp-tool-list.png">
  <img src="mcp-tool-list.png" alt="MCP tool configuration list">
</a>

### Verify MCP Integration

Test that TrustGraph can communicate with your MCP server:

```bash
tg-invoke-mcp-tool -n get_current_time
```

Expected output:

```json
{
    "time": "2025-07-15T13:57:54.925316"
}
```

Test the other tools:

```bash
tg-invoke-mcp-tool -n get_tesla_list_prices
tg-invoke-mcp-tool -n get_bank_balance
```

## Step 4: Configure Agent Tools

Now we'll make these MCP tools available to TrustGraph agents.

### Access Agent Tools Configuration

In the web interface, navigate to **"Agent Tools"**. You can delete the sample tools and add your MCP tools.

### Add MCP Tools for Agents

Add the following tool configurations:

1. **Get Current Time**
   - Type: `MCP Tool`
   - Tool ID: `get_current_time`
   - Name: `get_current_time`
   - Description: `Fetches the current time as an ISO format string`
   - Arguments: (leave empty)

2. **Get Bank Balance**
   - Type: `MCP Tool`
   - Tool ID: `get_bank_balance`
   - Name: `get_bank_balance`
   - Description: `Fetches the bank balance, the value returned is in GBP sterling`
   - Arguments: (leave empty)

3. **Get Tesla List Prices**
   - Type: `MCP Tool`
   - Tool ID: `get_tesla_list_prices`
   - Name: `get_tesla_list_prices`
   - Description: `Fetches the current Tesla vehicle price list. This contains information such as model, current price, and notes that are relevant`
   - Arguments: (leave empty)

### Optional: Add Knowledge Query Tool

If you loaded sample documents earlier, you can also add a knowledge query tool:

- **Surveillance and Intelligence**
  - Type: `Knowledge query`
  - Tool ID: `surveillance-and-intelligence`
  - Name: `surveillance-and-intelligence`
  - Description: `This tool has information about the topics of state surveillance and intelligence gathering. The question should be a natural language question.`

## Step 5: Test the Integration

### Command Line Testing

Run an agent query that uses multiple MCP tools:

```bash
tg-invoke-agent -v -q 'Is there enough money in my bank account to buy a
cybertruck? Can you take a look and summarise the kind of decisions I would
need to make in my life to buy a Cybertruck?'
```

Expected output shows the agent:
1. Fetching Tesla prices to find the Cybertruck cost
2. Checking the bank balance
3. Comparing values and providing recommendations

### Web Interface Testing

1. Go to the **GraphRAG** tab
2. Select **'Agent'** mode
3. Enter the same question

<a href="agent-chat.png">
  <img src="agent-chat.png" alt="MCP tool configuration list">
</a>

## How This Works

When you submit a question to the TrustGraph agent:

1. **Query Analysis**: The agent analyzes your question to determine what information it needs
2. **Tool Selection**: It identifies which MCP tools can provide the required data
3. **Tool Invocation**: The agent calls the MCP tools through TrustGraph's MCP integration layer
4. **Data Integration**: Results from multiple tools are combined and analyzed
5. **Response Generation**: The agent formulates a comprehensive answer based on all gathered information

The MCP protocol handles:
- **Tool Discovery**: TrustGraph automatically discovers available tools from the MCP server
- **Type Safety**: Input and output types are validated
- **Error Handling**: Failed tool calls are gracefully handled
- **Async Communication**: Tools can be called in parallel for efficiency

## Advanced Usage Examples

### Combining MCP Tools with Knowledge Queries

Try this query that combines MCP data with document knowledge:

```bash
tg-invoke-agent -v -q 'Given the current surveillance capabilities described
in the documents, and considering my bank balance, what privacy protection
measures could I afford if I wanted to protect myself from state
surveillance while saving for a Tesla?'
```

This demonstrates how agents can:
- Query knowledge graphs for context
- Use MCP tools for real-time data
- Synthesize information from multiple sources

### Creating More Complex MCP Tools

You can extend the MCP server with tools that:
- Query external APIs
- Access databases
- Perform calculations
- Integrate with other services

Example of a more complex tool:

```python
@mcp.tool()
def calculate_savings_timeline(target_amount: float, monthly_savings: float) -> dict:
    """Calculate how long it will take to save for a target amount"""
    months_needed = int(target_amount / monthly_savings)
    years = months_needed // 12
    remaining_months = months_needed % 12
    
    return {
        "total_months": months_needed,
        "years": years,
        "additional_months": remaining_months,
        "target_amount": target_amount,
        "monthly_savings": monthly_savings
    }
```

## Best Practices

### MCP Server Development

1. **Error Handling**: Always handle exceptions gracefully in your tools
2. **Documentation**: Provide clear descriptions for tools and parameters
3. **Type Hints**: Use proper type annotations for better integration
4. **Logging**: Implement logging for debugging and monitoring
5. **Security**: Validate inputs and sanitize outputs

### Integration Configuration

1. **Network Security**: Use proper firewall rules for MCP server ports
2. **Authentication**: Consider adding authentication for production deployments
3. **Performance**: Monitor tool execution times and optimize as needed
4. **Versioning**: Version your MCP tools to manage updates

### Tool Design

1. **Single Responsibility**: Each tool should do one thing well
2. **Idempotency**: Tools should produce consistent results for the same inputs
3. **Descriptive Names**: Use clear, action-oriented tool names
4. **Comprehensive Descriptions**: Help agents understand when to use each tool

## Troubleshooting

### Common Issues

**MCP Server Not Accessible**
- Verify the server is running on the correct port
- Check firewall settings
- Ensure you're using the correct host address for container access

**Tool Invocation Fails**
- Check MCP server logs for errors
- Verify tool configuration in TrustGraph matches the MCP server
- Test tools individually using `tg-invoke-mcp-tool`

**Agent Doesn't Use MCP Tools**
- Ensure tools are properly configured in Agent Tools
- Check tool descriptions are clear and relevant
- Verify the agent has access to the configured tools

### Debug Commands

```bash
# List configured MCP tools
tg-show-tools

# Test individual MCP tool
tg-invoke-mcp-tool -n <tool_name> -a '{"param": "value"}'

# Check agent configuration
tg-show-config | grep -A 10 agent
```

## Next Steps

- Explore creating custom MCP tools for your specific use cases
- Learn about [securing MCP deployments](../security/)
- Integrate with external APIs and services
- Build complex agent workflows using multiple tools

## Further Reading

- [MCP Protocol Specification](https://github.com/anthropics/mcp)
- [TrustGraph Agent Documentation](../../reference/apis/api-agent)
- [Advanced Agent Workflows](../../advanced/custom-algorithms)
