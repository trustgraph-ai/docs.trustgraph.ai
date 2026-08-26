---
title: Build the plugin
nav_order: 11
parent: Build an App
---

# Build the plugin

You have a working plugin template, data in the knowledge graph,
tested queries, and a UX plan. Now it's time to write the actual
plugin code — one step at a time, with a code assistant doing the
heavy lifting.

## Start with the problem, not the code

Before writing any code, describe what you want to build in terms
of the user experience. What questions will users ask? What answers
do they expect?

A good opening prompt describes the domain and the use cases, not
the implementation:

> We're building a plugin that helps new joiners find their way
> around an organisation. They need to find out who owns a service,
> what tools they need for their role, who to escalate to, and how
> spend approvals work. The data is in a knowledge graph with
> people, roles, teams, services, and processes.

This gives the assistant enough context to make architectural
suggestions rather than just writing boilerplate.

## Provide the ontology early

The knowledge graph schema is the most important context the
assistant needs. Share your ontology (the Turtle file, or even just
the class and property list) early in the conversation. The
assistant can't guess your predicates, and getting them wrong wastes
rounds of debugging.

A sample entity instance is even more useful than the schema alone —
it shows how the data actually looks, including literal types and
URI patterns:

> Here's a sample from the data:
>
>     :Person_AlexHernandez a :Person ;
>         rdfs:label "Alex Hernandez" ;
>         :hasRole :Role_TechnicalPm ;
>         :memberOf :Team_ProductManagement ;
>         :reportsTo :Person_KendallWilson .

## Tell the assistant what APIs exist

TrustGraph's platform APIs are not in the assistant's training data.
You need to explain what's available. The key things to communicate:

- **How to get an API handle**: `useSocket()` returns `BaseApi`,
  and `socket.flow(flowId)` returns `FlowApi` with the real methods
- **What methods exist**: `triplesQuery`, `textCompletion`,
  `graphRag`, `graphRagStreaming`, `embeddings`,
  `graphEmbeddingsQuery`
- **How data comes back**: Triple objects with `s`, `p`, `o` fields,
  where each is a `Term` (`{t: "i", i: "..."}` for IRIs,
  `{t: "l", v: "..."}` for literals)
- **What shared components exist**: `useTheme`, `Card`, `Badge`,
  `SearchInput`, `LoadingState` from `@trustgraph/trustkit`

You don't need to provide full type definitions. A brief description
of each method's signature and purpose is enough. The assistant will
ask if it needs more detail.

## Iterate in small steps

Keep the dev server running. After each meaningful change, build and
check the result in a browser:

```sh
npm run build
```

Then hard-reload (Shift-reload) to pick up the new build.

The cycle that works best:

1. Describe what you want (one feature at a time)
2. Let the assistant implement it
3. Build and test
4. Share what you see (screenshots, error messages)
5. Refine

Resist the urge to specify multiple features in one prompt. Small
iterations catch problems early and keep the assistant's context
focused.

## Describe the experience, not the implementation

Prompts that describe what the user should see tend to produce
better results than prompts that prescribe specific code.

Less effective:

> Add a useEffect that calls graphRagStreaming and updates state
> on each chunk.

More effective:

> The answer should stream in progressively so the user sees text
> appearing as it's generated, like a chat assistant.

The assistant knows how to implement streaming. What it doesn't
know is whether you want streaming in the first place.

## Use "don't code yet" for design discussions

When you're exploring an approach, say so explicitly. Without this,
the assistant will start implementing immediately:

> I'm thinking about a triage step that classifies questions first.
> Don't code this yet, we're just kicking ideas around.

This keeps the conversation collaborative. You can steer the
architecture before any code is written, which is far cheaper than
refactoring afterwards.

## Prompt patterns that work well

**Feature request with context:**
> Could we see a set of process steps to follow to buy something?
> The data has Process entities with hasStep relationships to
> ApprovalStep entities, each with a spendLimit.

**Visual refinement:**
> Could it be more visual? Like connected step cards with arrows
> instead of a numbered list.

**Bug report with evidence:**
> The presets menu drops off the bottom of the screen. [screenshot]

**Architectural nudge:**
> At the moment it feels quite search-y. I'm thinking a more
> conversational approach where the user can scroll back.

## Share errors exactly as they appear

When something breaks, paste the exact error message. The assistant
can usually diagnose the problem from the error alone:

> TypeError: o.split is not a function

This immediately tells the assistant that an object is being treated
as a string. Paraphrasing errors ("it's broken" or "the search
doesn't work") forces the assistant to guess.

## Point the assistant at existing code

When the platform has existing patterns (other plugins, library
source), point the assistant at them:

> Look at how the GraphRAG module in trustkit handles streaming.
> There's a lot in there, most of which you can ignore, but the
> response parsing is what we need.

The assistant can read code faster than you can explain it, and it
will pick up patterns and conventions automatically.

## The conversation arc

A typical plugin-building session follows this arc:

1. **Vision** — describe the domain and use cases
2. **Skeleton** — get a basic UI rendering with the plugin framework
3. **Data connection** — wire up the first API call, see real data
4. **Core features** — build each route or feature one at a time
5. **Polish** — visual refinements, edge cases, error handling
6. **Integration** — connect features together (e.g. clicking a card
   shows detail)

Each stage builds on confirmed working code from the previous stage.
The assistant maintains context across the session, so earlier
decisions inform later ones naturally.

## Common pitfalls

- **Letting the assistant over-engineer.** A code assistant will
  happily add error boundaries, retry logic, and abstraction layers
  you don't need. Keep it simple. If you notice unnecessary
  complexity creeping in, say so

- **Not explaining the runtime environment.** TrustGraph plugins
  run as IIFE bundles with externals mapped to shared globals. The
  assistant needs to know this to configure the build correctly.
  Share the Vite config and plugin config early

- **Assuming the assistant knows your API.** It doesn't. Every
  "not a function" error is usually because the assistant guessed
  at an API that doesn't exist. Front-load the API surface

- **Trying to do too much at once.** A prompt like "build me an
  onboarding assistant with triage, streaming, entity cards, and
  process visualisation" will produce a mess. Build one layer at a
  time

{: .highlight }
**Need a reference?** The
[finished onboarding plugin](https://github.com/trustgraph-ai/demo-onboarding/tree/master/ui-plugin-template)
was built using this approach with the ontology and dataset provided
in this guide. Use it if you get stuck or don't have a code assistant.

## Next

[Go to production](production) — package and deploy your plugin.
