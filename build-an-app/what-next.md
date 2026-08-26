---
title: What next?
nav_order: 13
parent: Build an App
---

# What next?

You've built a working TrustGraph plugin from scratch — from
ontology design through to a deployed container. Here are some
directions to explore next.

## Extend the plugin

- Add more screens from your UX plan — each one follows the same
  pattern of SPARQL query + component
- Use `graphRag` or `graphRagStreaming` to add natural language
  question answering backed by the knowledge graph
- Connect entity cards so clicking one navigates to a detail view

## Try a different domain

The onboarding bot is a starting point. The same approach works
for any domain where structured relationships matter:

- IT asset management — who owns what, what depends on what
- Compliance — which regulations apply to which processes
- Customer support — knowledge bases, escalation paths, SLAs

## Build your own ontology

The code assistant workflow from this guide scales to more complex
ontologies. Start with use cases, break them into concepts and
relationships, and iterate with the assistant.

## Learn more

- [TrustGraph documentation](/) — the full reference
- [Plugin template](https://github.com/trustgraph-ai/ui-plugin-template) —
  start a new plugin from scratch
- [Demo onboarding plugin](https://github.com/trustgraph-ai/demo-onboarding/tree/master/ui-plugin-template) —
  the finished plugin from this guide
