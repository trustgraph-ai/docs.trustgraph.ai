---
title: Query with Graph RAG
nav_order: 7
parent: Quickstart
---

# Query with Graph RAG

You've got structured knowledge in the graph. Now ask it a question —
and see exactly how the answer was produced.

## Run a Graph RAG query

From the Workflows page, select **Graph RAG Query**. This isn't just
a chatbot — it has full Explainable AI enabled so you can trace every
step of the reasoning.

Enter a query such as:

> What was the cause of the Bronze Age Collapse?

After a moment you should see a response.

## Read the explainability trace

The bottom right of the screen shows the explainability events,
tracing how the answer was produced:

- **Grounding** — retrieval selects key concepts from your question
  for discovery in the knowledge graph
- **Exploration** — graph nodes related to those concepts are selected
- **Focus** — the system narrows down to a core set of graph edges
  that are most relevant to your question
- **Synthesis** — the selected knowledge is processed to produce the
  answer

The answer appears on the left. But the real payoff is in the **Focus**
event — you can trace graph edges all the way back to the source
documents.

For example, a graph edge like *(Systems Collapse Model → proposed
by → Joseph Tainter)* has a source link below it. Following that link
shows the original text from the document where this knowledge was
extracted.

## Why this matters

This is the explainability that sets TrustGraph apart. You're not just
getting an answer — you can see which facts were used, why they were
selected, and where they came from. In production, this means you can
audit, verify, and trust what the AI tells you.

## Next

[Ontologies](ontologies) — take control of what knowledge gets
extracted.
