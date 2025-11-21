---
title: Flow Specifications
nav_order: 4
parent: Extending TrustGraph
---

# Flow Specifications

Flow specifications are declarative interfaces used with `FlowProcessor` to define how your service integrates with TrustGraph processing flows. They automatically handle the setup and management of Pulsar message queues, consumers, producers, and request/response clients.

## Overview

Flow specifications eliminate boilerplate code by:
- Automatically creating and managing Pulsar consumers and producers
- Handling topic configuration from flow definitions
- Providing typed interfaces for message handling
- Managing metrics and monitoring
- Enabling dynamic flow reconfiguration

## Core Specification Types

### ConsumerSpec

Declares an input message stream for processing.

```python
from trustgraph.base import FlowProcessor, ConsumerSpec

class MyProcessor(FlowProcessor):
    def __init__(self, **params):
        super().__init__(**params)
        
        self.register_specification(
            ConsumerSpec(
                name="input",                    # Flow interface name
                schema=InputMessageSchema,       # Message schema class
                handler=self.on_input_message,   # Handler method
                concurrency=4                    # Concurrent consumers
            )
        )
    
    async def on_input_message(self, msg, consumer, flow):
        """Handle incoming messages"""
        value = msg.value()
        # Process the message
        await flow("output").send(processed_value)
```

**Key Features**:
- Automatic topic subscription from flow configuration
- Configurable concurrency for parallel processing
- Built-in metrics for message processing
- Automatic message acknowledgment

### ProducerSpec

Declares an output message stream for publishing.

```python
self.register_specification(
    ProducerSpec(
        name="output",                  # Flow interface name
        schema=OutputMessageSchema      # Message schema class
    )
)
```

**Usage in Message Handlers**:
```python
async def on_input_message(self, msg, consumer, flow):
    result = await self.process_data(msg.value())
    
    # Send via the producer
    await flow("output").send(result)
```

### RequestResponseSpec

Declares a request/response client for calling other services.

```python
self.register_specification(
    RequestResponseSpec(
        request_name="service-request",     # Request topic name
        request_schema=ServiceRequest,      # Request schema
        response_name="service-response",   # Response topic name  
        response_schema=ServiceResponse,    # Response schema
        impl=ServiceClient                  # Optional custom client
    )
)
```

**Usage in Message Handlers**:
```python
async def on_input_message(self, msg, consumer, flow):
    # Make request to another service
    response = await flow("service-request").request(
        ServiceRequest(data="example"),
        timeout=30
    )
    
    # Process response
    result = self.process_response(response)
    await flow("output").send(result)
```

### SettingSpec

Declares configuration parameters from flow definitions.

```python
self.register_specification(
    SettingSpec(name="max_retries")
)
```

**Usage in Message Handlers**:
```python
async def on_input_message(self, msg, consumer, flow):
    max_retries = flow.config["max_retries"].value
    
    for attempt in range(max_retries):
        try:
            result = await self.process_with_retries(msg.value())
            break
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
```

### SubscriberSpec

Declares a pub/sub subscriber for broadcast messages.

```python
self.register_specification(
    SubscriberSpec(
        name="events",                    # Topic name
        schema=EventMessageSchema         # Message schema
    )
)
```

**Usage**:
```python
# Subscribe to events in your flow
subscriber = flow("events")
await subscriber.subscribe("event-id")
event = await subscriber.get_message()
```

## Specialized Client Specifications

TrustGraph provides pre-built client specifications for common services:

### PromptClientSpec

For LLM prompt services with built-in convenience methods.

```python
self.register_specification(
    PromptClientSpec(
        request_name="prompt-request",
        response_name="prompt-response"
    )
)
```

**Usage**:
```python
async def on_input_message(self, msg, consumer, flow):
    text = msg.value().text
    
    # Extract relationships using prompt service
    relationships = await flow("prompt-request").extract_relationships(
        text=text,
        timeout=600
    )
    
    # Extract definitions
    definitions = await flow("prompt-request").extract_definitions(
        text=text,
        timeout=600
    )
    
    # Custom prompt
    result = await flow("prompt-request").prompt(
        id="custom-prompt",
        variables={"input": text},
        timeout=600
    )
```

### EmbeddingsClientSpec

For text embedding services.

```python
self.register_specification(
    EmbeddingsClientSpec(
        request_name="embeddings-request",
        response_name="embeddings-response"
    )
)
```

**Usage**:
```python
async def on_input_message(self, msg, consumer, flow):
    text_chunks = msg.value().chunks
    
    # Generate embeddings
    vectors = await flow("embeddings-request").embed(
        text=text_chunks,
        timeout=30
    )
    
    # Process embeddings
    await flow("output").send(EmbeddingsResult(vectors=vectors))
```

### TextCompletionClientSpec

For LLM text completion services.

```python
self.register_specification(
    TextCompletionClientSpec(
        request_name="llm-request",
        response_name="llm-response"
    )
)
```

**Usage**:
```python
async def on_input_message(self, msg, consumer, flow):
    query = msg.value().query
    
    # Generate text completion
    response = await flow("llm-request").text_completion(
        system="You are a helpful assistant",
        prompt=query,
        timeout=600
    )
    
    await flow("output").send(TextResult(text=response))
```

### ToolClientSpec

For tool invocation services.

```python
self.register_specification(
    ToolClientSpec(
        request_name="tool-request",
        response_name="tool-response"
    )
)
```

**Usage**:
```python
async def on_input_message(self, msg, consumer, flow):
    # Invoke calculator tool
    result = await flow("tool-request").invoke(
        name="calculator",
        parameters={"operation": "add", "a": 5, "b": 3},
        timeout=30
    )
    
    await flow("output").send(CalculationResult(result=result))
```

### TriplesClientSpec

For RDF triple query services.

```python
self.register_specification(
    TriplesClientSpec(
        request_name="triples-request",
        response_name="triples-response"
    )
)
```

**Usage**:
```python
async def on_input_message(self, msg, consumer, flow):
    entity = msg.value().entity
    
    # Query for triples about the entity
    triples = await flow("triples-request").query(
        s=Uri(entity),
        p=None,
        o=None,
        limit=100,
        timeout=30
    )
    
    await flow("output").send(TriplesResult(triples=triples))
```

## Complete Example

Here's a complete example of a processor that uses multiple specifications:

```python
from trustgraph.base import FlowProcessor, ConsumerSpec, ProducerSpec
from trustgraph.base import PromptClientSpec, EmbeddingsClientSpec, SettingSpec
from trustgraph.schema import TextChunk, ProcessedData

class TextAnalysisProcessor(FlowProcessor):
    
    def __init__(self, **params):
        super().__init__(**params)
        
        # Input consumer
        self.register_specification(
            ConsumerSpec(
                name="input",
                schema=TextChunk,
                handler=self.on_text_chunk,
                concurrency=2
            )
        )
        
        # Output producer
        self.register_specification(
            ProducerSpec(
                name="output",
                schema=ProcessedData
            )
        )
        
        # LLM prompt client
        self.register_specification(
            PromptClientSpec(
                request_name="prompt-request",
                response_name="prompt-response"
            )
        )
        
        # Embeddings client
        self.register_specification(
            EmbeddingsClientSpec(
                request_name="embeddings-request",
                response_name="embeddings-response"
            )
        )
        
        # Configuration setting
        self.register_specification(
            SettingSpec(name="analysis_mode")
        )
    
    async def on_text_chunk(self, msg, consumer, flow):
        """Process text chunks with analysis"""
        chunk = msg.value()
        text = chunk.text
        
        # Get configuration
        mode = flow.config["analysis_mode"].value
        
        try:
            # Extract entities using prompt service
            entities = await flow("prompt-request").extract_definitions(
                text=text,
                timeout=300
            )
            
            # Generate embeddings
            vectors = await flow("embeddings-request").embed(
                text=[text],
                timeout=30
            )
            
            # Create processed result
            result = ProcessedData(
                text=text,
                entities=entities,
                embeddings=vectors[0],
                metadata=chunk.metadata,
                mode=mode
            )
            
            # Send to output
            await flow("output").send(result)
            
        except Exception as e:
            print(f"Processing error: {e}")
            # Could send to error queue or log

def run():
    TextAnalysisProcessor.launch("text-analysis", __doc__)

if __name__ == "__main__":
    run()
```

## Flow Configuration

Flow specifications are automatically configured through the TrustGraph configuration system. Here's how the configuration maps to specifications:

```json
{
  "flows": {
    "analysis-flow": {
      "interfaces": {
        "input": "text-chunks-queue",
        "output": "processed-data-queue",
        "prompt-request": "prompt-service-request",
        "prompt-response": "prompt-service-response",
        "embeddings-request": "embeddings-service-request",
        "embeddings-response": "embeddings-service-response",
        "analysis_mode": "detailed"
      }
    }
  }
}
```

## Benefits of Flow Specifications

1. **Declarative**: Define what you need, not how to set it up
2. **Automatic Management**: Queues, consumers, and producers are created automatically
3. **Type Safety**: Strongly typed message schemas
4. **Error Handling**: Built-in error handling and retry logic
5. **Metrics**: Automatic metrics collection for monitoring
6. **Dynamic Reconfiguration**: Flows can be started/stopped without code changes
7. **Reusable**: Specifications can be shared across processors

## Error Handling

All client specifications include automatic error handling:

```python
try:
    result = await flow("service-request").request(data, timeout=30)
except RuntimeError as e:
    # Service returned an error response
    print(f"Service error: {e}")
except asyncio.TimeoutError:
    # Request timed out
    print("Request timed out")
```

## Best Practices

1. **Use descriptive names**: Choose clear names for your specifications
2. **Set appropriate timeouts**: Configure timeouts based on expected processing times
3. **Handle errors gracefully**: Always handle potential service errors
4. **Configure concurrency**: Set appropriate concurrency levels for your workload
5. **Use typed schemas**: Define proper message schemas for type safety
6. **Monitor metrics**: Use built-in metrics for monitoring and debugging

## See Also

- [FlowProcessor](flow-processor) - Understanding the base class
- [Service Base Classes](service-base-classes) - Pre-built service patterns
- [AsyncProcessor](async-processor) - For non-flow services
