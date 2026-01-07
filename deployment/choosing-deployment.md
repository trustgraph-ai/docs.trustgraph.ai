---
title: Choosing a Deployment
nav_order: 1
parent: Deployment
review_date: 2026-01-08
guide_category:
  - Deployment decisions
guide_category_order: 1
guide_description: Decision guide to help you select the right deployment method for your needs
guide_difficulty: beginner
guide_time: 10 min
guide_emoji: 🤔
guide_banner: /../choosing-deployment.jpg
guide_labels:
  - Planning
  - Decision Guide
  - Getting Started
---

# Choosing a Deployment Option

**Decision guide to help you select the right deployment method for your needs**

<div style="border: 2px solid #48bb78; background-color: #1e3a2a; padding: 15px 20px; margin: 20px 0; border-radius: 8px;">

<h2 style="margin-top: 0;">🚀 I just want to try it out</h2>

<p style="margin-bottom: 15px; opacity: 0.9;">Simple standalone deployment that runs locally. Doesn't need a lot of planning or resources to be set up.</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 15px;">

<div style="border: 1px solid #48bb78; background-color: #0d2118; padding: 15px; border-radius: 4px;">
<h3 style="margin-top: 0; color: #d4f4dd;">Option 1: Docker Compose</h3>
<p style="margin: 10px 0; font-size: 0.95em; opacity: 0.9;">The easiest way to get started. Run TrustGraph locally in 15-30 minutes.</p>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Best for:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>First time trying TrustGraph</li>
<li>Learning and experimentation</li>
<li>Local development</li>
</ul>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Requirements:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>8GB RAM, 4 CPU cores</li>
<li>Docker or Podman installed</li>
<li>20GB disk space</li>
</ul>
<a href="docker-compose" style="display: inline-block; margin-top: 10px; padding: 8px 16px; background-color: #48bb78; color: #0d2118; text-decoration: none; border-radius: 4px; font-weight: bold;">Get Started →</a>
</div>

<div style="border: 1px solid #48bb78; background-color: #0d2118; padding: 15px; border-radius: 4px;">
<h3 style="margin-top: 0; color: #d4f4dd;">Option 2: Minikube</h3>
<p style="margin: 10px 0; font-size: 0.95em; opacity: 0.9;">Run TrustGraph in a local Kubernetes cluster. Great for learning Kubernetes.</p>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Best for:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>Learning Kubernetes</li>
<li>Testing K8s configurations</li>
<li>Production-like environment locally</li>
</ul>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Requirements:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>16GB RAM, 8 CPU cores</li>
<li>Minikube and kubectl installed</li>
<li>50GB disk space</li>
</ul>
<a href="minikube" style="display: inline-block; margin-top: 10px; padding: 8px 16px; background-color: #48bb78; color: #0d2118; text-decoration: none; border-radius: 4px; font-weight: bold;">Get Started →</a>
</div>

</div>

</div>

<div style="border: 2px solid #4a9eff; background-color: #1e2a3a; padding: 15px 20px; margin: 20px 0; border-radius: 8px;">

<h2 style="margin-top: 0;">🇪🇺 I need to use a European Cloud</h2>

<p style="margin-bottom: 15px; opacity: 0.9;">Deploy on European cloud providers with GDPR compliance and EU data residency. Keep your data within European borders for regulatory compliance and data sovereignty.</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 15px;">

<div style="border: 1px solid #4a9eff; background-color: #0d1621; padding: 15px; border-radius: 4px;">
<h3 style="margin-top: 0; color: #e8f4fd;">Option 1: OVHcloud</h3>
<p style="margin: 10px 0; font-size: 0.95em; opacity: 0.9;">Europe's largest cloud provider with Managed Kubernetes and AI Endpoints.</p>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Best for:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>European data sovereignty</li>
<li>No egress fees</li>
<li>Multi-region deployments</li>
</ul>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Key features:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>GDPR native compliance</li>
<li>40+ data centers worldwide</li>
<li>Anti-DDoS included</li>
</ul>
<a href="ovhcloud" style="display: inline-block; margin-top: 10px; padding: 8px 16px; background-color: #4a9eff; color: #0d1621; text-decoration: none; border-radius: 4px; font-weight: bold;">Get Started →</a>
</div>

<div style="border: 1px solid #4a9eff; background-color: #0d1621; padding: 15px; border-radius: 4px;">
<h3 style="margin-top: 0; color: #e8f4fd;">Option 2: Scaleway</h3>
<p style="margin: 10px 0; font-size: 0.95em; opacity: 0.9;">Cost-effective European cloud with Kubernetes Kapsule and Generative AI services.</p>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Best for:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>Budget-conscious deployments</li>
<li>GDPR compliance</li>
<li>Open source commitment</li>
</ul>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Key features:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>EU-based infrastructure</li>
<li>Competitive pricing</li>
<li>Mistral AI integration</li>
</ul>
<a href="scaleway" style="display: inline-block; margin-top: 10px; padding: 8px 16px; background-color: #4a9eff; color: #0d1621; text-decoration: none; border-radius: 4px; font-weight: bold;">Get Started →</a>
</div>

</div>

<p style="margin-top: 15px; padding: 10px; background-color: rgba(74, 158, 255, 0.1); border-left: 3px solid #4a9eff; border-radius: 4px; font-size: 0.9em;">
<strong>💡 Data Sovereignty:</strong> Both providers ensure your data remains within EU boundaries, meeting strict European data protection regulations including GDPR. This is essential for organizations handling EU citizen data or operating under EU regulatory frameworks.
</p>

</div>

<div style="border: 2px solid #9f7aea; background-color: #2d2642; padding: 15px 20px; margin: 20px 0; border-radius: 8px;">

<h2 style="margin-top: 0;">☁️ I need a global cloud provider</h2>

<p style="margin-bottom: 15px; opacity: 0.9;">Deploy on major global cloud platforms with enterprise-grade infrastructure, high availability, and comprehensive managed services.</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 15px;">

<div style="border: 1px solid #9f7aea; background-color: #1a1529; padding: 15px; border-radius: 4px;">
<h3 style="margin-top: 0; color: #e9d5ff;">Option 1: AWS RKE</h3>
<p style="margin: 10px 0; font-size: 0.95em; opacity: 0.9;">Production-ready RKE2 Kubernetes cluster on AWS with Bedrock AI integration.</p>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Best for:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>AWS-committed organizations</li>
<li>High availability requirements</li>
<li>Enterprise production</li>
</ul>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Key features:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>AWS Bedrock integration</li>
<li>RKE2 security hardening</li>
<li>Auto-scaling support</li>
</ul>
<a href="aws-rke" style="display: inline-block; margin-top: 10px; padding: 8px 16px; background-color: #9f7aea; color: #1a1529; text-decoration: none; border-radius: 4px; font-weight: bold;">Get Started →</a>
</div>

<div style="border: 1px solid #9f7aea; background-color: #1a1529; padding: 15px; border-radius: 4px;">
<h3 style="margin-top: 0; color: #e9d5ff;">Option 2: Azure AKS</h3>
<p style="margin: 10px 0; font-size: 0.95em; opacity: 0.9;">Managed Kubernetes on Azure with AI Foundry and dual AI model support.</p>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Best for:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>Microsoft ecosystem integration</li>
<li>Enterprise Azure deployments</li>
<li>Azure Active Directory</li>
</ul>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Key features:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>Phi-4 and GPT-4o support</li>
<li>Azure AI Foundry</li>
<li>Managed Kubernetes</li>
</ul>
<a href="azure" style="display: inline-block; margin-top: 10px; padding: 8px 16px; background-color: #9f7aea; color: #1a1529; text-decoration: none; border-radius: 4px; font-weight: bold;">Get Started →</a>
</div>

<div style="border: 1px solid #9f7aea; background-color: #1a1529; padding: 15px; border-radius: 4px;">
<h3 style="margin-top: 0; color: #e9d5ff;">Option 3: Google Cloud Platform</h3>
<p style="margin: 10px 0; font-size: 0.95em; opacity: 0.9;">GKE deployment with VertexAI Gemini integration and ML/AI optimization.</p>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Best for:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>ML/AI-focused projects</li>
<li>VertexAI integration</li>
<li>Google technology stack</li>
</ul>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Key features:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>VertexAI Gemini Flash 1.5</li>
<li>GKE managed Kubernetes</li>
<li>Free credits available</li>
</ul>
<a href="gcp" style="display: inline-block; margin-top: 10px; padding: 8px 16px; background-color: #9f7aea; color: #1a1529; text-decoration: none; border-radius: 4px; font-weight: bold;">Get Started →</a>
</div>

</div>

<p style="margin-top: 15px; padding: 10px; background-color: rgba(159, 122, 234, 0.1); border-left: 3px solid #9f7aea; border-radius: 4px; font-size: 0.9em;">
<strong>💡 Enterprise Features:</strong> All global cloud providers offer high availability, auto-scaling, enterprise support, and comprehensive managed services. Choose based on your existing cloud commitments and AI service preferences.
</p>

</div>

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
