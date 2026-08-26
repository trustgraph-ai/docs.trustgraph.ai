# Documentation User Journeys

## Personas

1. The Curious Evaluator
2. The Quick-starter
3. The App Builder
4. The Agent Builder
5. The Enterprise Planner
6. The Operator

---

## 1. The Curious Evaluator

### Persona
Someone who has encountered TrustGraph — maybe from a blog post, a
conference talk, a colleague's recommendation, or a search for GraphRAG
tooling. They're technically literate (developer, architect, or technical
decision-maker) but know little or nothing about TrustGraph specifically.
They're trying to decide whether it's worth investing time in.

They may be comparing TrustGraph against other options — vanilla RAG with
a vector DB, LangChain, LlamaIndex, or building something custom. They
need to understand what TrustGraph actually does, what makes it different,
and whether it fits their problem.

### Goal
Form a clear mental model of what TrustGraph is, what problems it solves,
and whether it's relevant to their situation. Leave the docs either
confident enough to try it, or confident that it's not for them. Both
outcomes are success — the failure case is leaving confused or unconvinced
due to poor communication.

### Snares

**Jargon wall**: The docs assume familiarity with TrustGraph-specific
concepts (knowledge graphs, Graph RAG, ontology RAG, flows, context cores)
without grounding them in problems the reader already understands. An
evaluator who doesn't yet know why they'd want a knowledge graph will
bounce.

**No clear differentiator**: "What does this do that a vector DB doesn't?"
is the first question an evaluator asks. If the answer requires reading
five pages and assembling it yourself, they'll leave before they find it.

**Feature list without story**: Features pages list capabilities but don't
connect them to outcomes. An evaluator doesn't care about "pub/sub
messaging architecture" — they care about "can I get accurate answers
from complex, multi-document knowledge?"

**No path to action**: The evaluator finishes reading and thinks "OK,
interesting" but there's no clear "ready to try it?" nudge. They close
the tab and forget. The overview section needs to hand off to the
quickstart at the right moment.

**Comparison vacuum**: Evaluators are comparing options. If the docs
don't acknowledge alternatives and explain the tradeoffs honestly, the
evaluator has to do that work themselves — and they'll do it with
incomplete information.

**Credibility gap**: No evidence of real-world usage, no performance
claims, no maturity signals. The evaluator can't tell if this is a
mature project or a weekend experiment. The maturity page exists but
isn't prominently surfaced in the evaluator's path.

### Journey

**Step 1: Land on the homepage.**
They've clicked a link from a blog post, search result, GitHub README,
or a colleague's message. They're seeing TrustGraph for the first time
and asking "what is this thing?"

**Step 2: Enter the "Learn about TrustGraph" pathway.**
The homepage makes it clear there's a guided route that will take them
through: What is TrustGraph? What problems does it solve? Why would I
choose it over alternatives? How does it work? What can it do? The
entry point should signal this arc — not a vague "Introduction" but
something like "What is TrustGraph?" that directly answers the question
they arrived with.

**Step 3: "What is TrustGraph?" — the problem and the solution.**
This is the most important page for the evaluator. It needs to lead
with the problems they're already feeling:
- Too much text in LLM context windows causes hallucination
- Existing RAG frameworks give no control over what information is
  actually presented to an LLM
- Information management has no precision — you get chunks of text, not
  the specific knowledge you need
- There's no explainability — you can't trace why an answer was given
  or what context produced it

Then position TrustGraph as the answer to these specific problems.
Don't lead with features or jargon — lead with pain, then relief.

**Step 4: "How does TrustGraph work?" — the approach.**
Now they're interested. Show them the solution:
- Multiple retrieval strategies — Graph RAG, Document RAG, Ontology RAG
  — not a one-size-fits-all approach
- Flexible pipelines so builders can control exactly which retrieval
  algorithms are used and how retrieval is integrated with their
  application
- Flexible integration with many kinds of language model and many ways
  of integrating — not locked into one provider or one pattern
- Explainability built in — trace answers back to the sources and
  reasoning that produced them

This is about the approach, not the implementation details. The
evaluator should leave this page thinking "that's a sensible
architecture" not drowning in component diagrams.

**Step 5: Spotlight — Retrieval methodologies.**
A focused page on how TrustGraph's retrieval strategies work and why
having multiple approaches matters. Graph RAG for relationship-rich
queries, Document RAG for broad semantic search, Ontology RAG for
domain-specific precision. Show how they differ, when you'd pick each,
and why having the choice is the point.

**Step 6: Spotlight — Explainability.**
Show how TrustGraph traces answers back to their sources. This is a
major differentiator — most RAG frameworks are black boxes. The
evaluator needs to see that they can understand and verify what the
AI is telling them.

**Step 7: Spotlight — Ontologies.**
Show how ontologies give you structured, domain-specific control over
knowledge extraction. This is about precision — instead of hoping the
LLM extracts the right things, you define what matters and TrustGraph
extracts accordingly.

**Step 8: How do people use TrustGraph?**
Use cases and real-world applications. The evaluator has understood the
technology — now they need to see themselves in it. Show concrete
scenarios: enterprise knowledge management, research analysis, agentic
AI systems, compliance-sensitive domains. Help them answer "is this
relevant to my problem?"

**Step 9: Open source positioning.**
TrustGraph is fully open source — what does that mean in practice?
No vendor lock-in, full auditability, self-host anywhere, community-
driven development. Position this as a deliberate choice, not a
limitation. For evaluators coming from proprietary alternatives, this
is either a dealmaker or they need reassurance about support and
maturity.

**Step 10: What next?**
The evaluator has the full picture. Give them clear exit points:
- "Ready to try it?" — link to the start of the Quick-starter journey
- "Need enterprise support?" — link to the TrustGraph Enterprise
  product page (commercial offering, managed support, SLAs)
- "Want to plan a production deployment?" — link to the Enterprise
  Planner journey

Don't leave them stranded. They've invested time reading — convert
that into action.

---

## 2. The Quick-starter

### Persona
A developer or technical user who wants to get TrustGraph running and
see what it can do. They may have come from the Curious Evaluator
journey and decided to try it, or they may have skipped straight here
because someone told them "just try it." They're comfortable with
Docker and the command line but don't want to read a manual first.
They want results fast — if it takes too long or requires too many
decisions, they'll abandon it.

### Goal
Go from zero to a working TrustGraph instance and run a meaningful
query against real data. They need to see it work with their own eyes
so they can decide whether to invest more time. Speed matters more
than understanding every detail.

### Snares

**Decision overload**: Before they can even start, they're asked to
choose an LLM provider, a graph store, a vector store, chunker
settings. They don't have the context to make these choices yet and
shouldn't need to.

**Too many prerequisites**: Python venv, CLI tools with version
matching, security tokens, config builder — each step is a point
where they might stall or hit an error.

**External tooling dependency**: The config builder is an external
web app. Sending the user off-site to generate config before they've
even started breaks the flow.

**No clear finish line**: They get it running but don't know what
"success" looks like. No sample query, no expected output, no
"you should see this" moment.

**Deployment guide masquerading as quickstart**: The compose page is
thorough and well-written, but it's a deployment reference, not a
quickstart. It covers every option rather than making opinionated
choices for the reader.

### Journey

**Step 1: Set the scene.**
Before diving into commands, tell them what's about to happen. You're
going to:
- Launch TrustGraph using Docker Compose / Podman Compose on a single
  machine — a laptop, workstation, or cloud instance will work
- Load some documents
- Do a bit of scripting to interact with the data
- Finish up in the web-based TrustGraph UI

Mention the minimal requirements (12GB+ RAM, 8 CPUs, Docker/Podman,
an LLM API key). If this isn't the right deployment option for them,
point to the deployment options page for Kubernetes, cloud platforms,
etc. — but don't dwell on it. Keep them moving.

**Step 2: Prepare the configuration.**
Generate the deployment config with opinionated defaults — pick
sensible choices for them (Cassandra, Qdrant, recursive chunking) so
they don't have to make decisions they can't yet understand. Walk
through the config builder, unpack the bundle, set the security token.
Keep it focused — this is prep, not a reference guide.

**Step 3: Launch TrustGraph.**
Start the containers. Docker Compose or Podman Compose, copy-paste
commands. Wait for startup. This should feel quick and
straightforward — they've done the prep, now it's just go.

**Step 4: Verify it's working.**
Run through some basic checks to confirm the system is up and the
LLM is plumbed in. Is the system healthy? Can it talk to the LLM?
Get a simple response back so they know the foundation is solid
before loading any data. Quick and reassuring — if something's
wrong, they need to know now, not after they've spent 20 minutes
loading documents.

**Step 5: Connect to the TrustGraph UI and run a prompt.**
Still a smoke test, but now they open the UI for the first
time, authenticate with their token, and fire off a simple LLM
prompt. This serves two purposes: confirms the UI is working end-to-
end, and introduces them to the UI before they need it for
real work. They've now seen the tool they'll be using.

**Step 6: Load sample documents and process one.**
Give them sample data so they don't have to find their own yet.
Load the documents, then walk them through processing one — running
it through the extraction pipeline so there's actual knowledge in the
graph. This is the first time something meaningful happens with real
data.

**Step 7: View the knowledge graph.**
Show them what was extracted — the entities and relationships that
TrustGraph built from the document. This is the "aha" moment where
they see it's not just chunks of text in a vector store, it's
structured knowledge.

**Step 8: Run a Graph RAG query and see explainability.**
Ask a question and get an answer. But the real payoff is showing
explainability — they can trace the answer back to the specific
knowledge graph nodes and source documents that produced it. This
is where the differentiators from the evaluator journey become
tangible. They've just seen the thing working.

**Step 9: Introduce ontologies.**
Brief explanation of what an ontology is and why it matters — you're
telling TrustGraph exactly what kinds of entities and relationships
to extract, instead of letting it guess. More precision, more
control, domain-specific knowledge extraction.

**Step 10: Load an ontology and process a document with it.**
Give them a ready-made ontology to load, then process a document
using it. Show the difference — the extracted knowledge is more
structured and domain-relevant compared to the ontology-free
extraction they did earlier.

**Step 11: "Feeling brave?" — build your own ontology.**
Optional side-quest. A brief look at how to create a custom ontology
using a code assistant. Not essential to the quickstart, but for the
curious it shows how accessible the process is — you don't need to
be an ontology expert to get started.

**Step 12: View the ontology-driven knowledge graph.**
Look at the knowledge graph produced from ontology extraction and
compare it with the earlier ontology-free result. Show how the graph
structure reflects the ontology — the entity types and relationships
match what was defined, not whatever the LLM happened to extract.
This makes the value of ontologies concrete rather than theoretical.

**Step 13: Introduce SPARQL and run a query.**
Now that they have structured knowledge in the graph, introduce
SPARQL as a way to query it precisely. Brief explanation — SPARQL
lets you ask exact questions about entities and relationships, not
just semantic similarity. Run a query against the ontology-driven
graph and show how the structured extraction makes precise querying
possible.

**Step 14: Explore the Context Graph viewer.**
Show them the Context Graph visualisation — an interactive view of
the knowledge graph showing how entities and relationships connect.
This brings the structured data to life and gives them a visual way
to understand what TrustGraph has built from their documents.

**Step 15: What next?**
They've deployed, loaded data, queried with Graph RAG, seen
explainability, used ontologies, run SPARQL, and explored the
Context Graph. Give them clear next steps:
- "Build an app" — link to the App Builder journey
- "Try your own documents" — point to the how-to guides for
  loading and processing custom data
- "Plan a production deployment" — link to the Enterprise Planner
  journey
- "Need enterprise support?" — link to TrustGraph Enterprise
- "Shut down" — how to cleanly stop and remove the containers

---

## 3. The App Builder

### Persona
A developer who has TrustGraph running — either from the Quick-starter
journey or an existing deployment — and now wants to build something
with it. They want to integrate TrustGraph's knowledge retrieval into
their own application. They're comfortable writing code and working
with APIs but don't know TrustGraph's integration points yet.

### Goal
Build a working application that uses TrustGraph for knowledge
retrieval. They need to go from "I have TrustGraph running" to "I
have my own app talking to it" with working code they can extend.

### Snares

**No tutorial exists**: The "Building with TrustGraph" guides are
almost entirely TODO. Developers hit the API reference with no
walkthrough to bridge the gap.

**Which integration to use?**: Python API, REST, WebSocket, CLI,
MCP — there are multiple ways in, but no guidance on which to pick
for what situation.

**No working examples**: API reference documents the interface but
doesn't show how to assemble the pieces into something real.

**Jump from UI to code**: The Quick-starter shows everything
in the UI. There's no bridge showing how to do the same things
programmatically.

### Journey

**Step 1: Set the scene.**
Explain what this journey covers: you're going to build a simple
application that connects to TrustGraph, loads a document, queries
it with Graph RAG, and handles the response — all in code.
Prerequisites: a running TrustGraph instance (link back to
Quick-starter or compose guide if they don't have one) and a
correctly configured Node.js / npm environment.

**Step 2: Clone the UI repo and run it locally.**
Check out the trustgraph-ui repository and run `npm run dev` to get
the TrustGraph UI running locally in development mode. This gives
them a working codebase they can modify and see changes immediately
— a much better starting point than building from scratch.

**Step 3: Clone the plugin template and build it.**
Check out the ui-plugin-template repository — this is a starter
template for building a TrustGraph UI plugin. Build the plugin
so it's ready to load.

**Step 4: Link the plugin into the UI and verify it loads.**
Modify the local trustgraph-ui setup to include the plugin, then
check that it loads and runs correctly in the dev environment. This
confirms the plugin architecture is working before they start
customising anything.

**Step 5: Make a small change and verify the round-trip.**
Do something trivial — change a label, add a line of text — rebuild
the plugin and confirm the change appears in the running UI. This
proves the edit-build-reload cycle works before they invest time on
real functionality.

**Step 6: Build an ontology for the scenario.**
This is a data-first process — before writing app code, define what
knowledge you want to extract.

The scenario we're building: an **Office Onboarding & "Who Knows
What?" Bot**. Index a company's internal tools, team roles, project
ownership, and Slack channels. The quickstart query: "Who owns the
payment gateway service, and who can approve my access?" This works
because everyone understands office hierarchy and tool access — it
showcases a simple 3-hop relationship (Employee → Role → Service →
Approver) using an everyday workplace scenario.

Provide a prompt they can paste into a code assistant to generate
an ontology for this domain. No need to write it by hand — the
code assistant does the heavy lifting, and they get to see how
accessible ontology creation is. Also provide a ready-made OWL
ontology for those who don't have a code assistant available.

**Step 7: Load the ontology into TrustGraph and check it.**
Load the OWL ontology and verify it looks right — check the entity
types and relationships are what you'd expect for the office
onboarding domain.

**Step 8: Generate a knowledge graph with a code assistant.**
Rather than loading documents and extracting knowledge (which
they've already seen in the Quick-starter), we take a different
track here to show an alternative data acquisition approach. Guide
the user through a code assistant session where they generate a
knowledge graph directly in Turtle format — structured data
describing the office's teams, tools, services, and ownership
relationships, conforming to the ontology they just loaded.

*Side-quest option:* if they'd prefer the document-driven approach,
point them to loading documents through ontology processing instead
— they already know how from the Quick-starter.

**Step 9: Load the Turtle data and explore the knowledge graph.**
Use the CLI to load the Turtle file into TrustGraph. Then look at
the knowledge graph — browse the entities, check the relationships,
verify the data matches what was generated. They should see the
office structure: employees, roles, services, approvers, all
connected as defined by the ontology.

**Step 10: Generate documentation and SPARQL queries.**
Back to the code assistant — using the ontology it generated, get
it to produce two reference files: an `ONTOLOGY.md` documenting the
ontology's entity types and relationships, and a `QUERIES.md`
documenting how to query the knowledge graph with SPARQL, including
example queries for the onboarding scenario. This shows a powerful
workflow: the ontology drives not just extraction but also
documentation and query generation.

**Step 11: Run a SPARQL query.**
Take one of the generated queries and run it against TrustGraph —
for example, "Who owns the payment gateway service, and who can
approve my access?" See the structured results come back from the
knowledge graph. Run a few more queries from the generated
`QUERIES.md` to build confidence that the data is structured
correctly and queryable.

**Step 12: Design the UX.**
Use the code assistant to suggest UX journeys for the onboarding
bot — what screens, what interactions, what the user flow looks
like. For example: a search bar to find a service, a detail view
showing the owner and approver chain, a team browser. Get concrete
suggestions that can be coded up in the plugin.

**Step 13: Build the plugin, one step at a time.**
Start coding the plugin using the code assistant. Key guidance:
work incrementally — make a change, rebuild, check it in the UI
before moving on. Don't try to build the whole thing in one go.

For the onboarding bot, the user can start with the `FlowView`
component to wire up an interactive query flow — a natural fit for
the "who owns this service?" conversational pattern. Build out the
UX journeys from step 12 one at a time, verifying each round-trip.

**Step 14: What next — shipping to production.**
Brief overview of what's needed to move from dev mode to a running
TrustGraph deployment — building the plugin for production,
packaging it into the container image, and configuring the
plugins.json manifest. Keep it light — point to the relevant
reference docs rather than walking through it in detail. The goal
is to show them the path exists, not to cover it end-to-end here.

**Step 15: Understanding the library layers.**
Explain the published npm packages so they know what's available
beyond the plugin approach:
- `@trustgraph/client` — low-level WebSocket client for talking to
  TrustGraph directly. Use this if you want full control and are
  building without our state management
- `@trustgraph/react-state` — generic React state management layer
  with no UX opinion. Handles connections, queries, and data flow
  but imposes no visual style
- `@trustgraph/trustkit` — component library with ready-made UI
  components built on top of react-state

This means a developer could build something using a completely
different UX toolkit or framework — they're not locked into our
component style. Pick the layer that fits their needs.

**Step 16: What next?**
They've built a working plugin from scratch. Give them clear
next steps:
- "Go deeper with ontologies" — link to ontology reference and
  advanced extraction guides
- "Explore the API reference" — for building beyond the plugin
  framework
- "Plan a production deployment" — link to the Enterprise Planner
  journey
- "Need enterprise support?" — link to TrustGraph Enterprise
- "Join the community" — Discord, contributing guidelines

---

## 4. The Agent Builder

### Persona
A developer building agentic AI systems who wants to use TrustGraph
as the knowledge backbone. They understand LLM agents and tool use
but want to see how TrustGraph's retrieval, agent orchestration, and
tool integration work in practice.

### Goal
Build an agent that can retrieve knowledge from TrustGraph, use
tools, and answer complex questions — then understand the enterprise
features that make this production-ready.

### Snares

**MCP guide is outdated**: The existing MCP integration page is
marked TODO with "needs complete rewrite." Agents are a key use
case with no working guide.

**Agent configuration is undocumented**: The agent orchestrator
supports multiple patterns (ReAct, Plan-then-Execute, Supervisor)
but there's no walkthrough of how to configure and use them.

**Tool integration is unclear**: TrustGraph supports MCP tools,
built-in tools, and custom tool services, but there's no guide
showing how they fit together.

### Journey

**Step 1: Set the scene.**
Explain what this journey covers: setting up a retrieval scenario
with data and an ontology, configuring the agent engine, wiring
up tools, and understanding the enterprise attestation advantage.
Prerequisites: a running TrustGraph instance with some knowledge
loaded (link back to Quick-starter if needed).

**Step 2: Set up a retrieval scenario.**
Load a dataset and ontology suited to an agentic use case —
something where multi-step reasoning matters. Process the
documents so there's a populated knowledge graph to work with.

**Step 3: Configure the agent engine.**
Walk through the agent orchestrator configuration — selecting a
pattern (ReAct, Plan-then-Execute, Supervisor), setting up the
agent's system prompt, and tuning parameters. Run a query and
see the agent reason through a multi-step answer.

**Step 4: Add tools.**
Wire up a couple of built-in tools so the agent can do more than
just retrieve knowledge. Show how the agent discovers tools at
runtime and uses them as part of its reasoning loop.

**Step 5: Add an MCP tool.**
Integrate a Model Context Protocol tool — showing how external
capabilities can be connected to the agent. This demonstrates
TrustGraph's interoperability with the broader MCP ecosystem.

**Step 6: Build a custom tool service.**
Create a custom tool service that the agent can call. This shows
the extensibility model — developers can add domain-specific
capabilities without modifying core TrustGraph code.

**Step 7: The attestation engine — enterprise advantage.**
Explain what the attestation engine solves: in enterprise and
regulated environments, it's not enough for an agent to give an
answer — you need verifiable proof of how it got there. The
attestation engine provides cryptographic attestation of the
reasoning chain, tool invocations, and source data. This is the
bridge from "cool agent demo" to "production-ready enterprise
system." Link to TrustGraph Enterprise for the commercial
conversation.

**Step 8: What next?**
Clear exit points:
- "Plan a production deployment" — link to the Enterprise Planner
  journey
- "Need enterprise support?" — link to TrustGraph Enterprise
- "Explore the API reference" — for deeper agent integration
- "Join the community" — Discord for ongoing support

---

## 5. The Enterprise Planner

### Persona
An architect or technical lead who has already evaluated TrustGraph
and decided it's the right fit. Now they're planning a production
deployment — reviewing the resources, infrastructure, and commercial
options available to make it happen at scale.

### Goal
Understand everything needed to go from proof-of-concept to
production: infrastructure requirements, enterprise features,
deployment options, and support. Leave with a clear picture of
what a production deployment looks like and what commercial
options are available.

### Snares

**No clear production path**: The docs cover getting started well
but don't clearly articulate what changes between a dev deployment
and a production one — what scales, what doesn't, what needs
replacing.

**Enterprise features are invisible**: RBAC, attestation engine,
and other enterprise edition features aren't surfaced in a way
that lets a planner understand the upgrade path from open source.

**Deployment options scattered**: Kubernetes, cloud platforms, and
scaling considerations are spread across multiple pages with no
unified planning view.

**No commercial context**: The planner needs to understand support
options, SLAs, and long-term viability — information that lives
outside the technical docs.

### Journey

**Step 1: What does a production deployment need?**
Start with the infrastructure picture for large-scale deployment.
Resource requirements, what components need to scale, storage
considerations, network architecture. What's different from the
single-machine compose setup they've been running.

**Step 2: Enterprise edition features.**
Overview of what the TrustGraph Enterprise edition adds beyond
the open source platform. This is the upgrade path — what do you
get, and why does it matter for production use.

**Step 3: Enterprise RBAC use cases.**
Show how fine-grained role-based access control works in practice.
Use cases: teams with different access levels, read-only analyst
roles, admin separation, workspace isolation between departments
or clients.

**Step 4: Attestation engine use cases.**
Show what the attestation engine provides — verifiable proof of
how answers were derived, audit trails, compliance requirements.
Use cases: regulated industries, legal, finance, healthcare where
you need to prove the provenance of AI-generated answers.

**Step 5: Deployment options.**
Walk through the production deployment options: Kubernetes
(Minikube, AWS, Azure AKS, GCP, Scaleway, OVHcloud), cloud-
specific considerations, GPU deployment for self-hosted models.
Help them match their infrastructure to the right deployment
approach.

**Step 6: Long-term support options.**
Commercial support, SLAs, managed services, training, and
consulting. What does the ongoing relationship look like? Link
to TrustGraph Enterprise for the commercial conversation.

**Step 7: What next?**
Clear exit points:
- "Get in touch" — link to TrustGraph Enterprise contact /
  sales page
- "Start a production deployment" — link to the relevant
  deployment guide for their chosen infrastructure
- "Review security" — link to security documentation
- "Join the community" — Discord for ongoing support

---

## 6. The Operator

### Persona
A DevOps engineer, platform engineer, or developer responsible for
a running TrustGraph instance. They've got it deployed — now they
need to keep it healthy and understand what to watch.

### Goal
Understand how to monitor a running TrustGraph deployment, manage
LLM costs, and know what to pay attention to. Leave with a clear
picture of what "healthy" looks like and where to find help when
things go wrong.

### Snares

**No operations landing page**: There's no single place that says
"you're running TrustGraph, here's what you need to know."

**Metrics without context**: Dashboards exist but there's no
guidance on what the numbers mean or what thresholds to worry about.

**LLM costs are opaque**: Token usage is tracked but there's no
guidance on managing costs or understanding consumption patterns.

### Journey

**Step 1: What should operators care about?**
Orientation page covering the key concerns for running TrustGraph:
system health, LLM token usage and costs, storage growth, flow
performance. Set expectations — what needs active monitoring vs
what takes care of itself.

**Step 2: Metrics and dashboards.**
Walk through the Grafana dashboards — what's there, what the key
metrics mean, what healthy looks like. Cover the system-level
metrics (container health, resource usage) and the TrustGraph-
specific metrics (request latency, extraction pipeline, store
operations).

**Step 3: LLM metrics and token management.**
Focused look at LLM-specific observability: token consumption per
request, per flow, per workspace. Understanding cost drivers —
which operations are token-heavy (extraction vs queries), how to
spot unexpected usage, and how to tune token budgets.

**Step 4: Common questions and further resources.**
Q&A-style section covering the things operators typically need:
- How do I manage users and workspaces?
- How do I back up / export a workspace?
- How do I upgrade TrustGraph?
- How do I troubleshoot a failed extraction?
- How do I manage flows and collections?

Each answer is brief with links to the relevant reference docs,
CLI commands, or guides. This is the hub — they'll come back here
when they need something specific.

