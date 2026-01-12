---
title: Scaleway
nav_order: 4
parent: Deployment
grand_parent: TrustGraph Documentation
review_date: 2026-01-06
guide_category:
  - European Cloud Providers
guide_category_order: 2
guide_description: Cost-effective Kubernetes deployment with GDPR compliance and European data residency
guide_difficulty: intermediate
guide_time: 1 - 2 hr
guide_emoji: 🇫🇷
guide_banner: /../scaleway.jpg
guide_labels:
  - Kubernetes
  - Europe
  - Budget-friendly
---

# Scaleway Deployment

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>Scaleway account with API access (see below for setup)</li>
<li>Pulumi installed locally</li>
<li>kubectl command-line tool</li>
<li>Python 3.11+ for CLI tools</li>
<li>Basic command-line and Kubernetes familiarity</li>
</ul>
{% endcapture %}

{% include guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Deploy a production-ready TrustGraph environment on Scaleway Kubernetes with GDPR-compliant European infrastructure using Infrastructure as Code."
%}

## Overview

This guide walks you through deploying TrustGraph on Scaleway's Kubernetes Kapsule service using Pulumi (Infrastructure as Code). The deployment automatically provisions a production-ready Kubernetes cluster integrated with Scaleway's Generative AI services.

**Pulumi** is an open-source Infrastructure as Code tool that uses general-purpose programming languages (TypeScript/JavaScript in this case) to define cloud infrastructure. Unlike manual deployments, Pulumi provides:
- Reproducible, version-controlled infrastructure
- Testable and retryable deployments
- Automatic resource dependency management
- Simple rollback capabilities

Once deployed, you'll have a complete TrustGraph stack running on European infrastructure with:
- Kubernetes Kapsule cluster (2-node pool, configurable)
- Scaleway Generative AI integration (Mistral Nemo Instruct)
- Complete monitoring with Grafana and Prometheus
- Web workbench for document processing and Graph RAG
- Secure secrets management

{: .note }
> **Why Scaleway for TrustGraph?**
>
> Scaleway offers unique advantages for European organizations:
> - **GDPR Compliance & EU Data Residency**: All data remains within European Union boundaries
> - **Cost-Effective**: Transparent, competitive pricing without hidden costs
> - **European AI**: Scaleway Gen AI provides access to models like Mistral with EU processing
> - **Developer-Friendly**: Simple APIs, strong open-source support, sustainable computing
>
> Ideal for organizations requiring strict data localization or GDPR compliance.

## Getting ready

### Scaleway Account

You'll need a Scaleway account with API access. If you don't have one:

1. Sign up at [https://console.scaleway.com/](https://console.scaleway.com/)
2. Complete account verification
3. Note your Organization ID and Project ID from the Scaleway console

To create API credentials:

1. Navigate to **IAM** → **API Keys** in the Scaleway console
2. Click **Generate API Key**
3. Save the **Access Key** and **Secret Key** securely
4. You'll also need your **Organization ID** and **Project ID** (found in Project Settings)

### Python

You need Python 3.11 or later installed for the TrustGraph CLI tools.

<details>
<summary>Check your Python version</summary>

<div markdown="1">
```bash
python3 --version
```

If you need to install or upgrade Python, visit [python.org](https://www.python.org/downloads/).
</div>
</details>

### Pulumi

Install Pulumi on your local machine:

<details>
<summary>Linux</summary>
<div markdown="1">
```bash
curl -fsSL https://get.pulumi.com | sh
```
</div>
</details>

<details>
<summary>MacOS</summary>
<div markdown="1">
```bash
brew install pulumi/tap/pulumi
```
</div>
</details>

<details>
<summary>Windows</summary>
<div markdown="1">
Download the installer from [pulumi.com](https://www.pulumi.com/docs/get-started/install/).
</div>
</details>

Verify installation:

```bash
pulumi version
```

Full installation details are at [pulumi.com](https://www.pulumi.com/docs/get-started/install/).

### kubectl

Install kubectl to manage your Kubernetes cluster:

- **Linux**: [Install kubectl on Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
- **MacOS**: `brew install kubectl`
- **Windows**: [Install kubectl on Windows](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/)

Verify installation:

```bash
kubectl version --client
```

### Node.js

The Pulumi deployment code uses TypeScript/JavaScript, so you'll need Node.js installed:

- **Download**: [nodejs.org](https://nodejs.org/) (LTS version recommended)
- **Linux**: `sudo apt install nodejs npm` (Ubuntu/Debian) or `sudo dnf install nodejs` (Fedora)
- **MacOS**: `brew install node`

Verify installation:

```bash
node --version
npm --version
```

### Scaleway Generative AI

The deployment uses Scaleway's Generative AI service with **Mistral Nemo Instruct** as the default model. The deployment automatically configures this integration, but you should verify Generative AI is available in your Scaleway account and region.

Scaleway Gen AI provides European-based AI processing, which is ideal for GDPR compliance and data residency requirements.

## Prepare the deployment

### Get the Pulumi code

Clone the TrustGraph Scaleway Pulumi repository:

```bash
git clone https://github.com/trustgraph-ai/pulumi-trustgraph-scaleway.git
cd pulumi-trustgraph-scaleway/pulumi
```

### Install dependencies

Install the Node.js dependencies for the Pulumi project:

```bash
npm install
```

### Configure Scaleway credentials

Set the required Scaleway environment variables using the credentials you created earlier:

```bash
export SCW_ACCESS_KEY="your_access_key_here"
export SCW_SECRET_KEY="your_secret_key_here"
export SCW_DEFAULT_ORGANIZATION_ID="your_org_id_here"
export SCW_DEFAULT_PROJECT_ID="your_project_id_here"
```

### Configure Pulumi state

You need to tell Pulumi which state to use. You can store this in an S3
bucket, but for experimentation, you can just use local state:

```sh
pulumi login --local
```

FIXME: Set PULUMI_CONFIG_PASSPHRASE
```sh
export PULUMI_CONFIG_PASSPHRASE=
```

### Create a Pulumi stack

Initialize a new Pulumi stack for your deployment:

```bash
pulumi stack init dev
```

You can use any name instead of `dev` - this helps you manage multiple deployments (dev, staging, prod, etc.).

### Configure the stack

Apply settings for region, and environment name.  The environment
name is used to construct resource names, so is important if you deploy
multiple stacks:

```sh
pulumi config set region fr-par
pulumi config set environment prod
```

At the time of writing available regions are:
- `fr-par` (Paris)
- `nl-ams` (Amsterdam)
- `pl-waw` (Warsaw)

Refer to the repository's README for more details.

## Deploy with Pulumi

### Preview the deployment

Before deploying, preview what Pulumi will create:

```bash
pulumi preview
```

This shows all the resources that will be created:
- Kubernetes Kapsule cluster
- Node pool with specified instance types
- IAM application with Gen AI permissions
- Kubernetes secrets for API keys and configuration
- TrustGraph deployments, services, and config maps

Review the output to ensure everything looks correct.

### Deploy the infrastructure

Deploy the complete TrustGraph stack:

```bash
pulumi up
```

Pulumi will ask for confirmation before proceeding. Type `yes` to continue.

The deployment typically takes 8 - 12 minutes and progresses through these
stages:

1. **Creating Kubernetes cluster** (5-7 minutes)
   - Provisions Kapsule cluster
   - Creates node pool
   - Configures networking

2. **Configuring IAM and secrets** (1-2 minutes)
   - Creates IAM application
   - Sets up API key access
   - Creates Kubernetes secrets

3. **Deploying TrustGraph** (4-6 minutes)
   - Applies Kubernetes manifests
   - Deploys all TrustGraph services
   - Starts pods and initializes services

You'll see output like:

```
Updating (dev)
     Type                                Name                     Status
 +   pulumi:pulumi:Stack                 trustgraph-scaleway-dev  created
 +   ├─ pulumi:providers:scaleway        scaleway-provider        created
 +   ├─ scaleway:network:PrivateNetwork  private-network          created
 +   ├─ scaleway:kubernetes:Cluster      cluster                  created
 +   ├─ scaleway:kubernetes:Pool         node-pool                created
 +   ├─ scaleway:iam:ApiKey              api-key                  created
 +   ├─ kubernetes:yaml/v2:ConfigGroup   resources                created
 +   ├─ pulumi:providers:kubernetes      k8sProvider              created
 +   ├─ scaleway:iam:Application         application              created
 +   ├─ kubernetes:core/v1:Secret        mcp-server-secret        created
 +   ├─ kubernetes:core/v1:Secret        gateway-secret           created
 +   ├─ kubernetes:core/v1:Secret        ai-secret                created
 +   └─ scaleway:iam:Policy              policy                   created

Resources:
    + 13 created

Duration: 8m32s
```

### Configure kubectl access

After deployment completes, a configuration file permitting access to the
Kubernetes cluster is written to kube.cfg.  This file should be treated as
a secret as it contains access keys for the Kubernetes cluster.

Check you can access the cluster:

```sh
export KUBECONFIG=$(pwd)/kube.cfg

# Verify access
kubectl get nodes
```

You should see your Scaleway Kapsule nodes listed as `Ready`.

### Check pod status

Verify that all pods are running:

```bash
kubectl -n trustgraph get pods
```

You should see output similar to this (pod names will have different random suffixes):

```
NAME                                        READY   STATUS      RESTARTS   AGE
agent-manager-74fbb8b64-nzlwb               1/1     Running     0          5m
api-gateway-b6848c6bb-nqtdm                 1/1     Running     0          5m
cassandra-6765fff974-pbh65                  1/1     Running     0          5m
pulsar-d85499879-x92qv                      1/1     Running     0          5m
text-completion-58ccf95586-6gkff            1/1     Running     0          5m
workbench-ui-5fc6d59899-8rczf               1/1     Running     0          5m
...
```

All pods should show `Running` status. Some init pods (names ending in `-init`) may fail or be shown `Completed` status - this is normal, their job is
to initialise cluster resources and then exit.

## Access services via port-forwarding

Since the Kubernetes cluster is running on Scaleway, you'll need to set up port-forwarding to access TrustGraph services from your local machine.

**Open three separate terminal windows** and run these commands (keep them running):

**Terminal 1 - API Gateway:**

```bash
export KUBECONFIG=$(pwd)/kubeconfig.yaml
kubectl -n trustgraph port-forward svc/api-gateway 8088:8088
```

**Terminal 2 - Workbench UI:**

```bash
export KUBECONFIG=$(pwd)/kubeconfig.yaml
kubectl -n trustgraph port-forward svc/workbench-ui 8888:8888
```

**Terminal 3 - Grafana:**

```bash
export KUBECONFIG=$(pwd)/kubeconfig.yaml
kubectl -n trustgraph port-forward svc/grafana 3000:3000
```

With these port-forwards running, you can access:

- **TrustGraph API**: [http://localhost:8088](http://localhost:8088)
- **Web Workbench**: [http://localhost:8888](http://localhost:8888)
- **Grafana Monitoring**: [http://localhost:3000](http://localhost:3000)

{: .note }
Keep these terminal windows open while you're working with TrustGraph. If you close them, you'll lose access to the services.

## Install CLI tools

Now install the TrustGraph command-line tools. These tools help you
interact with TrustGraph, load documents, and verify the system.

Create a Python virtual environment and install the CLI:

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install trustgraph-cli
```

## Verify startup

It can take 2-3 minutes for all services to stabilize after deployment. Services like Pulsar and Cassandra need time to initialize properly.

### Verify system health

Use the TrustGraph verification tool to check system health. First, set up port-forwarding to access the API gateway (see next section), then run:

```bash
# After setting up port-forwarding (see below)
tg-verify-system-status \
  --api-url http://localhost:8088 \
  --pulsar-url http://localhost:8080 \
  --ui-url http://localhost:8888
```

A healthy system will show:

```
============================================================
TrustGraph System Status Verification
============================================================

Phase 1: Infrastructure
------------------------------------------------------------
[00:00] ✓ Pulsar: Pulsar healthy
[00:00] ✓ API Gateway: API Gateway is responding

Phase 2: Core Services
------------------------------------------------------------
[00:00] ✓ Processors: Found 34 processors
[00:00] ✓ Flow Classes: Found 9 flow class(es)
[00:00] ✓ Flows: Flow manager responding (1 flow(s))
[00:00] ✓ Prompts: Found 16 prompt(s)

Phase 3: Data Services
------------------------------------------------------------
[00:00] ✓ Library: Library responding (0 document(s))

Phase 4: User Interface
------------------------------------------------------------
[00:00] ✓ Workbench UI: Workbench UI is responding

============================================================
Summary
============================================================
Checks passed: 8/8
Checks failed: 0/8

✓ System is healthy!
```

## Test LLM access

Test that Scaleway Gen AI integration is working by invoking the LLM through the gateway:

```bash
tg-invoke-llm 'Be helpful' 'What is 2 + 2?'
```

You should see output like:

```
2 + 2 = 4
```

This confirms that TrustGraph can successfully communicate with Scaleway's Generative AI service.

## Load sample documents

Load a small set of sample documents into the library for testing:

```bash
tg-load-sample-documents
```

This downloads documents from the internet and caches them locally. The download can take a little time to run.

## Workbench

TrustGraph includes a web interface for document processing and Graph RAG.

Access the TrustGraph workbench at [http://localhost:8888](http://localhost:8888) (requires port-forwarding to be running).

By default, there are no credentials.

You should be able to navigate to the Flows tab and see a single *default* flow running. The guide will return to the workbench to load a document.

## Monitoring dashboard

Access Grafana monitoring at [http://localhost:3000](http://localhost:3000) (requires port-forwarding to be running).

**Default credentials:**
- Username: `admin`
- Password: `admin`

All TrustGraph components collect metrics using Prometheus and make these available using this Grafana workbench. The Grafana deployment is configured with 2 dashboards:
- **Overview metrics dashboard**: Shows processing metrics
- **Logs dashboard**: Shows collated TrustGraph container logs

For a newly launched system, the metrics won't be particularly interesting yet.

## Check the LLM is working

Back in the workbench, select the *Assistant* tab.

In the top line next to the *Assistant* word, change the mode to *Basic LLM*.

Enter a question in the prompt box at the bottom of the tab and press *Send*. If everything works, after a short period you should see a response to your query.

![Simple LLM usage](llm-interaction.png)

If LLM interactions are not working, check the Grafana logs dashboard for errors in the `text-completion` service.

## Working with a document

### Load a document

Back in the workbench:

1. Navigate to the Library page
2. In the upper right-hand corner, there is a dark/light mode widget. To its left is a selector widget. Ensure the top and bottom lines say "default". If not, click on the widget and change.
3. On the library tab, select a document (e.g., "Beyond State Vigilance")
4. Click Submit on the action bar
5. Choose a processing flow (use Default processing flow)
6. Click Submit to process

Beyond State Vigilance is a relatively short document, so it's a good one to start with.

### Use Vector search

Select the *Vector Search* tab. Enter a string (e.g., "document") in the search bar and hit RETURN. The search term doesn't matter a great deal. If information has started to load, you should see some search results.

The vector search attempts to find up to 10 terms which are the closest matches for your search term. It does this even if the search terms are not a strong match, so this is a simple way to observe whether data has loaded.

![Vector search results](vector-search.png)

### Look at knowledge graph

Click on one of the Vector Search result terms on the left-hand side. This shows relationships in the graph from the knowledge graph linking to that term.

![Relationships view](relationships.png)

You can then click on the *Graph view* button to go to a 3D view of the discovered relationships.

### Query with Graph RAG

1. Navigate to *Assistant* tab
2. Change the Assistant mode to GraphRAG
3. Enter your question (e.g., "What is this document about?")
4. You will see the answer to your question after a short period

## Troubleshooting

### Deployment Issues

<details>
<summary>Pulumi deployment fails</summary>
<div markdown="1">

*Diagnosis:*

Check the Pulumi error output for specific failure messages. Common issues include:

```bash
# View detailed error information
pulumi stack --show-urns
pulumi logs
```

*Resolution:*

- **Authentication errors**: Verify your Scaleway credentials are set correctly (`SCW_ACCESS_KEY`, `SCW_SECRET_KEY`, etc.)
- **Quota limits**: Check your Scaleway account hasn't hit resource quotas (Kapsule clusters, nodes, etc.)
- **Region availability**: Ensure Kubernetes Kapsule is available in your selected region
- **Permissions**: Verify your Scaleway API key has permissions to create Kubernetes clusters and IAM resources

</div>
</details>

<details>
<summary>Pods stuck in Pending state</summary>
<div markdown="1">

*Diagnosis:*

```bash
kubectl -n trustgraph get pods | grep Pending
kubectl -n trustgraph describe pod <pod-name>
```

Look for scheduling failures or resource constraints in the describe output.

*Resolution:*

- **Insufficient resources**: Increase node count or node type in your Pulumi configuration
- **PersistentVolume issues**: Check PV/PVC status with `kubectl -n trustgraph get pv,pvc`
- **Node issues**: Check node status with `kubectl get nodes`

</div>
</details>

<details>
<summary>Scaleway Gen AI integration not working</summary>
<div markdown="1">

*Diagnosis:*

Test LLM connectivity:

```bash
tg-invoke-llm '' 'What is 2+2'
```

A timeout or error indicates Gen AI configuration issues. Check the `text-completion` pod logs:

```bash
kubectl -n trustgraph logs -l app=text-completion
```

*Resolution:*

- Verify Scaleway Gen AI is available in your region and project
- Check that IAM application has Generative AI permissions
- Ensure the Gen AI API key secret was created correctly by Pulumi
- Review Pulumi outputs to confirm Gen AI configuration: `pulumi stack output`

</div>
</details>

<details>
<summary>Port-forwarding connection issues</summary>
<div markdown="1">

*Diagnosis:*

Port-forward commands fail or connections time out.

*Resolution:*

- Verify `KUBECONFIG` environment variable is set correctly
- Check that the target service exists: `kubectl -n trustgraph get svc`
- Ensure no other process is using the port (e.g., port 8088, 8888, or 3000)
- Try restarting the port-forward with verbose logging: `kubectl port-forward -v=6 ...`

</div>
</details>

### Service Failure

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

Check the logs to identify why the container is crashing. Common causes:
- Application errors (configuration issues)
- Missing dependencies (ensure all required services are running)
- Incorrect secrets or environment variables
- Resource limits too low

</div>
</details>

<details>
<summary>Service not responding</summary>
<div markdown="1">

*Diagnosis:*

Check service and pod status:

```bash
kubectl -n trustgraph get svc
kubectl -n trustgraph get pods
kubectl -n trustgraph logs <pod-name>
```

*Resolution:*

- Verify the pod is running and ready
- Check pod logs for errors
- Ensure port-forwarding is active for the service
- Use `tg-verify-system-status` to check overall system health

</div>
</details>

## Shutting down

### Clean shutdown

When you're finished with your TrustGraph deployment, clean up all resources:

```bash
pulumi destroy
```

Pulumi will show you all the resources that will be deleted and ask for confirmation. Type `yes` to proceed.

The destruction process typically takes **5-10 minutes** and removes:
- All TrustGraph Kubernetes resources
- The Kubernetes Kapsule cluster
- Node pools
- IAM applications and API keys
- All associated networking and storage

{: .warning }
> **Cost Warning**: Scaleway charges for running Kubernetes clusters and nodes. Make sure to destroy your deployment when you're not using it to avoid unnecessary costs.

### Verify cleanup

After `pulumi destroy` completes, verify all resources are removed:

```bash
# Check Pulumi stack status
pulumi stack

# Verify no resources remain
pulumi stack --show-urns
```

You can also check the Scaleway console to ensure the Kapsule cluster and associated resources are deleted.

### Delete the Pulumi stack

If you're completely done with this deployment, you can remove the Pulumi stack:

```bash
pulumi stack rm dev
```

This removes the stack's state but doesn't affect any cloud resources (use `pulumi destroy` first).

## Next Steps

Now that you have TrustGraph running on Scaleway:

- **Guides**: See [Guides](../guides) for things you can do with your running TrustGraph
- **Scale the cluster**: Modify your Pulumi configuration to add more nodes or change node types
- **Integrate with Scaleway services**: Connect to Scaleway Object Storage, databases, or other services
- **GDPR compliance**: Ensure your document processing workflows meet data protection requirements
- **Production hardening**: Review the [GitHub repository](https://github.com/trustgraph-ai/pulumi-trustgraph-scaleway) for advanced configuration options

{: .note }
> **Additional Resources**
>
> For Pulumi-specific configuration details, customization options, and contributing to the deployment code, visit the [TrustGraph Scaleway Pulumi Repository](https://github.com/trustgraph-ai/pulumi-trustgraph-scaleway)
