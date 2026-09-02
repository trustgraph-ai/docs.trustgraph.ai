---
title: TrustGraph UI
nav_order: 2
parent: Changelogs
review_date: 2027-07-17
---

# Changelog - TrustGraph UI

## v2.0.3 (2026-08-24) — released in TrustGraph 2.8

### Architectural Changes
- **Monorepo Consolidation** (#56, #59): Dependency libraries previously
  published from separate GitHub repos are now consolidated into this
  repository monorepo-style using npm workspaces. Published packages:
  `@trustgraph/client`, `@trustgraph/react-provider`,
  `@trustgraph/react-state`, `@trustgraph/trustkit`. Automatic version
  stamping from git tags at publish time with npm provenance
  verification. The `packages/demo` directory renamed to
  `packages/portal` to reflect its role as the main application shell
- **Plugin Architecture** (#44, #45, #46, #47, #52): Manifest-driven
  plugin system with IIFE-based dynamic loading. 10+ demo explorers
  migrated from hardcoded builtins to dynamically loaded plugin
  packages. Shared libraries (React, trustkit) provided via
  `window.TrustKitShared` globals to ensure a single React instance.
  Support for multi-component bundles, remote plugins, and customer-
  configurable UI via volume-mounted `plugins.json`. Plugin development
  guide included

### Features
- **Runtime Theme System** (#38, #40, #41, #42, #54, #55): Complete
  migration from static colour imports to runtime `useTheme()` hook.
  Five theme presets: Dark (default), Midnight, Light, High Contrast,
  and Warm. Deep-merge theme override system with `ThemeContext`
  provider. Scalable typography via `sz()` scale helper with
  localStorage persistence. Theme selector in header toolbar dropdown
- **Generic UI Component Library** (#49, #50, #58): Reusable themed
  components extracted from duplicated inline styles — Input, Button,
  Select, Card, QueryWorkbench, SplitPane, DetailPanel, EmptyState,
  ModeSelector, Toolbar, PageLayout, GraphCanvas3D, and others.
  ~287 hardcoded font string occurrences replaced with theme tokens
- **Threat Explorer** (#33): Interactive investigation workbench for
  OCSF insider-threat analysis from knowledge graph data. Two-layer
  architecture: SPARQL for risk relationships, GraphQL for raw event
  drill-down. 12 risk event subtypes supported. Pivot breadcrumb trail
  with contextual AI analysis, investigation view with finding chain,
  and AI-powered incident report / response plan generation
- **3D Graph Visualisation** (#36): `GraphCanvas3D` component with
  perspective projection, domain clusters distributed on sphere using
  golden spiral placement, camera controls (drag, scroll, right-drag),
  and depth cues (perspective scaling, opacity falloff, z-sorting).
  ExploreView includes 2D/3D mode selector
- **Schema Index Split** (#34): Single `indexes` field split into
  `query-indexes` (exact-match) and `vector-indexes` (semantic search)
  with colour-coded UX
- **Prefix-Based Prompt Discovery** (#48): Replaced `template-index`
  configuration with automatic discovery via `template.` prefix filter,
  removing the index update step from create/delete operations

### Improvements
- **Incremental Data Loading** (#37): Law Explorer rewritten for
  fully incremental loading — no upfront bulk load, per-language
  caching, instant revisits. Socket readiness guards added to all data
  hooks across explorers. Animated loading spinners with mode-specific
  accent colours
- **Search Result Highlighting** (#31): Matched fields highlighted in
  structured data search results with tinted background, accent border,
  and bold value text. Composite index support via `index_name`
  splitting
- **Guidance System** (#53): Guidance context provider with
  `GuidanceSlot` anchor components, dismissible markdown popovers with
  version-aware localStorage persistence, and `ActionButtonBar` for
  config-driven toolbar buttons
- **Default API Port** (#43): Local dev port changed to 8888 to match
  updated API gateway default

### Bug Fixes
- **Light Theme Contrast** (#42, #55): Fixed light-mode contrast
  issues throughout the application, including Solar Mission side panel
  using hardcoded dark background
- **ESLint Config** (#41): Root ESLint config updated to exclude
  TypeScript sub-packages and plugin build output
- **CI Test Workflows**: Removed incorrect `-- --run` flag from npm
  test CI workflows

### Infrastructure / Technical
- **Plugin Build Pipeline** (#45): Plugin packages added to CI build
  chain; monorepo npm publish workflow publishes all four public
  packages on tag push; removed dead per-package workflow directories
- **Testing**: Updated `@vitest/ui` to ^4.1.10 to match vitest (#51)
- **Static File Serving** (#46): Added JSON file serving for
  `plugins.json` loading

---

## v0.3.12 (2026-07-17) — released in TrustGraph 2.6

### Features
- **Client-Side Routing** (#22): Adopted react-router so browser
  back/forward buttons, deep links, and page refresh all work correctly;
  header logo/title is now clickable to navigate home
- **Cross-Encoder Explainability** (#15): Updated explainability views
  to match the backend's switch from LLM-based edge scoring to
  cross-encoder reranking — `tg:reasoning` replaced with `tg:concept`
  (matched query concept) and `tg:score` (relevance score) across all
  parsers, types, renderers, graph tooltips, and tests
- **Subway-Map Pathway Finder** (#28): Replaced the flat per-path card
  layout with a merged, interactive subway-map DAG visualisation that
  consolidates all discovered paths into a single directed acyclic
  graph, revealing hub nodes and chokepoints at a glance
- **Innovation Intelligence Explorer** (#27): Full-featured ecosystem
  explorer with Browse (filterable entity list with category tabs),
  Pathway Finder (DFS-based pathfinding with edge type filters), and
  GTM Advisor (structured go-to-market analysis with streamed strategy
  report generation)
- **Risk Explorer** (#29): Master-detail risk domain viewer showing
  actors, risks, assets, events, processes, and process steps with
  search, risk-score bars, event-date badges, and navigable
  relationship links
- **Game Theory Explorer** (#30): Interactive game tree visualisation
  with backward induction, payoff matrix with Nash Equilibrium
  detection and heatmap, and sandbox mode with live sliders for
  real-time equilibrium recalculation
- **Law in Context Explorer** (#31, #32): Five-mode legal explorer
  (overview, institutions, rights, compliance, structure) with EN/LT
  language toggle, multi-law browsing, and flexible document tree
  handling
- **Brand Analytics Demo** (#12): Brand analytics demo page
- **Retail Demo** (#11): Retail demo with decision traces and product
  hover cards

### Improvements
- **UX Improvements** (#10): Workspace recovery from stale
  sessionStorage, delete/discard buttons on Document Ingest page,
  fielded input mode for prompt test panel (Fields/JSON toggle with
  improved Jinja variable extraction), delete and fielded argument
  editor for agent console
- **Dependency Updates** (#24): TypeScript 6, ESLint 10, vitest 4,
  eslint-plugin-react-refresh 0.5; npm audit resolves all advisories
- **Multi-Arch Container Builds** (#17): amd64 and arm64 builds with
  CI release workflow on native runners

### Bug Fixes
- **SPARQL Collection Routing** (#26): All SPARQL queries across demo
  hooks and the SPARQL workbench were missing the collection parameter,
  causing queries to always hit the default collection regardless of
  the active selection
- **Agent DAG Hang and Retry Storms** (#16): Fixed infinite loop in
  Full DAG explainability view caused by `prov:wasGeneratedBy`
  back-edges; fixed false derivation edges from triples attributed to
  wrong subjects; fixed agent retry storms by switching to single
  attempt with 180s timeout
- **Streaming Error Crash** (#14): Gateway top-level errors arrived as
  `{message, type}` objects but all six streaming receivers typed them
  as strings, causing React to crash with a blank screen; added
  `errorToString()` normalisation
- **RAG Streaming Timeouts** (#21): Increased GraphRAG and DocumentRAG
  streaming timeouts from 60s to 180s and disabled retries, matching
  agent query settings
- **Upload Chunk Size** (#19): Reduced upload chunk size from 5MB to
  2MB to stay within Pulsar's ~3MB message size limit after Base64/JSON
  encoding inflation
- **Triple Writer Reconnect Loop** (#23): WebSocket was reopened every
  2s even with nothing to send; connections now only open when there
  are triples to flush
- **default_workspace Rename** (#13): Aligned with backend IAM rename
  of `workspace` → `default_workspace` on user records and auth frames

---

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
