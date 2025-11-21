---
title: First Steps
nav_order: 3
parent: Getting Started
grand_parent: TrustGraph Documentation
---

# First Steps

Get started with your TrustGraph deployment and perform your first knowledge extraction and Graph RAG queries.

## Prerequisites

This guide assumes you have TrustGraph already deployed using one of the [installation methods](installation). If you haven't deployed TrustGraph yet, start with the [Installation Guide](installation).

## Install TrustGraph CLI

First, install the TrustGraph command-line interface in a Python virtual environment:

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install trustgraph-cli
```

> **Note**: Keep this virtual environment activated for all TrustGraph CLI commands.

## Verify TrustGraph Installation

### Check Container Status

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

### Verify Complete Startup

Check that all main services are running:

```bash
tg-show-flows
```

You should see a default flow. If you see an error, wait a moment and try again.

## Load Sample Documents

Load some sample documents to get started:

```bash
tg-load-sample-documents
```

## Access TrustGraph Interfaces

### Web Workbench

Access the TrustGraph web interface at [http://localhost:8888/](http://localhost:8888/)

Verify the workbench is working:
- **Prompts page**: Check that you can see system prompts
- **Library page**: Verify you can see the sample documents you just loaded

### Monitoring with Grafana

Access Grafana monitoring at [http://localhost:3000/](http://localhost:3000/)

- **Login**: admin / admin
- **Dashboard**: Select the TrustGraph dashboard
- **Skip password change** or set a new password

After loading documents, you should see the processing backlog rise to a few hundred document chunks.

## Process Your First Document

### Load a Document via Workbench

1. Go to the **Library page** in the workbench
2. Select a document ("Beyond State Vigilance" is a good starting document)
3. Click on the document to select it
4. Click **Submit** in the action bar at the bottom
5. Select a processing flow (use the default)
6. Click **Submit** to start processing

### Monitor Processing

Watch the processing progress in Grafana. You should see the backlog rise as the document is chunked and processed.

## Verify Knowledge Graph Creation

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

## Explore Your Knowledge

### Vector Search

1. In the workbench, click the **Vector Search** tab
2. Search for a term (e.g., "state")
3. Review the search results
4. Click on results to explore the knowledge graph
5. Use **Graph View** to visualize relationships

### Graph RAG Queries

1. In the workbench, click the **Graph RAG** tab
2. Enter a question about your document:
   ```
   What is this document about?
   ```
3. Review the contextual response generated using your knowledge graph

### CLI Graph RAG

You can also run Graph RAG queries from the command line:

```bash
tg-invoke-graph-rag "What are the main topics covered in the loaded documents?"
```

## Shut Down TrustGraph

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

## Next Steps

Now that you've successfully:
- ✅ Verified your TrustGraph installation
- ✅ Loaded and processed documents
- ✅ Created knowledge graphs
- ✅ Performed Graph RAG queries

**Continue learning:**
- [Core Concepts](concepts): Understand TrustGraph architecture
- [Deployment Options](../deployment/): Explore production deployments
- [API Reference](../reference/): Learn about TrustGraph APIs
