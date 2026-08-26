---
title: Ontologies
nav_order: 8
parent: Quickstart
---

# Ontologies

So far, TrustGraph has been extracting knowledge without any guidance —
the LLM decides what entities and relationships to pull from your
documents. That works, but you can do better.

## What's an ontology?

An ontology defines the types of entities and relationships that matter
in your domain. Instead of letting the LLM extract whatever it finds,
you tell TrustGraph exactly what to look for.

For example, a cybersecurity ontology might define entity types like
`ThreatActor`, `Vulnerability`, and `Asset`, with relationships like
`exploits` and `targets`. When TrustGraph processes a document using
this ontology, it extracts knowledge that conforms to this structure —
precise, consistent, and queryable.

This is TrustGraph's **BYOO** (Bring Your Own Ontology) approach.
You define what matters. TrustGraph extracts accordingly.

## Load an ontology

TrustGraph uses OWL ontologies. For this quickstart, we'll use a
sample ontology.

In the UI, go to the Workflows page and select **Ontology Management**.
You can import an OWL ontology file here. Load the sample ontology
and check that the entity types and relationships look right.

## Process a document with the ontology

Now process a document using an ontology-driven flow. The process is
the same as before — go to **Document Ingestion**, select a document,
and submit it for processing — but this time select a flow that uses
ontology extraction.

The difference is in what gets extracted. The ontology constrains and
guides the LLM, so the resulting knowledge graph is more structured
and domain-relevant than the ontology-free extraction you saw earlier.

## Build your own ontology

{: .highlight }
**Feeling brave?** You don't need to be an ontology expert to create
one. A code assistant (ChatGPT, Claude, Copilot) can generate a
working OWL ontology from a natural language description of your
domain. Try a prompt like: *"Generate an OWL ontology for [your
domain] with entity types for [X, Y, Z] and relationships for
[A, B, C]."* The result is a `.owl` file you can load directly into
TrustGraph.

For more on ontologies, see the
[Ontology RAG guide](../../guides/ontology-rag/) and the
[ontology configuration reference](../../reference/configuration/ontologies).

## Next

[View the ontology-driven knowledge graph](ontology-graph) — see how
the structure reflects the ontology.
