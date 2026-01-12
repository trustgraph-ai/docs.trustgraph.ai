---
title: Building with the Python API
nav_order: 2.4
parent: How-to Guides
grand_parent: TrustGraph Documentation
review_date: 2026-08-01
guide_category:
  - Building with TrustGraph
guide_category_order: 4
guide_description: Use the TrustGraph Python API to build custom applications and integrations
guide_difficulty: intermediate
guide_time: 30 min
guide_emoji: 🐍
guide_banner: /../python.jpg
guide_labels:
  - Python
  - API
todo: true
todo_notes: This is just a placeholder.
---

# Building with the Python API

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>A running TrustGraph deployment</li>
<li>Python 3.8 or higher</li>
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
pip install trustgraph-base==1.8.10
```
{% endcapture %}

{% capture uv_install_version %}
```bash
uv pip install trustgraph-base==1.8.10
```
{% endcapture %}

{% capture poetry_install_version %}
```bash
poetry add trustgraph-base@1.8.10
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

## Creating a Client

To connect to TrustGraph, create an `Api` client object:

```python
from trustgraph.api import Api

# Connect to TrustGraph
api = Api(url='http://localhost:8088/')
```

**With authentication:**

```python
from trustgraph.api import Api

# Connect with authentication token
api = Api(
    url='http://localhost:8088/',
    token='your-token-here'
)
```

**Using environment variables:**

```python
import os
from trustgraph.api import Api

# Get configuration from environment
url = os.getenv('TRUSTGRAPH_URL', 'http://localhost:8088/')
token = os.getenv('TRUSTGRAPH_TOKEN', None)

api = Api(url=url, token=token)
```

## Service Access Pattern

TrustGraph uses a consistent pattern: create an `Api` object, then call service methods to get service handlers.

**Global services** are accessed directly from the API object:

```python
api = Api(url='http://localhost:8088/')

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

**Flow-specific services** use a different pattern:

```python
api = Api(url='http://localhost:8088/')

# Access a specific flow
flow = api.flow().id('default')

# Use the flow
response = flow.text_completion(system="You are helpful", prompt="Hello")
```

**Async variants:**

All services have async variants with the `async_` prefix:

```python
api = Api(url='http://localhost:8088/')

# Async versions
flow_service = api.async_flow()
config_service = api.async_config()
# ... and so on
```
