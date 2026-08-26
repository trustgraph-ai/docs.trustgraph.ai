---
title: View the knowledge graph
nav_order: 6
parent: Quickstart
---

# View the knowledge graph

The document has been processed. Let's see what TrustGraph extracted
from it — this is where you see that it's not just chunks of text in
a vector store, it's structured knowledge.

## Open the Graph Explorer

From the Workflows page, select **Graph Explorer**.

You'll see a graph visualisation showing entities and relationships
that TrustGraph extracted from the document. Each node is an entity
(a person, place, concept, event) and each edge is a relationship
between them.

Click the **3D** button above the graph view to see it in three
dimensions — the graph is often easier to read this way.

## Explore the data

Click any node to highlight it and its connections. A side panel
appears showing the node's properties and links to related nodes —
you can navigate through the graph by following relationships.

Use the **Search** button (top left) to find specific entities. Enter
a term and matching nodes are listed — selecting one adds it to the
graph along with its neighbours.

The **Clear** button resets the view if it gets cluttered.

## What you're seeing

This is the fundamental difference from standard RAG. Instead of
storing the document as text chunks with vector embeddings, TrustGraph
has extracted the actual entities and relationships — the knowledge
structure of the document.

When you query with Graph RAG in the next step, TrustGraph traverses
this structure to find relevant knowledge, rather than just matching
similar text.

## Next

[Query with Graph RAG](graph-rag) — ask a question and see
explainability in action.
