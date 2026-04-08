---
title: Explainable AI
nav_order: 5
parent: Common knowledge management tasks
grand_parent: How-to Guides
review_date: 2027-01-01
guide_category:
  - Common knowledge management tasks
guide_category_order: 5
guide_description: Understand how TrustGraph's explainability works and how to use it in your applications
guide_difficulty: beginner
guide_time: 10 min
guide_emoji: "\U0001F50D"
guide_banner: banner.jpg
guide_labels:
  - Explainability
  - Provenance
  - Applications
---

# Explainable AI

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>Familiarity with TrustGraph's <a href="../../overview/explainability">core concepts</a></li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Understand what TrustGraph's explainability provides, how it integrates with applications, and what you can build with it."
%}

When an AI system answers a question, the natural follow-up is: *how do
you know that?*  TrustGraph's explainability system answers this
automatically.  Every query — whether it's a simple Graph RAG lookup or a
multi-step agent conversation — produces a full reasoning trace that links
the answer back through the retrieval pipeline to the original source
documents.

This guide explains how explainability works from an application
perspective: what information is available, how it reaches your
application, and what you can do with it.

## Explainability is always on

There is no flag to enable or configuration to set.  Every time TrustGraph
answers a question, the system records a complete provenance trace as
standard RDF triples.  This trace is persistent and queryable long after
the original question was asked.

What's optional is how much of this your application chooses to surface.
A simple chatbot might ignore it entirely.  A compliance dashboard might
display every step.  The data is always there; your application decides
what matters to your users.

## What the trace contains

A TrustGraph reasoning trace captures the full journey from question to
answer.  The exact steps depend on the query type, but the general shape
is consistent.

### For a Graph RAG query

When a question is answered using the knowledge graph, the trace records
five stages:

1. **Question** — the original query, with a timestamp
2. **Grounding** — the concepts extracted from the question that seed the
   graph search (e.g. "author" and "document")
3. **Exploration** — the entities discovered during knowledge graph
   traversal, and how many edges were examined
4. **Focus** — the specific knowledge graph edges selected as context for
   the answer, with the LLM's reasoning for why each was chosen
5. **Synthesis** — the final answer, linked to the context that produced it

### For an agent query

Agent queries using the ReAct framework produce a richer trace that
captures the agent's iterative reasoning:

1. **Question** — the session start
2. **Iterations** — each reasoning step records a thought (what the agent
   is considering), an action (which tool it invokes), and an observation
   (what it learned).  If the agent invokes Graph RAG as a tool, the full
   RAG trace is nested within the iteration.
3. **Conclusion** — the final synthesised answer

### For a Document RAG query

Document RAG traces follow a simpler pattern: question, chunk retrieval,
and synthesis.

## How explainability reaches your application

TrustGraph delivers explain events through a streaming callback alongside
the answer itself.  As the retrieval pipeline processes your query, events
fire in real time — you see the grounding concepts before the exploration
results, and the exploration results before the focus selection.

This means your application can show the reasoning process *as it
happens*, not just after the answer is complete.  A chat interface could
display "Searching 45 entities..." while the exploration runs, then show
the selected evidence as it arrives, before the final answer streams in.

After the query completes, the full trace is also stored persistently in
the knowledge graph.  Applications can retrieve past traces by querying
the graph directly, enabling audit logs, comparison views, and
retrospective analysis.

## The provenance chain

The most powerful aspect of explainability is the ability to trace any
piece of the answer back to its source text.  This works because
TrustGraph maintains two complementary provenance layers:

**Extraction provenance** records how knowledge entered the system.  When
a document is processed, TrustGraph records the chain: document was split
into pages, pages into chunks, and chunks into subgraphs of knowledge
graph edges.  Every edge in the knowledge graph can be traced back through
this chain to the exact chunk of text it was extracted from.

**Query-time provenance** records how knowledge was used to answer a
question.  The Focus stage identifies which edges were selected.  Each of
those edges exists in the knowledge graph, and the extraction provenance
tells you where it came from.

Connecting these two layers gives you a complete audit trail:

> **Question** → concept grounding → graph exploration → edge selection →
> **knowledge graph edge** → subgraph → chunk → page → **source document**

The chunk identifier also serves as a key into the document store, so
you can retrieve the actual text of the source passage — not just a
reference to a document, but the specific paragraph that produced the
fact.

## What you can build with this

### Source citations

The most common use of explainability is showing users where an answer
came from.  For each piece of evidence used in the answer, you can display
the source document name, page number, and a snippet of the original text.
This turns a black-box AI response into something a user can verify.

### Confidence assessment

By examining the reasoning trace, applications can assess answer quality.
If the focus stage selected many relevant edges from diverse sources, the
answer is likely well-supported.  If it relied on a single edge from one
chunk, it may warrant caution.  The exploration stage also reveals how
much of the knowledge graph was traversed — a narrow search might miss
relevant context.

### Audit and compliance

In regulated industries, you may need to demonstrate that AI-generated
content is grounded in approved source material.  The persistent
provenance trace provides exactly this: a timestamped, queryable record of
which documents, which pages, and which facts contributed to every answer
the system has ever produced.

### Debugging and quality improvement

When an answer is wrong or incomplete, the reasoning trace shows you
exactly where things went off track.  Was the question grounded on the
wrong concepts?  Were the right entities found but the wrong edges
selected?  Did the synthesis misinterpret the evidence?  Each stage is
independently inspectable, making it far easier to diagnose issues than
staring at a final answer and guessing.

### Knowledge gap analysis

By analysing traces across many queries, you can identify gaps in your
knowledge graph.  If queries about a particular topic consistently produce
thin exploration results or weak focus selections, that's a signal that
you need more source material on that subject.

### Comparative analysis

Since traces are persistent, you can compare how the system answers the
same question at different points in time — for example, before and after
loading new documents.  This helps verify that new material is being
incorporated correctly and that updates haven't degraded answers to
existing questions.

## Accessing explainability

TrustGraph provides several ways to work with explainability data,
depending on your needs:

- **Workbench** — the built-in web interface shows reasoning traces inline
  with answers.  See the
  [Explainability at a glance](../explainability/) guide..
- **CLI tools** — command-line tools for running explainable queries,
  listing past traces, and inspecting provenance chains.  See the
  [Explainability using CLI](../explainability-cli/) guide.
- **TypeScript/JavaScript API** — the `onExplain` callback on the
  `agent`, `graphRagStreaming`, and `documentRagStreaming` methods delivers
  events in real time for building custom interfaces.  See the
  [Explainable AI with TypeScript](../building/explainable-ai) guide.
- **Direct graph queries** — since all provenance is stored as standard
  RDF triples, you can query it directly using the triple store API or
  export it as Turtle/N-Triples for use with external tools.

## Next steps

- **[Explainability at a glance](../explainability/)** — see explainability
  in action using the Workbench
- **[Explainability using CLI](../explainability-cli/)** — inspect traces
  and provenance from the command line
- **[Explainable AI with TypeScript](../building/explainable-ai)** — build
  an application that consumes explainability events
- **[Explainability overview](../../overview/explainability)** — deeper
  technical detail on the RDF data model and named graphs
