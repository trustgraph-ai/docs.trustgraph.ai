---
title: Explainability using CLI
nav_order: 4
parent: Advanced knowledge management
grand_parent: How-to Guides
review_date: 2027-01-01
guide_category:
  - Advanced knowledge management
guide_category_order: 3
guide_description: Use command-line tools to trace GraphRAG answers back to their sources
guide_difficulty: intermediate
guide_time: 20 min
guide_emoji: "\U0001F50D"
guide_banner: banner.jpg
guide_labels:
  - Explainability
  - Provenance
  - GraphRAG
  - CLI
---

# Explainability Using CLI

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>TrustGraph deployed (<a href="../getting-started/quickstart">Quick Start</a>)</li>
<li>A document already loaded and processed with Graph RAG (see <a href="../graph-rag-cli">Graph RAG CLI guide</a>)</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Run explainable GraphRAG queries from the CLI, review reasoning traces, and trace edges back to source documents."
%}

This guide covers the same explainability workflow as the
[Explainability at a glance](../explainability/) guide, but using command-line tools
instead of the Workbench.

**New to explainability?** Read the
[Explainability overview](../../overview/explainability) first to
understand the concepts.

This guide demonstrates:
- Running GraphRAG queries with inline explainability
- Listing and reviewing past explainability sessions
- Viewing full reasoning traces
- Tracing edges back to source documents
- Querying provenance data directly

## Step 1: Run an Explainable GraphRAG Query

Use the `-x` flag to enable explainability:

```bash
tg-invoke-graph-rag \
  -x \
  -q "What are the key entities involved in Operation Phantom Cargo?" \
  -C intelligence
```

The answer streams to stdout as normal.  Meanwhile, explainability
events are reported to stderr as each pipeline stage completes:

```
  [question] urn:trustgraph:question:a1b2c3...
    Query: What are the key entities involved in Operation Phantom Cargo?
    Time: 2026-03-17T14:30:00Z

  [grounding] urn:trustgraph:grounding:d4e5f6...
    Concepts: 3
      - Operation Phantom Cargo
      - entities
      - involvement

  [exploration] urn:trustgraph:exploration:g7h8i9...
    Edges explored: 47
    Seed entities: 5
      - Operation Phantom Cargo
      - Viktor Sorokin
      - MV Horizon Star
      - Port of Odessa
      - Volkov Industrial Group

  [focus] urn:trustgraph:focus:j0k1l2...
    Focused on 8 edge(s)
      Edge: (Viktor Sorokin, orchestrated, Operation Phantom Cargo)
        Reason: Directly identifies a key entity and their role...
      Edge: (MV Horizon Star, transported, grey arms shipment)
        Reason: Names the vessel involved in the operation...
      ...

  [synthesis] urn:trustgraph:synthesis:m3n4o5...
    Document: ...
```

The answer then follows, grounded in the selected edges.

## Step 2: List existing explainability traces

All explainability traces are persistent.  List them with:

```bash
tg-list-explain-traces -C intelligence
```

Output:

```
Session ID                              Type      Question                                        Time
--------------------------------------  --------  ----------------------------------------------  --------------------
urn:trustgraph:question:a1b2c3...       GraphRAG  What are the key entities involved in Oper...   2026-03-17T14:30:00Z
urn:trustgraph:question:x9y8z7...       Agent     Summarise the intelligence findings             2026-03-17T14:25:00Z
urn:trustgraph:question:p5q6r7...       DocRAG    What is the timeline of events?                 2026-03-17T14:20:00Z
```

## Step 3: View a Full Trace

Pick a session ID from the listing and view its complete trace:

```bash
tg-show-explain-trace \
  -C intelligence \
  "urn:trustgraph:question:a1b2c3..."
```

This displays the same stages you saw inline., but formatted for

## Step 4: Trace Edges to Source Documents

Add `--show-provenance` to follow selected edges back through the
extraction provenance chain:

```bash
tg-show-explain-trace \
  --show-provenance \
  -C intelligence \
  "urn:trustgraph:question:a1b2c3..."
```

For each focused edge, this traces the reified triple through
`urn:graph:source` and displays the provenance chain and content
identifier:

```
  20. (clothing, definition, clothing)
      Reasoning: Defines 'clothing' which is related to 'fine clothes'.
      Source: https://trustgraph.ai/subgraph/2c356884-fef9-4998-bb69-8b546a67b6a1 -> Chunk 2 -> Page 157 -> A Concise Dictionary of Old Icelandic
      Content: urn:chunk:7ed8e3b6-4202-47eb-92bc-c1a4f2d232e9
```

The **Source** line traces the edge back through the subgraph, chunk,
page, and document it was extracted from.  The **Content** line provides
the content identifier for the chunk text.

## Step 5: View Chunk Content

Use the content identifier from step 4 to retrieve the actual chunk
text that the edge was extracted from:

```bash
tg-get-document-content urn:chunk:7ed8e3b6-4202-47eb-92bc-c1a4f2d232e9
```

```
-t œkr , a. headstrong, stubborn; -úðigr ,
a. staunch, firm o f mind ; -úðliga , adv.
firmly; -úðligr , adv. = -úðigr;-vingr , a.
```

This completes the audit trail from answer to source text — you can see
exactly which chunk of text produced each fact used in the answer.

## Step 6: View Extraction Provenance Directly

To see the full extraction hierarchy for a specific document, use
`tg-show-extraction-provenance`:

```bash
tg-show-extraction-provenance \
  -C intelligence \
  "urn:trustgraph:doc:phantom-cargo"
```

This displays a tree:

```
Document: PHANTOM CARGO
  Page: Page 1
    Chunk: chunk-001
      Subgraph: subgraph-001a (12 edges)
      Subgraph: subgraph-001b (8 edges)
    Chunk: chunk-002
      Subgraph: subgraph-002a (15 edges)
  Page: Page 2
    Chunk: chunk-003
      ...
```

Add `--show-content` to include the actual text at each level:

```bash
tg-show-extraction-provenance \
  --show-content \
  --max-content 500 \
  -C intelligence \
  "urn:trustgraph:doc:phantom-cargo"
```

Use `--format json` for machine-readable output.

## Step 7: Query Provenance Data Directly

Since all explainability data is stored as standard RDF triples in named
graphs, you can query it directly using `tg-show-graph` and
`tg-query-graph`:

```bash
# View all extraction provenance triples
tg-show-graph -g "urn:graph:source" -C intelligence

# View all query-time traces
tg-show-graph -g "urn:graph:retrieval" -C intelligence

# Find all chunks derived from a specific document
tg-query-graph \
  -p "http://www.w3.org/ns/prov#wasDerivedFrom" \
  -g "urn:graph:source" \
  -C intelligence

# Export provenance as Turtle for external tools
tg-graph-to-turtle -C intelligence > provenance.ttl
```

## Summary

In this guide you:

- Ran a GraphRAG query with inline explainability (`-x`)
- Listed past explainability sessions
- Reviewed a full reasoning trace
- Traced edges back to source documents with `--show-provenance`
- Viewed extraction provenance hierarchies
- Queried provenance data directly using graph tools

## Next Steps

- **[Explainability overview](../../overview/explainability)** — deeper
  understanding of the architecture and named graphs
- **[tg-list-explain-traces](../../reference/cli/tg-list-explain-traces)**
  — CLI reference
- **[tg-show-explain-trace](../../reference/cli/tg-show-explain-trace)**
  — CLI reference
- **[tg-show-extraction-provenance](../../reference/cli/tg-show-extraction-provenance)**
  — CLI reference
- **[tg-query-graph](../../reference/cli/tg-query-graph)** — CLI
  reference
