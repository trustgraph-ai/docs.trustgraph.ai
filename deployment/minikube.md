---
title: Minikube
nav_order: 2
parent: Deployment
grand_parent: TrustGraph Documentation
review_date: 2026-05-17
guide_category:
  - Standalone deployment
guide_category_order: 2
guide_description: Run TrustGraph in a local Kubernetes cluster for production-like development and testing
guide_difficulty: intermediate
guide_time: 2 - 3 hr
guide_emoji: ☸️
guide_banner: /../minikube.png
guide_labels:
  - Kubernetes
  - Local
  - Development
---

# Minikube Deployment

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>Machine with 11GB+ RAM and 9 CPUs available for TrustGraph to use - a 16GB laptop will likely cope</li>
<li>Minikube installed and configured</li>
<li>kubectl command-line tool</li>
<li>Docker Engine (most common driver for Minikube) or another virtualization driver</li>
<li>Python 3.11+ for CLI tools</li>
<li>Access to an LLM (cloud service like VertexAI, AWS Bedrock, or local with Ollama)</li>
<li>Basic command-line and Kubernetes familiarity</li>
</ul>
{% endcapture %}

{% include guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Launch a complete TrustGraph environment in a local Kubernetes cluster using Minikube for production-like development, testing, and learning."
%}

## Overview

Minikube allows you to run TrustGraph in a local Kubernetes cluster, providing a production-like environment for development and testing. This deployment method offers:

- **Kubernetes-native deployment** with local development capabilities
- **Production-like environment** for testing at scale
- **Resource isolation** and management
- **LoadBalancer** and service discovery testing

This is a good way to learn TrustGraph in a Kubernetes environment before deploying to production clusters, or to test Kubernetes-specific features locally.

## Getting ready

### System resources

As mentioned above, you need a machine with at least 11GB of RAM and 9 CPUs
available for TrustGraph. That means if you're running other significant
workloads on it, it will probably fail. A 16GB laptop can typically run TrustGraph
in Minikube, but not when other resource-intensive applications are running.

You can also deploy a Minikube instance to your favourite cloud provider and use
that if local resources are limited.

This has been tested with Linux, MacOS and Windows devices.

### Python

You need to have Python 3 installed to run the command-line tools. You
should use a newer version, Python 3.11 or later.

<details>

<summary>Specific guidance for MacOS</summary>

<div markdown="1">
MacOS X-Code is the usual way to get developer tools on your Macbook. Note
that X-Code doesn't track later Python versions (Python 3.9)? If you're
on MacOS you should consider using Homebrew to install Python3, and
making sure that the Homebrew version of Python takes priority over
the default OS version. You can run the `python` command to see what
version of Python you have installed as the default.
</div>

<div markdown="1">
```
Python 3.14.2 (main, Dec  5 2025, 00:00:00) [GCC 15.2.1 20251111 (Red
Hat 15.2.1-4)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
</div>

</details>

### Minikube and kubectl

You need to have Minikube and kubectl installed:

- [Install Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Install kubectl](https://kubernetes.io/docs/tasks/tools/)

Minikube requires a driver for virtualization. The most common is Docker Engine,
but there are several options available depending on your platform:

- [Full Minikube driver documentation](https://minikube.sigs.k8s.io/docs/drivers/)

{: .note }
If you are using Docker as the Minikube driver, you may need to review the resource
settings as described in the system resources section above.

### Large Language Model

You need to have access to an LLM. TrustGraph can work with many different
kinds of LLM. You can use a cloud-hosted service, or have an LLM hosted
locally on your device or network. TrustGraph can work with small models
which you can run on standard home/office equipment,
but small models are still demanding on resources. A 16GB laptop is able to
run an LLM but likely not at the same time as running Minikube with TrustGraph.

Here are some example ways to get an LLM to run:

| Provider | Description | Access type |
|----------|-------------|----------|
| **Google Cloud VertexAI** | This is a subscription-based service which is part of Google Cloud. The Gemini models are good and cost-effective. There are free credits for new users. | Cloud subscription |
| **AWS Bedrock** | Amazon's managed LLM service with Claude, Mistral, and other models available. Running Claude on Bedrock is a good option. | Cloud subscription |
| **Azure** | Microsoft's cloud subscription services include Machine Learning Services (MLS) and Cognitive Services (CS). The TrustGraph *Azure* integration can use the MLS service, while *Azure OpenAI* can use CS models. | Cloud subscription |
| **Anthropic Claude** | Integrates with Anthropic's APIs directly for access to the Claude models. Claude models are very capable. | API subscription |
| **Mistral AI** | Integrates with Mistral's APIs directly for access to the Mistral models. | API subscription |
| **OpenAI** | Integrates with OpenAI's API for GPT models | API subscription |
| **Ollama** | Run models locally on your machine. Supports Llama, Mistral, and many others. | Self-hosted |
| **vLLM** | The most comprehensive self-hosted model engine | Self-hosted |
| **LMStudio** | Desktop application for running local LLMs with an OpenAI-compatible API. LMStudio is a very user-friendly experience, which makes it easier to diagnose and solve hosting problems. Note: LMStudio is free, but only for non-work-related use. | Self-hosted |

Using a cloud-hosted service is a good starting point - you will need a
subscription, but no extra hardware. If you do want to run an LLM locally,
you will need a device with a good GPU, and likely some experience of
running this yourself as you may need to debug model / hosting issues.

### A word on networking and self-hosting

If you are self-hosting a model on the same device you are intending
to run Minikube, you will need to understand how to get TrustGraph
to talk to your model service.

When Minikube services want to access services on the host, the hostname
`host.minikube.internal` can be used. For example, if you're running
Ollama on your host machine on port 11434, you would configure:
```
export OLLAMA_HOST=http://host.minikube.internal:11434
```

If you are trying to connect TrustGraph to a service running on WSL,
read [WSL networking and self-hosted models](wsl-networking).

## Prepare the deployment

### Create configuration

Use the
[TrustGraph Configuration Builder](https://config-ui.demo.trustgraph.ai/)
to generate your deployment configuration. By default, the configurator
selects the newest stable deployment. To be compatible with this installation guide, you should make sure to use a version later than 1.8.9.

{: .note }
Remember the version number it is set up to deploy, you will need to know that to install CLI tools!

1. **Select Deployment**: Choose Kubernetes/Minikube
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

The configuration builder will download a `.yaml` file (e.g., `trustgraph-minikube.yaml`)
containing your Kubernetes deployment configuration which will be downloaded to your
device in e.g. a Downloads directory.

You should create a suitable directory for your work and move the YAML file there:

```sh
mkdir -p ~/trustgraph-minikube
cd ~/trustgraph-minikube
mv ~/Downloads/trustgraph-minikube.yaml .
```

## Install CLI tools

You need to have access to TrustGraph client tools. In the terminal
window you created above, install a virtual environment, and the
TrustGraph CLI tools. Make sure the version number of the CLI tools
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

<details>
<summary>Specific guidance for Azure</summary>
<div markdown="1">
There are 2 hosted model options for Azure:

- Machine Learning Services (MLS)
- Cognitive Services (CS)

TrustGraph's *Azure* is for integration with MLS. *Azure OpenAI* is for
integration with CS. If you are using the *Azure* / MLS integration, you
should make sure you know your model endpoint, and the token granted for the
endpoint, and configure these values thus:
```
export AZURE_ENDPOINT=https://ENDPOINT.API.HOST.GOES.HERE/
export AZURE_TOKEN=TOKEN-GOES-HERE
```
If you are using the *Azure OpenAI* / CS integration, you should make sure
you know your model endpoint, the token and configure them thus:
```
export AZURE_ENDPOINT=https://ENDPOINT.API.HOST.GOES.HERE/
export AZURE_TOKEN=TOKEN-GOES-HERE
```
</div>
</details>

<details>
<summary>Specific guidance for AWS Bedrock</summary>
<div markdown="1">
To use Bedrock, you need to have AWS credentials provisioned.
The easiest way is to create an IAM user, and create credentials for this
user. When you provision the user, you will be asked to give the user
permissions. To allow Bedrock access, the `AmazonBedrockFullAccess`
role should be added.

You would then provision credentials which would give you an *access key ID*
and a *secret access key*. You should pick the identifier of an
AWS region to connect to e.g. `eu-west-2`. In order to prepare to deploy,
you should set three environment variables using the information.

```
export AWS_ACCESS_KEY_ID=ID-KEY-HERE
export AWS_SECRET_ACCESS_KEY=TOKEN-GOES-HERE
export AWS_DEFAULT_REGION=AWS-REGION-HERE
```

Note: You should be very careful with AWS cloud credentials provisioned
this way: if lost or leaked this provides a malicious person access to the
AWS resources you gave this user.
</div>
</details>

<details>
<summary>Specific guidance for Anthropic Claude</summary>
<div markdown="1">
To use Anthropic's Claude models directly, sign up for API access at
[console.anthropic.com](https://console.anthropic.com/). Create an API key
from the dashboard. Set the key as an environment variable:

```
export CLAUDE_KEY=sk-ant-api03-xxxxx
```
</div>
</details>

<details>
<summary>Specific guidance for Cohere</summary>
<div markdown="1">
To use Cohere's models, sign up at [cohere.com](https://cohere.com/) and
create an API key from your dashboard. Set the key as an environment variable:

```
export COHERE_KEY=your-cohere-api-key-here
```
</div>
</details>

<details>
<summary>Specific guidance for Google AI Studio</summary>
<div markdown="1">
To use Google's Gemini models via AI Studio, visit
[aistudio.google.com](https://aistudio.google.com/) and generate an API key.
Set the key as an environment variable:

```
export GOOGLE_AI_STUDIO_KEY=your-api-key-here
```
</div>
</details>

<details>
<summary>Specific guidance for Llamafile / llama.cpp server</summary>
<div markdown="1">
If running a llamafile or llama.cpp server locally, configure the URL to point
to your server. The URL must include the `/v1` path:

```
export LLAMAFILE_URL=http://your-server-host:port/v1
```

If running on the same host as your Minikube cluster, use `host.minikube.internal`
as the hostname (e.g., `http://host.minikube.internal:7000/v1`).
</div>
</details>

<details>
<summary>Specific guidance for LMStudio</summary>
<div markdown="1">
If running LMStudio locally, configure the URL to point to your LMStudio server.
LMStudio typically runs on port 1234:

```
export LMSTUDIO_URL=http://your-server-host:1234
```

If running on the same host as your Minikube cluster, use `host.minikube.internal`
as the hostname (e.g., `http://host.minikube.internal:1234`).
</div>
</details>

<details>
<summary>Specific guidance for Mistral AI</summary>
<div markdown="1">
To use Mistral's API, sign up at [console.mistral.ai](https://console.mistral.ai/)
and create an API key. Set the key as an environment variable:

```
export MISTRAL_TOKEN=your-mistral-api-key-here
```
</div>
</details>

<details>
<summary>Specific guidance for Ollama</summary>
<div markdown="1">
If running Ollama locally, configure the URL to point to your Ollama server.
Ollama typically runs on port 11434:

```
export OLLAMA_HOST=http://your-server-host:11434
```

If running on the same host as your Minikube cluster, use `host.minikube.internal`
as the hostname (e.g., `http://host.minikube.internal:11434`).
</div>
</details>

<details>
<summary>Specific guidance for OpenAI</summary>
<div markdown="1">
To use OpenAI's API, sign up at [platform.openai.com](https://platform.openai.com/)
and create an API key. Set the key as an environment variable:

```
export OPENAI_TOKEN=your-openai-api-key-here
```

Many other services provide OpenAI-compatible APIs. You can use these by setting
the `OPENAI_BASE_URL` environment variable to point to the alternative service:

```
export OPENAI_BASE_URL=http://your-server-host:8000/v1
```
</div>
</details>

<details>
<summary>Specific guidance for Google Cloud VertexAI</summary>
<div markdown="1">
To use Google Cloud VertexAI, you need to create a service account with
appropriate permissions and download its credentials file.

1. In Google Cloud Console, create a service account
2. Grant the service account permissions to invoke VertexAI models (e.g.,
   `Vertex AI User` role - use minimal permissions, not admin roles)
3. Create and download a JSON key file for the service account
4. Save the key file as `vertexai/private.json` in your deployment directory

{: .warning }
**Important**: Service account credentials provide access to your Google Cloud
resources. Never commit `private.json` to version control. Use minimal
permissions - grant only what's needed for VertexAI model invocation, not
administrator roles.

You will need to create a Kubernetes secret with this credentials file:

```sh
kubectl -n trustgraph create secret generic vertexai-credentials \
    --from-file=private.json=vertexai/private.json
```
</div>
</details>

<details>
<summary>Specific guidance for vLLM</summary>
<div markdown="1">
If running vLLM locally, configure the URL to point to your vLLM server.
The URL should include the `/v1` path:

```
export VLLM_URL=http://your-server-host:port/v1
```

If running on the same host as your Minikube cluster, use `host.minikube.internal`
as the hostname (e.g., `http://host.minikube.internal:8000/v1`).
</div>
</details>

## Configure security settings

For this local deployment, set the following security variables to empty strings
to disable authentication:

```sh
export MCP_SERVER_SECRET=""
export GATEWAY_SECRET=""
```

The `MCP_SERVER_SECRET` protects the MCP server with a secret but is not fully
implemented yet. The `GATEWAY_SECRET` provides single-secret protection for the
gateway API, which does not currently support comprehensive API security. For a
local non-networked deployment, it is safe to disable authentication by setting
these to empty strings.

## Start Minikube

Minikube needs to be started with enough resources. As mentioned earlier,
this is roughly 9 CPUs and 11GB of memory.

```bash
minikube start --cpus=9 --memory=11264
```

### Verify Minikube

```bash
kubectl cluster-info
kubectl get nodes
```

You should see output indicating your cluster is running and the node is ready.

## Deploy TrustGraph

Now you're ready to deploy TrustGraph to your Minikube cluster.

### Apply Kubernetes configuration

```bash
kubectl apply -f trustgraph-minikube.yaml
```

This creates all the necessary Kubernetes resources (deployments, services, configmaps, etc.) for TrustGraph.

### Create secrets

You need to create some Kubernetes secrets for authentication. Based on your LLM
configuration settings above, create the appropriate secrets:

**Required for all deployments:**
```bash
kubectl -n trustgraph create secret generic gateway-secret \
    --from-literal=gateway-secret="${GATEWAY_SECRET}"

kubectl -n trustgraph create secret generic mcp-server-secret \
    --from-literal="mcp-server-secret=${MCP_SERVER_SECRET}"
```

**For specific LLM providers, create the appropriate secret:**

<details>
<summary>Azure</summary>
<div markdown="1">
```bash
kubectl -n trustgraph create secret generic azure-credentials \
    --from-literal="azure-endpoint=${AZURE_ENDPOINT}" \
    --from-literal="azure-token=${AZURE_TOKEN}"
```
</div>
</details>

<details>
<summary>AWS Bedrock</summary>
<div markdown="1">
```bash
kubectl -n trustgraph create secret generic bedrock-credentials \
    --from-literal="aws-access-key-id=${AWS_ACCESS_KEY_ID}" \
    --from-literal="aws-secret-access-key=${AWS_SECRET_ACCESS_KEY}" \
    --from-literal="aws-region=${AWS_DEFAULT_REGION}"
```
</div>
</details>

<details>
<summary>Anthropic Claude</summary>
<div markdown="1">
```bash
kubectl -n trustgraph create secret generic claude-credentials \
    --from-literal="claude-key=${CLAUDE_KEY}"
```
</div>
</details>

<details>
<summary>Cohere</summary>
<div markdown="1">
```bash
kubectl -n trustgraph create secret generic cohere-credentials \
    --from-literal="cohere-key=${COHERE_KEY}"
```
</div>
</details>

<details>
<summary>Google AI Studio</summary>
<div markdown="1">
```bash
kubectl -n trustgraph create secret generic google-ai-studio-credentials \
    --from-literal="google-ai-studio-key=${GOOGLE_AI_STUDIO_KEY}"
```
</div>
</details>

<details>
<summary>Llamafile</summary>
<div markdown="1">
```bash
kubectl -n trustgraph create secret generic llamafile-credentials \
    --from-literal="llamafile-url=${LLAMAFILE_URL}"
```
</div>
</details>

<details>
<summary>LMStudio</summary>
<div markdown="1">
```bash
kubectl -n trustgraph create secret generic lmstudio-credentials \
    --from-literal="lmstudio-url=${LMSTUDIO_URL}"
```
</div>
</details>

<details>
<summary>Mistral AI</summary>
<div markdown="1">
```bash
kubectl -n trustgraph create secret generic mistral-credentials \
    --from-literal="mistral-token=${MISTRAL_TOKEN}"
```
</div>
</details>

<details>
<summary>Ollama</summary>
<div markdown="1">
```bash
kubectl -n trustgraph create secret generic ollama-credentials \
    --from-literal="ollama-host=${OLLAMA_HOST}"
```
</div>
</details>

<details>
<summary>OpenAI</summary>
<div markdown="1">
```bash
kubectl -n trustgraph create secret generic openai-credentials \
    --from-literal="openai-token=${OPENAI_TOKEN}"
```

If using an alternative OpenAI-compatible API:
```bash
kubectl -n trustgraph create secret generic openai-credentials \
    --from-literal="openai-token=${OPENAI_TOKEN}" \
    --from-literal="openai-base-url=${OPENAI_BASE_URL}"
```
</div>
</details>

<details>
<summary>Google Cloud VertexAI</summary>
<div markdown="1">
As mentioned in the LLM configuration section, you should have already created this secret:
```bash
kubectl -n trustgraph create secret generic vertexai-credentials \
    --from-file=private.json=vertexai/private.json
```
</div>
</details>

<details>
<summary>vLLM</summary>
<div markdown="1">
```bash
kubectl -n trustgraph create secret generic vllm-credentials \
    --from-literal="vllm-url=${VLLM_URL}"
```
</div>
</details>

### Launch LoadBalancer

**In a separate terminal window:**

```bash
minikube tunnel
```

{: .warning }
**Important**: Keep this terminal window open. The LoadBalancer must remain running for cluster communications.

### Verify startup

It can take around 40 - 120 seconds for all services to stabilize. Services
like Pulsar and Cassandra need time to initialize properly.
There is a utility which runs a series of checks to verify the system
as it starts and reports when the system is working successfully.

```sh
tg-verify-system-status
```

If everything is working, the output looks something like this:

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

The *Checks failed* line is the most interesting and is hopefully zero. If
you are having issues, look at the troubleshooting section later.

If everything appears to be working, the following parts of the deployment
guide are a whistle-stop tour through various parts of the system.

## Load sample documents

There is a utility which loads a small set of sample documents into the
library. This does not initiate processing, but gives you a set of documents
to test with:

```sh
tg-load-sample-documents
```

This downloads documents from the internet and caches them in a local
directory, so that the load is quicker if you need to do it again.
The download can take a little time to run.

## Workbench

TrustGraph is bundled with a simple web interface which exercises most of
the functionality.

{: .note }
<!-- FIXME: Need to verify the correct way to access workbench in Minikube - is it through a service with LoadBalancer, port-forward, or minikube service command? -->
**FIXME**: Instructions needed for accessing the Workbench UI in Minikube. This may require port-forwarding or using `minikube service` command.

Access the TrustGraph workbench at the appropriate URL (see FIXME above).

By default, there are no credentials.

You should be able to navigate to the Flows tab, and see a single
*default* flow running. The guide will return to the workbench to load
a document.

## Monitoring dashboard

{: .note }
<!-- FIXME: Need to verify if Grafana is deployed in the Minikube configuration and how to access it -->
**FIXME**: Instructions needed for accessing Grafana monitoring in Minikube. Verify if Grafana is included in the Kubernetes deployment and provide access instructions.

If Grafana is deployed, access it at the appropriate URL.

**Default credentials:**
- Username: `admin`
- Password: `admin`

All TrustGraph components collect metrics using Prometheus and make these
available using this Grafana workbench. The Grafana deployment is
configured with 2 dashboards, the first is an Overview metrics dashboard
which shows processing metrics. For a newly launched system, the metrics
won't be particularly interesting.

There is also a Logs dashboard which shows collated TrustGraph container
logs.

## Check the LLM is working

Back in the workbench, select the *Assistant* tab.

In the top line next to the *Assistant* word change the mode to *Basic LLM*.

Enter a question in the prompt box at the bottom of the tab and press
*Send*. If everything works, after a short period you should see
a response to your query.

![Simple LLM usage](llm-interaction.png)

If LLM interactions are not working, this needs to be diagnosed and fixed
prior to continuing. You should check the logs to see if there are errors:

```bash
# Check logs for text-completion service
kubectl -n trustgraph logs -l app=text-completion

# Or use Grafana logs dashboard if available
```

## Working with a document

### Load a document

Back in the workbench:

1. Navigate to the Library page
2. In the upper right-hand corner, there is a dark/light mode widget.
   To its left, is a selector widget. Ensure the top and bottom lines say
   "default". If not click on the widget and change.
2. On the library tab, select a document (e.g., "Beyond State Vigilance")
3. Click Submit on the action bar
4. Choose a processing flow (use Default processing flow)
5. Click Submit to process

Beyond State Vigilance is a relatively short document, so a good one to
start with.

### Use Vector search

Select the *Vector Search* tab. Enter a string e.g. "document" in the search
bar, and hit RETURN. The search term doesn't matter a great deal. If
information has started to load, you should see some search results.

The vector search attempts to find up to 10 terms which are the closest
matches for your search term. It does this even if the search terms are not
a strong match, so this is a simple way to observe whether data has loaded.

![Vector search results](vector-search.png)

### Look at knowledge graph

Click on one of the Vector Search results terms on the left-hand-side.
This shows relationships in the graph from the knowledge graph linking to
that term.

![Relationships view](relationships.png)

You can then click on the *Graph view* button to go to a 3D view of the
discovered relationships.

### Query with Graph RAG

1. Navigate to *Assistant* tab
2. Change the Assistant mode to GraphRAG
3. Enter your question (e.g., "What is this document about?")
4. You will see the answer to your question after a short period

You can also test GraphRAG from the command line:

```bash
tg-invoke-graph-rag -q "What is this document about?"
```

## Troubleshooting

### Service Failure

<details>
<summary>Run out of memory</summary>
<div markdown="1">

*Diagnosis:*

Check which pods are running. Init containers (names ending in `-init`)
should show `Completed` - this is normal. Other pods should be running.

```bash
# Show all pods
kubectl -n trustgraph get pods

# Find OOM-killed pods (look for OOMKilled status)
kubectl -n trustgraph get pods | grep -i oom

# Inspect a failed pod for details
kubectl -n trustgraph describe pod <pod-name> | grep -A 5 "OOMKilled\|Error"
```

Look for `"OOMKilled": true` or error messages in the describe output.

*Resolution:*

- Increase memory allocation when starting Minikube:
  ```bash
  minikube stop
  minikube start --cpus=9 --memory=16384
  ```
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
# Check node resources
kubectl -n trustgraph top nodes

# Check pod resource usage
kubectl -n trustgraph top pods
```

If CPU usage remains very high for an extended period during startup
and operations, this indicates insufficient CPU resources.

*Resolution:*

Increase CPU allocation when starting Minikube:
```bash
minikube stop
minikube start --cpus=12 --memory=11264
```

TrustGraph requires 9 CPUs minimum, but more cores will improve
performance significantly.

</div>
</details>

<details>
<summary>Image Pull Issues</summary>
<div markdown="1">

*Diagnosis:*

Check for pods in ImagePullBackOff or ErrImagePull status:

```bash
# Check pod status
kubectl -n trustgraph get pods

# View pod events for image pull errors
kubectl -n trustgraph get events | grep -i "pull\|image"

# Describe a specific pod
kubectl -n trustgraph describe pod <pod-name>
```

Look for errors mentioning image pull failures, authentication issues, or network problems.

*Resolution:*

- **Network connectivity**: Ensure Minikube has internet access
- **Image registry access**: Verify you can reach the container registry
- **Authentication**: If using a private registry, ensure credentials are configured
- **Retry**: Sometimes transient network issues resolve themselves:
  ```bash
  kubectl -n trustgraph delete pod <pod-name>
  # Kubernetes will recreate the pod
  ```

</div>
</details>

<details>
<summary>LoadBalancer Not Starting</summary>
<div markdown="1">

*Diagnosis:*

The `minikube tunnel` command fails or services remain in Pending state:

```bash
# Check service status
kubectl -n trustgraph get services

# Check Minikube status
minikube status
```

Look for services with EXTERNAL-IP showing `<pending>`.

*Resolution:*

- Ensure `minikube tunnel` is running in a separate terminal window
- The tunnel command requires sudo/administrator privileges
- Check Minikube driver is working: `minikube config view`
- Restart the tunnel:
  ```bash
  # Stop existing tunnel (Ctrl+C)
  minikube tunnel
  ```

</div>
</details>

<details>
<summary>Application error</summary>
<div markdown="1">

*Diagnosis:*

Find failed pods and examine their logs:

```bash
# Show all pods with status
kubectl -n trustgraph get pods

# View logs for a specific pod
kubectl -n trustgraph logs <pod-name>

# Follow logs in real-time
kubectl -n trustgraph logs -f <pod-name>

# View logs for a specific container in a multi-container pod
kubectl -n trustgraph logs <pod-name> -c <container-name>
```

Alternatively, view aggregated logs in the Grafana dashboard if available.

*Resolution:*

Resolution depends on the specific error message. Common issues include
configuration errors, missing environment variables, missing secrets, or
service dependencies not being ready.

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

A long timeout or error indicates LLM configuration issues. Check the logs:

```bash
# Check text-completion service logs
kubectl -n trustgraph logs -l app=text-completion
```

Look for errors indicating LLM connection failures.

*Resolution:*

Review the LLM configuration settings in the [Configure LLM settings](#configure-llm-settings)
section. Common issues include:
- Missing or incorrect API keys
- Wrong endpoint URLs
- Missing `/v1` suffix for self-hosted models
- Incorrect `host.minikube.internal` hostname for local services
- Secrets not created properly in Kubernetes

Verify your secrets are created:
```bash
kubectl -n trustgraph get secrets
```

</div>
</details>

<details>
<summary>Locally-hosted LLM connectivity error</summary>
<div markdown="1">

*Diagnosis:*

Check the logs for connectivity errors:

```bash
kubectl -n trustgraph logs -l app=text-completion
```

Look for errors indicating connection refused, timeouts, or unreachable
hosts when attempting to connect to your LLM service.

*Resolution:*

Review your network connectivity and addressing configuration:

- Verify your LLM service is running and accessible from your host
- Check the URL configuration for your LLM (environment variables)
- For services on the same host, ensure you're using `host.minikube.internal`
  as the hostname
- Verify the correct port number
- Ensure URLs include `/v1` suffix where required
- Test connectivity from within Minikube:
  ```bash
  kubectl run -it --rm debug --image=curlimages/curl --restart=Never -- \
    curl -v http://host.minikube.internal:11434
  ```

See also:
- [WSL networking and self-hosted models](wsl-networking)

</div>
</details>

### Kubernetes-Specific Issues

<details>
<summary>Pods stuck in Pending state</summary>
<div markdown="1">

*Diagnosis:*

```bash
# Check pod status
kubectl -n trustgraph get pods | grep Pending

# Describe a pending pod
kubectl -n trustgraph describe pod <pod-name>
```

Look for scheduling failures, resource constraints, or node conditions.

*Resolution:*

- **Insufficient resources**: Increase Minikube resources (see above)
- **PersistentVolume issues**: Check PV/PVC status:
  ```bash
  kubectl -n trustgraph get pv,pvc
  ```
- **Node issues**: Check node status:
  ```bash
  kubectl describe node minikube
  ```

</div>
</details>

<details>
<summary>Pods in CrashLoopBackOff</summary>
<div markdown="1">

*Diagnosis:*

```bash
# Find crashing pods
kubectl -n trustgraph get pods | grep CrashLoopBackOff

# View logs from crashed container
kubectl -n trustgraph logs <pod-name> --previous
```

*Resolution:*

Check the previous logs to identify why the container is crashing. Common causes:
- Application errors (fix the configuration)
- Missing dependencies (ensure all required services are running)
- Incorrect environment variables or secrets
- Resource limits too low (increase in deployment configuration)

</div>
</details>

### Debug Commands

```bash
# Check cluster info
kubectl cluster-info

# Get all resources in trustgraph namespace
kubectl -n trustgraph get all

# Check node resources
kubectl describe node minikube

# View recent events
kubectl -n trustgraph get events --sort-by=.metadata.creationTimestamp

# Check Minikube logs
minikube logs

# Check specific service endpoints
kubectl -n trustgraph get endpoints
```

## Shutting down

### Clean shutdown

Once you have finished with your system, you can close it down.

```bash
# Remove TrustGraph deployment
kubectl delete -f trustgraph-minikube.yaml

# Stop Minikube
minikube stop

# Optional: Delete Minikube cluster (removes all data)
minikube delete
```

The `minikube delete` command completely removes the Minikube cluster and all
its data. Only use this if you want to start completely fresh.

### Verify cleanup

```bash
# Check no pods remain in trustgraph namespace
kubectl -n trustgraph get all

# Verify Minikube status
minikube status
```

If you deleted the cluster, `minikube status` should indicate no cluster exists.

## Next Steps

- **Guides**: See [Guides](../guides) for things you can do with your running
  TrustGraph
- **Production Kubernetes**: Scale to full Kubernetes clusters
- **Cloud Deployment**: Explore AWS EKS, GCP GKE, or Azure AKS for managed Kubernetes
