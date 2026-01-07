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

Deploy TrustGraph on Scaleway using Kubernetes Kapsule and Scaleway's European cloud infrastructure.

## Overview

TrustGraph provides a complete Scaleway deployment solution using **Pulumi** (Infrastructure as Code) that automatically provisions and configures a Kubernetes cluster with Scaleway's Generative AI services for a production-ready TrustGraph deployment.

## Why Choose Scaleway?

Scaleway offers unique advantages for TrustGraph deployments:

### 🇪🇺 **European Data Sovereignty**
- **GDPR Compliance**: Full compliance with European data protection regulations
- **EU-based Infrastructure**: All data remains within European Union boundaries
- **Data Residency**: Meet strict data localization requirements for European organizations
- **Privacy by Design**: Built-in privacy protections and transparent data handling

### 💰 **Cost-Effective Cloud Computing**
- **Competitive Pricing**: Transparent, affordable pricing model
- **No Hidden Costs**: Predictable billing with no surprise charges
- **Resource Efficiency**: Optimized infrastructure for better price-performance

### 🚀 **Developer-Friendly Platform**
- **Simple APIs**: Easy-to-use cloud services and APIs
- **Open Source Commitment**: Strong support for open-source technologies
- **European Innovation**: European cloud provider with focus on developer experience
- **Sustainable Computing**: Commitment to environmental responsibility

### 🛡️ **Enterprise Security**
- **ISO Certifications**: Multiple security and quality certifications
- **Network Security**: Advanced DDoS protection and network isolation
- **Compliance Ready**: SOC 2, ISO 27001, and other enterprise certifications

## What You Get

The Scaleway deployment includes:

- **Kubernetes Kapsule cluster** with 2-node pool
- **IAM application and policies** with Generative AI access
- **Complete TrustGraph stack** deployed and configured
- **Mistral Nemo Instruct** endpoint integration
- **Scaleway Gen AI services** integration
- **Secrets management** for secure configuration
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

**Kubernetes Platform**: Scaleway Kubernetes Kapsule
**Node Configuration**: 2 nodes (configurable)
**AI Integration**: Scaleway Generative AI services
**Default Model**: Mistral Nemo Instruct
**Network**: Scaleway VPC with managed networking
**Storage**: Scaleway Block Storage with automatic provisioning
**AI Service**: Scaleway Gen AI with API key authentication

## Quick Process Overview

1. **Install Pulumi** and dependencies
2. **Create Scaleway API key** in console
3. **Configure environment variables** (SCW_ACCESS_KEY, SCW_SECRET_KEY, etc.)
4. **Customize configuration** in `Pulumi.STACKNAME.yaml`
5. **Deploy** with `pulumi up`
6. **Access services** via port-forwarding

## Configuration Requirements

Required Scaleway environment variables:

```bash
export SCW_ACCESS_KEY=your_access_key
export SCW_SECRET_KEY=your_secret_key
export SCW_DEFAULT_ORGANIZATION_ID=your_org_id
export SCW_DEFAULT_PROJECT_ID=your_project_id
```

## Access Points

Once deployed, you'll have access to:

- **TrustGraph API**: Port 8088
- **Web Workbench**: Port 8888 (document processing, Graph RAG)
- **Grafana Monitoring**: Port 3000

## Scaleway AI Integration

The deployment includes Scaleway Generative AI integration with:

- **Default Model**: Mistral Nemo Instruct
- **Alternative Models**: Other models available through Scaleway Gen AI
- **API Access**: Secure API key-based authentication
- **European AI**: AI processing within EU boundaries

## Complete Documentation

For detailed step-by-step instructions, configuration options, and troubleshooting, visit:

**[TrustGraph Scaleway Deployment Guide](https://github.com/trustgraph-ai/pulumi-trustgraph-scaleway)**

The repository contains:
- Complete Pulumi deployment code
- Kubernetes Kapsule configuration
- Scaleway Gen AI integration setup
- Detailed setup instructions
- Troubleshooting guides
- Customization options

## Use Cases

Scaleway deployment is ideal for:

- **European Organizations**: Requiring EU data residency
- **GDPR Compliance**: Strict data protection requirements
- **Cost-Conscious Deployments**: Budget-friendly cloud solutions
- **Open Source Advocates**: Supporting European open-source innovation
- **Sustainable Computing**: Environmentally responsible cloud infrastructure

## Next Steps

After deployment, you can:
- Load documents through the web workbench
- Test Graph RAG queries with Mistral models
- Monitor processing through Grafana
- Scale the cluster as needed
- Integrate with other Scaleway services
- Ensure GDPR compliance for your AI workflows
