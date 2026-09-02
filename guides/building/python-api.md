---
title: Building with the Python API
nav_order: 4
parent: Building with TrustGraph
guide_category:
  - Building with TrustGraph
guide_category_order: 4
guide_description: Use the TrustGraph Python API to build custom applications and integrations
guide_difficulty: intermediate
guide_time: 10 min
guide_emoji: 🐍
guide_banner: python.jpg
guide_labels:
  - Python
  - API
review_date: 2026-11-01
---

# Building with the Python API

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>A running TrustGraph deployment</li>
<li>Python {{site.data.software.python-min-version}} or higher</li>
<li>Basic Python familiarity</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Use the TrustGraph Python API to integrate TrustGraph capabilities into your Python applications."
%}

## Installation

The TrustGraph Python API is provided in the `trustgraph-base` package.

{% capture pip_install %}
```bash
pip install trustgraph-base
```
{% endcapture %}

{% capture uv_install %}
```bash
uv pip install trustgraph-base
```
{% endcapture %}

{% capture poetry_install %}
```bash
poetry add trustgraph-base
```
{% endcapture %}

{% include code_tabs.html
   tabs="Pip,Uv,Poetry"
   content1=pip_install
   content2=uv_install
   content3=poetry_install
%}

For a specific version:

{% capture pip_install_version %}
```bash
pip install trustgraph-base==2.4.29
```
{% endcapture %}

{% capture uv_install_version %}
```bash
uv pip install trustgraph-base==2.4.29
```
{% endcapture %}

{% capture poetry_install_version %}
```bash
poetry add trustgraph-base@2.4.29
```
{% endcapture %}

{% include code_tabs.html
   tabs="Pip,Uv,Poetry"
   content1=pip_install_version
   content2=uv_install_version
   content3=poetry_install_version
%}

**Version compatibility:** For best compatibility, use the version of `trustgraph-base` that matches your deployed TrustGraph system version. Check your deployment version and install the corresponding package version.

## API Overview

The `trustgraph-base` package provides Python interfaces to TrustGraph functionality:

- **API client** - Connect to TrustGraph API gateway
- **Flows** - Interact with processing flows
- **Documents** - Load and manage documents
- **Queries** - Execute LLM, RAG, and agent queries
- **Collections** - Manage document collections
- **Knowledge graph** - Work with graph data

## Authentication

All API access requires a valid authentication token.  Tokens are either
API keys (long-lived tokens with a `tg_` prefix) or temporary JWT tokens
obtained through username/password login.

The simplest approach is to set the `TRUSTGRAPH_TOKEN` environment variable
before running your application:

```bash
export TRUSTGRAPH_TOKEN="tg_my-secret-token"
```

## Creating a Client

To connect to TrustGraph, create an `Api` client object with your
authentication token:

```python
import os
from trustgraph.api import Api

api = Api(
    url='http://localhost:8088/',
    token=os.getenv('TRUSTGRAPH_TOKEN'),
)
```

**Workspace selection:**

The `Api` client is scoped to a workspace.  All requests made through the
client are automatically routed to the specified workspace.  If no workspace
is specified, the `default` workspace is used.

```python
api = Api(
    url='http://localhost:8088/',
    token=os.getenv('TRUSTGRAPH_TOKEN'),
    workspace='my-workspace',
)
```

## Service Access Pattern

TrustGraph uses a consistent pattern: create an `Api` object, then call service methods to get service handlers.

**Global services** are accessed directly from the API object:

```python
# Access different services
flow_service = api.flow()
config_service = api.config()
knowledge_service = api.knowledge()
library_service = api.library()
collection_service = api.collection()
socket_service = api.socket()
bulk_service = api.bulk()
metrics_service = api.metrics()
```

The **flow-specific service** uses a different pattern:

```python
# Access a specific flow
flow = api.flow().id('default')

# Use the flow
response = flow.text_completion(system="You are helpful", prompt="Hello")
```

## Example: Get a Prompt Template

This example uses the config service to retrieve a specific prompt template:

```python
import os
from trustgraph.api import Api, ConfigKey
import json

# Create API client and get config service
api = Api(
    url='http://localhost:8088/',
    token=os.getenv('TRUSTGRAPH_TOKEN'),
).config()

# ConfigKey identifies a configuration item
# type="prompt" specifies we want a prompt template
# key="template.question" is the ID of the specific prompt we want
# (prompt templates are stored with "template." prefix)
values = api.get([
    ConfigKey(type="prompt", key="template.question")
])

# Config values are stored as JSON strings, so we decode them
prompt_data = json.loads(values[0].value)

# The decoded data contains a "prompt" field with the actual template text
print("Question prompt:")
print(prompt_data["prompt"])
```

This pattern demonstrates:
1. Creating the API client and accessing the config service
2. Using `ConfigKey` to specify what to retrieve (type="prompt", key="template.question")
3. Parsing the JSON response
4. Accessing the prompt text from the returned data

## Example: Query Triples from Knowledge Graph

This example demonstrates the flow-specific service pattern by querying triples from the knowledge graph:

```python
import os
from trustgraph.api import Api

# Create API client
api = Api(
    url='http://localhost:8088/',
    token=os.getenv('TRUSTGRAPH_TOKEN'),
)

# Access a specific flow using the flow-specific service pattern
# api.flow() returns a Flow service
# .id('default') selects the flow instance to use
flow = api.flow().id('default')

# Query triples from the knowledge graph
triples = flow.triples_query(limit=10)

# Display the results
print(f"Retrieved {len(triples)} triples:")
for triple in triples:
    print(f"  {triple.s} -> {triple.p} -> {triple.o}")
```

This demonstrates the flow-specific service pattern where operations are scoped to a particular flow instance. You can also filter triples by subject, predicate, or object:

```python
import os
from trustgraph.api import Api
from trustgraph.knowledge import Uri

api = Api(
    url='http://localhost:8088/',
    token=os.getenv('TRUSTGRAPH_TOKEN'),
)
flow = api.flow().id('default')

# Query triples with a specific subject
# Uri() wraps URIs used in the knowledge graph
subject_uri = Uri("https://trustgraph.ai/docs/cats")
triples = flow.triples_query(s=subject_uri, limit=10)

print(f"Triples with subject {subject_uri}:")
for triple in triples:
    print(f"  {triple.p} -> {triple.o}")
```

## Querying with Graph RAG

Graph RAG retrieves relevant information from the knowledge graph to answer questions. TrustGraph supports both non-streaming and streaming modes.

### Non-streaming Graph RAG

Use the standard flow service for non-streaming queries that return complete responses:

```python
import os
from trustgraph.api import Api

# Create API client and access flow
api = Api(
    url='http://localhost:8088/',
    token=os.getenv('TRUSTGRAPH_TOKEN'),
)
flow = api.flow().id('default')

# Execute Graph RAG query
response = flow.graph_rag(
    query="What is the scientific name for cats?",
    collection="default",
)

print(response)
```

Optional parameters for tuning graph traversal:
- `entity_limit` - Maximum entities to retrieve (default: 50)
- `triple_limit` - Maximum triples to retrieve (default: 30)
- `max_subgraph_size` - Maximum subgraph size (default: 150)
- `max_path_length` - Maximum path length (default: 2)

### Streaming Graph RAG

Use the socket service for streaming responses that arrive incrementally:

```python
import os
from trustgraph.api import Api

# Create API client and access socket service
api = Api(
    url='http://localhost:8088/',
    token=os.getenv('TRUSTGRAPH_TOKEN'),
)

# Socket service uses WebSockets for streaming
flow = api.socket().flow('default')

# Execute streaming Graph RAG query
for chunk in flow.graph_rag(
    query="What is the scientific name for cats?",
    collection="default",
    streaming=True,
):
    print(chunk, end='', flush=True)

print()
```

The streaming mode is useful for:
- Displaying responses in real-time to users
- Processing long responses incrementally
- Building interactive applications with live feedback

## Agent Queries with Streaming

Agents can reason, use tools, and provide step-by-step thinking. Streaming mode lets you observe the agent's thought process in real-time.

```python
import os
from trustgraph.api import Api
from trustgraph.api.types import AgentThought, AgentObservation, AgentAnswer

# Create API client and access socket service
api = Api(
    url='http://localhost:8088/',
    token=os.getenv('TRUSTGRAPH_TOKEN'),
)
flow = api.socket().flow('default')

# Execute streaming agent query
for chunk in flow.agent(
    question="What is the scientific name for cats?",
    streaming=True,
):
    if isinstance(chunk, AgentThought):
        print(f"Thought: {chunk.content}", end='', flush=True)
        if chunk.end_of_message:
            print()

    elif isinstance(chunk, AgentObservation):
        print(f"Observation: {chunk.content}", end='', flush=True)
        if chunk.end_of_message:
            print()

    elif isinstance(chunk, AgentAnswer):
        print(f"Answer: {chunk.content}", end='', flush=True)
        if chunk.end_of_message:
            print()
```

Agent streaming provides visibility into:
- **Thoughts** - The agent's reasoning and planning
- **Observations** - Results from tools the agent invokes
- **Answers** - The final response to the user's question

Optional parameters for agent queries:
- `state` - Initial agent state (dict)
- `group` - Tool group available to agent (string)
- `history` - Conversation history (list of dicts)
