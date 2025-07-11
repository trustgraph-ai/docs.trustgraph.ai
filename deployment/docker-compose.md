---
title: Docker Compose / Podman Compose
layout: default
nav_order: 1
parent: Deployment
grand_parent: TrustGraph Documentation
---

# Docker/Podman Compose Deployment

Deploy TrustGraph quickly using Docker Compose for local development and testing environments.

## Overview

Docker Compose provides the easiest way to get TrustGraph running locally with all required services orchestrated together. This deployment method is ideal for:
- Local development and testing
- Proof-of-concept implementations
- Small-scale deployments
- Learning and experimentation

## Prerequisites

### System Requirements

- **Docker Engine** or **Podman Machine** installed and running
- **Operating System**: Linux or macOS (Windows deployments not tested)
- **Python 3.x** for CLI tools
- Sufficient system resources (recommended: 8GB RAM, 4 CPU cores)

### Installation Links

- [Install Docker Engine](https://docs.docker.com/engine/install/)
- [Install Podman Machine](http://podman.io/)

> **Note**: If using Podman, substitute `podman` for `docker` in all commands.

## Configuration Setup

### 1. Create Configuration

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

### 2. Install CLI Tools

```bash
python3 -m venv env
source env/bin/activate
pip install trustgraph-cli
```

## Quick Start

### 1. Launch TrustGraph

```bash
docker-compose -f docker-compose.yaml up -d
```

### 2. Wait for Initialization

Allow 120 seconds for all services to stabilize. Services like Pulsar and Cassandra need time to initialize properly.

### 3. Verify Installation

Check that processors have started:

```bash
tg-show-processor-state
```

Verify all containers are running:

```bash
docker ps
```

Check that flows are available:

```bash
tg-show-flows
```

### 4. Load Sample Data

```bash
tg-load-sample-documents
```

## Services & Interfaces

### Web Workbench

Access the TrustGraph workbench at [http://localhost:8888/](http://localhost:8888/)

**Features:**
- Document library management
- Vector search interface
- Graph visualization
- Graph RAG query interface
- Prompt management

### Monitoring Dashboard

Access Grafana monitoring at [http://localhost:3000/](http://localhost:3000/)

**Default credentials:**
- Username: `admin`
- Password: `admin`

**Features:**
- TrustGraph dashboard
- Processing metrics
- System health monitoring
- Document processing backlog

## Working with Documents

### 1. Load Documents

**Via Workbench:**
1. Navigate to the Library page
2. Select a document (e.g., "Beyond State Vigilance")
3. Click Submit on the action bar
4. Choose a processing flow (use default)
5. Click Submit to process

**Via CLI:**
```bash
tg-load-pdf path/to/document.pdf
tg-load-text path/to/document.txt
```

### 2. Verify Knowledge Graph

Check graph parsing results:

```bash
tg-show-graph
```

This displays semantic triples in N-Triples format:

```
<http://trustgraph.ai/e/enterprise> <http://trustgraph.ai/e/was-carried> "to altitude and released for a gliding approach" .
<http://trustgraph.ai/e/enterprise> <http://www.w3.org/2000/01/rdf-schema#label> "Enterprise" .
```

### 3. Query with Graph RAG

**Via Workbench:**
1. Navigate to Graph RAG tab
2. Enter your question (e.g., "What is this document about?")
3. View contextual responses

**Via CLI:**
```bash
tg-invoke-graph-rag "What is this document about?"
```

## Troubleshooting

### Common Issues

**Services Not Starting:**
- Wait 120 seconds for full initialization
- Check container status: `docker ps -a`
- Review logs: `docker-compose logs [service-name]`

**Memory Issues:**
- Ensure sufficient RAM (8GB recommended)
- Monitor resource usage: `docker stats`

**Connection Issues:**
- Verify ports are available (8888, 3000)
- Check firewall settings
- Ensure Docker daemon is running

### Debugging Commands

```bash
# Check all containers
docker ps -a

# View logs for specific service
docker-compose logs [service-name]

# Check system resources
docker stats

# Verify TrustGraph flows
tg-show-flows

# Check processor state
tg-show-processor-state
```

## Shutdown

### Clean Shutdown

```bash
docker-compose -f docker-compose.yaml down -v -t 0
```

### Verify Cleanup

```bash
# Confirm no containers running
docker ps

# Confirm volumes removed
docker volume ls
```

## Next Steps

- **Production Deployment**: See [Production Considerations](production-considerations)
- **Cloud Deployment**: Explore [AWS](aws), [GCP](gcp), or [Scaleway](scaleway) guides
- **Advanced Configuration**: Check [Security Considerations](security-considerations)
- **Scaling**: Review [Minikube](minikube) for Kubernetes deployment
