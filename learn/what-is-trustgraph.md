---
title: What is TrustGraph?
nav_order: 1
parent: Learn about TrustGraph
---

# What is TrustGraph?

## The problem

AI agents are transforming how organisations work. But giving an AI agent
access to your knowledge — and getting accurate, trustworthy answers back
— is harder than it looks.

The standard approach is **Retrieval Augmented Generation (RAG)**: chunk
your documents into pieces, embed them as vectors, and retrieve the most
similar chunks when a question is asked. It works for simple cases. But
it breaks down fast:

**Too much text causes hallucination.**
When you dump large chunks of text into an LLM context window, the model
struggles to find the relevant signal. It starts making things up —
confidently, convincingly, and wrong.

**No control over what the LLM sees.**
Existing RAG frameworks retrieve text by similarity, but you have no
say in what actually gets presented to the model. You get whatever the
vector search returns — relevant or not. There's no way to be precise
about the knowledge an LLM reasons over.

**Information management has no precision.**
Vector search gives you chunks of text, not structured knowledge. You
can't query for specific facts, relationships, or entities. You can't
ask "who reports to whom" or "which service depends on which" — you can
only ask for text that looks similar to your question.

Consider the classic "Who's on First?" comedy routine: a baseball
team has players named *Who*, *What*, and *I Don't Know*. Ask a
vector search "Who is playing on first base?" and it breaks
completely — the embedding space maps "Who" to a generic identity
question, not the name of a player. Semantic similarity operates on
statistical probability. It cannot distinguish between the linguistic
use of a word as a pronoun and its use as a proper noun within a
specific context.

**No explainability.**
When the AI gives you an answer, you can't trace why. What sources were
used? What reasoning led to the response? In a demo this doesn't matter.
In production — especially in regulated, legal, or compliance-sensitive
environments — it's a dealbreaker.

## The solution

TrustGraph is an open-source **context orchestration layer** that
takes a fundamentally different approach to giving AI agents knowledge.

Instead of treating your documents as bags of text chunks, TrustGraph
**extracts structured knowledge** — entities, relationships, and facts
— and stores them in a **context hypergraph** alongside vector
embeddings. A hypergraph goes beyond simple binary relationships
(A → B) by connecting multiple entities into complex, real-world
events — linking a document to its author, approving manager,
compliance policy, and time/location metadata as a single conceptual
unit.

When an agent asks a question, TrustGraph retrieves precise,
structured context rather than raw text. Returning to "Who's on
First?" — a hypergraph knows that `:Who` is a `:Player` whose
`:playsPosition` is `:FirstBase`. There is no ambiguity, no
hallucination, because context is structured, not inferred via
probability.

This means:

- **Reduced hallucination** — the LLM receives focused, relevant
  knowledge instead of large blocks of loosely related text
- **Precise information control** — you control exactly what knowledge
  is extracted and how it's structured, using ontologies (BYOO —
  Bring Your Own Ontology) to define what matters in your domain
- **Relationship-aware retrieval** — answers can follow connections
  across your knowledge: who owns what, what depends on what, how
  things relate
- **Full explainability** — every answer can be traced back to the
  specific hypergraph nodes, source documents, and reasoning steps
  that produced it — not just traceable, but cryptographically
  verifiable

TrustGraph isn't just a better RAG pipeline. It's the context
orchestration layer for building AI systems that reason accurately
over your organisation's knowledge — and can prove how they got
there.

## Next

[How does TrustGraph work?](how-it-works) — the approach and
architecture.
