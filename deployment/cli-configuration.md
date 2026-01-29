---
title: CLI Configuration Tool
nav_order: 2
parent: Deployment
review_date: 2026-01-29
guide_category:
  - Deployment fundamentals
guide_category_order: 2
guide_description: Generate TrustGraph deployment configurations from the command line without using a browser
guide_difficulty: beginner
guide_time: 10 min
guide_emoji: ⌨️
guide_banner: cli-config.jpg
guide_labels:
  - CLI
  - Configuration
  - Quick Start
---

# CLI Configuration Tool

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>Node.js and npm installed</li>
<li>Basic command-line familiarity</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Generate a complete TrustGraph deployment configuration by answering a series of questions in your terminal."
%}

## Overview

Elsewhere we describe how to use the Configuration Portal to build your
TrustGraph deployment configuration.  This page describes the same thing in
command-line form.  This is an optional guide - if you're happy with the
browser experience you can stick with that.

The TrustGraph CLI Configuration Tool provides the same functionality as the
[TrustGraph Configuration Builder](https://config-ui.demo.trustgraph.ai/)
web interface, but runs entirely in your terminal. Answer around a dozen
questions about your deployment preferences and the tool generates a complete
configuration bundle ready to deploy.

This is useful when:
- You prefer working in a terminal
- You're on a headless server without a browser
- You want to script configuration generation
- You're working in an environment with restricted web access

## Running the Tool

Run the configuration tool using npx:

```bash
npx @trustgraph/config
```

The first time you run it, npm will prompt to install the package:

```
Need to install the following packages:
@trustgraph/config@1.0.0
Ok to proceed? (y)
```

Press `y` to continue. The tool will launch an interactive configuration wizard.

## Configuration Questions

The tool guides you through a series of questions to configure your deployment:

### 1. TrustGraph Version

```
◆  Which TrustGraph version?
│  ○ TrustGraph 2.0
│  ○ TrustGraph 1.9
│  ● TrustGraph 1.8 (Recommended)
│  ○ TrustGraph 1.7
│  ○ TrustGraph 1.6
```

Use the latest stable version (selected by default) unless you want to
experiment with something cutting edge.

{: .note }
Remember the version number you select - you'll need it later when installing
CLI tools to ensure version compatibility.

### 2. Platform

```
◆  Which platform?
│  ● Docker Compose (Recommended)
│  ○ Podman Compose
│  ○ Minikube
│  ○ Google Kubernetes Engine (GKE)
│  ○ AWS EKS
│  ○ Azure AKS
│  ○ Scaleway Kubernetes
│  ○ OVHCloud Kubernetes
```

Choose your deployment platform:

- **Docker Compose** - Easy to install on macOS and Linux. Great for evaluation
  and learning. May not be well suited to production deployments.
- **Podman Compose** - Open-source alternative to Docker with similar ease of use.
- **Minikube** - Local Kubernetes for development and testing.
- **Cloud Kubernetes** - GKE, EKS, AKS, Scaleway, and OVHCloud options for
  production deployments.

### 3. Graph Store

```
◆  Which graph store?
│  ● Apache Cassandra (Recommended)
│  ○ Neo4j
│  ○ Memgraph
│  ○ FalkorDB
```

Cassandra isn't strictly a graph database, but it covers all the functionality
TrustGraph needs - TrustGraph layers a graph schema on top of it. If you have
a preference for one of the dedicated graph databases, use that instead.

### 4. Vector Store

```
◆  Which vector database?
│  ● Qdrant (Recommended)
│  ○ Milvus
│  ○ Pinecone
```

Qdrant is recommended - it offers high requests-per-second, minimal latency,
and fast indexing with accuracy control.

### 5. Object Store

```
◆  Which object store?
│  ● Apache Cassandra
```

Currently there is only one option for object storage. Select Cassandra to continue.

### 6. LLM Provider

{% include llm/llm-providers-overview.md %}

```
◆  How will you run the LLM?
│  ● Ollama (Recommended)
│  ○ Llamafile
│  ○ LM Studio
│  ○ OpenAI
│  ○ Claude (Anthropic)
│  ○ Mistral
│  ○ Cohere
│  ○ Azure AI
│  ○ Azure OpenAI
│  ○ Amazon Bedrock
│  ○ Google AI Studio
│  ○ Vertex AI
│  ○ vLLM
│  ○ Text Generation Inference (TGI)
```

### 7. Maximum Output Tokens

```
◆  Maximum output tokens?
│  4096
```

This sets the maximum number of tokens the LLM can generate in a single
response. Choose based on your hosting capability:

- **2048** - Suitable for low-end or resource-constrained hosting
- **4096** - A good default for medium-capacity setups
- **8192 or more** - For high-compute hosting such as large cloud models

### 8. OCR Processing

```
◆  Enable OCR processing?
│  ○ Yes / ● No
```

The default PDF processing extracts text from PDFs that contain structured
text. If you need to process scanned documents or images, enable OCR
processing. Selecting **Yes** reveals additional options:

```
◆  Which OCR engine?
│  ● PDF Decode (Recommended)
│  ○ Tesseract
│  ○ Mistral
```

- **PDF Decode** - Default configuration for PDFs with structured text (no OCR)
- **Tesseract** - Open-source OCR engine for scanned documents
- **Mistral** - Uses Mistral's vision capabilities for OCR

### 9. Embeddings Engine

```
◆  Configure embeddings engine?
│  ○ Yes / ● No
```

The default embeddings engine is FastEmbed. If you want to use a different
engine, select **Yes** to reveal the options:

```
◆  Which embeddings engine?
│  ● FastEmbed (Recommended)
│  ○ HuggingFace sentence-transformers
│  ○ Ollama
```

- **FastEmbed** - Lightweight, fast Python library for embedding generation
  with a small container image and quick start time
- **HuggingFace sentence-transformers** - Access to a wider range of embedding models
- **Ollama** - Use Ollama for embeddings if you're already running it for your LLM

## Configuration Summary

After answering all questions, the tool displays a summary of your selections:

```
●  Configuration Summary:
│    Which TrustGraph version? TrustGraph 1.8
│    Which platform? Docker Compose
│    Which graph store? Apache Cassandra
│    Which vector database? Qdrant
│    Which object store? Apache Cassandra
│    How will you run the LLM? Ollama
│    Maximum output tokens? 4096
│    Enable OCR processing? No
│    Configure embeddings engine? No
│
◇  Configuration generated
│
◆  Save deployment package as:
│  deploy.zip
```

Review the summary to confirm your choices. Enter a filename for the
deployment package (or accept the default `deploy.zip`) and press Enter.

```
◇  Saved to deploy.zip
│
◇  Installation guide generated
│
◆  Save installation guide as:
│  INSTALLATION.md
```

The tool also generates an installation guide tailored to your configuration.
Enter a filename (or accept the default `INSTALLATION.md`) and press Enter.

```
◇  Saved to INSTALLATION.md
│
└  Done!
```

## Output Files

The tool generates two files:

- **deploy.zip** - A deployment bundle containing your `docker-compose.yaml`
  (or Kubernetes manifests) and configuration files for TrustGraph, Grafana,
  Prometheus, and other components.
- **INSTALLATION.md** - A tailored installation guide with step-by-step
  instructions for your specific configuration.

## Next Steps

1. Read the generated `INSTALLATION.md` for instructions specific to your setup
2. Unpack the deployment bundle and follow the installation guide
3. For additional details, see the platform-specific guides:
   - [Docker/Podman Compose](compose)
   - [Minikube](minikube)
   - [AWS EC2](aws-ec2)
   - [Google Cloud](gcp)
   - [Azure AKS](azure)

