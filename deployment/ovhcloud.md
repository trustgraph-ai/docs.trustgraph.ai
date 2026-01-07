---
title: OVHcloud
nav_order: 4.5
parent: Deployment
review_date: 2026-02-02
guide_category:
  - European Cloud Providers
guide_category_order: 1
guide_description: Deploy on OVHcloud Managed Kubernetes with European data sovereignty and AI Endpoints
guide_difficulty: intermediate
guide_time: 2 hr
guide_emoji: 🇪🇺
guide_banner: ovhcloud.png
guide_labels:
  - Kubernetes
  - Europe
  - Cloud
---

# OVHcloud Deployment

Deploy TrustGraph on OVHcloud using Managed Kubernetes Service (MKS) and OVHcloud's global cloud infrastructure with integrated AI services.

## Overview

TrustGraph provides a complete OVHcloud deployment solution using **Pulumi** (Infrastructure as Code) that automatically provisions and configures a Kubernetes cluster with OVHcloud's AI Endpoints for a production-ready TrustGraph deployment.

## Why Choose OVHcloud?

OVHcloud offers unique advantages for TrustGraph deployments:

### 🇪🇺 **European Leadership & Global Reach**
- **European Cloud Leader**: Largest European cloud provider with global presence
- **Data Sovereignty**: Full control over data location with 40+ data centers worldwide
- **GDPR Native**: Built-in compliance with European data protection standards
- **Multi-Region**: Deploy in Europe, North America, or Asia-Pacific

### 💰 **Predictable Pricing**
- **No Egress Fees**: Unlimited outbound traffic included
- **Transparent Costs**: Simple, predictable pricing without hidden charges
- **Anti-DDoS Included**: Enterprise-grade protection at no extra cost
- **Competitive Rates**: Cost-effective solutions for all deployment sizes

### 🚀 **High-Performance Infrastructure**
- **Water-Cooled Servers**: Innovative cooling for better performance and sustainability
- **OVHcloud Link**: High-speed private network backbone
- **NVMe Storage**: Ultra-fast storage options for demanding workloads
- **Bare Metal Options**: Dedicated servers when you need maximum performance

### 🛡️ **Security & Compliance**
- **ISO/IEC 27001**: Information security management certification
- **SOC 1 & 2**: Service organization controls attestation
- **HDS Certification**: Healthcare data hosting compliance
- **SecNumCloud**: French government security qualification

## What You Get

The OVHcloud deployment includes:

- **Managed Kubernetes cluster** with configurable node pool
- **Private network** with subnet configuration
- **Service account** with AI Endpoints access
- **Complete TrustGraph stack** deployed and configured
- **Mistral Nemo Instruct** endpoint integration (default)
- **OVHcloud AI Endpoints** integration
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

**Kubernetes Platform**: OVHcloud Managed Kubernetes Service (MKS)
**Node Configuration**: 2 nodes (configurable)
**AI Integration**: OVHcloud AI Endpoints
**Default Model**: Mistral Nemo Instruct
**Network**: Private network with managed subnet
**Storage**: OVHcloud Block Storage with automatic provisioning
**AI Service**: OVHcloud AI Endpoints with token authentication

## Quick Process Overview

1. **Install Pulumi** and dependencies
2. **Create OVHcloud API credentials** via console
3. **Generate AI Endpoints token** separately
4. **Configure environment variables** (OVH_APPLICATION_KEY, etc.)
5. **Customize configuration** in `Pulumi.ovhcloud.yaml`
6. **Deploy** with `pulumi up`
7. **Access services** via port-forwarding

## Configuration Requirements

Required OVHcloud environment variables:

```bash
export OVH_ENDPOINT=ovh-eu  # or ovh-ca, ovh-us
export OVH_APPLICATION_KEY=your_application_key
export OVH_APPLICATION_SECRET=your_application_secret
export OVH_CONSUMER_KEY=your_consumer_key
```

## Access Points

Once deployed, you'll have access to:

- **TrustGraph API**: Port 8088
- **Web Workbench**: Port 8888 (document processing, Graph RAG)
- **Grafana Monitoring**: Port 3000

## OVHcloud AI Integration

The deployment includes OVHcloud AI Endpoints integration with:

- **Default Model**: Mistral Nemo Instruct
- **Alternative Models**: Mixtral, LLaMA 3, Codestral available
- **Token Access**: Secure token-based authentication
- **European AI**: Processing available in European data centers

Available models include:
- `mistral-nemo-instruct-2407`
- `mixtral-8x7b-instruct-0123`
- `llama-3-8b-instruct`
- `codestral-2405`

## Complete Documentation

For detailed step-by-step instructions, configuration options, and troubleshooting, visit:

**[TrustGraph OVHcloud Deployment Guide](https://github.com/trustgraph-ai/ovhcloud)**

The repository contains:
- Complete Pulumi deployment code
- Managed Kubernetes Service configuration
- OVHcloud AI Endpoints integration setup
- Detailed setup instructions
- Troubleshooting guides
- Customization options

## Use Cases

OVHcloud deployment is ideal for:

- **European Organizations**: Requiring EU data sovereignty
- **Global Enterprises**: Needing multi-region deployment options
- **Cost-Conscious Teams**: Benefiting from no egress fees
- **High-Performance Applications**: Leveraging water-cooled infrastructure
- **Regulated Industries**: Meeting compliance requirements (HDS, SecNumCloud)
- **Sustainable Computing**: Using eco-friendly infrastructure

## Next Steps

After deployment, you can:
- Load documents through the web workbench
- Test Graph RAG queries with Mistral models
- Monitor processing through Grafana
- Scale the cluster as needed
- Integrate with other OVHcloud services
- Leverage OVHcloud's global network for multi-region deployments
