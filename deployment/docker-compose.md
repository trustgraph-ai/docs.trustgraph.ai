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

# Docker/Podman compose deployment

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>Machine with 12GB+ RAM and 8 CPUs (16GB recommended)</li>
<li>Docker Engine or Podman installed</li>
<li>Python 3 for CLI tools</li>
<li>Access to an LLM (cloud service like VertexAI, AWS Bedrock, or local with Ollama)</li>
<li>Basic command-line familiarity</li>
</ul>
{% endcapture %}

{% include guide-intro-box.html
   description=page.guide_description
   difficulty="{{ page.guide_difficulty | capitalize }}"
   duration=page.guide_time
   you_will_need=requirements
   goal="Launch a complete TrustGraph environment locally using Docker or Podman for development, testing, and learning."
%}

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

### System requirements

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

## Configuration setup

### Create configuration

Use the
[TrustGraph Configuration Builder](https://config-ui.demo.trustgraph.ai/)
to generate your deployment configuration.  By default, the configurator
selects the newest stable deployment.  To be compatible with this installation guide, you should make sure to use a version later than 1.8.9.

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
unzip -l deploy.zip 
```

The output should look something like this:

```sh
Archive:  deploy.zip
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
mkdir -p ~/trustgraph
cd ~/trustgraph
unzip ~/Downloads/deploy.zip
```

That may be all you need to unpack the TrustGraph file.  If you are having
problems launching TrustGraph, you might consider modifying the unpacked
files to help Docker or Podman work with them.

The first thing you might try doing is add read permissions to the files
for any user on your system.  This may be necessary if your system has
stricter access control policies on the files that can be read by containers.

```sh
find garage/ loki/ prometheus/ grafana/ trustgraph/ vertexai/ -type f | xargs chmod 644

find garage/ loki/ prometheus/ grafana/ trustgraph/ vertexai/ -type d | xargs chmod 755
```

On Linux, if you are running SElinux, it may also be necessary to grant
particular SElinux permissions to the configuration files so that they
can be read by Linux:

```sh
sudo chcon -Rt svirt_sandbox_file_t garage/ loki/ grafana/ \
    prometheus/ vertexai/ trustgraph/
```

## Install CLI tools

You need to have access to TrustGraph client tools.  In the terminal
window you created above, install a virtual environment, and the
TrustGraph CLI tools.  Make sure the version number of the CLI tools
matches the version you chose to build a configuration for earlier:

```sh
python3 -m venv env
. env/bin/activate
pip install trustgraph-cli==1.8.9
```

## Launch TrustGraph

{% capture docker %}
```sh
docker compose -f docker-compose.yaml up -d
```
{% endcapture %}

{% capture podman %}
```sh
podman-compose -f docker-compose.yaml up -d
```
{% endcapture %}

{% include code_tabs.html
   tabs="Docker,Podman"
   content1=docker
   content2=podman
%}

## Wait for initialization

Allow 120 seconds for all services to stabilize. Services like Pulsar and Cassandra need time to initialize properly.

### Verify installation

There is a utility which runs a series of checks to verify the system
as it starts.

```sh
tg-verify-system-status
```

The output looks something like...

```
============================================================
TrustGraph System Status Verification
============================================================

Phase 1: Infrastructure
------------------------------------------------------------
[00:00] ⏳ Checking Pulsar...
[00:03] ⏳ Checking Pulsar... (attempt 2)
[00:03] ✓ Pulsar: Pulsar healthy (0 cluster(s))
[00:03] ⏳ Checking API Gateway...
[00:03] ✓ API Gateway: API Gateway is responding

Phase 2: Core Services
------------------------------------------------------------
[00:03] ⏳ Checking Processors...
[00:03] ✓ Processors: Found 34 processors (≥ 15)
[00:03] ⏳ Checking Flow Classes...
[00:06] ⏳ Checking Flow Classes... (attempt 2)
[00:09] ⏳ Checking Flow Classes... (attempt 3)
[00:22] ⏳ Checking Flow Classes... (attempt 4)
[00:35] ⏳ Checking Flow Classes... (attempt 5)
[00:38] ⏳ Checking Flow Classes... (attempt 6)
[00:38] ✓ Flow Classes: Found 9 flow class(es)
[00:38] ⏳ Checking Flows...
[00:38] ✓ Flows: Flow manager responding (1 flow(s))
[00:38] ⏳ Checking Prompts...
[00:38] ✓ Prompts: Found 16 prompt(s)

Phase 3: Data Services
------------------------------------------------------------
[00:38] ⏳ Checking Library...
[00:38] ✓ Library: Library responding (0 document(s))

Phase 4: User Interface
------------------------------------------------------------
[00:38] ⏳ Checking Workbench UI...
[00:38] ✓ Workbench UI: Workbench UI is responding

============================================================
Summary
============================================================
Checks passed: 8/8
Checks failed: 0/8
Total time: 00:38

✓ System is healthy!
```

## Load sample documents

There is a utility which loads a small set of sample documents into the
library.  This does not initiate processing, but gives you a set of documents
to test with:

```sh
tg-load-sample-documents
```

## Workbench

Access the TrustGraph workbench at [http://localhost:8888/](http://localhost:8888/)

## Monitoring dashboard

Access Grafana monitoring at [http://localhost:3000/](http://localhost:3000/)

**Default credentials:**
- Username: `admin`
- Password: `admin`

## Working with a document

### Load Documents

**Via Workbench:**
1. Navigate to the Library page
2. In the upper right-hand corner, there is a dark/light mode widget.
   To its left, is a selector width.  Ensure the top and bottom lines say
   "default".  If not click on the widget and change.
2. On the library tab, select a document (e.g., "Beyond State Vigilance")
3. Click Submit on the action bar
4. Choose a processing flow (use Default processing flow)
5. Click Submit to process

### Use Vector search

Select the *Vector Search* tab.  Enter a string e.g. "document" in the search
bar, and hit RETURN.  The search term doesn't matter a great deal.  If
information has started to load, you should see some search results.

The vector search attempts to find up to 10 terms which are the closest
matches for your search term.  It does this even if the search terms are not
a strong match, so this is a simple way to observe whether dat has loaded.

### Verify knowledge graph

Check graph parsing results:

```bash
tg-show-graph
```

You should see some lines of text scrolling past.  This displays semantic
triples in N-Triples format:

```
<http://trustgraph.ai/e/enterprise> <http://trustgraph.ai/e/was-carried> "to altitude and released for a gliding approach" .
<http://trustgraph.ai/e/enterprise> <http://www.w3.org/2000/01/rdf-schema#label> "Enterprise" .
```

The structure isn't hugely important for this test, but it is a simple
way to verify that data has loaded.

### Query with Graph RAG

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

{% capture docker_shutdown %}
```bash
docker compose -f docker-compose.yaml down -v -t 0
```
{% endcapture %}

{% capture podman_shutdown %}
```bash
podman-compose -f docker-compose.yaml down -v -t 0
```
{% endcapture %}

{% include code_tabs.html
   tabs="Docker,Podman"
   content1=docker_shutdown
   content2=podman_shutdown
%}

### Verify Cleanup

{% capture docker_verify %}
```bash
# Confirm no containers running
docker ps

# Confirm volumes removed
docker volume ls
```
{% endcapture %}

{% capture podman_verify %}
```bash
# Confirm no containers running
podman ps

# Confirm volumes removed
podman volume ls
```
{% endcapture %}

{% include code_tabs.html
   tabs="Docker,Podman"
   content1=docker_verify
   content2=podman_verify
%}

## Next Steps

- **Guides**: See [Guides](../guides) for things you can do with your running
  TrustGraph
