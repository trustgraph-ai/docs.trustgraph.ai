---
title: Benchmarks
nav_order: 7
parent: TrustGraph Documentation
review_date: 2026-02-01
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

<table>
  <thead>
    <tr>
      <th>Platform</th>
      <th>GPU</th>
      <th>Model</th>
      <th>Config</th>
      <th>Token Rate</th>
      <th>Time to Process</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>vLLM on Intel Gaudi 2 🏆</td>
      <td>Gaudi 2, 8 cards</td>
      <td>meta-llama/Llama-3.3-70B-Instruct</td>
      <td>TC1</td>
      <td>In: 1493.6<br/>Out: 1545.8<br/>Total: 3039.5</td>
      <td>8.5 min</td>
    </tr>
    <tr>
      <td>vllm-server on NVidia</td>
      <td>H100-SXM5-80GB (Tensordock)</td>
      <td>TheBloke/Mistral-7B-v0.1-AWQ</td>
      <td>TC1</td>
      <td>In: 304.3<br/>Out: 1845.6<br/>Total: 2150.0</td>
      <td>12.0 min</td>
    </tr>
    <tr>
      <td>VertexAI</td>
      <td>n/a</td>
      <td>Gemini 2.0 Flash</td>
      <td>TC1</td>
      <td>In: 216.2<br/>Out: 155.8<br/>Total: 372.0</td>
      <td>69.4 min</td>
    </tr>
    <tr>
      <td>LMStudio</td>
      <td>Radeon RX 7900 XTX</td>
      <td>Gemma3 4B QAT</td>
      <td>TC1</td>
      <td>In: 116.2<br/>Out: 133.9<br/>Total: 250.1</td>
      <td>103.3 min</td>
    </tr>
    <tr>
      <td>Granite Ridge</td>
      <td>128 Xeon Gen 6 CPU</td>
      <td>mistralai/Mistral-7B-Instruct-v0.3</td>
      <td>TC1</td>
      <td>In: 117.7<br/>Out: 90.0<br/>Total: 207.8</td>
      <td>124.3 min</td>
    </tr>
    <tr>
      <td>LMStudio</td>
      <td>Radeon RX 7900 XTX</td>
      <td>Gemma2 9B</td>
      <td>TC1</td>
      <td>In: 119.6<br/>Out: 73.0<br/>Total: 192.6</td>
      <td>134.1 min</td>
    </tr>
    <tr>
      <td>Granite Ridge</td>
      <td>128 Xeon Gen 6 CPU</td>
      <td>meta-llama/Llama-3.3-70B-Instruct</td>
      <td>TC1</td>
      <td>In: 67.0<br/>Out: 22.4<br/>Total: 89.3</td>
      <td>289.3 min</td>
    </tr>
  </tbody>
</table>

### Test Configurations

<table>
  <thead>
    <tr>
      <th>Config ID</th>
      <th>Flow</th>
      <th>Source Material</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TC1</td>
      <td>document-rag+graph-rag</td>
      <td>NASA Challenger Report Volume 1 (1,549,890 tokens)</td>
    </tr>
  </tbody>
</table>

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
