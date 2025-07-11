---
title: Installation
layout: default
nav_order: 2
parent: Getting Started
grand_parent: TrustGraph Documentation
---

# Installation

Choose the TrustGraph deployment method that best fits your needs.

## Easiest Deployment Options

### Docker Compose / Podman Compose (Recommended)

The simplest way to get TrustGraph running locally:

- **Best for**: Local development, testing, proof-of-concept
- **Requirements**: 16GB RAM minimum, Docker or Podman
- **Platform**: Linux (Podman recommended), macOS, Windows
- **Setup time**: ~15 minutes

**→ [Docker Compose Deployment Guide](../deployment/docker-compose)**

### AWS EC2 Single Instance

Simple cloud deployment for experimentation:

- **Best for**: Quick cloud testing, temporary deployments
- **Requirements**: AWS account, basic AWS knowledge
- **Features**: Automated Pulumi deployment, AWS Bedrock integration
- **Setup time**: ~20 minutes

**→ [AWS EC2 Deployment Guide](../deployment/aws-ec2)**

## Production Deployment Options

For production use, choose from enterprise-grade deployment options:

- **[AWS RKE](../deployment/aws-rke)**: Multi-node Kubernetes with AWS Bedrock
- **[Google Cloud](../deployment/gcp)**: GKE with VertexAI integration
- **[Azure AKS](../deployment/azure)**: Azure Kubernetes with AI Foundry
- **[Scaleway](../deployment/scaleway)**: European cloud with GDPR compliance
- **[Intel Tiber Cloud](../deployment/intel)**: High-performance Intel accelerators
- **[Minikube](../deployment/minikube)**: Local Kubernetes development

## System Requirements

### Minimum Requirements (Docker Compose)
- **Memory**: 16GB RAM
- **Storage**: 20GB available disk space
- **CPU**: 4 cores recommended
- **Container Engine**: Docker or Podman

### Cloud Deployments
- **AWS EC2**: t3.xlarge or larger
- **Production clusters**: 8GB+ RAM per node
- **GPU acceleration**: Available for Intel Tiber Cloud

## Quick Start Recommendation

1. **New to TrustGraph?** Start with [Docker Compose](../deployment/docker-compose)
2. **Want cloud testing?** Try [AWS EC2](../deployment/aws-ec2)
3. **Planning production?** Review [production deployment options](../deployment/)

## Next Steps

After choosing your deployment method:
1. Follow the deployment guide for your chosen platform
2. Proceed to [First Steps](first-steps) to start using TrustGraph
3. Explore [Concepts](concepts) to understand TrustGraph architecture
