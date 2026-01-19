---
title: Changelog - Workbench
nav_order: 2
parent: Reference
grand_parent: TrustGraph Documentation
review_date: 2026-01-15
---

# Changelog - Workbench UI

## v1.5.5 (2026-01-19) - released in TrustGraph 1.8

### Enhancements
- **Nomenclature Update** (#115): Renamed "flow class" to "flow blueprint"
  throughout the UI for consistency with backend terminology.
- **Light/Dark Mode Fixes** (#121): Fixed color modes in flow blueprint
  viewer and ontology editor for proper theming support.

### Bug Fixes
- **WebSocket Proxy Auth** (#112): Fixed gateway authentication error by
  passing query string through websocket proxy.
- **GraphRAG Client** (#113): Updated dependencies to pull in GraphRAG
  client fix.
- **Graph View** (#114): Fixed graph view issues by rolling back problematic
  dependencies while keeping TrustGraph deps current; also fixed critical
  vulnerability.
- **Flow Blueprint Issues** (#117, #118): Fixed flow blueprint layout and URL
  routing issues.
- **Dialog List** (#119): Fixed dialog list fault.
- **Knowledge Core Loading** (#120): Fixed load kg-core ignoring collection
  parameter.

---

## v1.4.1 (2025-12-04) - released in TrustGraph 1.6

### Features
- **Stream LLM Interactions** (#110): Added streaming support for LLM
  interactions for real-time response display.

### Enhancements
- **Agent Dialog UI** (#111): Improved agent dialog by collapsing agent thinking and observation messages for a cleaner interface.

---

## v1.3.7 (2025-11-23) - release in TrustGraph 1.5

### Features
- **LLM Models** (#98): Added LLM model selection support.
- **MCP Auth Token UX** (#108): Added MCP authentication token user interface.

### Bug Fixes
- **Multi Ontology Import** (#109): Fixed issues with importing multiple ontologies.
- **Flow Class Viewer Crash** (#104): Fixed crash in flow class viewer.
- **Socket Provider** (#105): Fixed socket provider issues.

### Performance Improvements
- **Faster System UI** (#100): Improved system UI performance.

### Maintenance
- **Library Breakout** (#99): Refactored library into separate modules.
- **Module Updates** (#102): Updated to new modules.
- **React State Bump** (#106): Updated react-state dependency.
- **Ontology Editing** (#103): Minor improvements to ontology editing and parsing.
- **Fallback Route** (#101): Fallback route now serves the index page.

---

## v1.2.6 - released in TrustGraph 1.4

### Features
- **Flow Class Visual Editor** (#90): New visual viewer for flow classes.
- **Flow Parameters** (#93, #95): Added flow parameters with advanced parameters section support.
- **Collections Dialogue** (#96): New collections management dialogue.
- **Collection Selectors** (#97): Added collection selector components.

### Bug Fixes
- **Workbench Breakage** (#92): Fixed workbench breakage issues.
- **Dedupe Flow Classes Pages** (#94): Fixed duplicate flow classes pages.

### Enhancements
- **OWL Ontology Editor** (#91): Updated ontology editor to support OWL format.

---

## v1.1.6 - released in TrustGraph 1.3

### Features
- **Structured Query Page** (#79): New page for structured queries.
- **Structured Query Tool Type** (#80): Added structured query tool type on agent tools page.
- **Tools Groups and States** (#83): Added tool grouping and state management.
- **Collection Settings** (#81, #82): Collection is now a configurable setting with support for structured query collections.

### Bug Fixes
- **Search Issues** (#85, #88, #89): Fixed collection not used in search, empty search results handling, and needing to search twice.
- **Graph View Collection** (#87): Fixed use of collection in graph view.
- **Relationships Collection** (#86): Fixed relationships collection not being used.
- **Default Settings** (#84): Fixed default trustgraph/user settings.

### Maintenance
- **Taxonomy → Ontology** (#75): Renamed taxonomy to ontology throughout.
- **Dependency Pinning** (#77): Locked react-force-graph to 1.46.x.

---

## v1.0.5

### Features
- **MCP Tool Arguments** - Enhanced Model Context Protocol tool integration with improved argument handling (#73)
- **Gateway Secret Implementation** - Added secure gateway authentication mechanism (#66)
- **Settings Page** - New dedicated settings management interface (#64)
- **Taxonomy Management** - Complete taxonomy management system for better content organization (#60)
- **Schema Management** - Comprehensive schema management capabilities (#59)
- **Graph UI Enhancements** - Improved graph visualization interface with better user experience (#49)

### Performance Improvements
- **API Key Change Performance** - Fixed slowdowns when changing API keys and during app startup (#71)
- **Socket Reliability** - Major refactor improving WebSocket connection stability and reliability (#68)
- **Retry Logic** - Enhanced retry mechanisms for better fault tolerance (#57, #55)
- **Table Consolidation** - Optimized database operations by consolidating table structures (#69)

### Bug Fixes
- **Settings Notifications** - Removed excessive notification noise when updating settings (#70)
- **Submission Flow** - Fixed submission error handling and default flow behavior (#65, #56)
- **Schema Issues** - Resolved schema-related bugs (#63)
- **Dark Mode** - Fixed broken agent response rendering in dark mode (#48)

### Maintenance
- **Code Refactoring** - Minor refactoring for improved code maintainability (#67)
- **Code Formatting** - Applied consistent code prettification standards (#58)
- **Document Palette** - Improved document management interface (#50)
- **Security Patches** - Applied vulnerability patches (with subsequent revert and re-application) (#52, #54)

### Notes
- Total of 21 commits since v0.3.15
- Versions v0.4.0 through v0.4.6 were intermediate releases leading to v1.0.0

