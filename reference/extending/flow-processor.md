---
title: FlowProcessor
layout: default
nav_order: 2
parent: Extending TrustGraph
---

# FlowProcessor

The `FlowProcessor` class extends `AsyncProcessor` to provide automatic flow management and integration with TrustGraph's processing pipelines. This is ideal for services that need to be dynamically configured and participate in data processing flows.

## Overview

FlowProcessor builds on AsyncProcessor by adding:
- Automatic flow lifecycle management (start/stop flows)
- Configuration-driven consumer/producer setup
- Declarative specifications for message routing
- Integration with flow-based processing pipelines
- Automatic Pulsar queue management

## When to Use FlowProcessor

Use FlowProcessor when you need to create:
- Data processing services that participate in flows
- Services that need dynamic reconfiguration
- Services with multiple input/output streams
- Services that should be flow-aware and manageable

## Key Concepts

### Specifications
FlowProcessor uses specifications to declare what resources your service needs:
- `ConsumerSpec`: Declares input message streams
- `ProducerSpec`: Declares output message streams  
- `PromptClientSpec`: Declares LLM prompt integration
- `SettingSpec`: Declares configuration parameters

### Flow Management
Flows are automatically started and stopped based on configuration updates. Each flow gets its own isolated set of consumers and producers.

## Basic Implementation

### Step 1: Create Your Service Class

```python
from trustgraph.base import FlowProcessor, ConsumerSpec, ProducerSpec
from trustgraph.schema import InputSchema, OutputSchema

class YourProcessor(FlowProcessor):
    
    def __init__(self, **params):
        super(YourProcessor, self).__init__(**params)
        
        # Declare input consumer
        self.register_specification(
            ConsumerSpec(
                name="input",
                schema=InputSchema,
                handler=self.on_message,
                concurrency=1,
            )
        )
        
        # Declare output producer
        self.register_specification(
            ProducerSpec(
                name="output",
                schema=OutputSchema
            )
        )
```

### Step 2: Implement Message Handler

```python
    async def on_message(self, msg, consumer, flow):
        """Process incoming messages"""
        v = msg.value()
        
        try:
            # Process the message
            result = await self.process_data(v)
            
            # Send to output using flow context
            await flow("output").send(result)
            
        except Exception as e:
            print(f"Processing error: {e}")
```

### Step 3: Add Command-line Arguments

```python
    @staticmethod
    def add_args(parser):
        FlowProcessor.add_args(parser)
        
        parser.add_argument(
            '--concurrency',
            type=int,
            default=1,
            help='Number of concurrent processing threads'
        )
```

### Step 4: Create the Entry Point

```python
def run():
    YourProcessor.launch("your-processor-id", __doc__)

if __name__ == "__main__":
    run()
```

## Specification Types

### ConsumerSpec
Declares an input message stream:

```python
ConsumerSpec(
    name="input",              # Name for referencing in flow
    schema=YourInputSchema,    # Message schema
    handler=self.on_message,   # Message handler function
    concurrency=1,             # Number of concurrent consumers
)
```

### ProducerSpec
Declares an output message stream:

```python
ProducerSpec(
    name="output",             # Name for referencing in flow
    schema=YourOutputSchema    # Message schema
)
```

### PromptClientSpec
Declares LLM prompt integration:

```python
PromptClientSpec(
    request_name="prompt-request",   # Request queue name
    response_name="prompt-response", # Response queue name
)
```

## Flow Context

The `flow` parameter passed to message handlers provides access to:
- Producers: `await flow("output").send(message)`
- Prompt clients: `await flow("prompt-request").extract_entities(text="...")`

## Real-World Example: KG Relationships Extractor

The relationships extractor (`../trustgraph/trustgraph-flow/trustgraph/extract/kg/relationships/extract.py`) demonstrates FlowProcessor usage:

```python
class Processor(FlowProcessor):
    
    def __init__(self, **params):
        super(Processor, self).__init__(**params)
        
        # Input: text chunks
        self.register_specification(
            ConsumerSpec(
                name="input",
                schema=Chunk,
                handler=self.on_message,
                concurrency=concurrency,
            )
        )
        
        # Output: extracted triples
        self.register_specification(
            ProducerSpec(
                name="triples",
                schema=Triples
            )
        )
        
        # LLM integration for extraction
        self.register_specification(
            PromptClientSpec(
                request_name="prompt-request",
                response_name="prompt-response",
            )
        )
    
    async def on_message(self, msg, consumer, flow):
        v = msg.value()
        chunk = v.chunk.decode("utf-8")
        
        # Extract relationships using LLM
        rels = await flow("prompt-request").extract_relationships(
            text=chunk
        )
        
        # Convert to triples and send
        triples = self.convert_to_triples(rels, v.metadata)
        await flow("triples").send(Triples(
            metadata=v.metadata,
            triples=triples
        ))
```

## Configuration Integration

FlowProcessor automatically handles configuration updates for flow management. The configuration service sends updates that start/stop flows as needed.

### Configuration Structure
```json
{
  "flows-active": {
    "your-processor-id": {
      "flow-name": {
        "interfaces": {
          "input": "input-queue-name",
          "output": "output-queue-name",
          "prompt-request": "prompt-request-queue",
          "prompt-response": "prompt-response-queue"
        }
      }
    }
  }
}
```

## Advanced Features

### Multiple Flows
A single processor can handle multiple flows simultaneously:

```python
async def on_message(self, msg, consumer, flow):
    # Flow-specific processing
    flow_name = flow.name
    
    if flow_name == "flow-a":
        await self.process_flow_a(msg, flow)
    elif flow_name == "flow-b":
        await self.process_flow_b(msg, flow)
```

### Dynamic Specifications
You can register specifications dynamically:

```python
def __init__(self, **params):
    super().__init__(**params)
    
    # Register base specifications
    self.register_base_specs()
    
    # Add conditional specifications
    if params.get("enable_advanced_features"):
        self.register_advanced_specs()
```

### Custom Flow Logic
Override flow management for custom behavior:

```python
async def start_flow(self, flow_name, flow_config):
    """Custom flow startup logic"""
    print(f"Starting custom flow: {flow_name}")
    
    # Custom initialization
    await self.initialize_flow_resources(flow_name, flow_config)
    
    # Call parent implementation
    await super().start_flow(flow_name, flow_config)

async def stop_flow(self, flow_name):
    """Custom flow shutdown logic"""
    print(f"Stopping custom flow: {flow_name}")
    
    # Custom cleanup
    await self.cleanup_flow_resources(flow_name)
    
    # Call parent implementation
    await super().stop_flow(flow_name)
```

## Best Practices

1. **Use meaningful spec names**: Choose descriptive names for consumers and producers
2. **Handle concurrency**: Set appropriate concurrency levels for your workload
3. **Process errors gracefully**: Implement proper exception handling in message handlers
4. **Use flow context**: Access producers and services through the flow parameter
5. **Keep handlers focused**: Each message handler should have a single responsibility
6. **Test with multiple flows**: Ensure your processor works with multiple concurrent flows

## Comparison with AsyncProcessor

| Feature | AsyncProcessor | FlowProcessor |
|---------|---------------|---------------|
| Flow Management | Manual | Automatic |
| Configuration | Manual handling | Automatic flow config |
| Queue Setup | Manual | Declarative specs |
| Multi-flow Support | Manual | Built-in |
| Use Case | Global services | Flow-based processing |

## See Also

- [AsyncProcessor](async-processor) - For global services
- [Configuration Management](../configuration) - How configuration works
- [Flow Architecture](../flows) - Understanding TrustGraph flows
