---
title: Intel GPU
nav_order: 11
parent: Deployment
review_date: 2026-01-28
guide_category:
  - Data centre
guide_banner: intel-ai.jpg
guide_category_order: 2
guide_description: Self-hosting TrustGraph with OpenVINO on Intel GPU accelerators
guide_difficulty: advanced
guide_time: 2 - 4 hr
guide_emoji: 🔴
guide_labels:
  - GPU
  - OpenVINO
  - Intel Arc
todo: true
todo_notes: Placeholder page - content to be added.
---

# Self-Hosting with OpenVINO and Intel GPU

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>Intel GPU with sufficient VRAM (e.g., Intel Arc B60 24GB)</li>
<li>Intel GPU drivers installed</li>
<li>Python {{site.data.software.python-min-version}}+ for CLI tools</li>
<li>Basic command-line familiarity</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Deploy TrustGraph with OpenVINO running on Intel GPU hardware for high-performance local inference."
%}

## Why Intel GPU?

Intel's edge GPUs may not match the raw specifications of NVIDIA and AMD
offerings, but they provide a compelling option for Edge AI deployments.
With a lower price point and excellent compute performance per watt,
Intel Arc GPUs are well-suited for scenarios where power efficiency and
cost-effectiveness are priorities. Intel provides [OpenVINO](https://docs.openvino.ai/) support for
model hosting which provides a polished experience.

## What is OpenVINO?

OpenVINO (Open Visual Inference and Neural Network Optimization) is an
open-source toolkit developed by Intel for optimizing and deploying deep
learning models. It supports inference on Intel CPUs, integrated and discrete
GPUs, and NPU accelerators.

OpenVINO provides flexible model support, allowing you to use models trained
with popular frameworks such as PyTorch, TensorFlow, and ONNX. It can directly
integrate models from Hugging Face using Optimum Intel. The toolkit accelerates
AI inference with lower latency and higher throughput while maintaining
accuracy and optimizing hardware utilization.

## The model: Mistral Nemo 12B

Mistral Nemo is a 12 billion parameter large language model developed by
Mistral AI. It offers strong performance across a range of tasks while
remaining small enough to run on consumer hardware. In this guide, we will
use the 4-bit quantized version of the model, which significantly reduces
memory requirements while maintaining good quality output.

## Roadmap

In this guide we will:

1. Pull the OpenVINO model serving image
2. Get a Hugging Face token (if you don't already have one)
3. Run some CLI commands to verify the GPU is visible
4. Launch the OpenVINO container and check it's running
5. Build and deploy TrustGraph

## Deploying

### Intel GPU drivers

Intel GPUs require the standard driver package to be installed. Intel provides
[Edge Developer Kit Reference Scripts](https://github.com/intel/edge-developer-kit-reference-scripts)
to assist with setup. Note that these are reference setups; your host may
already have similar drivers installed depending on your acquisition path.

### Hugging Face token

You will need a Hugging Face token to access the model, which will be
downloaded from Hugging Face when the container starts. If you don't already
have an account, sign up at [huggingface.co](https://huggingface.co/). Once
logged in, navigate to your
[Access Tokens settings](https://huggingface.co/settings/tokens) and create
a new token. Keep this token safe as you will need it later.

### Pull the OpenVINO model server image

Pull the OpenVINO model server image with GPU support:

{% capture docker_pull %}
```bash
docker pull docker.io/openvino/model_server:latest-gpu
```
{% endcapture %}

{% capture podman_pull %}
```bash
podman pull docker.io/openvino/model_server:latest-gpu
```
{% endcapture %}

{% include code_tabs.html
   tabs="Docker,Podman"
   content1=docker_pull
   content2=podman_pull
%}

### Run the OpenVINO container

First, set your Hugging Face token as an environment variable:

```bash
export HF_TOKEN=your-huggingface-token
```

Then launch the OpenVINO model server container:

{% capture docker_run %}
```bash
docker run --user $(id -u):$(id -g) -d \
  --device /dev/dri \
  --group-add=$(stat -c "%g" /dev/dri/render* | head -n 1) \
  --rm -p 7000:7000 \
  -v $(pwd)/models:/models:rw \
  -e HF_TOKEN=$HF_TOKEN \
  docker.io/openvino/model_server:latest-gpu \
      --source_model llmware/mistral-nemo-instruct-2407-ov \
      --model_repository_path models \
      --task text_generation \
      --rest_port 7000 \
      --target_device GPU \
      --cache_size 2
```
{% endcapture %}

{% capture podman_run %}
```bash
podman run --user $(id -u):$(id -g) -d \
  --device /dev/dri \
  --group-add=$(stat -c "%g" /dev/dri/render* | head -n 1) \
  --rm -p 7000:7000 \
  -v $(pwd)/models:/models:rw \
  -e HF_TOKEN=$HF_TOKEN \
  docker.io/openvino/model_server:latest-gpu \
      --source_model llmware/mistral-nemo-instruct-2407-ov \
      --model_repository_path models \
      --task text_generation \
      --rest_port 7000 \
      --target_device GPU \
      --cache_size 2
```
{% endcapture %}

{% include code_tabs.html
   tabs="Docker,Podman"
   content1=docker_run
   content2=podman_run
%}

