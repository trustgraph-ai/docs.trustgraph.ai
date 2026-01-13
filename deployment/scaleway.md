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
<li>Python {{site.data.software.python-min-version}}+ for CLI tools</li>
<li>Basic command-line and Kubernetes familiarity</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
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

{% include deployment/python-requirement.md %}

### Pulumi

{% include deployment/pulumi-install.md %}

### kubectl

{% include deployment/kubectl-install.md %}

### Node.js

{% include deployment/nodejs-install.md %}

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

{% include deployment/pulumi-configure-state.md %}

### Create a Pulumi stack

{% include deployment/pulumi-create-stack.md %}

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

### Configure and verify kubectl access

{% include kubernetes/configure-kubectl-access.md %}

### Check pod status

{% include kubernetes/check-pod-status.md %}

## Access services via port-forwarding

{% include kubernetes/port-forwarding.md %}

## Install CLI tools

{% include deployment/install-cli-tools.md %}

## Startup period

It can take 2-3 minutes for all services to stabilize after deployment. Services like Pulsar and Cassandra need time to initialize properly.

### Verify system health

{% include deployment/application-localhost/verify-system-health.md %}

If everything appears to be working, the following parts of the deployment
guide are a whistle-stop tour through various parts of the system.

## Test LLM access

{% include deployment/application-localhost/test-llm-access.md %}

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
