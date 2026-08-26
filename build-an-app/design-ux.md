---
title: Design the UX
nav_order: 10
parent: Build an App
---

# Design the UX

You have a working plugin, a loaded knowledge graph, and SPARQL
queries that prove the data supports your use cases. Now it's time
to plan what the user experience looks like.

## Ask the code assistant for UX suggestions

Share the use cases and the SPARQL queries with the code assistant
and ask it to suggest UX journeys for the onboarding bot. Be
specific about what you want:

> Given the onboarding bot use cases (service ownership, access
> approval, spend approval, role-based tooling, escalation) and the
> SPARQL queries we've built, suggest UX journeys for a plugin.
> What screens, what interactions, what does the user flow look
> like?

The assistant might suggest things like:

- A **search bar** to find a service, person, or team
- A **service detail view** showing the owning team, required roles,
  and access approval chain
- A **team browser** showing members, managed services, and
  communication channels
- An **approval flow view** showing the steps and spend thresholds
  for a given process
- A **"new starter" view** that takes a role and shows everything
  that person needs access to

## Keep it simple to start

You don't need to build all of this. Pick one journey to start with
— the service ownership lookup is a good choice because it's a
simple query with a clear result.

The goal is to get something working end to end, then iterate. A
single screen that takes a service name and shows who owns it is
more valuable than a half-finished dashboard with five tabs.

## Next

[Build the plugin](build-plugin) — start coding, one step at a time.
