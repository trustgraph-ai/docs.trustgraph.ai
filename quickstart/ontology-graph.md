---
title: Ontology-driven knowledge graph
nav_order: 9
parent: Quickstart
---

# Ontology-driven knowledge graph

You've processed a document with an ontology. Let's see the difference
it makes.

## Compare the graphs

Go back to the **Graph Explorer** from the Workflows page.

Look at the knowledge graph from the ontology-driven extraction and
compare it with the earlier ontology-free result. The differences
should be clear:

- **Entity types match the ontology** — instead of generic nodes, you
  see the specific types you defined (or that the sample ontology
  defined)
- **Relationships are consistent** — the same relationship names
  appear across different entities, making the graph queryable with
  precision
- **Less noise** — the ontology filters out irrelevant extractions
  that the LLM might otherwise produce

## Why this matters

Without an ontology, extraction is best-effort — the LLM extracts
whatever it considers important, using whatever labels it chooses.
Two documents about the same topic might produce completely different
entity types and relationship names.

With an ontology, extraction is guided. The LLM maps document content
to the entity types and relationships you defined. The result is a
knowledge graph that's consistent, predictable, and precise enough to
query with SPARQL — which is exactly what we'll do next.

## Next

[Query with SPARQL](sparql) — run precise queries against the
structured knowledge.
