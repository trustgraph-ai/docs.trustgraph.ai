---
title: Query with SPARQL
nav_order: 10
parent: Quickstart
---

# Query with SPARQL

Graph RAG answers questions in natural language. But sometimes you want
to ask exact questions — "which entities of type X are connected to
entity Y?" — and get structured results back. That's what SPARQL does.

## What is SPARQL?

SPARQL is a query language for graph data, similar to how SQL queries
relational databases. It lets you match patterns in the knowledge
graph — find specific entities, follow relationships, filter by type.

Because the ontology-driven extraction produces consistent entity
types and relationship names, SPARQL queries work reliably across
your data.

## Run a SPARQL query

You can run SPARQL queries from the CLI:

```sh
tg-invoke-sparql-query 'SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10'
```

This returns the first 10 triples in the knowledge graph — a quick way
to see what's there.

A more targeted query might look like:

```sparql
SELECT ?entity ?relationship ?target
WHERE {
  ?entity a <http://example.org/YourEntityType> .
  ?entity ?relationship ?target .
}
```

Replace `YourEntityType` with an entity type from the ontology you
loaded. The results show all entities of that type and their
relationships.

## The precision payoff

This is where the value of ontologies and structured extraction
becomes concrete. You can't run a meaningful SPARQL query against
free-form text chunks — there's no consistent structure to query
against. But with ontology-driven extraction, the knowledge graph has
a predictable schema, and SPARQL can exploit it.

For more on SPARQL with TrustGraph, see the
[Knowledge graph basics guide](../../guides/knowledge-graphs/).

## Next

[Context Graph viewer](context-graph) — explore the graph visually.
