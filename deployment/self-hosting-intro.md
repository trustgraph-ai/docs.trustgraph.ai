---
title: Introduction to Self-Hosting
nav_order: 10
parent: Deployment
review_date: 2026-01-28
guide_category:
  - Data centre
guide_banner: self-hosted-gpu.jpg
guide_category_order: 1
guide_description: Overview of GPU options and self-hosting software for running TrustGraph locally
guide_difficulty: beginner
guide_time: 10 min
guide_emoji: 🏠
guide_labels:
  - Self-Hosting
  - Introduction
todo: true
todo_notes: Placeholder page - content to be added.
---

# Introduction to Self-Hosting

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>No prerequisites - this is an overview guide</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Get an overview of GPU options for self-hosting and understand the landscape of accessible self-hosting software."
%}

## Running Your Own Models

There are three broad approaches to running LLMs:

**Cloud LLM APIs** (OpenAI, Anthropic, Google, etc.) - You send prompts to a provider's API and pay per token. Simple to use, but your data is processed on their servers and costs scale with usage.

**Rented GPU infrastructure** - You rent GPU time from providers like RunPod, Lambda Labs, or cloud GPU instances. You run the model yourself, controlling the software stack, but on hardware you don't own. Costs are typically hourly or monthly.

**Self-hosting on your own hardware** - You own the GPUs and run everything on-premises. The cost model is capital expenditure on equipment plus electricity, rather than ongoing rental or per-token fees.

This guide focuses on the last two approaches - running models yourself rather than using hosted APIs. The key benefits:

- **Data control** - your prompts and documents stay on infrastructure you control
- **Predictable costs** - no per-token charges; costs are fixed (owned hardware) or time-based (rented)
- **Flexibility** - run any model, configure it how you want

Rented GPU infrastructure gives you most of these benefits without the upfront hardware investment. True self-hosting on owned hardware makes sense when you have consistent, long-term workloads where the capital cost pays off.

Most users run quantized models to reduce memory requirements. Quantization (Q4, Q8, etc.) compresses model weights, allowing larger models to fit on consumer GPUs with modest VRAM. All the tools covered in this guide support quantized models.

## GPU Options

Running LLMs efficiently requires GPU acceleration. Here are the main options:

### NVIDIA (CUDA)

The most widely supported option. Nearly all LLM software supports NVIDIA GPUs out of the box. Consumer cards (RTX 3090, 4090) work well for smaller models. Data centre cards (A100, H100) handle larger models and higher throughput.

**Pros:** Best software compatibility, mature ecosystem
**Cons:** Premium pricing, supply constraints on high-end cards

### AMD (ROCm)

AMD GPUs offer competitive performance at lower prices. ROCm (AMD's GPU compute platform) support has improved significantly. Cards like the RX 7900 XTX or Instinct MI series work with vLLM and other inference servers.

**Pros:** Better price/performance, improving software support
**Cons:** Narrower software compatibility than NVIDIA

### Intel Arc

Intel Arc GPUs are an accessible option for self-hosting. Lower cost than
equivalent NVIDIA cards, and modest power requirements make them easier to
host - no need for specialist cooling or high-current power supplies. Software
support is maturing, with TGI and other inference servers now supporting Arc.

**Pros:** Lower cost, reasonable power draw, easy to host
**Cons:** Smaller ecosystem than NVIDIA, still maturing

Intel's Gaudi accelerators are a separate, specialist option for data centre deployments - purpose-built for AI but not widely available outside cloud services.

### Google TPUs

Tensor Processing Units are Google's custom AI accelerators. Available through Google Cloud or as Edge TPUs for embedded use. Not typically used for on-premises self-hosting.

**Pros:** Excellent performance for supported models
**Cons:** Cloud-only for most use cases

## Self-Hosting Software

This section covers the most accessible options for running LLMs locally. All of these can serve models via an OpenAI-compatible API, which TrustGraph can connect to.

### Ollama

The easiest way to get started. Ollama is a lightweight tool that handles model downloads, GPU detection, and serving - all through a simple interface. It manages the complexity of model formats and GPU configuration for you. Available for Linux, macOS, and Windows. Uses GGUF model format. MIT licence.

**Best for:** Getting started quickly, simple setups, learning

### llama.cpp / llamafile / llama-server

These are related projects built on the same foundation. **llama.cpp** is a C++ library that runs LLMs efficiently with minimal dependencies. **llamafile** packages a model and the runtime into a single executable - download one file and run it, nothing to install. **llama-server** is an HTTP server that exposes an OpenAI-compatible API.

The llama.cpp ecosystem is lightweight and portable. It works on CPU (slower but no GPU required) or GPU (fast). A good choice when you want something minimal with few dependencies. Uses GGUF model format. MIT licence.

**Best for:** Lightweight deployments, CPU fallback, maximum portability

### vLLM

A high-performance inference server built for production workloads. vLLM implements optimisations like continuous batching (processing multiple requests efficiently) and PagedAttention (better memory management) to maximise throughput. If you need to serve many concurrent users or process high volumes, vLLM is designed for that.

Supports NVIDIA and AMD GPUs. Uses safetensors/Hugging Face model format. Apache 2.0 licence.

**Best for:** Production deployments, high throughput, concurrent users

### Text Generation Inference (TGI)

Hugging Face's production inference server. Similar goals to vLLM - optimised for throughput and low latency. Tight integration with the Hugging Face model hub makes it easy to deploy models hosted there. Supports NVIDIA and Intel GPUs. Uses safetensors/Hugging Face model format. Apache 2.0 licence.

**Best for:** Hugging Face ecosystem, production deployments, Intel hardware

### LM Studio

A desktop application with a graphical interface. You can browse and download models from a built-in catalogue, adjust parameters like temperature and context length, and run a local server - all without touching the command line. Uses GGUF model format. Free for personal use; commercial use requires a paid licence.

**Best for:** Users who prefer a GUI, experimentation, non-technical users

## Next Steps

The following guides in this section walk through specific self-hosting setups:

- [AMD GPU](amd-gpu.html) - Self-hosting with vLLM on AMD hardware
- [Intel GPU](intel.html) - Deployment on Intel Gaudi systems
