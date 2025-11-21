---
title: Amazon Web Services (RKE)
nav_order: 9
parent: Deployment
grand_parent: TrustGraph Documentation
review_date: 2025-11-21
---

# Amazon Web Services (RKE) Deployment

Deploy TrustGraph on Amazon Web Services using RKE2 Kubernetes and AWS Bedrock integration.

## Overview

TrustGraph provides a complete AWS deployment solution using **Pulumi** (Infrastructure as Code) that automatically provisions and configures an RKE2 Kubernetes cluster with AWS Bedrock LLM integration for a production-ready TrustGraph deployment.

## What You Get

The AWS deployment includes:

- **RKE2 Kubernetes cluster** with 1 server and multiple agent nodes
- **IAM roles and policies** with Bedrock access permissions
- **EBS CSI driver** for persistent storage provisioning
- **Complete TrustGraph stack** deployed and configured
- **AWS Bedrock integration** with Claude 3.5 Haiku (configurable)
- **Mistral Nemo Instruct** endpoint configured
- **Secrets management** for secure credential handling
- **Monitoring and observability** with Grafana
- **Web workbench** for document processing and Graph RAG

## Deployment Method

The deployment uses **Pulumi**, an Infrastructure as Code tool that:

- Has an open-source license
- Uses general-purpose programming languages (TypeScript/JavaScript)
- Provides testable infrastructure code
- Offers retryable deployments
- Supports local or S3 state management

## Architecture

**Kubernetes Platform**: RKE2 (Rancher Kubernetes Engine 2)
**Node Configuration**: t3a.xlarge instances (configurable)
**Default Setup**: 3 nodes, Amazon Linux 2023
**Network**: Custom VPC with configurable CIDR blocks
**Storage**: EBS volumes with automatic provisioning
**LLM Service**: AWS Bedrock with multiple model options

## Quick Process Overview

1. **Install Pulumi** and dependencies
2. **Configure AWS credentials** via `.aws/credentials`
3. **Set up Bedrock model access** in AWS console
4. **Customize configuration** in `Pulumi.STACKNAME.yaml`
5. **Deploy** with `pulumi up`
6. **Wait for initialization** (~30 seconds after pods are running)
7. **Access services** via port-forwarding

## Configuration Options

Customizable settings include:

- **Environment**: dev, staging, production
- **Region**: us-west-2 (default, configurable)
- **VPC CIDR**: 172.38.0.0/16
- **Node type**: t3a.xlarge (configurable)
- **Node count**: 3 (configurable)
- **AMI**: Amazon Linux 2023

## Access Points

Once deployed, you'll have access to:

- **TrustGraph API**: Port 8088
- **Web Workbench**: Port 8888 (document processing, Graph RAG)
- **Grafana Monitoring**: Port 3000

## Bedrock Integration

The deployment includes AWS Bedrock integration with:

- **Default Model**: Claude 3.5 Haiku
- **Alternative Models**: Mistral Nemo Instruct and others
- **Model Access**: Requires enabling specific models in Bedrock console
- **Secure Access**: IAM roles and policies automatically configured

## Complete Documentation

For detailed step-by-step instructions, configuration options, and troubleshooting, visit:

**[TrustGraph AWS RKE Deployment Guide](https://github.com/trustgraph-ai/pulumi-trustgraph-aws-rke)**

The repository contains:
- Complete Pulumi deployment code
- RKE2 cluster configuration
- AWS Bedrock integration setup
- Detailed setup instructions
- Troubleshooting guides
- Customization options

## Important Notes

**Storage Cleanup**: The EBS CSI driver doesn't automatically clean up volumes on teardown. Manual cleanup may be required in the EC2 console.

**Initialization Time**: Allow ~30 seconds after all pods are running for application initialization to complete.

**Bedrock Access**: Ensure you have enabled the required models in your AWS Bedrock console before deployment.

## Next Steps

After deployment, you can:
- Load documents through the web workbench
- Test Graph RAG queries with Bedrock models
- Monitor processing through Grafana
- Scale the cluster by adjusting node count
- Integrate with other AWS services
