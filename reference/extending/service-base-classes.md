---
title: Service Base Classes
layout: default
nav_order: 3
parent: Extending TrustGraph
---

# Service Base Classes

TrustGraph provides specialized service base classes that extend `FlowProcessor` to remove boilerplate code for common service patterns. These classes handle the standard request/response flows and error handling, allowing you to focus on implementing the core business logic.

## Overview

Each service base class follows a consistent pattern:
- Extends `FlowProcessor` with pre-configured specifications
- Handles message routing and error responses automatically
- Requires you to implement only the core business logic method
- Includes built-in metrics and monitoring
- Supports concurrency where appropriate

## Available Service Base Classes

### AgentService

**Purpose**: Multi-step agent processing with thought/action loops

**Key Features**:
- Supports agent workflows with multiple response types
- Handles `next` actions for chained processing
- Built-in error handling for agent-specific errors

**Implementation Required**:
```python
from trustgraph.base import AgentService

class YourAgentService(AgentService):
    
    async def agent_request(self, request, respond, next, flow):
        """
        Process agent requests with multiple possible responses
        
        Args:
            request: AgentRequest object
            respond: Function to send final response
            next: Function to send next action in chain
            flow: Flow context for accessing other services
        """
        # Your agent logic here
        
        # Send intermediate response
        await respond(AgentResponse(
            thought="I need to analyze this...",
            observation=None,
            answer=None
        ))
        
        # Or send next action
        await next(AgentRequest(
            operation="next-step",
            parameters={"data": "processed"}
        ))
```

**Message Flow**:
- Input: `AgentRequest` on "request" topic
- Outputs: `AgentResponse` on "response" topic, `AgentRequest` on "next" topic

### EmbeddingsService

**Purpose**: Text-to-vector embedding generation

**Key Features**:
- Configurable concurrency for parallel processing
- Built-in metrics for processing times
- Rate limiting support

**Implementation Required**:
```python
from trustgraph.base import EmbeddingsService

class YourEmbeddingsService(EmbeddingsService):
    
    async def on_embeddings(self, text):
        """
        Generate embeddings for input text
        
        Args:
            text: List of strings to embed
            
        Returns:
            List of vectors (list of floats)
        """
        # Your embedding logic here
        vectors = await self.generate_embeddings(text)
        return vectors
```

**Message Flow**:
- Input: `EmbeddingsRequest` on "request" topic
- Output: `EmbeddingsResponse` on "response" topic

### LlmService

**Purpose**: Large Language Model text completion

**Key Features**:
- Configurable concurrency
- Built-in timing metrics with detailed buckets
- Token usage tracking
- Rate limiting support

**Implementation Required**:
```python
from trustgraph.base import LlmService, LlmResult

class YourLlmService(LlmService):
    
    async def generate_content(self, system, prompt):
        """
        Generate text completion using LLM
        
        Args:
            system: System prompt/instructions
            prompt: User prompt
            
        Returns:
            LlmResult object with text, token counts, and model info
        """
        # Your LLM logic here
        response_text = await self.call_llm(system, prompt)
        
        return LlmResult(
            text=response_text,
            in_token=len(prompt.split()),  # Approximate
            out_token=len(response_text.split()),  # Approximate
            model="your-model-name"
        )
```

**Message Flow**:
- Input: `TextCompletionRequest` on "request" topic
- Output: `TextCompletionResponse` on "response" topic

### ToolService

**Purpose**: Tool invocation and execution

**Key Features**:
- JSON parameter parsing
- Support for string and object responses
- Built-in invocation metrics
- Configurable concurrency

**Implementation Required**:
```python
from trustgraph.base import ToolService

class YourToolService(ToolService):
    
    async def invoke_tool(self, name, parameters):
        """
        Invoke a tool with given parameters
        
        Args:
            name: Tool name to invoke
            parameters: Dict of tool parameters
            
        Returns:
            String response or object that can be JSON serialized
        """
        # Your tool logic here
        if name == "calculator":
            return parameters["a"] + parameters["b"]
        elif name == "search":
            return {"results": ["result1", "result2"]}
        else:
            raise ValueError(f"Unknown tool: {name}")
```

**Message Flow**:
- Input: `ToolRequest` on "request" topic
- Output: `ToolResponse` on "response" topic

## Query Services

### TriplesQueryService

**Purpose**: RDF triple querying and retrieval

**Implementation Required**:
```python
from trustgraph.base import TriplesQueryService

class YourTriplesQueryService(TriplesQueryService):
    
    async def query_triples(self, request):
        """
        Query triples matching the request pattern
        
        Args:
            request: TriplesQueryRequest with subject, predicate, object patterns
            
        Returns:
            List of Triple objects matching the query
        """
        # Your triple query logic here
        matching_triples = await self.search_triples(
            request.subject, request.predicate, request.object
        )
        return matching_triples
```

### GraphEmbeddingsQueryService

**Purpose**: Graph entity embedding queries

**Implementation Required**:
```python
from trustgraph.base import GraphEmbeddingsQueryService

class YourGraphEmbeddingsQueryService(GraphEmbeddingsQueryService):
    
    async def query_graph_embeddings(self, request):
        """
        Query graph embeddings by vector similarity
        
        Args:
            request: GraphEmbeddingsRequest with query vectors
            
        Returns:
            List of entities with similarity scores
        """
        # Your graph embedding query logic here
        similar_entities = await self.find_similar_entities(
            request.vectors, request.limit
        )
        return similar_entities
```

### DocumentEmbeddingsQueryService

**Purpose**: Document embedding queries

**Implementation Required**:
```python
from trustgraph.base import DocumentEmbeddingsQueryService

class YourDocumentEmbeddingsQueryService(DocumentEmbeddingsQueryService):
    
    async def query_document_embeddings(self, request):
        """
        Query document embeddings by vector similarity
        
        Args:
            request: DocumentEmbeddingsRequest with query vectors
            
        Returns:
            List of documents with similarity scores
        """
        # Your document embedding query logic here
        similar_docs = await self.find_similar_documents(
            request.vectors, request.limit
        )
        return similar_docs
```

## Store Services

### TriplesStoreService

**Purpose**: RDF triple storage

**Implementation Required**:
```python
from trustgraph.base import TriplesStoreService

class YourTriplesStoreService(TriplesStoreService):
    
    async def store_triples(self, triples):
        """
        Store triples in the graph database
        
        Args:
            triples: Triples object containing list of Triple objects
        """
        # Your triple storage logic here
        await self.save_to_database(triples.triples)
```

### GraphEmbeddingsStoreService

**Purpose**: Graph entity embedding storage

**Implementation Required**:
```python
from trustgraph.base import GraphEmbeddingsStoreService

class YourGraphEmbeddingsStoreService(GraphEmbeddingsStoreService):
    
    async def store_graph_embeddings(self, embeddings):
        """
        Store graph embeddings in the vector database
        
        Args:
            embeddings: GraphEmbeddings object with entity vectors
        """
        # Your graph embedding storage logic here
        await self.save_embeddings(embeddings.entities)
```

### DocumentEmbeddingsStoreService

**Purpose**: Document embedding storage

**Implementation Required**:
```python
from trustgraph.base import DocumentEmbeddingsStoreService

class YourDocumentEmbeddingsStoreService(DocumentEmbeddingsStoreService):
    
    async def store_document_embeddings(self, embeddings):
        """
        Store document embeddings in the vector database
        
        Args:
            embeddings: DocumentEmbeddings object with document vectors
        """
        # Your document embedding storage logic here
        await self.save_document_embeddings(embeddings.documents)
```

## Common Patterns

### Error Handling

All service base classes automatically handle errors:
- `TooManyRequests`: Re-raised to trigger rate limiting
- Other exceptions: Caught and converted to appropriate error responses

### Metrics

Most services include built-in metrics:
- **LlmService**: Timing histograms with detailed buckets
- **ToolService**: Invocation counters by tool name
- **EmbeddingsService**: Processing time metrics

### Concurrency

Services that support concurrency:
- `EmbeddingsService`: Configurable with `--concurrency` flag
- `LlmService`: Configurable with `--concurrency` flag  
- `ToolService`: Configurable with `--concurrency` flag

### Command-line Arguments

All services inherit FlowProcessor arguments and some add their own:
```python
@staticmethod
def add_args(parser):
    parser.add_argument(
        '-c', '--concurrency',
        type=int,
        default=1,
        help='Concurrent processing threads'
    )
    FlowProcessor.add_args(parser)
```

## Complete Example

Here's a complete example of implementing a simple calculator tool service:

```python
from trustgraph.base import ToolService

class CalculatorService(ToolService):
    
    async def invoke_tool(self, name, parameters):
        """Calculator tool implementation"""
        
        if name == "add":
            return parameters["a"] + parameters["b"]
        elif name == "multiply":
            return parameters["a"] * parameters["b"]
        elif name == "divide":
            if parameters["b"] == 0:
                raise ValueError("Cannot divide by zero")
            return parameters["a"] / parameters["b"]
        else:
            raise ValueError(f"Unknown operation: {name}")

def run():
    CalculatorService.launch("calculator", __doc__)

if __name__ == "__main__":
    run()
```

## Benefits

Using service base classes provides:
- **Reduced boilerplate**: No need to write message handling code
- **Consistent patterns**: All services follow the same structure
- **Built-in monitoring**: Metrics and error handling included
- **Flow integration**: Automatic flow management and configuration
- **Type safety**: Strongly typed request/response schemas

## See Also

- [FlowProcessor](flow-processor) - Understanding the underlying base class
- [AsyncProcessor](async-processor) - For services that don't fit these patterns
- [Service Architecture](../architecture) - Overall service design patterns
