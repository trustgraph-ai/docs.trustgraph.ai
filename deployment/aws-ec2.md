---
title: AWS EC2 Single Instance
nav_order: 7
parent: Deployment
grand_parent: TrustGraph Documentation
review_date: 2026-01-20
guide_category:
  - Standalone deployment
guide_category_order: 3
guide_description: Single AWS EC2 instance with Podman for development, testing, and small-scale deployments
guide_difficulty: advanced
guide_time: 2 - 5 hr
guide_emoji: 🖥️
guide_banner: /../aws-ec2.png
guide_labels:
  - AWS
  - Podman
  - Development
---

# AWS EC2 Single Instance Deployment

Deploy TrustGraph on a single AWS EC2 instance for development, testing, and experimentation.

## Overview

TrustGraph provides a simplified AWS deployment using **Pulumi** (Infrastructure as Code) that deploys a single EC2 instance with Podman containers. This deployment method is designed for:

- **Development and testing**
- **Experimentation and learning**
- **Quick prototyping**
- **Analysis and evaluation**

⚠️ **Not Recommended for Production**: This is a single instance deployment with no redundancy or high availability. For production use, consider the [AWS RKE deployment](aws) or container services like EKS/ECS.

## What You Get

The AWS EC2 deployment includes:

- **Single EC2 instance** running Amazon Linux with Podman
- **IAM role** with AWS Bedrock access (no credential management needed)
- **Complete TrustGraph stack** deployed via Podman Compose
- **AWS Bedrock integration** with automatic credential handling
- **SSH access** with generated private key
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

**Platform**: Single AWS EC2 instance
**Container Engine**: Podman with Compose
**Operating System**: Amazon Linux (Ubuntu user)
**Credential Management**: AWS instance metadata (no key passing)
**Storage**: EBS volumes attached to instance
**LLM Service**: AWS Bedrock with IAM role authentication

## Quick Process Overview

1. **Install Pulumi** and dependencies
2. **Configure AWS credentials** (AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY or AWS_PROFILE)
3. **Customize configuration** in `Pulumi.analysis.yaml`
4. **Deploy** with `pulumi up`
5. **SSH access** using generated private key
6. **Access services** via SSH port forwarding

## Key Features

**Simplified Setup**: No complex Kubernetes configuration
**Automatic Credentials**: AWS Bedrock access via IAM roles
**SSH Access**: Direct instance access for debugging
**Container Management**: Podman for container orchestration
**Port Forwarding**: Access web interfaces via SSH tunneling

## Access Points

Once deployed, you'll have access to:

- **TrustGraph API**: Available on instance
- **Web Workbench**: Port 8888 (via SSH forwarding)
- **Grafana Monitoring**: Port 3000 (via SSH forwarding)
- **SSH Access**: Direct instance login with generated key

## Usage Example

After deployment, access the instance:

```bash
# Set correct permissions on SSH key
chmod 600 ssh-private.key

# SSH with port forwarding
ssh -L 3000:localhost:3000 -L 8888:localhost:8888 \
    -i ssh-private.key ubuntu@[instance-ip]

# Activate TrustGraph CLI
. /usr/local/trustgraph/env/bin/activate

# View containers
sudo podman ps -a
```

## Complete Documentation

For detailed step-by-step instructions, configuration options, and troubleshooting, visit:

**[TrustGraph AWS EC2 Deployment Guide](https://github.com/trustgraph-ai/pulumi-trustgraph-ec2)**

The repository contains:
- Complete Pulumi deployment code
- EC2 instance configuration
- Podman Compose setup
- AWS Bedrock integration
- SSH key management
- Detailed setup instructions
- Troubleshooting guides

## Important Limitations

**Single Point of Failure**: No redundancy or high availability
**No Auto-scaling**: Fixed instance capacity
**Limited Monitoring**: Basic container-level monitoring only
**Manual Updates**: No automated deployment updates
**Storage Limitations**: Limited to single instance storage

## Production Alternatives

For production deployments, consider:
- **[AWS RKE Deployment](aws)**: Multi-node Kubernetes cluster
- **AWS EKS**: Managed Kubernetes service
- **AWS ECS**: Container orchestration service
- **Multi-instance setup**: Load balanced instances

## Next Steps

After deployment, you can:
- Load documents through the web workbench
- Test Graph RAG queries with Bedrock models
- Monitor processing through Grafana
- Experiment with different configurations
- Migrate to production-ready architecture when ready
