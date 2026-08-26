---
title: How does TrustGraph work?
nav_order: 2
parent: Learn about TrustGraph
---

# How does TrustGraph work?

TrustGraph is a context orchestration layer that combines several
technologies into a platform designed for accurate, controllable, and
explainable knowledge retrieval. Here's the approach at a high level
— later pages go deeper on each aspect.

## Multiple retrieval strategies

There is no single retrieval approach that works for every situation.
TrustGraph provides three, each suited to different kinds of questions
and data:

- **Graph RAG** — extracts entities and relationships from documents
  into a context hypergraph. Queries traverse the graph to find
  connected information. Best for complex, relationship-rich questions
  across diverse data
- **Ontology RAG** — extends Graph RAG by using a domain ontology to
  guide extraction (BYOO — Bring Your Own Ontology). You define the
  entity types and relationships that matter, and TrustGraph extracts
  accordingly. Best for domain-specific precision
- **Document RAG** — the familiar vector similarity approach, enhanced
  with concept extraction, hybrid retrieval (BM25 + vector fusion),
  and full explainability. Best for broad semantic search across
  unstructured content

You choose which strategy fits your use case — or combine them.

## HyperFlows: configurable agent workflows

TrustGraph's architecture is built around **HyperFlows** — custom
agentic workflows where processing capabilities are chained together.
Developers can configure specific LLMs and specific hypergraph access
permissions for every step of a workflow.

A HyperFlow can route a query from a lightweight local model for
classification, to a heavy reasoning model for synthesis, drawing
from different hypergraph collections at each step based on governance
rules.

HyperFlows are composed of modular services connected through a
pub/sub messaging fabric. This means you can:

- Swap components without changing application code
- Run multiple retrieval strategies in parallel
- Add custom processing steps for domain-specific needs
- Scale individual services independently

## Context management

Managing enterprise knowledge at scale requires structure. TrustGraph
provides three levels of context organisation:

- **Workspaces** — deep, programmatic data isolation for users, agents,
  and HyperFlows. An HR agent cannot read financial data; multi-tenant
  data remains strictly compartmentalised
- **Collections** — distinct knowledge bases within a workspace that
  can be partitioned, managed, and dynamically combined at query time
- **Context Cores** — modular, portable, reusable units of context.
  Package domain-specific knowledge into a Context Core and plug it
  into any agent or workflow. Context Cores load in a fraction of the
  time taken to create the original knowledge

## Open LLM inference stack

TrustGraph works with over 40 LLM providers — including OpenAI,
Anthropic, Google VertexAI, AWS Bedrock, Mistral, Ollama, and vLLM.
It's not locked into any single provider or deployment model.

You can use cloud-hosted models, self-hosted open-source models on
any hardware (Nvidia, AMD, or Intel accelerators), or a mix. The same
HyperFlow works regardless of which LLM is behind it — keeping your
data and compute entirely within your sovereignty.

## Explainability built in

TrustGraph captures all event metadata in the hypergraph, providing
real-time traceability for every decision an agent makes. Which
concepts were extracted from the question, which hypergraph nodes
were visited, which edges were selected and why, and which source
documents contributed to the answer.

This isn't a bolt-on feature — it's woven into every retrieval
pipeline. If an agent takes an action, you can trace the exact path
through the hypergraph that led to that outcome.

## Open and extensible

TrustGraph is fully open source with a modular architecture. All
services communicate through open APIs, so you can extend the platform
with custom processors, tools, and integrations without modifying
core code.

## Next

[Retrieval methodologies](retrieval) — a closer look at how Graph RAG,
Document RAG, and Ontology RAG work and when to use each.
