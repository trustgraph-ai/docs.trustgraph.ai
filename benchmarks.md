---
layout: default
title: Benchmarks
nav_order: 7
parent: TrustGraph Documentation
---

# Benchmarks

## Data ingest token rates

### Why?

This benchmark measures the token load rate while loading a standard
document.  TrustGraph knowledge extraction build a big backlog of stuff to
process, so it's a good load test.  In reality, the knowledge extraction
(definitions and relationships) is the bottleneck, so this test is largely
measuring:
- The LLM service itself
- How well TrustGraph can load the LLM service.
- The configuration that we're testing with

### Results

| Platform | GPU | Model | Flow | Source material | In tok/s | Out tok/s | Total tok/s |
| -------- | --- | ----- | ---- | --------------- | ---------- | ----------- | ---------- |
| vLLM on Intel Gaudi 2 | Gaudi 2, 8 cards | meta-llama/Llama-3.3-70B-Instruct | document-rag+graph-rag | NASA Challenger Report Volume 1 | 1493.6 | 1545.8 | 3039.5 |
| vllm-server | H100-SXM5-80GB (Tensordock) | TheBloke/Mistral-7B-v0.1-AWQ | document-rag+graph-rag | NASA Challenger Report Volume 1 | 304.3 | 1845.6 | 2150.0 |
| VertexAI | n/a | Gemini 2.0 Flash | document-rag+graph-rag | NASA Challenger Report Volume 1 | 216.2 | 155.8 | 372.0 |
| LMStudio | Radeon RX 7900 XTX | Gemma3 4B QAT | document-rag+graph-rag | NASA Challenger Report Volume 1 | 116.2 | 133.9 | 250.1 |
| Granite Ridge | 128 Xeon Gen 6 CPU | mistralai/Mistral-7B-Instruct-v0.3 | document-rag+graph-rag | NASA Challenger Report Volume 1 | 117.7 | 90.0 | 207.8 |
| LMStudio | Radeon RX 7900 XTX | Gemma2 9B | document-rag+graph-rag | NASA Challenger Report Volume 1 | 119.6 | 73.0 | 192.6 |
| Granite Ridge | 128 Xeon Gen 6 CPU | meta-llama/Llama-3.3-70B-Instruct | document-rag+graph-rag | NASA Challenger Report Volume 1 | 67.0 | 22.4 | 89.3 |

## Procedure

How it works:
- Start TrustGraph
- Load the Challenger report volume 1
- Submit with the default flow (document RAG + graph RAG)
- Monitor the throughput in Grafana.
  - With this document expect an early boost from the content and preface
    pages, and then throughput plateaus out.  So leaving for a couple of
    minutes lets this phase go away
  - Some cloud model-as-a-service facilities will let you have some
    high rate action as a boost, and then reduce the rate so again, let this
    phase subside.  important to look at the pub/sub backlog chart so you
    can see when things have settled in.
- Start tg-show-token-rate
- Wait for it to finish, runs for 1 minute
- Record the last line produced which is an average across the period.
