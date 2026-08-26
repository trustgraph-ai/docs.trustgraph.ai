---
title: Ontologies
nav_order: 5
parent: Learn about TrustGraph
---

# Ontologies

Standard Graph RAG lets an LLM discover whatever entities and
relationships it finds in your documents. This works surprisingly well
for general-purpose knowledge. But when you're working in a specific
domain — legal, medical, financial, technical — you often need more
control over what gets extracted.

That's where ontologies come in. TrustGraph supports **BYOO — Bring
Your Own Ontology** — loading your domain schema in OWL format to
guide knowledge extraction.

## What is an ontology?

An ontology is a structured description of the concepts and
relationships that matter in a domain. Think of it as a schema for
human knowledge — it defines:

- **Entity types** — the kinds of things that exist (e.g. Person,
  Service, Role, Department)
- **Relationships** — how those things connect (e.g. "manages",
  "depends on", "approves access to")
- **Constraints** — which relationships are valid between which
  entity types

If you've worked with database schemas, the concept is familiar.
The difference is that ontologies describe knowledge about the world,
not rows in a table.

## Why use ontologies with RAG?

Without an ontology, Graph RAG extraction is opportunistic — the LLM
extracts whatever it finds. This means:

- Different documents may produce inconsistent entity types
- Important domain-specific relationships might be missed
- The LLM might focus on generic relationships rather than
  domain-relevant ones

With an ontology, extraction is guided. You tell TrustGraph what kinds
of entities and relationships matter, and it extracts accordingly. The
ontology-enabled hypergraph uses the provided ontology for semantic
compliance on all ingested data, dramatically improving agentic
accuracy and precision. The result is a more consistent, more precise,
and more useful context hypergraph.

## How TrustGraph uses ontologies

TrustGraph's approach to ontology-guided extraction is pragmatic. Good
ontologies can be large, and flooding an LLM context window with the
full ontology would be counterproductive — exactly the kind of context
overload that causes problems.

Instead, TrustGraph applies a retrieval operation on the ontology
itself. For each chunk of text being processed, it selects the relevant
subset of the ontology to guide extraction. This means the LLM always
has the right context for the text it's processing, without being
overwhelmed.

## Creating ontologies

Ontologies have a reputation for being complex and time-consuming to
create. In academic and enterprise knowledge engineering, that
reputation is deserved — formal ontology projects can take years.

But for practical RAG use cases, you don't need a perfect, exhaustive
ontology. You need one that's good enough to guide extraction in your
domain. Modern code assistants can generate a working OWL ontology from
a description of your domain in minutes. You can refine it as you go.

TrustGraph supports OWL ontologies and includes tooling for loading,
inspecting, and managing them through both the Workbench UI and CLI.

## Next

[How do people use TrustGraph?](use-cases) — real-world applications
and scenarios.
