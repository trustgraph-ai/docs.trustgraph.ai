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
guide_banner: azure.jpg
guide_labels:
  - Azure
  - Kubernetes
  - Production
---

# Microsoft Azure AKS Deployment

Deploy TrustGraph on Microsoft Azure using Azure Kubernetes Service (AKS) with comprehensive AI integration.

## Overview

TrustGraph provides a complete Azure deployment solution using **Pulumi** (Infrastructure as Code) that automatically provisions and configures an AKS cluster with Azure's AI services for a production-ready TrustGraph deployment.

## What You Get

The Azure deployment includes:

- **Dedicated resource group** for complete resource isolation
- **Azure Identity service principal** for secure component authentication
- **AKS cluster** deployed in managed resource group
- **Key Vault and Storage Account** for AI component requirements
- **Azure AI Foundry integration** with AI hub, workspace, and serverless endpoints
- **Azure Cognitive Services** with OpenAI GPT-4o-mini deployment
- **Dual AI model support**: Phi-4 and OpenAI models
- **Complete TrustGraph stack** deployed and configured
- **Secrets management** for secure credential handling
- **Monitoring and observability** with Grafana
- **Web workbench** for document processing and Graph RAG

## Deployment Method

The deployment uses **Pulumi**, an Infrastructure as Code tool that:

- Has an open-source license
- Uses general-purpose programming languages (TypeScript/JavaScript)
- Provides testable infrastructure code
- Offers retryable deployments
- Supports local or cloud state management

## Architecture

**Kubernetes Platform**: Azure Kubernetes Service (AKS)
**AI Services**: Azure AI Foundry + Cognitive Services
**Default Models**: Phi-4 (Machine Learning) and GPT-4o-mini (OpenAI)
**Identity Management**: Azure Identity service principal
**Storage**: Azure Key Vault and Storage Account
**Network**: Managed AKS networking with Azure CNI
**Monitoring**: Integrated Azure monitoring and Grafana

## AI Model Options

Choose between two AI configurations:

### Machine Learning Services (AI Foundry)
- **Model**: Phi-4 (serverless endpoint)
- **Configuration**: Copy `resources.yaml.mls` to `resources.yaml`
- **Features**: Azure-native model hosting

### Cognitive Services (OpenAI)
- **Model**: GPT-4o-mini
- **Configuration**: Copy `resources.yaml.cs` to `resources.yaml`
- **Features**: OpenAI API compatibility

## Quick Process Overview

1. **Choose AI model** (Phi-4 or OpenAI)
2. **Install Pulumi** and dependencies
3. **Configure Azure credentials** using `az login`
4. **Customize configuration** in `Pulumi.azure.yaml`
5. **Deploy** with `pulumi up`
6. **Access services** via port-forwarding

## Configuration Options

Customizable settings include:

- **Location**: Azure deployment region
- **Environment**: dev, staging, production
- **AI Endpoint Model**: e.g., `azureml://registries/azureml/models/Phi-4`
- **OpenAI Model**: e.g., `gpt-4o-mini`
- **OpenAI Version**: e.g., `"2024-07-18"` (quoted for date format)
- **Content Filtering**: e.g., `Microsoft.DefaultV2` (Responsible AI policy)

## Access Points

Once deployed, you'll have access to:

- **TrustGraph API**: Port 8088
- **Web Workbench**: Port 8888 (document processing, Graph RAG)
- **Grafana Monitoring**: Port 3000

## Azure AI Integration

The deployment includes comprehensive Azure AI integration:

### Machine Learning Services
- **AI Hub**: Central workspace for ML operations
- **AI Workspace**: Project-specific environment
- **Serverless Endpoints**: Scalable model hosting
- **Model Catalog**: Access to Azure's model library

### Cognitive Services
- **OpenAI Service**: GPT models via Azure
- **Content Filtering**: Responsible AI policies
- **API Management**: Secure API access
- **Usage Monitoring**: Built-in analytics

## Complete Documentation

For detailed step-by-step instructions, configuration options, and troubleshooting, visit:

**[TrustGraph Azure AKS Deployment Guide](https://github.com/trustgraph-ai/pulumi-trustgraph-aks)**

The repository contains:
- Complete Pulumi deployment code
- AKS cluster configuration
- Azure AI services integration
- Dual model configuration templates
- Detailed setup instructions
- Troubleshooting guides
- Customization options

## Important Notes

**Storage Account Issues**: Azure occasionally reports "parallel access to resources" errors during Storage Account creation. If deployment fails, retry with `pulumi up` - it's retryable and continues from where it left off.

**Model Selection**: Choose your AI model before deployment by copying the appropriate `resources.yaml.*` file to `resources.yaml`.

**Resource Groups**: Azure automatically creates separate resource groups for AKS cluster components.

**SSH Keys**: An SSH private key is generated but typically not needed for AKS management.

## Azure Enterprise Features

**Enterprise Integration**: Native integration with Azure Active Directory
**Compliance**: Built-in compliance tools and reporting
**Security**: Azure Security Center integration
**Networking**: Advanced networking with Azure CNI
**Monitoring**: Azure Monitor and Application Insights
**Backup**: Azure Backup integration for persistent data

## Next Steps

After deployment, you can:
- Load documents through the web workbench
- Test Graph RAG queries with Phi-4 or OpenAI models
- Monitor processing through Grafana and Azure Monitor
- Scale the AKS cluster as needed
- Integrate with other Azure services
- Leverage Azure's enterprise security features
