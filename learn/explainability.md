---
title: Explainability
nav_order: 4
parent: Learn about TrustGraph
---

# Explainability

Most RAG frameworks are black boxes. You ask a question, you get an
answer, and you have no idea why. TrustGraph takes a fundamentally
different approach: every answer is traceable.

## Why this matters

When an AI system gives you an answer, you need to be able to ask:

- **Which documents** contributed to this answer?
- **Which facts** were selected from the knowledge graph?
- **Why** were those facts chosen over others?
- **What reasoning** led to the final response?

In a demo, this doesn't matter. In production — especially in
regulated industries like financial services, healthcare, or legal —
auditable AI reasoning is not optional. Even outside regulated
contexts, explainability builds confidence and helps identify when
the system is drawing on incorrect or outdated information.

## How TrustGraph does it

TrustGraph records two layers of provenance:

**Extraction provenance** tracks how knowledge entered the system.
When documents are processed, TrustGraph records the full derivation
chain: document → pages → chunks → extracted knowledge. Given any fact
in the knowledge graph, you can trace it back to the exact chunk of
text it was extracted from.

**Query-time explainability** tracks how an answer was derived. When a
query runs, TrustGraph records each stage: what concepts were extracted
from the question, which knowledge graph nodes were visited, which
relationships were selected and why, and how the final answer was
synthesised.

## The complete audit trail

The real power comes from connecting these two layers. For any answer,
you can follow the full chain:

> **Your question** → concept extraction → graph traversal →
> relationship selection (with reasoning) → **specific knowledge** →
> extraction chain → chunk → page → **source document**

Every link in this chain is recorded, queryable, and persistent.
Reasoning traces aren't ephemeral — they're stored as standard RDF
triples and remain available for later review, auditing, or reporting.

## Deeper dive

For the full technical details on how explainability works — including
named graphs, context graph architecture, and how extraction provenance
connects to query-time traces — see the
[Explainability overview](../../architecture/explainability).

## Next

[Ontologies](ontologies) — how domain-specific schemas give you
precision control over knowledge extraction.
