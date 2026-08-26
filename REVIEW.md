# Documentation User Journeys

Working document to map out the ideal user journeys through the docs,
identify gaps, and plan improvements.

## Personas

### 1. The Curious Evaluator
**Who**: Technical decision-maker, architect, or developer who's heard about
TrustGraph and wants to understand what it is and whether it's relevant.

**Goal**: Understand what TrustGraph does, how it compares to alternatives,
and whether it's worth trying.

**Current path**: Homepage "Learn" box -> Introduction -> Philosophy ->
Retrieval -> Features -> Use Cases

**What works**: The overview section is fairly complete and covers the
conceptual ground well.

**What's missing**:
- No clear "why TrustGraph over just using a vector DB?" comparison
- Use Cases page doesn't link to specific guides for each use case
- No path from "I'm convinced" to "let me try it" — the evaluator has to
  go back to the homepage and pick another pathway

**Ideal journey**:
Overview/Introduction -> Philosophy -> Retrieval Strategies -> Features ->
Use Cases -> **"Ready to try it? Start here" link to Quickstart**

---

### 2. The Quick-starter
**Who**: Developer or technical user who wants to get TrustGraph running
and see what it can do, as fast as possible.

**Goal**: Go from zero to a working query in the shortest possible time.

**Current path**: Homepage "Try it out" box -> Compose deployment page ->
Graph RAG guide (separately) -> Document RAG guide (separately)

**What's broken**:
- There is no actual quickstart page — the "Quickstart" pathway just links
  to the full compose deployment reference, which is thorough but
  overwhelming for a first-timer
- User must make decisions they don't have context for yet (LLM provider,
  graph store, vector store, chunker settings)
- Config builder is an external tool with no guidance on what to pick
- Security token setup feels heavy for someone just exploring
- After deployment, the "Next Steps" section just says "see Guides" with
  no specific direction
- No sample query results shown — user doesn't know what success looks like

**Ideal journey**:
Quickstart (single page) ->
  1. Prerequisites (Docker/Podman, Python, one LLM key)
  2. Deploy with opinionated defaults (copy-paste commands, no choices)
  3. Verify it's running
  4. Load a sample document
  5. Run a Graph RAG query, see results
  6. Run a Document RAG query, see results
  7. "What just happened?" (brief explanation)
  8. Next steps: explore the Workbench, try your own documents, learn about
     retrieval strategies, build an app

**Action needed**: Create a dedicated Quickstart page that is opinionated
and linear. The compose page stays as the full deployment reference.

---

### 3. The App Builder
**Who**: Developer who has TrustGraph running and wants to build something
with it — an app, an integration, an agent.

**Goal**: Build a working application that uses TrustGraph for knowledge
retrieval.

**Current path**: Homepage "Developer integration" box -> Compose ->
Knowledge Graphs -> Graph RAG -> API Reference -> MCP Integration

**What's broken**:
- The "Building with TrustGraph" guide section is almost entirely TODO
  (introduction, CLI tools, React, TypeScript, custom processing,
  explainable AI)
- MCP Integration is TODO ("needs complete rewrite")
- The path jumps from "here's how RAG works in the Workbench" to "here's
  the API reference" with nothing in between
- No "build your first app" tutorial
- No working code examples showing how to integrate TrustGraph into a
  real application
- No guidance on which API/SDK to use for what

**Ideal journey**:
Deploy (quickstart or compose) ->
  **Build Your First App** (new page) ->
    1. Overview of integration options (Python API, CLI, REST, MCP)
    2. Install the Python client library
    3. Connect to TrustGraph
    4. Load a document programmatically
    5. Query with Graph RAG via the API
    6. Handle the response in your app
    7. Next steps: advanced queries, custom processing, MCP for agents

  Then branch to:
  - Python API deep dive (reference/apis)
  - CLI automation (when cli-tools guide is updated)
  - MCP for agentic systems (when rewritten)
  - React/TypeScript frontend (when guides exist)
  - Custom processors (when guide exists)

**Action needed**:
- Create a "Build Your First App" guide using current Python API
- Update the developer pathway on the homepage to route through it
- Prioritise the building/* TODO pages

---

### 4. The Enterprise Planner
**Who**: Technical lead, architect, or DevOps engineer planning a production
deployment.

**Goal**: Understand deployment options, security, scalability, and
operational requirements.

**Current path**: Homepage "Plan a production deployment" box ->
Introduction -> Use Cases -> Maturity -> Security -> Choose Deployment

**What's broken**:
- Security overview is TODO
- Production considerations page is TODO
- No Day 2 operations guidance (monitoring exists but is isolated)
- No capacity planning or scaling guidance
- No multi-tenancy / workspace setup guide
- Managing-users guide is empty
- Deployment index doesn't link to operational guides

**Ideal journey**:
Introduction -> Use Cases -> Maturity -> Security (complete) ->
Architecture -> **Production Planning** (new or updated page) ->
  - Deployment options comparison
  - Capacity & resource planning
  - Security & authentication setup
  - Workspace / multi-tenancy configuration
  - Monitoring & observability
  - Backup & recovery
  - Scaling considerations

**Action needed**:
- Complete security.md
- Complete production-considerations.md
- Create operations/Day 2 content
- Add cross-links from deployment pages to operational guides

---

### 5. The Operator
**Who**: DevOps/platform engineer or developer managing a running TrustGraph
instance.

**Goal**: Manage documents, flows, users, workspaces, monitor health, and
troubleshoot issues.

**Current path**: No clear entry point — user has to find relevant guides
in the nav sidebar.

**What's broken**:
- Flows guide is TODO (Workbench UX mismatch)
- Context cores guide is TODO (Workbench UX mismatch)
- Managing-users is empty
- Monitoring guide exists but isn't connected to an operations pathway
- No troubleshooting guide beyond the compose page's section
- No "common tasks" landing page for operators

**Ideal journey**:
**Operations Hub** (new section or landing page) ->
  - Managing documents & collections
  - Managing flows
  - Managing users & workspaces
  - Monitoring & dashboards
  - Troubleshooting common issues
  - CLI reference for operational tasks

**Action needed**:
- Complete flows and context-cores guides
- Create managing-users content
- Consider an operations landing page
- Add troubleshooting content

---

## Cross-cutting Issues

### Missing connective tissue
Pages tend to end without directing the user to the next logical step.
Every page should answer "what should I do next?" with specific links,
not generic "see Guides."

### TODO pages in critical paths
14 pages marked TODO, many in high-traffic paths (building/*, MCP,
security, production, flows, context-cores). These create dead ends
in otherwise well-structured journeys.

### Homepage paths promise more than they deliver
The pathway boxes look polished but several cards link to incomplete
or TODO content. The paths need to be validated end-to-end.

### No "Build an App" content
The biggest single gap. Users who want to integrate TrustGraph have
to reverse-engineer the API reference with no tutorial guidance.

---

## Priority Order

1. **Quickstart page** — highest impact, unblocks the most common journey
2. **Build Your First App guide** — unblocks the developer journey
3. **Fix "next steps" links across all pages** — low effort, high impact
4. **Complete building/* TODO pages** — unblocks developer pathway
5. **Complete security & production pages** — unblocks enterprise pathway
6. **Operations content** — unblocks operator pathway
