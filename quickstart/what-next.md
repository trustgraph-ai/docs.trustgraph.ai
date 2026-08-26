---
title: What next?
nav_order: 12
parent: Quickstart
---

# What next?

You've deployed TrustGraph, loaded data, queried with Graph RAG, seen
explainability in action, used ontologies for precision extraction,
run SPARQL queries, and explored the Context Graph.

Here's where to go from here.

## Build an app

Ready to integrate TrustGraph into your own application? The App
Builder guide walks you through building a UI plugin from scratch —
including ontology design, data loading, and a working interface.

[Start building →](../build-an-app/)

## Build an agent

If you're building agentic AI systems, the Agent Builder guide covers
agent orchestration, tool integration, and MCP interoperability.

[Start building agents →](../build-an-agent/)

## Try your own documents

You've seen TrustGraph work with sample data. Now try your own
documents — the [Document RAG guide](../../guides/document-rag/)
and [Graph RAG guide](../../guides/graph-rag/) cover loading and
querying custom data in detail.

## Plan a production deployment

If you're an architect or technical lead planning a production
rollout, the Enterprise Planner covers infrastructure requirements,
deployment options, and enterprise features.

[Plan your deployment →](../enterprise/)

## Talk to us

- [TrustGraph Enterprise](https://trustgraph.ai/enterprise) —
  commercial offering, managed support, and SLAs
- [Discord](https://discord.gg/trustgraph) — community support and
  discussion
- [GitHub](https://github.com/trustgraph-ai/trustgraph) — source
  code, issues, and contributions

## Shutting down

When you're done, shut down TrustGraph cleanly:

{% capture docker_shutdown %}
```sh
docker-compose -f docker-compose.yaml down -v -t 0
```
{% endcapture %}

{% capture podman_shutdown %}
```sh
podman-compose -f docker-compose.yaml down -v -t 0
```
{% endcapture %}

{% include code_tabs.html
   tabs="Docker,Podman"
   content1=docker_shutdown
   content2=podman_shutdown
%}

The `-v` option removes data volumes. The `-t 0` option skips the
graceful shutdown wait.
