---
title: Choosing a Deployment
nav_order: 1
parent: Deployment
review_date: 2026-01-08
---

# Choosing a Deployment Option

**Decision guide to help you select the right deployment method for your needs**

## Quick Decision Tree

```
Are you just trying TrustGraph for the first time?
├─ YES → Docker Compose (15 minutes)
└─ NO ↓
   Is this for production use?
   ├─ NO (dev/test) ↓
   │  ├─ Need Kubernetes? → Minikube
   │  └─ Simple setup? → Docker Compose
   └─ YES (production) ↓
      Do you need high availability and scaling?
      ├─ NO (small scale) ↓
      │  ├─ Scaleway, OVHcloud, AWS EC2, GCP, Azure
      │  └─ Elsewhere? → Docker Compose
      └─ YES (enterprise scale) ↓
         Which cloud are you using?
         ├─ Need GPU acceleration? → Use cloud-hosted GPU + vLLM
         ├─ Model-as-a-service? → Scaleway, OVHcloud
         ├─ AWS → AWS RKE
         ├─ Azure → Azure AKS
         └─ GCP → Google Cloud Platform
```

## Comparison Matrix

### By Use Case

| Deployment | First Try | Dev/Test | Small Prod | Enterprise | GPU Workloads |
|------------|-----------|----------|------------|------------|---------------|
| **Docker Compose** | ✅ Best | ✅ Great | ⚠️ Limited | ❌ No | ❌ No |
| **Minikube** | ⚠️ Complex | ✅ Great | ❌ No | ❌ No | ❌ No |
| **AWS EC2** | ❌ Slow | ✅ Good | ✅ Good | ⚠️ Limited | ❌ No |
| **AWS RKE** | ❌ Complex | ⚠️ Costly | ✅ Good | ✅ Best | ⚠️ Possible |
| **Azure AKS** | ❌ Complex | ⚠️ Costly | ✅ Good | ✅ Best | ⚠️ Possible |
| **GCP** | ❌ Complex | ✅ Good | ✅ Good | ✅ Best | ✅ Great |
| **Intel/Tiber** | ❌ Complex | ⚠️ Specialty | ✅ Good | ✅ Good | ✅ Best |
| **Scaleway** | ❌ Complex | ✅ Good | ✅ Good | ⚠️ Limited | ❌ No |

### By Technical Requirements

| Deployment | Setup Time | Complexity | HA Support | Auto-Scale | Cost |
|------------|------------|------------|------------|------------|------|
| **Docker Compose** | 15 min | Low | ❌ | ❌ | Free |
| **Minikube** | 30 min | Medium | ❌ | ❌ | Free |
| **AWS EC2** | 1 hour | Low | ❌ | ❌ | € |
| **AWS RKE** | 2-3 hours | High | ✅ | ✅ | €€€ |
| **Azure AKS** | 2-3 hours | High | ✅ | ✅ | €€€ |
| **GCP** | 2-3 hours | High | ✅ | ✅ | €€ |
| **Intel/Tiber** | 2-4 hours | High | ✅ | ✅ | €€-€€€ |
| **Scaleway** | 2-3 hours | Medium | ✅ | ✅ | € |

**Legend**:
- ✅ = Excellent support
- ⚠️ = Limited or conditional
- ❌ = Not supported
- € = Low cost, €€ = Medium, €€€ = High

## Detailed Deployment Profiles

### Docker Compose

**Best for**: First-time users, POCs, local development, small teams

**Strengths**:
- ✅ Fastest setup (15 minutes)
- ✅ Simplest architecture
- ✅ Easy to tear down and restart
- ✅ No cloud costs
- ✅ Complete control

**Limitations**:
- ❌ Single machine only
- ❌ No automatic scaling
- ❌ No built-in HA
- ❌ Manual backup/restore

**Resource Requirements**:
- 8GB RAM minimum
- 4 CPU cores minimum
- 20GB disk space
- Docker or Podman

**When to choose**:
- First time trying TrustGraph
- Local development
- Small document sets (<10k documents)
- Budget constraints
- Learning and experimentation

**Migration path**: Can export data and migrate to cloud deployments later.

---

### Minikube

**Best for**: Kubernetes learning, K8s deployment testing

**Strengths**:
- ✅ Real Kubernetes environment
- ✅ Test K8s manifests locally
- ✅ Good for learning
- ✅ No cloud costs

**Limitations**:
- ❌ Single node
- ❌ Resource intensive
- ❌ Not for production
- ❌ Complex setup

**Resource Requirements**:
- 16GB RAM recommended
- 8 CPU cores recommended
- 50GB disk space
- Minikube, kubectl

**When to choose**:
- Learning Kubernetes
- Testing K8s deployments before cloud
- Validating manifests
- K8s-based development workflow

---

### AWS EC2 Single Instance

**Best for**: Simple AWS deployments, small production workloads

**Strengths**:
- ✅ Simple AWS deployment
- ✅ Cost-effective for small scale
- ✅ Easy to manage
- ✅ AWS integration

**Limitations**:
- ❌ No automatic scaling
- ❌ Single point of failure
- ❌ Limited to instance size
- ⚠️ Manual backup required

**Resource Requirements**:
- t3.xlarge or larger
- 50GB+ EBS volume
- Security groups configured
- AWS account

**When to choose**:
- Small AWS deployments
- <100 concurrent users
- Development/staging on AWS
- Simple operational model
- Cost-conscious production

**Cost estimate**: $100-200/month for t3.xlarge

---

### AWS RKE (Production Kubernetes)

**Best for**: Enterprise AWS deployments, high availability

**Strengths**:
- ✅ Full HA support
- ✅ Auto-scaling
- ✅ Production-grade
- ✅ AWS managed services integration
- ✅ RKE2 security hardening

**Limitations**:
- ⚠️ Complex setup
- ⚠️ Higher cost
- ⚠️ Requires K8s expertise
- ⚠️ Operational overhead

**Resource Requirements**:
- Multiple EC2 instances
- RDS, EBS, ELB
- VPC configuration
- Terraform knowledge helpful

**When to choose**:
- Production deployments on AWS
- Need high availability
- Scaling requirements
- Compliance requirements
- Enterprise features needed

**Cost estimate**: $500-2000+/month depending on scale

---

### Azure AKS

**Best for**: Azure-committed organizations, enterprise deployments

**Strengths**:
- ✅ Managed Kubernetes
- ✅ Azure integration
- ✅ Enterprise support
- ✅ HA and scaling
- ✅ Azure Active Directory integration

**Limitations**:
- ⚠️ Complex setup
- ⚠️ Higher cost
- ⚠️ Azure vendor lock-in
- ⚠️ Requires K8s expertise

**Resource Requirements**:
- AKS cluster
- Azure Storage
- Load balancers
- Azure account

**When to choose**:
- Already on Azure
- Enterprise Azure commitment
- Need Microsoft support
- Azure service integration

**Cost estimate**: $500-2000+/month

---

### Google Cloud Platform

**Best for**: GCP users, ML/AI workloads, VertexAI integration

**Strengths**:
- ✅ GKE managed Kubernetes
- ✅ VertexAI integration
- ✅ ML/AI optimized
- ✅ Free credits available
- ✅ Good for AI projects

**Limitations**:
- ⚠️ Complex setup
- ⚠️ GCP vendor lock-in
- ⚠️ Requires K8s expertise

**Resource Requirements**:
- GKE cluster
- Cloud Storage
- Load balancers
- GCP account

**When to choose**:
- Already on GCP
- Using VertexAI for LLMs
- ML/AI focused projects
- Google technology stack

**Cost estimate**: $400-1800+/month (free credits help)

---

### Intel / Tiber Cloud

**Best for**: GPU-accelerated workloads, high-performance computing

**Strengths**:
- ✅ GPU acceleration
- ✅ Intel optimizations
- ✅ High performance
- ✅ Specialized hardware

**Limitations**:
- ⚠️ Complex setup
- ⚠️ Specialized platform
- ⚠️ Variable pricing

**Resource Requirements**:
- Intel GPU instances
- Specialized configuration
- Intel platform familiarity

**When to choose**:
- Need GPU acceleration
- High-performance requirements
- Large-scale processing
- Intel hardware preference

**Cost estimate**: Variable, contact for pricing

---

### Scaleway

**Best for**: Budget-conscious deployments, EU data residency

**Strengths**:
- ✅ Lower cost than major clouds
- ✅ European data centers
- ✅ GDPR compliance
- ✅ Kubernetes support

**Limitations**:
- ⚠️ Smaller ecosystem
- ⚠️ Less mature than major clouds
- ⚠️ Limited regions

**Resource Requirements**:
- Scaleway Kubernetes
- Object storage
- Load balancers
- Scaleway account

**When to choose**:
- Budget constraints
- EU data residency required
- European operations
- Cost-effective scaling

**Cost estimate**: $200-1000+/month

---

## Decision Factors

### By Scale

**<1,000 documents**:
- Docker Compose (local)
- AWS EC2 Single (cloud)

**1,000 - 50,000 documents**:
- Docker Compose (powerful machine)
- AWS EC2 Single Instance
- Scaleway

**50,000 - 500,000 documents**:
- AWS RKE
- Azure AKS
- GCP
- Scaleway

**500,000+ documents**:
- AWS RKE (with scaling)
- Azure AKS (with scaling)
- GCP (with scaling)
- Intel/Tiber (with GPU)

### By Budget

**$0 (free)**:
- Docker Compose
- Minikube

**<$200/month**:
- AWS EC2 Single Instance
- Scaleway (small)

**$200-1000/month**:
- Scaleway (medium)
- GCP (with free credits)
- AWS RKE (minimal)

**$1000+/month**:
- AWS RKE (production)
- Azure AKS (production)
- GCP (production)
- Intel/Tiber

### By Team Expertise

**Beginner**:
- Docker Compose

**Intermediate**:
- AWS EC2 Single Instance
- Minikube
- Scaleway

**Advanced**:
- AWS RKE
- Azure AKS
- GCP
- Intel/Tiber

## Migration Paths

### From Docker Compose to Cloud

1. Export your data using backup tools
2. Set up cloud deployment
3. Import data to cloud instance
4. Validate and cutover

### From Single Instance to Kubernetes

1. Move to managed K8s (AKS, GKE, or RKE)
2. Use Kubernetes manifests
3. Implement HA and scaling
4. Migrate data

### Between Cloud Providers

1. Export knowledge graphs and configurations
2. Deploy to new cloud
3. Import data
4. Reconfigure integrations

## Next Steps

### Ready to Deploy?

1. **Selected your option?** → Go to the specific deployment guide
2. **Still unsure?** → Start with [Docker Compose](docker-compose) to try it out
3. **Need help deciding?** → Ask in [community support](../contributing/getting-help)

### Before Production

Review these critical guides:
- [Production Considerations](production-considerations) - HA, monitoring, backups
- [Security Guide](../guides/security/) - Authentication and encryption (Phase 4)
- [Troubleshooting](troubleshooting) - Common issues

### Get Started

- **[Docker Compose](docker-compose)** - Quickest way to start
- **[Deployment Index](index)** - All deployment options
- **[Getting Started](../getting-started/)** - Complete beginner guide
