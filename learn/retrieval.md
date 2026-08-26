---
title: Retrieval methodologies
nav_order: 3
parent: Learn about TrustGraph
---

# Retrieval methodologies

Having multiple retrieval strategies isn't just a feature list — it's
the difference between getting useful answers and getting noise. Each
approach has different strengths, and the right choice depends on your
data and your questions.

## Graph RAG

Graph RAG is TrustGraph's flagship retrieval mechanism, in development
since 2023.

**How it works:** Documents are chunked and processed through knowledge
extraction. An LLM identifies entities and their relationships, storing
them in a context hypergraph with vector embeddings for each entity.

When a question is asked, TrustGraph extracts key concepts from the
query, finds relevant entities via semantic similarity, then traverses
the knowledge graph to discover related information. A cross-encoder
reranker scores the relevance of discovered relationships. The result
is a focused subgraph of precisely relevant knowledge — not a pile of
text chunks.

**When to use it:**
- Questions that require understanding relationships between things
- Answers that need context from multiple documents
- Connecting disparate information across a large corpus
- When reducing hallucination is critical

**The advantage:** Graph RAG understands structure. "Who reports to the
VP of Engineering?" requires traversing a reporting chain — vector
similarity alone can't do this.

## Ontology RAG

Ontology RAG extends Graph RAG with domain-specific precision.

**How it works:** You Bring Your Own Ontology (BYOO) — a structured
description of the entity types and relationships that matter in your
domain. Think of it as a schema for human knowledge. TrustGraph uses
this ontology to guide extraction, ensuring the hypergraph reflects
your domain model rather than whatever the LLM happens to find.

The clever part: rather than flooding the LLM context window with the
full ontology, TrustGraph uses a retrieval operation on the ontology
itself to select the relevant subset for each chunk being processed.

**When to use it:**
- Domains with well-defined structures (legal, medical, financial,
  technical)
- When you need consistent, predictable extraction across documents
- When the quality of the knowledge graph matters more than speed of
  setup

**The advantage:** Precision. Instead of hoping the LLM extracts the
right things, you define what "right" means.

## Document RAG

Document RAG is the familiar vector similarity approach — enhanced in
TrustGraph with concept extraction and full explainability.

**How it works:** Document chunks are embedded and stored in a vector
database. At query time, TrustGraph extracts key concepts from the
question (not just raw embedding), retrieves relevant chunks, and
generates an answer with full provenance tracking.

TrustGraph also supports **hybrid retrieval** — combining BM25 keyword
search with vector similarity using Reciprocal Rank Fusion — for
improved recall.

**When to use it:**
- Broad semantic search across unstructured content
- When relationship structure isn't the primary concern
- As a complement to Graph RAG for different types of questions

**The trade-off:** Document RAG is simpler to set up (no knowledge
extraction step), but retrieved chunks are isolated text fragments
with no understanding of how concepts relate to each other.

## Choosing a strategy

| | Graph RAG | Ontology RAG | Document RAG |
|---|---|---|---|
| **Best for** | Relationship-rich queries | Domain-specific precision | Broad semantic search |
| **Setup effort** | Medium | Higher (BYOO) | Low |
| **Extraction cost** | LLM tokens at ingest | LLM tokens at ingest | Embeddings only |
| **Relationship awareness** | Yes | Yes, guided by schema | No |
| **Explainability** | Full | Full | Full |

In practice, many deployments use more than one strategy. Graph RAG or
Ontology RAG for structured knowledge queries, Document RAG for broader
searches.

## Next

[Explainability](explainability) — how TrustGraph traces answers back
to their sources.
