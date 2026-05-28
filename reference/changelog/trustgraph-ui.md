---
title: Changelog - TrustGraph UI
nav_order: 2
parent: Reference
grand_parent: TrustGraph Documentation
review_date: 2027-05-21
---

# Changelog - TrustGraph UI

TrustGraph UI (`trustgraph-ui`) is the replacement for the
[Workbench UI](workbench), which was deprecated in TrustGraph v2.4.

## v0.1.1 (2026-05-21) - released in TrustGraph 2.4

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
