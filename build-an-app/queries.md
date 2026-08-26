---
title: Run queries
nav_order: 9
parent: Build an App
---

# Run queries

You have data in the knowledge graph. Before building the UI, it's
worth validating that the data actually supports the use cases you
designed for — and capturing the queries you'll need later.

## Generate example queries

Go back to the code assistant. Ask it to recall the ontology and the
use cases, then generate example SPARQL queries for each one:

> Recall the onboarding ontology and the use cases we identified
> (service ownership, access approval, spend approval, role-based
> tooling, escalation). Write example SPARQL queries that resolve
> each use case against the knowledge graph.

These queries serve two purposes:

1. **Validation** — run them now to confirm the data is structured
   correctly and the queries return sensible results
2. **Input to the coding step** — you'll use these queries (or
   variations of them) when building the plugin, so capture them
   in a file like `QUERIES.md` for reference

It's also worth asking the assistant to generate an `ONTOLOGY.md`
documenting the entity types and relationships — a quick reference
you can come back to when writing code.

{: .highlight }
**Example queries:** See [queries.txt](https://raw.githubusercontent.com/trustgraph-ai/demo-onboarding/refs/heads/master/queries.txt) for a set of
queries that work with the supplied ontology and sample data.

## Run the queries

You can run SPARQL queries from the CLI:

```sh
tg-invoke-sparql-query -q 'SELECT ?service ?team WHERE {
  ?team <http://example.org/ontology/office#owns> ?service .
}'
```

Or use the **SPARQL Query** workflow in the UI for a more
interactive experience.

Try each of the generated queries and check the results make sense.
For example:

- **Service ownership**: query for which team owns a given service
  — does it return the right team?
- **Spend approval**: query for approval steps above a certain
  threshold — do the right roles come back?
- **Role-based tooling**: query for services required by a given
  role — does the list make sense?

If the results are wrong, the problem is in the data, not the query
— go back and adjust the generation script and reload.

## Next

[Design the UX](design-ux) — plan the plugin's user experience.
