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

{% include decisions/decision-section-start.html
   border_color="#48bb78"
   bg_color="#1e3a2a"
   emoji="🚀"
   title="I just want to try it out"
   description="Simple standalone deployment that runs locally. Doesn't need a lot of planning or resources to be set up."
%}

{% capture docker_best_for %}
<li>First time trying TrustGraph</li>
<li>Learning and experimentation</li>
<li>Local development</li>
{% endcapture %}

{% capture docker_requirements %}
<li>8GB RAM, 4 CPU cores</li>
<li>Docker or Podman installed</li>
<li>20GB disk space</li>
{% endcapture %}

{% include decisions/decision-option-card.html
   border_color="#48bb78"
   bg_color="#0d2118"
   text_color="#d4f4dd"
   title="Option 1: Docker/Podman Compose"
   description="The easiest way to get started. Run TrustGraph locally in 15-30 minutes."
   best_for=docker_best_for
   list2_title="Requirements"
   list2_items=docker_requirements
   link="compose"
   button_bg="#48bb78"
   button_text="#0d2118"
%}

{% capture minikube_best_for %}
<li>Learning Kubernetes</li>
<li>Testing K8s configurations</li>
<li>Production-like environment locally</li>
{% endcapture %}

{% capture minikube_requirements %}
<li>16GB RAM, 8 CPU cores</li>
<li>Minikube and kubectl installed</li>
<li>50GB disk space</li>
{% endcapture %}

{% include decisions/decision-option-card.html
   border_color="#48bb78"
   bg_color="#0d2118"
   text_color="#d4f4dd"
   title="Option 2: Minikube"
   description="Run TrustGraph in a local Kubernetes cluster. Great for learning Kubernetes."
   best_for=minikube_best_for
   list2_title="Requirements"
   list2_items=minikube_requirements
   link="minikube"
   button_bg="#48bb78"
   button_text="#0d2118"
%}

{% include decisions/decision-section-end.html %}

{% include decisions/decision-section-start.html
   border_color="#4a9eff"
   bg_color="#1e2a3a"
   emoji="🇪🇺"
   title="I need to use a European Cloud"
   description="Deploy on European cloud providers with GDPR compliance and EU data residency. Keep your data within European borders for regulatory compliance and data sovereignty."
%}

{% capture ovh_best_for %}
<li>European data sovereignty</li>
<li>No egress fees</li>
<li>Multi-region deployments</li>
{% endcapture %}

{% capture ovh_features %}
<li>GDPR native compliance</li>
<li>40+ data centers worldwide</li>
<li>Anti-DDoS included</li>
{% endcapture %}

{% include decisions/decision-option-card.html
   border_color="#4a9eff"
   bg_color="#0d1621"
   text_color="#e8f4fd"
   title="Option 1: OVHcloud"
   description="Europe's largest cloud provider with Managed Kubernetes and AI Endpoints."
   best_for=ovh_best_for
   list2_title="Key features"
   list2_items=ovh_features
   link="ovhcloud"
   button_bg="#4a9eff"
   button_text="#0d1621"
%}

{% capture scaleway_best_for %}
<li>Budget-conscious deployments</li>
<li>GDPR compliance</li>
<li>Open source commitment</li>
{% endcapture %}

{% capture scaleway_features %}
<li>EU-based infrastructure</li>
<li>Competitive pricing</li>
<li>Mistral AI integration</li>
{% endcapture %}

{% include decisions/decision-option-card.html
   border_color="#4a9eff"
   bg_color="#0d1621"
   text_color="#e8f4fd"
   title="Option 2: Scaleway"
   description="Cost-effective European cloud with Kubernetes Kapsule and Generative AI services."
   best_for=scaleway_best_for
   list2_title="Key features"
   list2_items=scaleway_features
   link="scaleway"
   button_bg="#4a9eff"
   button_text="#0d1621"
%}

{% include decisions/decision-section-end.html
   info_label="💡 Data Sovereignty"
   info_text="Both providers ensure your data remains within EU boundaries, meeting strict European data protection regulations including GDPR. This is essential for organizations handling EU citizen data or operating under EU regulatory frameworks."
   info_bg="rgba(74, 158, 255, 0.1)"
   info_border="#4a9eff"
%}

{% include decisions/decision-section-start.html
   border_color="#9f7aea"
   bg_color="#2d2642"
   emoji="☁️"
   title="I need a global cloud provider"
   description="Deploy on major global cloud platforms with enterprise-grade infrastructure, high availability, and comprehensive managed services."
%}

{% capture aws_best_for %}
<li>AWS-committed organizations</li>
<li>High availability requirements</li>
<li>Enterprise production</li>
{% endcapture %}

{% capture aws_features %}
<li>AWS Bedrock integration</li>
<li>RKE2 security hardening</li>
<li>Auto-scaling support</li>
{% endcapture %}

{% include decisions/decision-option-card.html
   border_color="#9f7aea"
   bg_color="#1a1529"
   text_color="#e9d5ff"
   title="Option 1: AWS RKE"
   description="Production-ready RKE2 Kubernetes cluster on AWS with Bedrock AI integration."
   best_for=aws_best_for
   list2_title="Key features"
   list2_items=aws_features
   link="aws-rke"
   button_bg="#9f7aea"
   button_text="#1a1529"
%}

{% capture azure_best_for %}
<li>Microsoft ecosystem integration</li>
<li>Enterprise Azure deployments</li>
<li>Azure Active Directory</li>
{% endcapture %}

{% capture azure_features %}
<li>Phi-4 and GPT-4o support</li>
<li>Azure AI Foundry</li>
<li>Managed Kubernetes</li>
{% endcapture %}

{% include decisions/decision-option-card.html
   border_color="#9f7aea"
   bg_color="#1a1529"
   text_color="#e9d5ff"
   title="Option 2: Azure AKS"
   description="Managed Kubernetes on Azure with AI Foundry and dual AI model support."
   best_for=azure_best_for
   list2_title="Key features"
   list2_items=azure_features
   link="azure"
   button_bg="#9f7aea"
   button_text="#1a1529"
%}

{% capture gcp_best_for %}
<li>ML/AI-focused projects</li>
<li>VertexAI integration</li>
<li>Google technology stack</li>
{% endcapture %}

{% capture gcp_features %}
<li>VertexAI Gemini Flash 1.5</li>
<li>GKE managed Kubernetes</li>
<li>Free credits available</li>
{% endcapture %}

{% include decisions/decision-option-card.html
   border_color="#9f7aea"
   bg_color="#1a1529"
   text_color="#e9d5ff"
   title="Option 3: Google Cloud Platform"
   description="GKE deployment with VertexAI Gemini integration and ML/AI optimization."
   best_for=gcp_best_for
   list2_title="Key features"
   list2_items=gcp_features
   link="gcp"
   button_bg="#9f7aea"
   button_text="#1a1529"
%}

{% include decisions/decision-section-end.html
   info_label="💡 Enterprise Features"
   info_text="All global cloud providers offer high availability, auto-scaling, enterprise support, and comprehensive managed services. Choose based on your existing cloud commitments and AI service preferences."
   info_bg="rgba(159, 122, 234, 0.1)"
   info_border="#9f7aea"
%}

{% include decisions/decision-section-start.html
   border_color="#f59e0b"
   bg_color="#3a2e1e"
   emoji="🏢"
   title="I want to self-host"
   description="Deploy on your own infrastructure with complete control over hardware, data, and operations. Perfect for high-performance requirements and maximum data sovereignty."
%}

{% capture intel_best_for %}
<li>GPU-accelerated workloads</li>
<li>Large model inference (70B+)</li>
<li>High-performance computing</li>
{% endcapture %}

{% capture intel_features %}
<li>Intel GPU/Gaudi optimization</li>
<li>Llama 3.3 70B support</li>
<li>vLLM and TGI servers</li>
{% endcapture %}

{% include decisions/decision-option-card.html
   border_color="#f59e0b"
   bg_color="#221a10"
   text_color="#fef3c7"
   title="Option 1: Intel Gaudi"
   description="High-performance AI deployment with Intel Gaudi and GPU accelerators for large models."
   best_for=intel_best_for
   list2_title="Key features"
   list2_items=intel_features
   link="intel"
   button_bg="#f59e0b"
   button_text="#221a10"
%}

{% include decisions/decision-section-end.html
   info_label="💡 Self-Hosting Benefits"
   info_text="Complete control over your data and infrastructure, no vendor lock-in, and the ability to optimize for your specific hardware. Ideal for organizations with strict data governance requirements or specialized performance needs."
   info_bg="rgba(245, 158, 11, 0.1)"
   info_border="#f59e0b"
%}
