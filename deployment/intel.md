---
title: Intel GPU / Tiber Cloud
nav_order: 3
parent: Deployment
grand_parent: TrustGraph Documentation
review_date: 2025-11-21
---

# Intel Tiber Cloud Deployment

Deploy TrustGraph on Intel Tiber Cloud with Intel GPU and Gaudi accelerated systems for high-performance AI workloads.

## Overview

TrustGraph provides specialized deployment configurations for Intel's advanced hardware platforms, including Intel Tiber Cloud and bare-metal Intel GPU/Gaudi systems. This deployment method is designed for:

- **High-performance AI inference** with Intel accelerators
- **Self-hosted deployments** on Intel hardware
- **Research and development** with cutting-edge Intel AI technologies
- **Enterprise workloads** requiring Intel-optimized performance

⚠️ **Work in Progress**: This deployment method is actively being developed and optimized for Intel's latest hardware platforms.

## What You Get

The Intel Tiber Cloud deployment includes:

- **Intel accelerated systems** (Gaudi, GPU, or GR platforms)
- **Optimized AI inference** with vLLM or TGI servers
- **Large language models** like Llama 3.3 70B
- **Complete TrustGraph stack** deployed via containerization
- **SSH-based deployment** with automated scripts
- **Port forwarding setup** for secure access
- **Monitoring and observability** with Grafana
- **Web workbench** for document processing and Graph RAG

## Intel Hardware Platforms

### Intel Gaudi Systems
- **Software**: TrustGraph 1.0.13 + vLLM (HabanaAI fork)
- **Model**: Llama 3.3 70B
- **Deployment**: `deploy-gaudi-vllm.zip`
- **Optimized for**: AI training and inference workloads

### Intel GPU Multi-GPU 1550 Systems
- **Software**: TrustGraph 1.0.13 + TGI Server 3.3.1-intel-xpu
- **Deployment**: `deploy-gpu-tgi.zip`
- **Optimized for**: High-throughput GPU inference

### Intel GR Systems
- **Software**: TrustGraph 1.0.13 + TGI Server 3.3.1-intel-xpu
- **Deployment**: `deploy-gr.zip`
- **Optimized for**: Specialized Intel AI workloads

## Why Choose Intel Tiber Cloud?

### 🚀 **Cutting-Edge AI Hardware**
- **Intel Gaudi**: Purpose-built for AI training and inference
- **Intel GPU**: High-performance parallel processing
- **Specialized Architecture**: Optimized for AI/ML workloads

### ⚡ **Performance Optimization**
- **Hardware-Accelerated Inference**: Native Intel optimization
- **Large Model Support**: Handle models like Llama 3.3 70B efficiently
- **Reduced Latency**: Direct hardware acceleration

### 🔒 **Self-Hosted Control**
- **Data Sovereignty**: Complete control over data and models
- **Custom Configuration**: Tailor deployments to specific needs
- **Enterprise Security**: Self-hosted infrastructure

### 🛠️ **Developer Access**
- **Research Platform**: Access to latest Intel AI technologies
- **Experimentation**: Test advanced AI configurations
- **Direct Hardware Access**: Low-level optimization capabilities

## Deployment Method

The Intel deployment uses automated deployment scripts that:

- Connect via SSH jump host to Intel Tiber Cloud
- Deploy pre-configured TrustGraph packages
- Set up Intel-optimized AI inference servers
- Configure port forwarding for secure access
- Initialize monitoring and web interfaces

## Quick Process Overview

1. **Obtain access** to Intel Tiber Cloud instance
2. **Create HuggingFace token** and accept model licenses
3. **Choose deployment type** (Gaudi, GPU, or GR)
4. **Deploy via script** with SSH parameters
5. **Connect via SSH** with port forwarding
6. **Access services** through forwarded ports

## Access Configuration

Intel Tiber Cloud uses SSH jump host access:

```bash
# SSH connection format
ssh -J guest@[jump-host] sdp@[target-host]

# Deployment command
./deploy-tiber guest@[jump-host] sdp@[target-host] [deployment-package]

# Port forwarding
./port-forward guest@[jump-host] sdp@[target-host]
```

## Access Points

Once deployed, you'll have access to:

- **TrustGraph API**: Port 8089 (forwarded from 8088)
- **Web Workbench**: Port 8889 (forwarded from 8888)
- **Grafana Monitoring**: Port 3001 (forwarded from 3000)

## Model Support

**Large Language Models**: Llama 3.3 70B and other HuggingFace models
**License Requirements**: HuggingFace account with model access
**Hardware Optimization**: Intel-specific optimizations for inference
**Inference Engines**: vLLM (Gaudi) and TGI (GPU/GR)

## Complete Documentation

For detailed step-by-step instructions, deployment packages, and troubleshooting, visit:

**[TrustGraph Intel Tiber Cloud Guide](https://github.com/trustgraph-ai/trustgraph-tiber-cloud)**

The repository contains:
- Deployment automation scripts
- Intel platform-specific configurations
- Pre-built deployment packages
- SSH connection utilities
- Port forwarding setup
- Detailed setup instructions
- Intel hardware optimization guides

## Prerequisites

**Intel Tiber Cloud Access**: Account and instance allocation
**HuggingFace Token**: For model downloads and licensing
**SSH Access**: Familiarity with SSH jump host connections
**Model Licenses**: Acceptance of required model licenses (e.g., Llama)

## Performance Benefits

**Hardware Acceleration**: Native Intel AI acceleration
**Large Model Efficiency**: Optimized for 70B+ parameter models
**Reduced Infrastructure Costs**: Efficient hardware utilization
**Custom Optimization**: Direct access to hardware-level tuning

## Use Cases

**Research & Development**: Access to cutting-edge Intel AI hardware
**High-Performance Inference**: Large model deployment with optimal performance
**Self-Hosted AI**: Complete control over AI infrastructure
**Intel Ecosystem Integration**: Leverage Intel's AI software stack

## Next Steps

After deployment, you can:
- Load documents through the web workbench
- Test Graph RAG queries with Llama 3.3 70B
- Monitor Intel hardware performance through Grafana
- Experiment with Intel-optimized AI configurations
- Benchmark performance against other platforms
- Integrate with Intel's AI development tools
