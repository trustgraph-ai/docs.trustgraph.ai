---
title: OVHcloud
nav_order: 4.5
parent: Deployment
grand_parent: TrustGraph Documentation
review_date: 2026-02-02
guide_category:
  - European Cloud Providers
guide_category_order: 1
guide_description: Deploy on OVHcloud Managed Kubernetes with European data sovereignty and AI Endpoints
guide_difficulty: intermediate
guide_time: 1 - 3 hr
guide_emoji: 🇪🇺
guide_banner: ovhcloud.png
guide_labels:
  - Kubernetes
  - Europe
  - Cloud
---

# OVHcloud Deployment

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>OVHcloud account with API access (see below for setup)</li>
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
   goal="Deploy a production-ready TrustGraph environment on OVHcloud Managed Kubernetes with European data sovereignty using Infrastructure as Code."
%}

## Overview

This guide walks you through deploying TrustGraph on OVHcloud's Managed Kubernetes Service (MKS) using Pulumi (Infrastructure as Code). The deployment automatically provisions a production-ready Kubernetes cluster integrated with OVHcloud's AI Endpoints.

**Pulumi** is an open-source Infrastructure as Code tool that uses general-purpose programming languages (TypeScript/JavaScript in this case) to define cloud infrastructure. Unlike manual deployments, Pulumi provides:
- Reproducible, version-controlled infrastructure
- Testable and retryable deployments
- Automatic resource dependency management
- Simple rollback capabilities

Once deployed, you'll have a complete TrustGraph stack running on OVHcloud infrastructure with:
- Managed Kubernetes cluster (2-node pool, configurable)
- OVHcloud AI Endpoints integration (Mistral Nemo Instruct)
- Complete monitoring with Grafana and Prometheus
- Web workbench for document processing and Graph RAG
- Secure secrets management

{: .note }
> **Why OVHcloud for TrustGraph?**
>
> OVHcloud offers unique advantages for global organizations:
> - **European Cloud Leader**: Largest European cloud provider with 40+ data centers worldwide
> - **No Egress Fees**: Unlimited outbound traffic included at no extra cost
> - **GDPR Native**: Built-in compliance with European data protection standards
> - **Transparent Pricing**: Predictable costs without hidden charges
> - **Anti-DDoS Included**: Enterprise-grade protection at no extra cost
>
> Ideal for organizations requiring European data sovereignty with global reach.

## Getting ready

### OVHcloud Account

You'll need an OVHcloud account with API access. If you don't have one:

1. Sign up at [https://www.ovh.com/](https://www.ovh.com/)
2. Complete account verification
3. Access the OVHcloud Control Panel

To create API credentials:

1. Navigate to the [OVHcloud API token creation page](https://www.ovh.com/auth/api/createToken)
2. Fill in the form with:
   - **Application name**: TrustGraph Deployment
   - **Application description**: Pulumi deployment for TrustGraph
   - **Validity**: Choose appropriate duration (or unlimited)
   - **Rights**: Grant full access or specific rights for Kubernetes and AI services
3. Click **Create keys**
4. Save the **Application Key**, **Application Secret**, and **Consumer Key** securely

### Python

{% include deployment/python-requirement.md %}

### Pulumi

{% include deployment/pulumi-install.md %}

### kubectl

{% include deployment/kubectl-install.md %}

### Node.js

{% include deployment/nodejs-install.md %}

### OVHcloud AI Endpoints

The deployment uses OVHcloud's AI Endpoints service with **Mistral Nemo Instruct** as the default model. You'll need to:

1. Access OVHcloud AI Endpoints in the Control Panel
2. Generate an AI Endpoints token for authentication
3. Note the token for configuration later

OVHcloud AI Endpoints provides access to various AI models including Mistral, LLaMA 3, and Codestral, with processing available in European data centers.

## Prepare the deployment

### Get the Pulumi code

Clone the TrustGraph OVHcloud Pulumi repository:

```bash
git clone https://github.com/trustgraph-ai/pulumi-trustgraph-ovhcloud.git
cd pulumi-trustgraph-ovhcloud/pulumi
```

### Install dependencies

Install the Node.js dependencies for the Pulumi project:

```bash
npm install
```

### Configure OVHcloud credentials

Set the required OVHcloud environment variables using the credentials you created earlier:

```bash
export OVH_ENDPOINT=ovh-eu  # or ovh-ca, ovh-us based on your region
export OVH_APPLICATION_KEY="your_application_key_here"
export OVH_APPLICATION_SECRET="your_application_secret_here"
export OVH_CONSUMER_KEY="your_consumer_key_here"
```

### Configure Pulumi state

{% include deployment/pulumi-configure-state.md %}

### Create a Pulumi stack

{% include deployment/pulumi-create-stack.md %}

### Configure the stack

Apply settings for region, service name, and AI token. The service name is used to construct resource names:

```bash
pulumi config set ovhcloud:region GRA11  # or other available region
pulumi config set serviceName trustgraph-prod
pulumi config set --secret aiEndpointsToken your_ai_endpoints_token_here
```

Available regions include:
- `GRA11` (Gravelines, France)
- `SBG5` (Strasbourg, France)
- `BHS5` (Beauharnois, Canada)
- `DE1` (Frankfurt, Germany)
- `WAW1` (Warsaw, Poland)

Refer to the repository's README for more region options and configuration details.

## Deploy with Pulumi

### Preview the deployment

Before deploying, preview what Pulumi will create:

```bash
pulumi preview
```

This shows all the resources that will be created:
- Managed Kubernetes cluster
- Node pool with specified instance types
- Private network configuration
- Service account with AI Endpoints access
- Kubernetes secrets for API keys and configuration
- TrustGraph deployments, services, and config maps

Review the output to ensure everything looks correct.

### Deploy the infrastructure

Deploy the complete TrustGraph stack:

```bash
pulumi up
```

Pulumi will ask for confirmation before proceeding. Type `yes` to continue.

The deployment typically takes 8 - 12 minutes and progresses through these stages:

1. **Creating Kubernetes cluster** (5-7 minutes)
   - Provisions Managed Kubernetes cluster
   - Creates node pool
   - Configures networking

2. **Configuring service account and secrets** (1-2 minutes)
   - Creates service account
   - Sets up AI Endpoints access
   - Creates Kubernetes secrets

3. **Deploying TrustGraph** (4-6 minutes)
   - Applies Kubernetes manifests
   - Deploys all TrustGraph services
   - Starts pods and initializes services

You'll see output showing the creation progress of all resources.

### Configure and verify kubectl access

After deployment completes, a configuration file permitting access to the Kubernetes cluster is written to kubeconfig.yaml. This file should be treated as a secret as it contains access keys for the Kubernetes cluster.

Check you can access the cluster:

```sh
export KUBECONFIG=$(pwd)/kubeconfig.yaml

# Verify access
kubectl get nodes
```

You should see your OVHcloud Managed Kubernetes nodes listed as `Ready`.

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

Test that OVHcloud AI Endpoints integration is working by invoking the LLM through the gateway:

```bash
tg-invoke-llm 'Be helpful' 'What is 2 + 2?'
```

You should see output like:

```
2 + 2 = 4
```

This confirms that TrustGraph can successfully communicate with OVHcloud's AI Endpoints service.

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

- **Authentication errors**: Verify your OVHcloud credentials are set correctly (`OVH_APPLICATION_KEY`, `OVH_APPLICATION_SECRET`, etc.)
- **Quota limits**: Check your OVHcloud account hasn't hit resource quotas (Kubernetes clusters, nodes, etc.)
- **Region availability**: Ensure Managed Kubernetes is available in your selected region
- **Permissions**: Verify your API credentials have permissions to create Kubernetes clusters and access AI services

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
<summary>OVHcloud AI Endpoints integration not working</summary>
<div markdown="1">

*Diagnosis:*

Test LLM connectivity:

```bash
tg-invoke-llm '' 'What is 2+2'
```

A timeout or error indicates AI Endpoints configuration issues. Check the `text-completion` pod logs:

```bash
kubectl -n trustgraph logs -l app=text-completion
```

*Resolution:*

- Verify OVHcloud AI Endpoints is enabled in your account
- Check that the AI Endpoints token is correct and has not expired
- Ensure the token secret was created correctly by Pulumi
- Review Pulumi outputs to confirm AI configuration: `pulumi stack output`

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
- The Managed Kubernetes cluster
- Node pools
- Service accounts and API access
- All associated networking and storage

{: .warning }
> **Cost Warning**: OVHcloud charges for running Kubernetes clusters and nodes. Make sure to destroy your deployment when you're not using it to avoid unnecessary costs.

### Verify cleanup

After `pulumi destroy` completes, verify all resources are removed:

```bash
# Check Pulumi stack status
pulumi stack

# Verify no resources remain
pulumi stack --show-urns
```

You can also check the OVHcloud Control Panel to ensure the Managed Kubernetes cluster and associated resources are deleted.

### Delete the Pulumi stack

If you're completely done with this deployment, you can remove the Pulumi stack:

```bash
pulumi stack rm dev
```

This removes the stack's state but doesn't affect any cloud resources (use `pulumi destroy` first).

## Next Steps

Now that you have TrustGraph running on OVHcloud:

- **Guides**: See [Guides](../guides) for things you can do with your running TrustGraph
- **Scale the cluster**: Modify your Pulumi configuration to add more nodes or change node types
- **Integrate with OVHcloud services**: Connect to Object Storage, databases, or other OVHcloud services
- **Multi-region deployment**: Deploy TrustGraph across multiple OVHcloud regions for high availability
- **Production hardening**: Review the [GitHub repository](https://github.com/trustgraph-ai/pulumi-trustgraph-ovhcloud) for advanced configuration options

{: .note }
> **Additional Resources**
>
> For Pulumi-specific configuration details, customization options, and contributing to the deployment code, visit the [TrustGraph OVHcloud Pulumi Repository](https://github.com/trustgraph-ai/pulumi-trustgraph-ovhcloud)
