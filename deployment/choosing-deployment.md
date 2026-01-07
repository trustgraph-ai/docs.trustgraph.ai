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

<div style="border: 2px solid #f59e0b; background-color: #3a2e1e; padding: 15px 20px; margin: 20px 0; border-radius: 8px;">

<h2 style="margin-top: 0;">🏢 I want to self-host</h2>

<p style="margin-bottom: 15px; opacity: 0.9;">Deploy on your own infrastructure with complete control over hardware, data, and operations. Perfect for high-performance requirements and maximum data sovereignty.</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 15px;">

<div style="border: 1px solid #f59e0b; background-color: #221a10; padding: 15px; border-radius: 4px;">
<h3 style="margin-top: 0; color: #fef3c7;">Option 1: Intel Gaudi</h3>
<p style="margin: 10px 0; font-size: 0.95em; opacity: 0.9;">High-performance AI deployment with Intel Gaudi and GPU accelerators for large models.</p>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Best for:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>GPU-accelerated workloads</li>
<li>Large model inference (70B+)</li>
<li>High-performance computing</li>
</ul>
<p style="margin: 10px 0; font-size: 0.9em;"><strong>Key features:</strong></p>
<ul style="margin: 5px 0; padding-left: 20px; font-size: 0.9em;">
<li>Intel GPU/Gaudi optimization</li>
<li>Llama 3.3 70B support</li>
<li>vLLM and TGI servers</li>
</ul>
<a href="intel" style="display: inline-block; margin-top: 10px; padding: 8px 16px; background-color: #f59e0b; color: #221a10; text-decoration: none; border-radius: 4px; font-weight: bold;">Get Started →</a>
</div>

</div>

<p style="margin-top: 15px; padding: 10px; background-color: rgba(245, 158, 11, 0.1); border-left: 3px solid #f59e0b; border-radius: 4px; font-size: 0.9em;">
<strong>💡 Self-Hosting Benefits:</strong> Complete control over your data and infrastructure, no vendor lock-in, and the ability to optimize for your specific hardware. Ideal for organizations with strict data governance requirements or specialized performance needs.
</p>

</div>
