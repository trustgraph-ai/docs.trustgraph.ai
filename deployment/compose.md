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
guide_time: 10 - 15 min
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
<li>Machine with 12GB+ RAM and 8 CPUs available for TrustGraph to use - a 16GB Macbook or laptop will probably cope</li>
<li>Docker Engine or Podman installed (see below)</li>
<li>Python 3 for CLI tools (see below)</li>
<li>Access to an LLM (cloud service like VertexAI, AWS Bedrock, or local with Ollama)</li>
<li>Basic command-line familiarity</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Launch a complete TrustGraph environment locally using Docker or Podman for development, testing, and learning."
%}

## Overview

Docker and Podman are popular container hosting environments which run on
many types of system.  Docker was the original container engine and runs on
Linux, MacOS and Windows.  Podman uses the Linux-kernel container
capabilities, and can also run on MacOS.  Podman is an open-source alternative
built to be highly compatible with Docker engine.

Docker and Podman both have a "compose" utility which lets you easily
manage a group of running containers.  This guide takes you through
launching TrustGraph using Docker/Podman compose.

Using Docker/Podman is the easiest way to launch a TrustGraph, because you
can run it on a standalone environment.  If you have a desktop/laptop
with enough resources, you can run TrustGraph directly on that device.

This is a good way to get started for local development and testing,
proof-of-concept building, small-scale experiments, or just to learn more.

## Getting ready

### System resources

As mentioned above, you need a machine with at least 12GB of RAM and 8 CPUs
available for TrustGraph.  That means if you're running other significant
resources on it, it will probably fail. We can run TrustGraph on 16GB
Macbook, but not when other things are running.

You can also deploy an instance to your favourite cloud provider and use
that.

This has been tested with Linux, MacOS and Windows devices.

### Python

{% include deployment/python-requirement.md %}

### Docker / Podman

{% include deployment/docker-podman-install.md %}

### Large Language Model

{% include llm/llm-providers-overview.md %}

### A word on networking and self-hosting

If you are self-hosting a model on the same device you are intending
to run TrustGraph, you will need to understand how to get TrustGraph
to talk to your model service.

If you are trying to connect TrustGraph to a service running on the host,
read [Container networking and self-hosted models](container-networking).

If you are trying to connect TrustGraph to a service running on WSL,
read [WSL networking and self-hosted models](wsl-networking).

## Prepare the deployment

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

It is possible that this is all you need to prepare to launch the
containers.  If you are having problems launching TrustGraph you might
consider modifying the unpacked configuration for environments
where container engines use stricter access policies:

<details>
<summary>Remove file access restrictions</summary>

<div markdown="1">
The first thing you might try doing is add read permissions to the files
for any user on your system.  This may be necessary if your system has
stricter access control policies on the files that can be read by containers.
</div>

<div markdown="1">
```sh
find garage/ loki/ prometheus/ grafana/ trustgraph/ -type f | xargs chmod 644
find garage/ loki/ prometheus/ grafana/ trustgraph/ -type d | xargs chmod 755
```
</div>

<div markdown="1">
This adds global-read access of these configuration files to any user on your
system, which may be a problem if you have multiple users accessing the
system.
</div>

</details>

<details>
<summary>Configure SElinux access controls</summary>

<div markdown="1">
On Linux, if you are running SElinux, it may also be necessary to grant
particular SElinux permissions to the configuration files so that they
can be read by Linux:
</div>

<div markdown="1">
```sh
sudo chcon -Rt svirt_sandbox_file_t garage/ loki/ grafana/ prometheus/ trustgraph/
```
</div>

</details>

## Install CLI tools

You need to have access to TrustGraph client tools.  In the terminal
window you created above, install a virtual environment, and the
TrustGraph CLI tools.  Make sure the version number of the CLI tools
matches the version you chose to build a configuration for earlier.
i.e. replace `1.8.9` with the version you used earlier.

```sh
python3 -m venv env
. env/bin/activate
pip install trustgraph-cli==1.8.9
```

## Configure LLM settings

Depending on which LLM you selected, there are some configuration settings
you need to prepare:

{% include llm/llm-configuration-details-compose.md %}

## Configure security settings

For this local deployment, set the following security variables to
empty strings to disable authentication:

```sh
export MCP_SERVER_SECRET=""
export GATEWAY_SECRET=""
```

The `MCP_SERVER_SECRET` protects the MCP server with a secret but is not fully
implemented yet. The `GATEWAY_SECRET` provides single-secret protection for the
gateway API, which does not currently support comprehensive API security. For a
local non-networked deployment, it is safe to disable authentication by setting
these to empty strings.

## Launch TrustGraph

{% capture docker %}
```sh
docker-compose -f docker-compose.yaml up -d
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

### Startup period

It can take around 40 - 120 seconds for all services to stabilize. Services
like Pulsar and Cassandra need time to initialize properly.
There is a utility which runs a series of checks to verify the system
as it starts and reports when the system is working successfully.

### Verify system health

{% include deployment/application-localhost/verify-system-health.md %}

If everything appears to be working, the following parts of the deployment
guide are a whistle-stop tour through various parts of the system.

## Load sample documents

{% include deployment/application-localhost/load-sample-documents.md %}

## Workbench

{% include deployment/application-localhost/workbench.md %}

## Monitoring dashboard

{% include deployment/application-localhost/monitoring-dashboard.md %}

## Check the LLM is working

{% include deployment/workbench/check-llm-working.md %}

## Working with a document

### Load a document

{% include deployment/workbench/load-document.md %}

### Use Vector search

{% include deployment/workbench/vector-search.md %}

### Look at knowledge graph

{% include deployment/workbench/knowledge-graph.md %}

### Query with Graph RAG

{% include deployment/workbench/graph-rag-query.md %}

## Shutting down

### Clean shutdown

Once you have finished with your system, you can close it down.
The easiest way is to reverse the launch operation you ran up:

{% capture docker_shutdown %}
```bash
docker-compose -f docker-compose.yaml down -v -t 0
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

The `-v` option specifies to delete all data volumes.  The `-t 0` option
directs to close down containers without delay - the default is to wait for
clean shutdown.

### Manual cleanup

If the compose shutdown has problems, you can check and see what containers
are running with the `docker`/`podman` tools.


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

## Troubleshooting

### Service Failure

<details>
<summary>Run out of memory</summary>
<div markdown="1">

*Diagnosis:*

Check which containers are running. Init containers (names ending in `-init`)
should show `Exited (0)` - this is normal. Other containers should be running.

{% capture docker_ps %}
```bash
# Show all containers
docker ps -a

# Find OOM-killed containers (exit code 137)
docker ps -a --filter 'exited=137'

# Inspect a failed container for details
docker inspect <container-name> | grep -A 5 "OOMKilled\|Error"
```
{% endcapture %}

{% capture podman_ps %}
```bash
# Show all containers
podman ps -a

# Find OOM-killed containers (exit code 137)
podman ps -a --filter 'exited=137'

# Inspect a failed container for details
podman inspect <container-name> | grep -A 5 "OOMKilled\|Error"
```
{% endcapture %}

{% include code_tabs.html
   tabs="Docker,Podman"
   content1=docker_ps
   content2=podman_ps
%}

Look for `"OOMKilled": true` or error messages in the inspect output.

*Resolution:*

- **Docker Desktop**: Increase memory allocation in Settings → Resources
- **Alternative**: Run on a machine with more available memory (16GB+ recommended)

</div>
</details>

<details>
<summary>Hitting major CPU resource limits</summary>
<div markdown="1">

*Diagnosis:*

System is very slow to start, taking several minutes to become available.
Operations are sluggish. Check CPU load:

```bash
# Monitor CPU usage
top

# Or use htop if available
htop
```

If CPU load remains very high (near 100%) for an extended period during startup
and operations, this indicates insufficient CPU resources or an older CPU
architecture struggling with the workload.

*Resolution:*

Migrate to a device with more CPU cores or a newer CPU architecture. TrustGraph
requires 8 CPUs minimum, but more cores or faster processors will improve
performance significantly.

</div>
</details>

<details>
<summary>Configuration volume mount access restriction</summary>
<div markdown="1">

*Diagnosis:*

Check for failures in containers that need configuration files (Prometheus, Grafana,
Loki). View their logs for permission denied or file access errors:

{% capture docker_config_logs %}
```bash
# Check Prometheus logs
docker logs prometheus

# Check Grafana logs
docker logs grafana
```
{% endcapture %}

{% capture podman_config_logs %}
```bash
# Check Prometheus logs
podman logs prometheus

# Check Grafana logs
podman logs grafana
```
{% endcapture %}

{% include code_tabs.html
   tabs="Docker,Podman"
   content1=docker_config_logs
   content2=podman_config_logs
%}

Look for errors mentioning "permission denied" or inability to read configuration files.

*Resolution:*

Review and apply the file permission steps from the [Unpack the configuration](#unpack-the-configuration)
section, including:
- Setting global-read permissions with `chmod`
- Configuring SELinux permissions with `chcon` (Linux only)

</div>
</details>

<details>
<summary>Application error</summary>
<div markdown="1">

*Diagnosis:*

Find failed containers and examine their logs:

{% capture docker_logs %}
```bash
# Show all containers
docker ps -a

# View logs for a specific container
docker logs <container-name>

# Follow logs in real-time
docker logs -f <container-name>
```
{% endcapture %}

{% capture podman_logs %}
```bash
# Show all containers
podman ps -a

# View logs for a specific container
podman logs <container-name>

# Follow logs in real-time
podman logs -f <container-name>
```
{% endcapture %}

{% include code_tabs.html
   tabs="Docker,Podman"
   content1=docker_logs
   content2=podman_logs
%}

Alternatively, view aggregated logs in the Grafana dashboard at
[http://localhost:3000/](http://localhost:3000/) (default credentials:
admin/admin). The Logs dashboard shows all TrustGraph container logs in one place.

*Resolution:*

Resolution depends on the specific error message. Common issues include
configuration errors, missing environment variables, or service dependencies
not being ready.

</div>
</details>

### LLM Failure

<details>
<summary>LLM configuration error</summary>
<div markdown="1">

*Diagnosis:*

The system appears to be running but LLM connectivity is not working. Test LLM
connectivity:

```bash
tg-invoke-llm '' 'What is 2+2'
```

A long timeout or error indicates LLM configuration issues. Check the Grafana
logs dashboard at [http://localhost:3000/](http://localhost:3000/) for
application logs. Look for errors in the `text-completion` container logs
which indicate LLM connection failures.

*Resolution:*

Review the LLM configuration settings in the [Configure LLM settings](#configure-llm-settings)
section. Common issues include:
- Missing or incorrect API keys
- Wrong endpoint URLs
- Missing `/v1` suffix for self-hosted models
- Incorrect `host.containers.internal` hostname for local services

</div>
</details>

<details>
<summary>Locally-hosted LLM connectivity error</summary>
<div markdown="1">

*Diagnosis:*

Check the Grafana logs dashboard for connectivity errors in the `text-completion`
container. Look for errors indicating connection refused, timeouts, or unreachable
hosts when attempting to connect to your LLM service.

*Resolution:*

Review your network connectivity and addressing configuration:

- Verify your LLM service is running and accessible
- Check the URL configuration for your LLM (environment variables like
  `OLLAMA_HOST`, `LMSTUDIO_URL`, `VLLM_URL`, etc.)
- For services on the same host, ensure you're using `host.containers.internal`
  as the hostname
- Verify the correct port number
- Ensure URLs include `/v1` suffix where required

See also:
- [Container networking and self-hosted models](container-networking)
- [WSL networking and self-hosted models](wsl-networking)

</div>
</details>

## Next Steps

- **Guides**: See [Guides](../guides) for things you can do with your running
  TrustGraph

