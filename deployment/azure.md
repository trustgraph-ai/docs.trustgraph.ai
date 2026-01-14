---
title: Azure AKS
nav_order: 5
parent: Deployment
grand_parent: TrustGraph Documentation
review_date: 2026-02-21
guide_category:
  - Global cloud
guide_category_order: 2
guide_description: Deploy on Azure Kubernetes Service with AI Foundry and dual AI model support
guide_difficulty: advanced
guide_time: 2 - 4 hr
guide_emoji: ☁️
guide_banner: aks.jpg
guide_labels:
  - Azure
  - Kubernetes
  - Production
---

# Microsoft Azure AKS Deployment

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>Azure account with active subscription (see below for setup)</li>
<li>Azure CLI installed and configured</li>
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
   goal="Deploy a production-ready TrustGraph environment on Azure Kubernetes Service with AI Foundry and dual AI model support using Infrastructure as Code."
%}

## Overview

This guide walks you through deploying TrustGraph on Microsoft Azure's Kubernetes Service (AKS) using Pulumi (Infrastructure as Code). The deployment automatically provisions a production-ready Kubernetes cluster integrated with Azure's AI services including AI Foundry and Cognitive Services.

**Pulumi** is an open-source Infrastructure as Code tool that uses general-purpose programming languages (TypeScript/JavaScript in this case) to define cloud infrastructure. Unlike manual deployments, Pulumi provides:
- Reproducible, version-controlled infrastructure
- Testable and retryable deployments
- Automatic resource dependency management
- Simple rollback capabilities

Once deployed, you'll have a complete TrustGraph stack running on Azure infrastructure with:
- Azure Kubernetes Service (AKS) cluster (2-node pool, configurable)
- Azure AI Foundry integration with Phi-4 model
- Azure Cognitive Services with OpenAI GPT-4o-mini
- Complete monitoring with Grafana and Prometheus
- Web workbench for document processing and Graph RAG
- Secure secrets management with Azure Key Vault

{: .note }
> **Why Microsoft Azure for TrustGraph?**
>
> Azure offers unique advantages for enterprise organizations:
> - **Dual AI Models**: Choose between Azure AI Foundry (Phi-4) and OpenAI (GPT-4o-mini)
> - **Enterprise Integration**: Native integration with Microsoft 365, Active Directory, and enterprise services
> - **Hybrid Cloud**: Seamless hybrid cloud capabilities with Azure Arc
> - **Compliance**: Extensive compliance certifications (ISO, SOC, HIPAA, FedRAMP, etc.)
> - **Global Scale**: 60+ regions worldwide with Microsoft's global network
>
> Ideal for organizations in the Microsoft ecosystem requiring enterprise-grade AI and compliance.

## Getting ready

### Azure Account

You'll need an Azure account with an active subscription. If you don't have one:

1. Sign up at [https://azure.microsoft.com/](https://azure.microsoft.com/)
2. Complete account verification
3. Create or select a subscription
4. New users receive $200 in free credits for 30 days

### Create a Resource Group (Optional)

While Pulumi will create a resource group, you may want to pre-create one for organizational purposes:

```bash
az group create --name trustgraph-rg --location eastus
```

### Install Azure CLI

Install the Azure command-line tool:

<details>
<summary>Linux</summary>
<div markdown="1">
```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```
</div>
</details>

<details>
<summary>MacOS</summary>
<div markdown="1">
```bash
brew update && brew install azure-cli
```
</div>
</details>

<details>
<summary>Windows</summary>
<div markdown="1">
Download the installer from [aka.ms/installazurecliwindows](https://aka.ms/installazurecliwindows)
</div>
</details>

Verify installation:

```bash
az --version
```

### Configure Azure Authentication

Authenticate with your Azure account:

```bash
az login
```

This will open a browser for authentication. After successful login, set your default subscription:

```bash
az account set --subscription "YOUR_SUBSCRIPTION_ID"
```

You can list your subscriptions with:

```bash
az account list --output table
```

### Register Required Resource Providers

Ensure necessary Azure resource providers are registered:

```bash
az provider register --namespace Microsoft.ContainerService
az provider register --namespace Microsoft.Compute
az provider register --namespace Microsoft.Network
az provider register --namespace Microsoft.Storage
az provider register --namespace Microsoft.KeyVault
az provider register --namespace Microsoft.CognitiveServices
```

### Python

{% include deployment/python-requirement.md %}

### Pulumi

{% include deployment/pulumi-install.md %}

### kubectl

{% include deployment/kubectl-install.md %}

### Node.js

{% include deployment/nodejs-install.md %}

### Azure AI Services Access

The deployment supports two AI configurations:

#### Option 1: Azure AI Foundry (Machine Learning)
- **Model**: Phi-4 (serverless endpoint)
- **Configuration**: Uses `resources.yaml.mls`
- **Requirements**: Azure subscription with AI Foundry access

#### Option 2: Azure Cognitive Services (OpenAI)
- **Model**: GPT-4o-mini
- **Configuration**: Uses `resources.yaml.cs`
- **Requirements**: Azure subscription with Cognitive Services access

You'll choose your AI model during deployment preparation.

## Prepare the deployment

### Get the Pulumi code

Clone the TrustGraph Azure Pulumi repository:

```bash
git clone https://github.com/trustgraph-ai/pulumi-trustgraph-azure.git
cd pulumi-trustgraph-azure/pulumi
```

### Choose your AI model configuration

Select which AI model to use:

**For Azure AI Foundry (Phi-4):**
```bash
cp resources.yaml.mls resources.yaml
```

**For Azure Cognitive Services (OpenAI GPT-4o-mini):**
```bash
cp resources.yaml.cs resources.yaml
```

{: .note }
> You can switch between configurations by copying the appropriate template file to `resources.yaml` and re-deploying.

### Install dependencies

Install the Node.js dependencies for the Pulumi project:

```bash
npm install
```

### Configure Pulumi state

{% include deployment/pulumi-configure-state.md %}

### Create a Pulumi stack

{% include deployment/pulumi-create-stack.md %}

### Configure the stack

Apply settings for Azure region and environment:

```bash
pulumi config set azure-native:location eastus
pulumi config set environment dev
```

Available Azure regions include:
- `eastus` (East US)
- `westus2` (West US 2)
- `northeurope` (North Europe)
- `westeurope` (West Europe)
- `uksouth` (UK South)
- `southeastasia` (Southeast Asia)
- `australiaeast` (Australia East)

Refer to [Azure Regions](https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/) for a complete list.

### Configure AI model settings

**For Azure AI Foundry (Phi-4):**
```bash
pulumi config set aiEndpointModel "azureml://registries/azureml/models/Phi-4"
```

**For Azure Cognitive Services (OpenAI):**
```bash
pulumi config set openaiModel gpt-4o-mini
pulumi config set openaiVersion "2024-07-18"
pulumi config set contentFiltering Microsoft.DefaultV2
```

Refer to the repository's README for additional configuration options and model choices.

## Deploy with Pulumi

### Preview the deployment

Before deploying, preview what Pulumi will create:

```bash
pulumi preview
```

This shows all the resources that will be created:
- Resource group for all TrustGraph resources
- Azure Identity service principal
- AKS Kubernetes cluster
- Node pool with specified VM sizes
- Azure Key Vault for secrets
- Storage account for AI services
- Azure AI Foundry (AI hub, workspace, serverless endpoints) OR
- Cognitive Services (OpenAI deployment)
- Kubernetes secrets for Azure credentials
- TrustGraph deployments, services, and config maps

Review the output to ensure everything looks correct.

### Deploy the infrastructure

Deploy the complete TrustGraph stack:

```bash
pulumi up
```

Pulumi will ask for confirmation before proceeding. Type `yes` to continue.

The deployment typically takes 15 - 25 minutes and progresses through these stages:

1. **Creating Azure resources** (8-12 minutes)
   - Creates resource group
   - Sets up service principal
   - Provisions Key Vault and Storage Account

2. **Creating AKS cluster** (8-10 minutes)
   - Provisions AKS cluster
   - Creates node pool
   - Configures networking

3. **Configuring AI services** (2-3 minutes)
   - Sets up Azure AI Foundry (Phi-4) OR Cognitive Services (OpenAI)
   - Creates AI endpoints
   - Configures authentication

4. **Deploying TrustGraph** (4-6 minutes)
   - Applies Kubernetes manifests
   - Deploys all TrustGraph services
   - Starts pods and initializes services

You'll see output showing the creation progress of all resources.

### Configure and verify kubectl access

After deployment completes, configure kubectl to access your AKS cluster:

```bash
az aks get-credentials --resource-group trustgraph-rg --name trustgraph-aks
```

Verify access:

```bash
kubectl get nodes
```

You should see your AKS nodes listed as `Ready`.

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

Test that Azure AI integration is working by invoking the LLM through the gateway:

```bash
tg-invoke-llm 'Be helpful' 'What is 2 + 2?'
```

You should see output like:

```
2 + 2 = 4
```

This confirms that TrustGraph can successfully communicate with your chosen Azure AI service (AI Foundry or Cognitive Services).

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

- **Authentication errors**: Verify `az login` was successful and you have an active subscription
- **Provider not registered**: Ensure all required Azure resource providers are registered (see "Register Required Resource Providers" section)
- **Quota limits**: Check your Azure subscription hasn't hit resource quotas (AKS clusters, VMs, cores)
- **Permission issues**: Ensure your account has Contributor or Owner role on the subscription
- **Region capacity**: Try a different Azure region if resources aren't available

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

- **Insufficient resources**: Increase node count or VM size in your Pulumi configuration
- **PersistentVolume issues**: Check PV/PVC status with `kubectl -n trustgraph get pv,pvc`
- **Node issues**: Check node status with `kubectl get nodes`
- **Azure disk limits**: Verify you haven't exceeded disk attachment limits per VM

</div>
</details>

<details>
<summary>Azure AI integration not working</summary>
<div markdown="1">

*Diagnosis:*

Test LLM connectivity:

```bash
tg-invoke-llm '' 'What is 2+2'
```

A timeout or error indicates AI service configuration issues. Check the `text-completion` pod logs:

```bash
kubectl -n trustgraph logs -l app=text-completion
```

*Resolution:*

- Verify the correct `resources.yaml` file is being used (`.mls` for AI Foundry, `.cs` for Cognitive Services)
- Check that AI services are properly deployed in Azure Portal
- Verify service principal has appropriate permissions for AI services
- Ensure API keys are correctly stored in Kubernetes secrets
- Review Pulumi outputs: `pulumi stack output`
- Check Azure AI Foundry or Cognitive Services quotas in Azure Portal

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
- Check AKS cluster status: `az aks show --resource-group trustgraph-rg --name trustgraph-aks`

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
- Azure credentials not properly configured

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
- Check AKS cluster health: `az aks show --resource-group trustgraph-rg --name trustgraph-aks`

</div>
</details>

### Azure-Specific Issues

<details>
<summary>AKS cluster creation fails</summary>
<div markdown="1">

*Diagnosis:*

Check Azure subscription and permissions:

```bash
az account show
az role assignment list --assignee YOUR_USER_ID
```

*Resolution:*

- Verify you have sufficient quota for AKS in your region
- Request quota increases via Azure Portal if needed
- Ensure your account has `Microsoft.ContainerService/managedClusters/write` permission
- Try a different Azure region if capacity is unavailable
- Check service health: [Azure Status](https://status.azure.com/)

</div>
</details>

<details>
<summary>Azure AI Foundry quota exceeded</summary>
<div markdown="1">

*Diagnosis:*

Error messages about Azure AI quota or rate limits.

*Resolution:*

- Check AI service quotas in Azure Portal under "Quotas"
- Request quota increases if needed
- Switch to Cognitive Services (OpenAI) if AI Foundry quota is unavailable
- Implement rate limiting in your application
- Consider upgrading to a higher pricing tier

</div>
</details>

<details>
<summary>Key Vault access denied</summary>
<div markdown="1">

*Diagnosis:*

Errors related to Azure Key Vault access when deploying or running services.

*Resolution:*

- Verify the service principal has appropriate Key Vault permissions
- Check Key Vault access policies in Azure Portal
- Ensure Key Vault firewall settings allow AKS access
- Review service principal role assignments: `az role assignment list --assignee SERVICE_PRINCIPAL_ID`

</div>
</details>

## Shutting down

### Clean shutdown

When you're finished with your TrustGraph deployment, clean up all resources:

```bash
pulumi destroy
```

Pulumi will show you all the resources that will be deleted and ask for confirmation. Type `yes` to proceed.

The destruction process typically takes **10-15 minutes** and removes:
- All TrustGraph Kubernetes resources
- The AKS cluster
- Node pools
- Azure AI services (AI Foundry or Cognitive Services)
- Service principal
- Key Vault
- Storage account
- Resource group (if created by Pulumi)

{: .warning }
> **Cost Warning**: Azure charges for running AKS clusters, VMs, AI services, and storage. Make sure to destroy your deployment when you're not using it to avoid unnecessary costs. AKS charges include cluster management fees plus compute and storage costs.

### Verify cleanup

After `pulumi destroy` completes, verify all resources are removed:

```bash
# Check Pulumi stack status
pulumi stack

# Verify no resources remain
pulumi stack --show-urns

# Check Azure for remaining resources
az aks list --output table
az group show --name trustgraph-rg
```

### Delete the Pulumi stack

If you're completely done with this deployment, you can remove the Pulumi stack:

```bash
pulumi stack rm dev
```

This removes the stack's state but doesn't affect any cloud resources (use `pulumi destroy` first).

## Cost Optimization

### Monitor Costs

Keep track of your Azure spending:

1. Navigate to **Cost Management + Billing** in Azure Portal
2. View cost analysis and breakdown by resource
3. Set up budget alerts

### Cost-Saving Tips

- **Spot VMs**: Use Azure Spot VMs for non-production workloads (up to 90% cheaper)
- **Reserved Instances**: Purchase 1 or 3-year reserved instances for production (up to 72% savings)
- **Autoscaling**: Configure cluster autoscaler to scale down during idle periods
- **Dev/Test pricing**: Use Azure Dev/Test subscription for development environments
- **Shut down non-production**: Stop dev/test clusters when not in use
- **Right-size VMs**: Choose appropriate VM sizes based on actual usage

Example cost estimates (East US):
- **AKS management**: Free (only pay for VMs)
- **2 x Standard_D2s_v3 nodes**: ~$140/month
- **Azure AI Foundry**: Pay per use (varies by model and requests)
- **Cognitive Services**: Pay per use (varies by model and requests)
- **Storage & Key Vault**: ~$10-20/month
- **Total estimated**: ~$150-200/month for basic deployment (plus AI usage)

## Switching Between AI Models

You can switch between Azure AI Foundry and Cognitive Services:

1. **Copy the desired configuration:**
   ```bash
   # For AI Foundry (Phi-4)
   cp resources.yaml.mls resources.yaml

   # For Cognitive Services (OpenAI)
   cp resources.yaml.cs resources.yaml
   ```

2. **Update Pulumi configuration:**
   ```bash
   # Update the stack config based on your choice
   pulumi config set aiEndpointModel "azureml://registries/azureml/models/Phi-4"
   # OR
   pulumi config set openaiModel gpt-4o-mini
   ```

3. **Re-deploy:**
   ```bash
   pulumi up
   ```

## Next Steps

Now that you have TrustGraph running on Azure:

- **Guides**: See [Guides](../guides) for things you can do with your running TrustGraph
- **Scale the cluster**: Configure AKS autoscaling or increase node pool size
- **Production hardening**: Set up Azure Front Door, Application Gateway, and private AKS cluster
- **Integrate Azure services**: Connect to Azure Storage, Azure SQL, or Cosmos DB
- **CI/CD**: Set up Azure DevOps or GitHub Actions for automated deployments
- **Monitoring**: Integrate with Azure Monitor and Application Insights
- **Multi-region**: Deploy across multiple Azure regions for high availability
- **Azure AD integration**: Configure authentication with Azure Active Directory
- **Advanced AI**: Explore Azure OpenAI fine-tuning or custom models

{: .note }
> **Additional Resources**
>
> - [TrustGraph Azure Pulumi Repository](https://github.com/trustgraph-ai/pulumi-trustgraph-azure) - Full source code and configuration
> - [AKS Best Practices](https://learn.microsoft.com/en-us/azure/aks/best-practices) - Microsoft's recommendations
> - [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-studio/) - Learn more about Azure's AI platform
> - [Azure Free Account](https://azure.microsoft.com/en-us/free/) - Information about free credits and services
