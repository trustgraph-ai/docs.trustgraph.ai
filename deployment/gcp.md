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
guide_difficulty: advanced
guide_time: 2 - 4 hr
guide_emoji: ☁️
guide_banner: gcp.jpg
guide_labels:
  - GCP
  - Kubernetes
  - Production
---

# Google Cloud Platform Deployment

Deploy TrustGraph on Google Cloud Platform using Google Kubernetes Engine (GKE) and other GCP services.

## Overview

TrustGraph provides a complete GCP deployment solution using **Pulumi** (Infrastructure as Code) that automatically provisions and configures all necessary GCP resources for a production-ready TrustGraph deployment.

## What You Get

The GCP deployment includes:

- **GKE Kubernetes cluster** with 2-node pool
- **Service accounts** with VertexAI access
- **Complete TrustGraph stack** deployed and configured
- **VertexAI Gemini Flash 1.5** LLM integration
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

## Quick Process Overview

1. **Install Pulumi** and dependencies
2. **Configure GCP credentials** using `gcloud auth login`
3. **Customize configuration** in `Pulumi.STACKNAME.yaml`
4. **Deploy** with `pulumi up`
5. **Access services** via port-forwarding or load balancers

## Access Points

Once deployed, you'll have access to:

- **TrustGraph API**: Port 8088
- **Web Workbench**: Port 8888 (document processing, Graph RAG)
- **Grafana Monitoring**: Port 3000

## Complete Documentation

For detailed step-by-step instructions, configuration options, and troubleshooting, visit:

**[TrustGraph GCP Deployment Guide](https://github.com/trustgraph-ai/pulumi-trustgraph-gke)**

The repository contains:
- Complete Pulumi deployment code
- Configuration templates
- Detailed setup instructions
- Troubleshooting guides
- Customization options

## Next Steps

After deployment, you can:
- Load documents through the web workbench
- Test Graph RAG queries
- Monitor processing through Grafana
- Scale the cluster as needed
- Integrate with existing GCP services
