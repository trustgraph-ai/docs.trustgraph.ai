---
title: Deployment
nav_order: 4
has_children: true
parent: TrustGraph Documentation
review_date: 2025-12-29
---

# Deployment Guide

**Deploy and operate TrustGraph across different environments**

## What's in This Section?

This section provides **platform-specific deployment instructions** for running TrustGraph in various environments, from local development to production cloud deployments.

### This Section is For:
- **DevOps engineers** deploying TrustGraph infrastructure
- **System administrators** managing TrustGraph instances
- **Developers** setting up local development environments
- **Architects** planning production deployments

### Not What You Need?
- **First time user?** → Start with [Quick Start](../getting-started/quickstart)
- **Understanding concepts?** → See [Overview](../overview/)
- **Looking for how-tos?** → Check [Guides](../guides/)

## Choosing Your Deployment

Not sure which deployment option fits your needs? See **[Choosing a Deployment](choosing-deployment)** for a decision guide with comparison tables and recommendations.

### Quick Decision Guide

| Your Situation | Recommended Option |
|----------------|-------------------|
| First time trying TrustGraph | [Docker Compose](docker-compose) |
| Local development & testing | [Docker Compose](docker-compose) or [Minikube](minikube) |
| Learning Kubernetes | [Minikube](minikube) |
| Small production (<100 users) | [AWS EC2 Single Instance](aws-ec2) or [Docker Compose](docker-compose) |
| Production with scaling needs | [AWS RKE](aws-rke), [Azure AKS](azure), or [GCP](gcp) |
| GPU acceleration required | [Intel/Tiber Cloud](intel) |
| Budget-conscious cloud | [Scaleway](scaleway) |

## Deployment Options

### Local Development

Perfect for testing, development, and evaluation.

#### [Docker Compose](docker-compose)
**Easiest way to get started** - Deploy TrustGraph locally with all services orchestrated.

- ✅ **Best for**: First-time users, POCs, local development
- ✅ **Pros**: Simple setup, all-in-one, easy to tear down
- ⚠️ **Limits**: Single machine, not for production scale
- **Time to deploy**: 15 minutes
- **Prerequisites**: Docker/Podman, 8GB RAM, 4 CPU cores

#### [Minikube](minikube)
**Local Kubernetes** - Run TrustGraph on Kubernetes locally.

- ✅ **Best for**: Learning K8s, testing K8s deployments
- ✅ **Pros**: Real Kubernetes environment, good for learning
- ⚠️ **Limits**: Single node, resource intensive
- **Time to deploy**: 30 minutes
- **Prerequisites**: Minikube, kubectl, 16GB RAM recommended

### Cloud Platforms

Production-ready deployments with scalability.

#### [AWS (Amazon Web Services)](aws-rke)
**Production AWS with RKE2** - Enterprise-ready deployment on AWS.

- ✅ **Best for**: Production deployments, enterprise scale
- ✅ **Pros**: High availability, auto-scaling, managed services
- 💰 **Cost**: Medium to high (depends on resources)
- **Time to deploy**: 2-3 hours
- **Also see**: [AWS EC2 Single Instance](aws-ec2) for simpler development setup

#### [Azure AKS](azure)
**Microsoft Azure Kubernetes** - Deploy on Azure with AKS.

- ✅ **Best for**: Azure-committed organizations
- ✅ **Pros**: Azure integration, managed K8s, enterprise support
- 💰 **Cost**: Medium to high
- **Time to deploy**: 2-3 hours

#### [Google Cloud Platform](gcp)
**GCP deployment** - Run TrustGraph on Google Cloud.

- ✅ **Best for**: GCP users, ML/AI workloads
- ✅ **Pros**: VertexAI integration, GKE, good for AI projects
- 💰 **Cost**: Medium (free credits available)
- **Time to deploy**: 2-3 hours

#### [Intel / Tiber Cloud](intel)
**GPU-accelerated** - High-performance with Intel GPU acceleration.

- ✅ **Best for**: GPU workloads, high-performance needs
- ✅ **Pros**: Hardware acceleration, optimized for Intel
- 💰 **Cost**: Variable
- **Time to deploy**: 2-4 hours

#### [Scaleway](scaleway)
**Budget-friendly European cloud** - Cost-effective cloud deployment.

- ✅ **Best for**: Budget-conscious deployments, EU data residency
- ✅ **Pros**: Lower cost, European data centers
- 💰 **Cost**: Lower than major clouds
- **Time to deploy**: 2-3 hours

#### [AWS EC2 Single Instance](aws-ec2)
**Simple AWS setup** - Single EC2 instance for development/testing.

- ✅ **Best for**: Development, small-scale testing on AWS
- ✅ **Pros**: Simple, cost-effective for development
- ⚠️ **Limits**: Not for production scale
- 💰 **Cost**: Low
- **Time to deploy**: 1 hour

## Production Considerations

### Before Going to Production

Review these critical resources:

1. **[Production Considerations](production-considerations)** - HA, monitoring, backups, disaster recovery
2. **[Security Guide](../guides/security/)** - Authentication, encryption, access control (Phase 4)
3. **[Choosing a Deployment](choosing-deployment)** - Detailed comparison and requirements

### Production Checklist

- [ ] High availability configured
- [ ] Monitoring and alerting set up
- [ ] Backup strategy implemented
- [ ] Security hardening completed
- [ ] Resource sizing validated
- [ ] Disaster recovery plan tested
- [ ] Performance benchmarks established
- [ ] Documentation for operations team

## Troubleshooting

### Common Issues

See **[Troubleshooting Guide](troubleshooting)** for solutions to common deployment problems:
- Container startup failures
- Network connectivity issues
- Resource constraints
- Configuration errors
- Service dependencies

### Getting Help

- **[Troubleshooting Guide](troubleshooting)** - Detailed problem-solving
- **[Getting Help](../contributing/getting-help)** - Community support
- **[GitHub Issues](https://github.com/trustgraph-ai/trustgraph/issues)** - Report bugs

## Deployment Architecture

### Components

TrustGraph deployments typically include:

- **Processing Services**: Document processing, entity extraction, GraphRAG
- **Storage Layer**: Graph database (Cassandra), vector store (Qdrant)
- **Message Queue**: Apache Pulsar for service communication
- **LLM Integration**: Connection to local or cloud LLMs
- **Web Interface**: TrustGraph Workbench
- **Monitoring**: Grafana dashboards (optional but recommended)

### Network Requirements

- **Internal**: Service-to-service communication
- **External**: API access, web interface
- **LLM Access**: Outbound to cloud LLMs or local model access
- **Storage**: Persistent volumes for databases

## Next Steps

### Just Starting?
1. Try [Docker Compose](docker-compose) locally
2. Load sample data: [Getting Started](../getting-started/quickstart)
3. Explore features: [How-to Guides](../guides/)

### Planning Production?
1. Read [Choosing a Deployment](choosing-deployment)
2. Review [Production Considerations](production-considerations)
3. Set up monitoring and security
4. Select your cloud platform guide above

### Need Help?
- Check [Troubleshooting](troubleshooting) for common issues
- Visit [Getting Help](../contributing/getting-help) for support options
