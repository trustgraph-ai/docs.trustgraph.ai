---
title: Changelog - TrustGraph UI
nav_order: 2
parent: Reference
grand_parent: TrustGraph Documentation
review_date: 2027-06-10
---

# Changelog - TrustGraph UI

TrustGraph UI (`trustgraph-ui`) is the replacement for the
[Workbench UI](workbench), which was deprecated in TrustGraph v2.4.

## v0.2.4 (2026-06-10) — released in TrustGraph 2.5

### Features
- **SPARQL Workbench**: Interactive SPARQL query editor with
  syntax-highlighted results table, error reporting, and query history
- **GraphQL Workbench** (#9): GraphQL query page with editor, presets,
  and table/raw result views for structured data queries
- **Config-Driven Query Presets** (#9): Preset/example query support
  for SPARQL, Graph RAG, and Agent pages, driven by config-svc entries
  (type `query`, keyed by language)
- **Workspace/Collection/Flow Switcher**: Header workspace switcher
  with live workspace, collection, and flow pills driven by IAM
  (`whoami`, `list-my-workspaces`) over the authenticated WebSocket;
  all post-auth calls scoped to the active workspace; ~40 hardcoded
  `flow("default")` and `COLLECTION` references replaced with live
  session/settings reads; workspace-scoped query caches wiped on switch
- **Demo Pages**: Solar System Missions (top-down ecliptic
  visualisation of spacecraft trajectories via SPARQL) and World Events
  Explorer (geo-temporal event viewer with map, timeline range brush,
  and type filtering) split into a dedicated Demos page with header
  navigation

### Bug Fixes
- **Multi-Response Workspace Stamp** (#8): `makeRequestMulti` was not
  attaching the active workspace to outbound messages, so streaming
  operations (SPARQL queries, agent, document streaming, graph/document
  RAG) always hit the token's default workspace
- **Catch-All API Proxy**: Added generic `/api/v1` proxy for unhandled
  gateway endpoints that previously fell through to the static file
  handler, returning 405
- **WebSocket Proxy** (#7): Detect `Upgrade: websocket` header in the
  `/api/v1` catch-all and proxy as a full bidirectional WebSocket
  (needed for bulk import/export paths)
- **Empty Query String** (#7): Guard against appending bare `?` when
  query string is empty on import-core, export-core, and socket
  handlers
- **Dropdown Transparency** (#9): Fixed dropdown menu transparency
  making text unreadable
- **Status Bar Overlap** (#9): Fixed status bar overlapping page
  content using `--page-height` CSS variable

### Infrastructure / Technical
- **API URL Unification**: Frontend socket path changed from
  `/api/socket` to `/api/v1/socket`; Vite proxy rewrites removed in
  favour of a single `/api/v1` pass-through

---

## v0.1.1 (2026-05-21) — released in TrustGraph 2.4

### Features
- **Agent Console**: Agent query interface with streaming responses and
  explainability event tracking
- **GraphRAG View**: Interactive graph RAG query interface with
  explainability DAG visualisation and inline provenance display
- **Document RAG View**: Document retrieval query interface
- **Knowledge Explorer**: Interactive knowledge graph explorer with
  dynamic graph loading, 3D view, multiple navigation views, edge
  pulse animation, and dynamic property loading with BFS neighbourhood
  extraction
- **Document Ingestion**: Document upload and submission workflow with
  file uploading, page/chunk inspection, and document structure
  browsing
- **Flow Management**: Flow creation and detail views with configurable
  parameters, controlled-by relationships, temperature controls, and
  grouped storage column layout
- **Prompt Editor**: Prompt editing workflow
- **Workspace UX**: Workspace selection and management
- **Schema Workbench** (#1): Interactive schema management with list,
  create, edit, and delete operations including field and index
  management
- **Ontology Workbench** (#1): Full ontology editor with class/property
  trees, metadata editor, and validation panel:
  - OWL/XML and Turtle import with tokenizer support for real-world
    ontologies
  - OWL/XML, RDF/XML, and Turtle export with round-trip fidelity
  - Ontology validator covering metadata, class references, property
    references, and circular dependency detection
  - Safe delete UX with confirmation dialogs
- **Component and Patterns Library**: Shared UI component library and
  reusable workflow patterns with demo workflow selector
- **Home Page**: Workflow card grid for navigating available features

### Bug Fixes
- **JPEG Image Support** (#2): Added missing `.jpg`/`.jpeg` content
  type handling in the container static file server

### Infrastructure / Technical
- **Python Container Service**: Static file serving with auth proxying
- **Test Suite**: 160 tests covering importers, exporters, validator,
  schema validation, explain parsing, URI helpers, theme colours, and
  graph data helpers
- **Apache 2 Licence**
