---
title: Docker / Podman Compose
nav_order: 1
parent: Deployment
grand_parent: TrustGraph Documentation
review_date: 2026-03-20
guide_category:
  - Standalone deployment
guide_category_order: 1
guide_description: Easiest way to get TrustGraph running locally with Docker or Podman for development and testing
guide_difficulty: beginner
guide_time: 30 - 60 min
guide_emoji: 🐳
guide_banner: /../podman.png
guide_labels:
  - Docker
  - Local
  - Quick Start
---

# Docker/Podman Compose Deployment

## Overview

Docker and Podman are popular container hosting environments which run on
many types of system.  Docker was the original container engine and runs on
Linux, MacOS and Windows.  Podman uses the Linux-kernel container
capabilties, and can also run on MacOS.  Podman is an open-source alternative
built to be highly compatible with Docker engine.

Docker and Podman both have a "compose" utility which lets you easily
manage a group of running containers.  This guide takes you through
launching TrustGraph using Docker/Podman compose.

Using Docker/Podman is the easiest way to launch a TrustGraph, because you
can run it on a standalone environment.  If you have a desktop/laptop
with enough resources, you can run TrustGraph directly on that device.

This is a good way to get started for local development and testing,
proof-of-concept building, small-scale experiments, or just to learn more.

## Prerequisites

### System Requirements

You need a machine with at least 12GB of RAM and 8 CPUs available.
A 16GB machine is probably enough.

This has been tested with Linux, MacOS and Windows deployments.

You need to have Python 3 installed to run the command-line tools.

### Docker / Podman

For Windows / MacOS we would recommend using Docker.  For Linux, podman is
natively available with all major distributions.  You will need to have this
installed before running this guide.

- [Install Docker Engine](https://docs.docker.com/engine/install/)
- [Install Podman Machine](http://podman.io/)

### Large Language Model

You need to have access to an LLM.  TrustGraph can work with many different
kinds of LLM.  You can use a cloud-hosted service, or have an LLM hosted
locally on your device or network.  TrustGraph can work with small models,
but small models are still demanding on resources.

Using a cloud-hosted service is a good starting point - you will need a
subscription, but no extra hardware.  If you do want to run an LLM locally,
you will need a device with a good GPU, and likely some experience of
running this yourself as you may need to debug model / hosting issues.

Here are some example ways to get an LLM to run:

| Provider | Description | Best For |
|----------|-------------|----------|
| **Google Cloud VertexAI** | Access to Gemini models and other Google-hosted LLMs. Offers free credits for new users. | Cost-effective cloud option, good performance with Gemini Flash 1.5 |
| **AWS Bedrock** | Amazon's managed LLM service with Claude, Mistral, and other models available. | AWS ecosystem integration, enterprise deployments |
| **Azure OpenAI** | Microsoft's managed service providing GPT-4o and other OpenAI models. | Azure ecosystem integration, enterprise support |
| **Anthropic Claude** | Direct access to Claude models via API subscription. | High-quality responses, large context windows |
| **OpenAI** | Direct access to GPT models (GPT-4, GPT-3.5) via API subscription. | Wide model selection, familiar API |
| **Ollama** | Run models locally on your machine. Supports Llama, Mistral, and many others. | Local deployment, no cloud costs, privacy |
| **LMStudio** | Desktop application for running local LLMs with an OpenAI-compatible API. | Easy local setup, GPU acceleration, privacy |
| **vLLM** | The most comprehensive self-hosted model engine | Well supported, GPU acceleration, privacy |

> **Note**: If using Podman, substitute `podman` for `docker` in all commands.

## Configuration Setup

### Create Configuration

Use the
[TrustGraph Configuration Builder](https://config-ui.demo.trustgraph.ai/)
to generate your deployment configuration.  By default, the configurator
selects the newest stable deployment.

{: .note }
Remember the version number it is set up to deploy, you will need to know that to install CLI tools!

1. **Select Deployment**: Choose Docker Compose or Podman Compose
2. **Graph Store**: Select Cassandra (recommended for ease of use)
3. **Vector Store**: Select Qdrant (recommended for ease of use)
4. **Chunker Settings**: 
   - Type: Recursive
5. **LLM Model**: Choose your preferred model as discussed above
6. **Output Tokens**: 2048 is a safe default, 4096 works for most models,
   8192 for the biggest models
7. **Customization**: Leave defaults
8. **Finish Deployment**: Click 'Generate' and then Download the
   deployment bundle
   
## Unpack the configuration

The configuration builder will download a `.zip` file containing your
deployment configuration which will be downloaded to your device in
e.g. a Downloads directory.  You need to find that zip file, and interact
with it in a terminal.  You can use the `unzip` command to list the
contents of the ZIP file.  There should be a `docker-compose.yaml` file
which is used to launch TrustGraph.  There are also various configuration
files for TrustGraph, Grafana, Garage, Loki and Prometheus.

```sh
unzip -l output.zip 
```

The output should look something like this:

```sh
Archive:  output.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
    26353  01-06-2026 23:04   docker-compose.yaml
   208539  01-06-2026 23:04   trustgraph/config.json
      581  01-06-2026 23:04   garage/garage.toml
     4084  01-06-2026 23:04   grafana/dashboards/log-dashboard.json
    36032  01-06-2026 23:04   grafana/dashboards/overview-dashboard.json
      336  01-06-2026 23:04   grafana/provisioning/dashboard.yml
      773  01-06-2026 23:04   grafana/provisioning/datasource.yml
     1518  01-06-2026 23:04   loki/local-config.yaml
     5259  01-06-2026 23:04   prometheus/prometheus.yml
---------                     -------
   283475                     9 files
```

You should use the terminal window to create a suitable directory for your
work and unpack the ZIP file e.g.

```sh
$ mkdir -p ~/trustgraph
$ cd ~/trustgraph
$ unzip ~/Downloads/trustgraph-deployment.zip
```

That may be all you need to unpack the TrustGraph file.  If you are having
problems launching TrustGraph, you might consider modifying the unpacked
files to help Docker or Podman work with them.

The first thing you might try doing is add read permissions to the files
for any user on your system.  This may be necessary if your system has
stricter access control policies on the files that can be read by containers.

```sh
$ find garage/ loki/ prometheus/ grafana/ trustgraph/ vertexai/ -type f | xargs chmod 644
$ find garage/ loki/ prometheus/ grafana/ trustgraph/ vertexai/ -type d | xargs chmod 755
```

On Linux, if you are running SElinux, it may also be necessary to grant
particular SElinux permissions to the configuration files so that they
can be read by Linux:

```sh
sudo chcon -Rt svirt_sandbox_file_t garage/ loki/ grafana/ \
    prometheus/ vertexai/ trustgraph/
```

## Install CLI Tools

You need to have access to TrustGraph client tools.  In the terminal
window you created above, install a virtual environment, and the
TrustGraph CLI tools.  Make sure the version number of the CLI tools
matches the version you chose to build a configuration for earlier:

```sh
python3 -m venv env
. env/bin/activate
pip install trustgraph-cli==1.8.8
```

## Launch TrustGraph

```sh
docker-compose -f docker-compose.yaml up -d
```

## Wait for Initialization

Allow 120 seconds for all services to stabilize. Services like Pulsar and Cassandra need time to initialize properly.

### Verify Installation

Check that processors have started:

```sh
tg-show-processor-state
```

Verify all containers are running:

```sh
docker ps
```

Check that flows are available:

```sh
tg-show-flows
```

### Load Sample Data

```sh
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

- **Guides**: See [Guides](../guides) for things you can do with your running
  TrustGraph
