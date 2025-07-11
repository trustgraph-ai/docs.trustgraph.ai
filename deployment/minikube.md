---
title: Minikube
layout: default
nav_order: 2
parent: Deployment
grand_parent: TrustGraph Documentation
---

# Minikube Deployment

Deploy TrustGraph on Minikube for local Kubernetes development and testing.

## Overview

Minikube allows you to run TrustGraph in a local Kubernetes cluster, providing a production-like environment for development and testing. This deployment method offers:

- **Kubernetes-native deployment** with local development capabilities
- **Production-like environment** for testing at scale
- **Resource isolation** and management
- **LoadBalancer** and service discovery testing

## Prerequisites

### System Requirements

- **Minikube** installed and configured
- **kubectl** command-line tool
- **Docker Engine** (most common driver for Minikube)
- **Minimum resources**: 4 CPU cores, 8GB RAM
- **Python 3.x** for TrustGraph CLI tools

### Driver Requirements

Minikube requires a driver for virtualization. The most common is Docker Engine. See the [full Minikube driver documentation](https://minikube.sigs.k8s.io/docs/drivers/) for all available options.

## Installation

### 1. Install Prerequisites

```bash
# Install TrustGraph CLI tools
python3 -m venv env
source env/bin/activate
pip install trustgraph-cli
```

### 2. Start Minikube

```bash
minikube start --cpus=4 --memory=8192
```

### 3. Verify Minikube

```bash
kubectl cluster-info
kubectl get nodes
```

## Configuration

### YAML Configuration

Obtain your TrustGraph Kubernetes configuration file from the [TrustGraph Configuration Builder](https://config-ui.demo.trustgraph.ai/):

1. Select **Kubernetes/Minikube** as deployment method
2. Configure your preferred LLM, graph store, and vector store
3. Download the generated YAML configuration file

## Deployment

### 1. Deploy TrustGraph

```bash
kubectl apply -f <configuration-file.yaml>
```

### 2. Launch LoadBalancer

**In a separate terminal window:**

```bash
minikube tunnel
```

> **Important**: Keep this terminal window open. The LoadBalancer must remain running for cluster communications.

### 3. Verify Services

Check that TrustGraph services are running:

```bash
tg-processor-state
```

To continuously monitor service status:

```bash
watch tg-processor-state
```

> **Note**: On macOS, install watch with: `brew install watch`

### 4. Wait for Stabilization

Wait until all container **STATUS** switches to `Running` before proceeding.

## Working with Documents

### Load Sample Data

Create a sources directory and download a test document:

```bash
mkdir sources
curl -o sources/Challenger-Report-Vol1.pdf https://sma.nasa.gov/SignificantIncidents/assets/rogers_commission_report.pdf
```

### Load Documents

**Single PDF:**
```bash
tg-load-pdf sources/Challenger-Report-Vol1.pdf
```

**Single Text File:**
```bash
tg-load-text sources/<txt-file.txt>
```

**Batch Loading:**
```bash
# Load all PDFs from directory
tg-load-pdf sources/*.pdf

# Load all text files from directory
tg-load-text sources/*.txt
```

## Accessing Services

### Service Discovery

With the LoadBalancer running, TrustGraph services are accessible through Kubernetes service discovery. The exact URLs depend on your configuration, but typically include:

- **TrustGraph API**: Available through service mesh
- **Monitoring**: Grafana dashboards if configured
- **Web Interface**: TrustGraph workbench if enabled

### Port Forwarding

For direct access to specific services:

```bash
# Forward specific service port
kubectl port-forward svc/<service-name> <local-port>:<service-port>
```

## Monitoring

### Check Knowledge Graph

Verify graph parsing results:

```bash
tg-graph-show
```

### Count Graph Edges

```bash
tg-graph-show | wc -l
```

> **Tip**: Wait for at least 1000 graph edges for meaningful testing.

### Kubernetes Monitoring

```bash
# Check pod status
kubectl get pods

# Check service status
kubectl get services

# View pod logs
kubectl logs <pod-name>

# Describe pod details
kubectl describe pod <pod-name>
```

## Testing with Graph RAG

### Basic Query

```bash
tg-invoke-graph-rag -q "Give me 20 facts about the space shuttle Challenger"
```

### Custom Queries

```bash
tg-invoke-graph-rag -q "Your custom question here"
```

### Expected Output

Successful GraphRAG queries will return contextual facts extracted from your knowledge graph, formatted as structured responses with numbered points.

## Troubleshooting

### Common Issues

**LoadBalancer Not Starting:**
- Ensure `minikube tunnel` is running in separate terminal
- Check Minikube status: `minikube status`
- Verify driver is working: `minikube config view`

**Services Not Ready:**
- Check pod status: `kubectl get pods`
- View pod logs: `kubectl logs <pod-name>`
- Verify resources: `kubectl describe node minikube`

**Image Pull Issues:**
- Check network connectivity
- Verify image registry access
- Monitor pod events: `kubectl get events`

### Debug Commands

```bash
# Check cluster info
kubectl cluster-info

# Get all resources
kubectl get all

# Check node resources
kubectl describe node minikube

# View recent events
kubectl get events --sort-by=.metadata.creationTimestamp

# Check Minikube logs
minikube logs
```

## Shutdown

### Clean Shutdown

```bash
# Remove TrustGraph deployment
kubectl delete -f <configuration-file.yaml>

# Stop Minikube
minikube stop

# Optional: Delete Minikube cluster
minikube delete
```

### Verify Cleanup

```bash
# Check no resources remain
kubectl get all

# Verify Minikube status
minikube status
```

## Next Steps

- **Production Kubernetes**: Scale to full Kubernetes clusters
- **Cloud Deployment**: Explore [AWS](aws), [GCP](gcp) managed Kubernetes
- **Monitoring**: Set up comprehensive monitoring with Prometheus/Grafana
- **Security**: Review [Security Considerations](security-considerations)
- **Performance**: Optimize for larger workloads