---
title: Generate data
nav_order: 7
parent: Build an App
---

# Generate data

You have an ontology loaded. Normally you'd load documents and let
TrustGraph extract knowledge using the ontology — and that works
well. But for this exercise we're going to take a different approach:
generate the knowledge graph data directly in Turtle format.

Why?

1. **It shows a different way of working with TrustGraph.** Loading
   Turtle data directly is a useful technique to know about, and
   you've already seen document-driven extraction in the Quickstart.
2. **When building an app, it's easier if the data is in a raw form
   you can edit.** Having the data as a Turtle file means you can
   tweak it, add to it, and reload quickly — it removes a document
   ingest step from the feedback loop, so you can iterate faster on
   the app.

{: .highlight }
**Prefer the document-driven approach?** If you'd rather load
documents and extract knowledge using the ontology, you already
know how from the [Quickstart](../quickstart/ontologies). Skip
ahead to the [queries](queries) page once you have data loaded.

## Generate a knowledge graph with the code assistant

Rather than asking the code assistant to write out Turtle directly,
it's better to ask it to **write a script that generates the data**.
If you ask for Turtle directly, you'll get a small, hand-crafted
dataset — maybe 20–30 entities. A script can generate hundreds of
entities with realistic variety, and when you want to change the
data shape later, you just re-run it.

### Step 1: Share the ontology

Make sure the code assistant has the ontology available — either
from the earlier conversation or by sharing the `.ttl` file.

### Step 2: Describe what you want

Ask it to write a Python script that generates sample Turtle data
conforming to the ontology. Be specific about the shape of the data:

> Write a Python script that generates Turtle data conforming to the
> onboarding ontology. Create a fictional company with:
>
> - 4–5 departments, each with 2–3 teams
> - 30–50 people with realistic names, assigned to teams with roles
> - 10–15 internal services (tools and platforms) owned by teams
> - 5–6 processes (IT requests, access requests, procurement) with
>   approval steps and spend thresholds at different levels
> - Slack channels linked to teams and services
>
> Randomise the assignments so the data has variety. Output valid
> Turtle using the ontology's namespace and vocabulary.

### Step 3: Review and iterate

Run the script and check the output. The code assistant will
probably get close on the first pass — check that:

- The namespace and property names match the ontology
- Relationships make sense (people are in teams, teams own services,
  approval steps have the right roles)
- There's enough data to make queries interesting

If something's off, tell the assistant what to fix and regenerate.
The advantage of having a script is that adjustments are quick —
change a parameter, re-run, get new data.

### Tips

- **Remind the assistant of the goal.** Code assistants can drift —
  if the output isn't right, re-state what you're building and why.
- **Share the use cases.** Paste in the use cases from the ontology
  step (service ownership, spend approval, etc.) so the assistant
  generates data that actually supports the queries you want to run.
- **Do a quick visual inspection.** Scan the output to check it
  makes sense — you don't need to validate every triple, just
  confirm it looks reasonable.

### Step 4: Save the output

Save the generated Turtle to a file, e.g. `onboarding-data.ttl`.

{: .highlight }
**Don't have a code assistant?** Use our
[ready-made dataset](https://raw.githubusercontent.com/trustgraph-ai/demo-onboarding/refs/heads/master/onboarding-data.ttl) instead.

## Next

[Load the data](load-data) — load the ontology and data into the
knowledge graph.
