---
title: Explainability
nav_order: 4
parent: Common knowledge management tasks
grand_parent: How-to Guides
review_date: 2027-01-01
guide_category:
  - Common knowledge management tasks
guide_category_order: 3
guide_description: Trace GraphRAG answers back to their sources using the Workbench
guide_difficulty: beginner
guide_time: 15 min
guide_emoji: "\U0001F50D"
guide_banner: banner.jpg
guide_labels:
  - Explainability
  - Provenance
  - GraphRAG
---

# Explainability Guide

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>TrustGraph deployed (<a href="../getting-started/quickstart">Quick Start</a>)</li>
<li>Understanding of <a href="../getting-started/concepts">Core Concepts</a>)</li>
<li>A document already loaded and processed with Graph RAG (see <a href="../graph-rag">Graph RAG guide</a>)</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Run an explainable GraphRAG query, review the reasoning trace, and trace selected edges back to source documents."
%}

**Understand how TrustGraph arrives at its answers**

This guide walks through the explainability features using a GraphRAG
query as the example.  You'll see how TrustGraph records each stage of
the reasoning process and how you can trace facts back to the documents
they came from.

**New to explainability?** Read the
[Explainability overview](../../overview/explainability) first to
understand the concepts.

## Prerequisites

This guide assumes you've already loaded and processed a document using
Graph RAG.  If you haven't done that yet, follow the
[Graph RAG guide](../graph-rag/) first.

## What You'll Learn

1. Running a GraphRAG query with explainability enabled
2. Reviewing the reasoning trace (question, grounding, exploration,
   focus, synthesis)
3. Understanding why specific edges were selected
4. Tracing edges back to source documents
5. Browsing past explainability sessions

## Step 1: Run an Explainable Query

In the Workbench, navigate to the **Graph RAG** query page.

Enter a question and enable the **Explainability** toggle before
submitting the query.

<!-- placeholder: screenshot of the Workbench Graph RAG query page
     with the Explainability toggle enabled and a question entered -->

The answer will stream as normal, but behind the scenes TrustGraph
records the full reasoning trace.

## Step 2: View the Reasoning Trace

After the query completes, navigate to the **Explainability** page in
the Workbench.

You'll see a list of all recorded sessions.  Find your query — it will
show the question text, type (GraphRAG), and timestamp.

<!-- placeholder: screenshot of the Workbench explainability sessions
     list showing several recorded queries with their types and
     timestamps -->

Click on a session to view its full trace.

## Step 3: Review the GraphRAG Trace

The trace view shows each stage of the reasoning pipeline:

### Question

The original query and when it was submitted.

<!-- placeholder: screenshot of the Question section of the trace view,
     showing the query text and timestamp -->

### Grounding

The concepts extracted from your question that were used to seed the
graph search.  These are the terms TrustGraph used to find entry points
into the knowledge graph.

<!-- placeholder: screenshot of the Grounding section showing a list
     of extracted concepts -->

### Exploration

The graph traversal results: which entities were found as starting
points, and how many edges were explored.

<!-- placeholder: screenshot of the Exploration section showing seed
     entities and edge count -->

### Focus

This is the most important stage.  It shows which edges were selected
from the explored subgraph, and *why* each edge was chosen.

The LLM provides reasoning for each selection, explaining why it
considered that fact relevant to answering your question.

<!-- placeholder: screenshot of the Focus section showing selected
     edges as (subject, predicate, object) triples with the LLM's
     reasoning text alongside each one -->

### Synthesis

The final generated answer, along with a reference to the document
context that was assembled for the LLM.

<!-- placeholder: screenshot of the Synthesis section showing the
     generated answer -->

## Step 4: Trace Back to Source Documents

From the Focus stage, you can trace any selected edge back to its
source document.  This uses the extraction provenance stored in the
`urn:graph:source` named graph.

Select an edge and choose **Show provenance**.  TrustGraph will show
the chain:

> **Selected edge** → Subgraph → Chunk → Page → **Source document**

<!-- placeholder: screenshot of the provenance view showing the
     chain from a selected edge back through chunk and page to the
     original document, with the chunk text visible -->

This tells you exactly which text in which document produced the fact
that TrustGraph used to answer your question.

## Step 5: Browse Past Sessions

All explainability traces are persistent.  You can return to the
Explainability page at any time to review past queries — useful for
auditing, debugging, or understanding how the system's answers relate
to the underlying knowledge.

Sessions are listed with their type (GraphRAG, DocRAG, or Agent), the
question text, and timestamp.

## Summary

In this guide you:

- Ran a GraphRAG query with explainability enabled
- Reviewed the 5-stage reasoning trace
- Examined why specific edges were selected
- Traced a fact back to its source document
- Browsed past explainability sessions

## Next Steps

- **[Explainability using CLI](../explainability-cli/)** — the same
  workflow using command-line tools, with more control over output
  formats
- **[Explainability overview](../../overview/explainability)** — deeper
  understanding of the architecture
