---
title: Google Cloud Platform
nav_order: 6
parent: Deployment
grand_parent: TrustGraph Documentation
review_date: 2026-02-09
guide_category:
  - Global cloud
guide_category_order: 3
guide_description: Production GKE deployment with VertexAI Gemini integration and comprehensive GCP services
guide_difficulty: intermediate
guide_time: 2 - 4 hr
guide_emoji: ☁️
guide_banner: /../gcp.jpg
guide_labels:
  - GCP
  - Kubernetes
  - Production
---

# Google Cloud Platform Deployment

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>GCP account with billing enabled (see below for setup)</li>
<li>gcloud CLI installed and configured</li>
<li>Pulumi installed locally</li>
<li>kubectl command-line tool</li>
<li>Python 3.11+ for CLI tools</li>
<li>Basic command-line and Kubernetes familiarity</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Deploy a production-ready TrustGraph environment on Google Kubernetes Engine with VertexAI Gemini integration using Infrastructure as Code."
%}

## Overview

This guide walks you through deploying TrustGraph on Google Cloud Platform's Kubernetes Engine (GKE) using Pulumi (Infrastructure as Code). The deployment automatically provisions a production-ready Kubernetes cluster integrated with Google's VertexAI services.

**Pulumi** is an open-source Infrastructure as Code tool that uses general-purpose programming languages (TypeScript/JavaScript in this case) to define cloud infrastructure. Unlike manual deployments, Pulumi provides:
- Reproducible, version-controlled infrastructure
- Testable and retryable deployments
- Automatic resource dependency management
- Simple rollback capabilities

Once deployed, you'll have a complete TrustGraph stack running on GCP infrastructure with:
- Google Kubernetes Engine (GKE) cluster (2-node pool, configurable)
- VertexAI Gemini Flash 1.5 integration
- Complete monitoring with Grafana and Prometheus
- Web workbench for document processing and Graph RAG
- Secure secrets management

{: .note }
> **Why Google Cloud Platform for TrustGraph?**
>
> GCP offers unique advantages for AI-focused organizations:
> - **VertexAI Integration**: Native access to Google's Gemini models for state-of-the-art LLM capabilities
> - **ML/AI Optimization**: Purpose-built infrastructure for machine learning workloads
> - **Global Infrastructure**: Deploy across 40+ regions worldwide with Google's network
> - **Sustainability**: Carbon-neutral operations with renewable energy commitment
> - **Free Tier & Credits**: $300 in free credits for new users to get started
>
> Ideal for organizations requiring cutting-edge AI capabilities and ML/AI-optimized infrastructure.

## Getting ready

### GCP Account

You'll need a GCP account with billing enabled. If you don't have one:

1. Sign up at [https://cloud.google.com/](https://cloud.google.com/)
2. Complete account verification
3. Enable billing for your project
4. New users receive $300 in free credits

### Create a GCP Project

Create a dedicated project for TrustGraph:

1. Navigate to the [GCP Console](https://console.cloud.google.com/)
2. Click on the project dropdown at the top
3. Click **New Project**
4. Enter a project name (e.g., `trustgraph-prod`)
5. Note the **Project ID** - you'll need this later

### Enable Required APIs

Enable the necessary GCP APIs for your project:

```bash
gcloud services enable container.googleapis.com
gcloud services enable compute.googleapis.com
gcloud services enable aiplatform.googleapis.com
gcloud services enable iam.googleapis.com
```

### Install gcloud CLI

Install the Google Cloud CLI:

<details>
<summary>Linux</summary>
<div markdown="1">
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
```
</div>
</details>

<details>
<summary>MacOS</summary>
<div markdown="1">
```bash
brew install --cask google-cloud-sdk
gcloud init
```
</div>
</details>

<details>
<summary>Windows</summary>
<div markdown="1">
Download the installer from [cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)
</div>
</details>

Verify installation:

```bash
gcloud version
```

### Configure gcloud Authentication

Authenticate with your GCP account:

```bash
gcloud auth login
gcloud auth application-default login
```

Set your default project:

```bash
gcloud config set project YOUR_PROJECT_ID
```

### Python

{% include deployment/python-requirement.md %}

### Pulumi

{% include deployment/pulumi-install.md %}

### kubectl

{% include deployment/kubectl-install.md %}

### Node.js

{% include deployment/nodejs-install.md %}

### VertexAI Access

The deployment uses Google's VertexAI with **Gemini Flash 1.5** as the default model. VertexAI is automatically available in GCP projects with billing enabled.

Available Gemini models include:
- `gemini-1.5-flash` (fast, cost-effective)
- `gemini-1.5-pro` (advanced reasoning)
- `gemini-1.0-pro` (production-ready)

## Prepare the deployment

### Get the Pulumi code

Clone the TrustGraph GCP Pulumi repository:

```bash
git clone https://github.com/trustgraph-ai/pulumi-trustgraph-gke.git
cd pulumi-trustgraph-gke/pulumi
```

### Install dependencies

Install the Node.js dependencies for the Pulumi project:

```bash
npm install
```

### Configure GCP Project

Set your GCP project ID for Pulumi:

```bash
pulumi config set gcp:project YOUR_PROJECT_ID
```

### Configure Pulumi state

{% include deployment/pulumi-configure-state.md %}

### Create a Pulumi stack

{% include deployment/pulumi-create-stack.md %}

### Configure the stack

Apply settings for region, zone, and cluster configuration:

```bash
pulumi config set gcp:region us-central1
pulumi config set gcp:zone us-central1-a
pulumi config set clusterName trustgraph-gke
pulumi config set nodeCount 2
```

Available regions include:
- `us-central1` (Iowa, USA)
- `us-east1` (South Carolina, USA)
- `europe-west1` (Belgium)
- `europe-west4` (Netherlands)
- `asia-southeast1` (Singapore)
- `australia-southeast1` (Sydney)

Refer to [GCP Regions](https://cloud.google.com/compute/docs/regions-zones) for a complete list.

### Configure VertexAI

Set the VertexAI model and location:

```bash
pulumi config set vertexaiModel gemini-1.5-flash
pulumi config set vertexaiLocation us-central1
```

Refer to the repository's README for additional configuration options.

## Deploy with Pulumi

### Preview the deployment

Before deploying, preview what Pulumi will create:

```bash
pulumi preview
```

This shows all the resources that will be created:
- GKE Kubernetes cluster
- Node pool with specified machine types
- VPC network and subnets
- Service accounts with VertexAI permissions
- IAM roles and bindings
- Kubernetes secrets for GCP credentials
- TrustGraph deployments, services, and config maps

Review the output to ensure everything looks correct.

### Deploy the infrastructure

Deploy the complete TrustGraph stack:

```bash
pulumi up
```

Pulumi will ask for confirmation before proceeding. Type `yes` to continue.

The deployment typically takes 10 - 15 minutes and progresses through these stages:

1. **Creating GKE cluster** (6-8 minutes)
   - Provisions GKE cluster
   - Creates node pool
   - Configures VPC networking

2. **Configuring service accounts** (1-2 minutes)
   - Creates service account
   - Sets up VertexAI permissions
   - Creates Kubernetes secrets

3. **Deploying TrustGraph** (4-6 minutes)
   - Applies Kubernetes manifests
   - Deploys all TrustGraph services
   - Starts pods and initializes services

You'll see output showing the creation progress of all resources.

### Configure and verify kubectl access

After deployment completes, configure kubectl to access your GKE cluster:

```bash
gcloud container clusters get-credentials trustgraph-gke --zone us-central1-a
```

Verify access:

```bash
kubectl get nodes
```

You should see your GKE nodes listed as `Ready`.

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

If everything appears to be working, the following parts of the deployment guide are a whistle-stop tour through various parts of the system.

## Test LLM access

Test that VertexAI Gemini integration is working by invoking the LLM through the gateway:

```bash
tg-invoke-llm 'Be helpful' 'What is 2 + 2?'
```

You should see output like:

```
2 + 2 = 4
```

This confirms that TrustGraph can successfully communicate with Google's VertexAI service.

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

- **Authentication errors**: Verify `gcloud auth application-default login` was run and your project ID is correct
- **API not enabled**: Ensure all required GCP APIs are enabled (see "Enable Required APIs" section)
- **Quota limits**: Check your GCP project hasn't hit resource quotas (GKE clusters, CPUs, IP addresses)
- **Billing not enabled**: Verify billing is enabled for your GCP project
- **Permissions**: Ensure your account has Owner or Editor role on the project

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

- **Insufficient resources**: Increase node count or machine type in your Pulumi configuration
- **PersistentVolume issues**: Check PV/PVC status with `kubectl -n trustgraph get pv,pvc`
- **Node issues**: Check node status with `kubectl get nodes`
- **Resource quotas**: Verify your GCP project hasn't hit CPU or memory quotas

</div>
</details>

<details>
<summary>VertexAI integration not working</summary>
<div markdown="1">

*Diagnosis:*

Test LLM connectivity:

```bash
tg-invoke-llm '' 'What is 2+2'
```

A timeout or error indicates VertexAI configuration issues. Check the `text-completion` pod logs:

```bash
kubectl -n trustgraph logs -l app=text-completion
```

*Resolution:*

- Verify VertexAI API is enabled: `gcloud services list --enabled | grep aiplatform`
- Check service account has VertexAI permissions: `gcloud projects get-iam-policy YOUR_PROJECT_ID`
- Ensure the Gemini model is available in your selected region
- Review Pulumi outputs to confirm VertexAI configuration: `pulumi stack output`
- Verify billing is enabled (VertexAI requires active billing)

</div>
</details>

<details>
<summary>Port-forwarding connection issues</summary>
<div markdown="1">

*Diagnosis:*

Port-forward commands fail or connections time out.

*Resolution:*

- Verify kubectl is configured: `kubectl config current-context`
- Check that the target service exists: `kubectl -n trustgraph get svc`
- Ensure no other process is using the port (e.g., port 8088, 8888, or 3000)
- Try restarting the port-forward with verbose logging: `kubectl port-forward -v=6 ...`
- Check GKE cluster connectivity: `gcloud container clusters describe trustgraph-gke --zone us-central1-a`

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
- GCP credentials not properly configured

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
- Check GKE cluster health: `gcloud container clusters describe trustgraph-gke --zone us-central1-a`

</div>
</details>

### GCP-Specific Issues

<details>
<summary>GKE cluster creation fails</summary>
<div markdown="1">

*Diagnosis:*

Check GCP quota and permissions:

```bash
gcloud compute project-info describe --project=YOUR_PROJECT_ID
```

*Resolution:*

- Request quota increases if needed via GCP Console
- Verify your account has `roles/container.admin` permission
- Check if the zone has available capacity
- Try a different zone or region

</div>
</details>

<details>
<summary>VertexAI quota exceeded</summary>
<div markdown="1">

*Diagnosis:*

Error messages about VertexAI quota or rate limits.

*Resolution:*

- Check VertexAI quotas in GCP Console under "IAM & Admin" → "Quotas"
- Request quota increases if needed
- Switch to a different Gemini model with higher quotas
- Implement rate limiting in your application

</div>
</details>

## Shutting down

### Clean shutdown

When you're finished with your TrustGraph deployment, clean up all resources:

```bash
pulumi destroy
```

Pulumi will show you all the resources that will be deleted and ask for confirmation. Type `yes` to proceed.

The destruction process typically takes **8-12 minutes** and removes:
- All TrustGraph Kubernetes resources
- The GKE cluster
- Node pools
- Service accounts and IAM bindings
- VPC network resources (if created)
- All associated storage

{: .warning }
> **Cost Warning**: GCP charges for running GKE clusters and node instances. Make sure to destroy your deployment when you're not using it to avoid unnecessary costs. GKE charges include cluster management fees plus compute costs.

### Verify cleanup

After `pulumi destroy` completes, verify all resources are removed:

```bash
# Check Pulumi stack status
pulumi stack

# Verify no resources remain
pulumi stack --show-urns

# Check GCP for remaining resources
gcloud container clusters list
gcloud compute instances list
```

### Delete the Pulumi stack

If you're completely done with this deployment, you can remove the Pulumi stack:

```bash
pulumi stack rm dev
```

This removes the stack's state but doesn't affect any cloud resources (use `pulumi destroy` first).

## Cost Optimization

### Monitor Costs

Keep track of your GCP spending:

1. Navigate to **Billing** in GCP Console
2. View cost breakdown by service
3. Set up budget alerts

### Cost-Saving Tips

- **Preemptible Nodes**: Use preemptible VMs for non-production workloads (60-90% cheaper)
- **Autoscaling**: Configure cluster autoscaling to scale down during idle periods
- **Resource Requests**: Set appropriate CPU/memory requests to avoid over-provisioning
- **Committed Use Discounts**: For long-term deployments, purchase committed use contracts
- **Regional vs Zonal**: Use zonal clusters instead of regional for lower costs (less HA)

Example cost estimates (us-central1):
- **Cluster management fee**: $0.10/hour (~$73/month)
- **2 x n1-standard-2 nodes**: ~$100/month
- **VertexAI API calls**: Pay per use (varies by model and usage)
- **Total estimated**: ~$180-250/month for basic deployment

## Next Steps

Now that you have TrustGraph running on GCP:

- **Guides**: See [Guides](../guides) for things you can do with your running TrustGraph
- **Scale the cluster**: Configure GKE autoscaling or increase node pool size
- **Production hardening**: Set up Cloud Armor, Cloud NAT, and private GKE cluster
- **Integrate GCP services**: Connect to Cloud Storage, BigQuery, or Cloud SQL
- **CI/CD**: Set up Cloud Build for automated deployments
- **Monitoring**: Integrate with Cloud Monitoring and Cloud Logging
- **Multi-region**: Deploy across multiple GCP regions for high availability
- **Advanced VertexAI**: Explore other Gemini models or fine-tuning options

{: .note }
> **Additional Resources**
>
> - [TrustGraph GCP Pulumi Repository](https://github.com/trustgraph-ai/pulumi-trustgraph-gke) - Full source code and configuration
> - [GKE Best Practices](https://cloud.google.com/kubernetes-engine/docs/best-practices) - Google's recommendations
> - [VertexAI Documentation](https://cloud.google.com/vertex-ai/docs) - Learn more about Google's AI platform
> - [GCP Free Tier](https://cloud.google.com/free) - Information about free credits and always-free resources
