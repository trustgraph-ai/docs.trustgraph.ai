---
title: Getting Started
layout: default
nav_order: 2
has_children: true
parent: TrustGraph Documentation
---

# Getting Started with TrustGraph

Welcome to TrustGraph! This section will help you get up and running quickly.

## Quick Start Path

1. **[Core Concepts](concepts)** - Understand key TrustGraph concepts
2. **[Installation](installation)** - Deploy TrustGraph in the environment of your choice
3. **[First Steps](first-steps)** - Interact with your TrustGraph instance,
   load some data and get some results from it.

## What You'll Learn

- What TrustGraph is, and why you would want to use it
- Core concepts and terminology
- How to deploy TrustGraph
- Basic configuration and setup
- First-hand experience of some basic usage

## Quickstart with Docker

Docker Compose provides the easiest way to get TrustGraph running locally with all required services orchestrated together. This deployment method is ideal for:
- Local development and testing
- Proof-of-concept implementations
- Small-scale deployments
- Learning and experimentation

### System Requirements

- **Docker Engine** or **Podman Machine** installed and running
- **Operating System**: Linux or macOS (Windows deployments not tested)
- **Python 3.x** for CLI tools
- Sufficient system resources (recommended: 8GB RAM, 4 CPU cores)

### Installation Links

- [Install Docker Engine](https://docs.docker.com/engine/install/)
- [Install Podman Machine](http://podman.io/)

> **Note**: If using Podman, substitute `podman` for `docker` in all commands.

### Configuration Setup

#### Create Configuration

Use the [TrustGraph Configuration Builder](https://config-ui.demo.trustgraph.ai/) to generate your deployment configuration:

1. **Select Deployment**: Choose Docker Compose or Podman Compose
2. **Graph Store**: Select Cassandra (recommended for ease of use)
3. **Vector Store**: Select Qdrant (recommended for ease of use)
4. **Chunker Settings**: 
   - Type: Recursive
   - Chunk size: 1000
   - Overlap: 50
5. **LLM Model**: Choose your preferred model:
   - **Local**: LMStudio or Ollama for local GPU deployment
   - **Cloud**: VertexAI on Google (offers free credits)
6. **Output Tokens**: 2048 (safe default)
7. **Customization**: Enable LLM Prompt Manager and Agent Tools
8. **Generate**: Download the deployment bundle

#### Install CLI Tools

```bash
python3 -m venv env
source env/bin/activate # On Windows: env\Scripts\activate
pip install trustgraph-cli
```

> **Note**: Keep this virtual environment activated for all TrustGraph CLI commands.

### Verify TrustGraph Installation

#### Check Container Status

After deployment, it may take a while to pull all necessary components. Verify that TrustGraph processors have started:

```bash
tg-show-processor-state
```

Processors start quickly, but Pulsar and Cassandra can take up to 60 seconds to initialize.

If you're using Docker Compose, check that containers are running:

```bash
docker ps
```

Any containers that have exited unexpectedly can be found with:

```bash
docker ps -a
```

> **Important**: Allow the system to stabilize for 120 seconds before proceeding. Services may appear "stuck" if they didn't have time to initialize correctly.

#### Verify Complete Startup

Check that all main services are running:

```bash
tg-show-flows
```

You should see a default flow. If you see an error, wait a moment and try again.

### Load Sample Documents

Load some sample documents to get started:

```bash
tg-load-sample-documents
```

### Access TrustGraph Interfaces

#### Web Workbench

Access the TrustGraph web interface at [http://localhost:8888/](http://localhost:8888/)

Verify the workbench is working:
- **Prompts page**: Check that you can see system prompts
- **Library page**: Verify you can see the sample documents you just loaded

#### Monitoring with Grafana

Access Grafana monitoring at [http://localhost:3000/](http://localhost:3000/)

- **Login**: admin / admin
- **Dashboard**: Select the TrustGraph dashboard
- **Skip password change** or set a new password

After loading documents, you should see the processing backlog rise to a few hundred document chunks.

### Process Your First Document

#### Load a Document via Workbench

1. Go to the **Library page** in the workbench
2. Select a document ("Beyond State Vigilance" is a good starting document)
3. Click on the document to select it
4. Click **Submit** in the action bar at the bottom
5. Select a processing flow (use the default)
6. Click **Submit** to start processing

#### Monitor Processing

Watch the processing progress in Grafana. You should see the backlog rise as the document is chunked and processed.

### Verify Knowledge Graph Creation

Check that the knowledge graph is successfully parsing data:

```bash
tg-show-graph
```

The output should show semantic triples in [N-Triples](https://www.w3.org/TR/rdf12-n-triples/) format:

```
<http://trustgraph.ai/e/enterprise> <http://trustgraph.ai/e/was-carried> "to altitude and released for a gliding approach" .
<http://trustgraph.ai/e/enterprise> <http://www.w3.org/2000/01/rdf-schema#label> "Enterprise" .
<http://trustgraph.ai/e/enterprise> <http://www.w3.org/2004/02/skos/core#definition> "A prototype space shuttle orbiter used for atmospheric flight testing" .
```

### Explore Your Knowledge

#### Vector Search

1. In the workbench, click the **Vector Search** tab
2. Search for a term (e.g., "state")
3. Review the search results
4. Click on results to explore the knowledge graph
5. Use **Graph View** to visualize relationships

#### GraphRAG Queries

1. In the workbench, click the **Graph RAG** tab
2. Enter a question about your document:
   ```
   What is this document about?
   ```
3. Review the contextual response generated using your knowledge graph

#### CLI GraphRAG

You can also run Graph RAG queries from the command line:

```bash
tg-invoke-graph-rag "What are the main topics covered in the loaded documents?"
```

### Shut Down TrustGraph

When you're finished, properly shut down TrustGraph:

**For Docker Compose:**
```bash
docker-compose down -v -t 0
```

**Verify cleanup:**
```bash
# Check no containers are running
docker ps

# Check volumes are removed
docker volume ls
```
