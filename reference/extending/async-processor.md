---
title: AsyncProcessor
layout: default
nav_order: 1
parent: Extending TrustGraph
---

# AsyncProcessor

The `AsyncProcessor` class provides a foundation for building TrustGraph services that operate independently of flow management. This is ideal for "global" services that process data or respond to requests without needing to be tied to specific processing flows.

## Overview

AsyncProcessor handles core service infrastructure including:
- Pulsar client connections and message handling
- Configuration management and updates
- Task group management for async operations
- Metrics collection and monitoring
- Command-line argument parsing
- Automatic retry logic and error handling

## When to Use AsyncProcessor

Use AsyncProcessor when you need to create:
- Global services that operate independently (like the Knowledge service)
- Services that handle direct request/response patterns
- Services that don't need flow-specific message routing
- Core infrastructure services

## Basic Implementation

### Step 1: Create Your Service Class

```python
from trustgraph.base import AsyncProcessor, Consumer, Producer
from trustgraph.schema import YourRequestSchema, YourResponseSchema

class YourService(AsyncProcessor):
    
    def __init__(self, **params):
        super(YourService, self).__init__(**params)
        
        # Set up your consumers and producers
        self.request_consumer = Consumer(
            taskgroup=self.taskgroup,
            client=self.pulsar_client,
            flow=None,
            topic="your-request-queue",
            subscriber=self.id,
            schema=YourRequestSchema,
            handler=self.on_request,
        )
        
        self.response_producer = Producer(
            client=self.pulsar_client,
            topic="your-response-queue", 
            schema=YourResponseSchema,
        )
```

### Step 2: Implement Message Handlers

```python
    async def on_request(self, msg, consumer, flow):
        """Handle incoming requests"""
        v = msg.value()
        
        try:
            # Process the request
            result = await self.process_request(v)
            
            # Send response
            await self.response_producer.send(result)
            
        except Exception as e:
            # Handle errors appropriately
            await self.send_error_response(str(e))
```

### Step 3: Override Lifecycle Methods

```python
    async def start(self):
        """Start the service"""
        await super().start()
        await self.request_consumer.start()
        await self.response_producer.start()
        
    def stop(self):
        """Stop the service"""
        super().stop()
        # Clean up any additional resources
```

### Step 4: Add Command-line Arguments

```python
    @staticmethod
    def add_args(parser):
        AsyncProcessor.add_args(parser)
        
        parser.add_argument(
            '--your-custom-arg',
            default='default_value',
            help='Description of your argument'
        )
```

### Step 5: Create the Entry Point

```python
def run():
    YourService.launch("your-service-id", __doc__)

if __name__ == "__main__":
    run()
```

## Configuration Management

AsyncProcessor automatically subscribes to configuration updates. You can register handlers for configuration changes:

```python
def __init__(self, **params):
    super().__init__(**params)
    
    # Register for configuration updates
    self.register_config_handler(self.on_config_change)

async def on_config_change(self, config, version):
    """Handle configuration updates"""
    print(f"Config version {version} received")
    
    # Process configuration changes
    if "your-service-config" in config:
        self.update_settings(config["your-service-config"])
```

## Real-World Example: Knowledge Service

The Knowledge service (`../trustgraph/trustgraph-flow/trustgraph/cores/service.py`) demonstrates AsyncProcessor usage:

```python
class Processor(AsyncProcessor):
    
    def __init__(self, **params):
        super(Processor, self).__init__(**params)
        
        # Set up request/response handling
        self.knowledge_request_consumer = Consumer(
            taskgroup=self.taskgroup,
            client=self.pulsar_client,
            flow=None,
            topic=knowledge_request_queue,
            subscriber=id,
            schema=KnowledgeRequest,
            handler=self.on_knowledge_request,
        )
        
        self.knowledge_response_producer = Producer(
            client=self.pulsar_client,
            topic=knowledge_response_queue,
            schema=KnowledgeResponse,
        )
        
        # Initialize business logic
        self.knowledge = KnowledgeManager(
            cassandra_host=cassandra_host,
            cassandra_user=cassandra_user,
            cassandra_password=cassandra_password,
            keyspace=keyspace,
            flow_config=self,
        )
```

## Key Features

### Automatic Retry Logic
AsyncProcessor includes built-in retry logic that automatically restarts your service if it encounters exceptions, making it resilient to temporary failures.

### Metrics Integration
Metrics are automatically collected for:
- Service parameters and configuration
- Consumer and producer performance
- Processing times and error rates

### Task Group Management
All async operations are managed within a task group, ensuring proper cleanup and coordinated shutdown.

### Configuration Subscription
Services automatically receive configuration updates through the Pulsar configuration queue, with configurable handlers for processing changes.

## Best Practices

1. **Always call parent methods**: When overriding `start()` or `stop()`, call the parent implementation
2. **Use task groups**: All async operations should use the provided `taskgroup`
3. **Handle errors gracefully**: Implement proper exception handling in message handlers
4. **Register configuration handlers**: Use `register_config_handler()` for configuration updates
5. **Add meaningful metrics**: Include custom metrics for monitoring service health

## See Also

- [FlowProcessor](flow-processor) - For flow-aware services
- [Service Architecture](../architecture) - Overall service design patterns
