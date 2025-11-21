
# TrustGraph Documentation Refactoring Plan

**Status**: In Progress - Phase 4 Complete
**Started**: 2025-11-20
**Target Completion**: TBD
**Last Updated**: 2025-11-21

## Overview

This document outlines a comprehensive restructuring of the TrustGraph documentation to address structural issues, improve navigation, and enhance user experience.

## Problems Identified

### 1. Structure & Organization
- **Getting Started vs Overview overlap**: `getting-started/concepts.md` duplicates overview content
- **Installation embedded in index**: Quickstart guide is in `getting-started/index.md` instead of `installation.md`
- **Maturity docs duplicated**: Real content in root `maturity.md`, empty placeholder in `overview/feature-maturity.md`
- **Community section misnamed**: Contains project development/contributing info, not community interaction

### 2. Navigation & Signposting
- **Landing page lacks user journeys**: No personas, no clear paths for different users
- **Section indexes too minimal**: All major sections lack proper signposting
- **Deployment decisions unclear**: No guidance on local vs cloud, platform selection
- **Examples vs Guides confusion**: Unclear distinction between tutorials, guides, and examples

### 3. Content Gaps
- **Missing RAG guides**: No how-to guides for DocumentRAG, GraphRAG, OntologyRAG
- **Security documentation inadequate**: Only stubs, no real security guidance
- **20+ placeholder pages**: Many sections are "Coming soon" with no content
- **Guides index mismatch**: Lists 8 categories, only 4 exist

### 4. Technical Issues
- **GitHub edit links broken**: Points to wrong repository
- **Build artifacts unignored**: `_site/` directory tracked in git
- **Template leftovers**: Just-the-Docs template references still present
- **Branch confusion**: Working on `master`, config specifies `main`

---

## Vision: What Good Looks Like

When this refactoring is complete, the TrustGraph documentation will be:

### User-Centric & Journey-Oriented

**Landing Experience**:
- A visitor arrives at docs.trustgraph.ai and immediately sees **their path** based on their role (developer, deployer, data scientist, contributor)
- Within 30 seconds, they know exactly where to go for their immediate need
- A clear "Get started in 5 minutes" path for the impatient
- Value proposition is immediately clear: "TrustGraph helps you..."

**Navigation Flow**:
- Every section landing page answers: "What is this section for? Who should read it? Where should I start?"
- No dead ends - every page links to logical next steps
- Clear breadcrumbs showing "You are here, you came from there, you can go to..."
- Consistent "See Also" sections connecting related content

### Structurally Sound & Logically Organized

**Information Architecture**:
- **Getting Started**: Pure practical "how to run TrustGraph" - no theory
- **Overview**: Pure conceptual "what is TrustGraph and why" - no installation steps
- **Guides**: Task-oriented how-tos organized by workflow, not by component
- **Reference**: Exhaustive technical details organized by API/CLI/config
- **Examples**: Working code samples and datasets that demonstrate real use cases
- **Contributing**: Everything needed to contribute to the project

**Content Relationships**:
- Zero duplication - each concept explained once, in the right place
- Clear hierarchy: overview → guide → reference → example
- Cross-references make connections explicit: "For the theory, see Overview/Architecture. For the implementation, see this guide."

### Complete & Honest

**Content Coverage**:
- Core workflows documented: DocumentRAG, GraphRAG, OntologyRAG with complete examples
- Security documented to production standards: authentication, encryption, access control, threat model
- Deployment guidance includes decision frameworks, not just "here are options"
- No "Coming soon" without context - every WIP page clearly states expected completion and why it matters

**Quality Standards**:
- Every guide is tested and works
- Every example can be copy-pasted and run
- Every API is documented with request/response examples
- Every CLI command has a complete example with real output

### Discoverable & Scannable

**Finding Information**:
- Search works excellently (already does)
- Section indexes are comprehensive directories, not minimal lists
- Comparison tables help choose between options (e.g., "When to use DocumentRAG vs GraphRAG")
- Decision trees guide complex choices (e.g., "Which deployment option?")

**Reading Experience**:
- Clear headings allow skimming
- Code examples are syntax-highlighted and commented
- Callouts highlight warnings, tips, and important notes
- Diagrams illustrate complex concepts

### Production-Ready

**Deployment Confidence**:
- Clear path from "trying it locally" to "running in production"
- Security considerations integrated into deployment guides, not separate
- Performance guidance includes actual numbers and benchmarks
- Troubleshooting sections answer real problems users face

**Enterprise Readiness**:
- Architecture diagrams show how components fit together at scale
- High availability and disaster recovery documented
- Monitoring and observability guidance
- Cost optimization considerations

### Maintainable & Sustainable

**For Documentation Contributors**:
- Clear guidelines on where new content goes
- Templates for common page types (guide, API reference, tutorial)
- Consistent terminology (documented glossary)
- Automated link checking prevents broken references

**For Product Development**:
- Easy to keep docs in sync with code
- Clear process for marking features as beta/stable/deprecated
- Changelog integration shows what changed when

---

## Success Metrics

When we've achieved this vision:

1. **User can find their first-run guide in < 60 seconds** from landing page
2. **Zero placeholder pages without WIP markers and expected dates**
3. **Every major user journey documented end-to-end** (ingest data → query → get results)
4. **Security reviewer can assess production-readiness** from documentation alone
5. **New contributor can find "how to contribute" in < 30 seconds**
6. **Zero broken internal links**
7. **Search returns relevant results** for key terms like "authentication", "deploy", "query"
8. **Each section index provides clear navigation guidance**, not just a list

---

## Refactoring Plan

### Phase 1: Configuration & Cleanup ✅ COMPLETE

**Goal**: Fix technical issues and prepare for restructuring

1. **✅ Update `.gitignore`**
   - ✅ Add `_site/` (Jekyll build output)
   - ✅ Add `review.txt*` and temp files
   - ✅ Add `.#*` (Emacs lock files)

2. **✅ Fix `_config.yml`**
   - ✅ Update `gh_edit_repository` to `https://github.com/trustgraph-ai/docs.trustgraph.ai`
   - ✅ Remove template repository aux_link (line 10)
   - ✅ Add WIP callout style for placeholder marking
   - ✅ Verify `gh_edit_branch` matches actual workflow (confirmed: `main`)

3. **✅ Add callout styles**
   ```yaml
   callouts:
     warning:
       title: Warning
       color: red
     wip:
       title: Work in Progress
       color: yellow
   ```

**Files affected**: `.gitignore`, `_config.yml`

**Completed**: 2025-11-20

---

### Phase 2: Content Reorganization ✅ COMPLETE

**Goal**: Move content to logical locations and eliminate duplication

#### 2.1 ✅ Consolidate Maturity Documentation

- ✅ **Move** `maturity.md` → `overview/maturity.md`
- ✅ **Delete** `overview/feature-maturity.md` (empty placeholder)
- ✅ **Update** navigation order in moved file (nav_order: 5, parent: Overview)
- **Rationale**: Feature maturity is overview/meta information, belongs with architecture and features

**Files affected**:
- `maturity.md` → `overview/maturity.md` (moved)
- `overview/feature-maturity.md` (deleted)

#### 2.2 ✅ Restructure Getting Started

- ✅ **Extract** quickstart from `getting-started/index.md` → `getting-started/quickstart.md`
- ✅ **Simplify** `getting-started/index.md` to be a proper landing page with user journeys
- ✅ **Move** conceptual content from `getting-started/concepts.md` → `overview/introduction.md`
- ✅ **Rewrite** `getting-started/concepts.md` to focus on practical concepts needed for first steps
- **Rationale**: Separate "learning about TrustGraph" from "getting TrustGraph running"

**Files affected**:
- `getting-started/index.md` (rewritten with user paths)
- `getting-started/quickstart.md` (new, extracted 200-line quickstart)
- `getting-started/concepts.md` (rewritten - practical focus)
- `overview/introduction.md` (new, conceptual architecture content)

#### 2.3 ✅ Rename Community Section

- ✅ **Rename** `community/` → `contributing/` (directory and all references)
- ✅ **Update** section title and description
- ✅ **Reorganize** content:
  - ✅ Keep: contributing.md, code-of-conduct.md, development-guide.md, developer.md
  - ✅ Move: `roadmap.md` → `overview/roadmap.md`
  - ✅ Move: `changelog/` → `reference/changelog/`
  - ✅ Rename: `support.md` → `getting-help.md`
- ✅ Update all parent references in child pages

**Files affected**:
- `community/` → `contributing/` (renamed)
- `contributing/index.md` (rewritten)
- `community/roadmap.md` → `overview/roadmap.md` (moved)
- `community/changelog/` → `reference/changelog/` (moved)
- `community/support.md` → `contributing/getting-help.md` (renamed)
- All child pages updated with correct parent references

#### 2.4 ✅ Clarify Examples vs Guides

**Defined clear distinction**:
- **Guides**: Task-oriented how-to instructions ("How do I...?")
- **Examples**: Complete working code samples and datasets
- **Tutorials**: Learning-oriented lessons (step-by-step learning paths)

**Completed**:
- ✅ Rewrite `examples/index.md` with clear scope and Examples vs Guides comparison table
- ✅ Rewrite `guides/index.md` with clear scope, available guides listed, planned guides marked WIP
- ✅ Add cross-references between sections
- ✅ Document the distinction in both index pages

**Files affected**:
- `examples/index.md` (completely rewritten - clear scope, comparison table)
- `guides/index.md` (completely rewritten - task finder table, WIP markers)

**Completed**: 2025-11-20

---

### Phase 3: Navigation & Signposting ✅ COMPLETE

**Goal**: Help users find what they need quickly

#### 3.1 ✅ Rewrite Landing Page

**File**: `index.md`

**Completed**:
- ✅ Added value proposition and tagline
- ✅ Created 5 user journey paths:
  - 👨‍💻 Developer (API integration, guides, examples)
  - 🏗️ Deploying TrustGraph (deployment options, production)
  - 📊 Data Scientist (GraphRAG, extraction, queries)
  - 🏢 Evaluating TrustGraph (concepts, use cases, maturity)
  - 🔧 Extending TrustGraph (contributing, custom development)
- ✅ Added key features section with descriptions
- ✅ Added documentation sections overview
- ✅ Added "Quick Links by Task" table
- ✅ Added getting help resources

#### 3.2 ✅ Add Section Signposting

**Completed for all major section indexes**:
- ✅ Purpose statements ("This section is for...")
- ✅ Audience identification
- ✅ Navigation guides with "If you want X, see Y" patterns
- ✅ Reading order recommendations
- ✅ Prerequisites listed
- ✅ Cross-references to other sections

**Files updated**:
- ✅ `overview/index.md` - 3 reading paths, quick answers, comparison tables
- ✅ `deployment/index.md` - Decision tables, quick decision guide, production checklist, component architecture
- ✅ `guides/index.md` - Already updated in Phase 2 with task finder table
- ✅ `reference/index.md` - Quick find tables, API/CLI quick references, usage guidance
- ✅ `examples/index.md` - Already updated in Phase 2 with Examples vs Guides comparison
- ✅ `advanced/index.md` - Prerequisites, topic roadmap, decision table, contribution guide
- ✅ `getting-started/index.md` - Already updated in Phase 2 with user paths

#### 3.3 ✅ Create Deployment Decision Guide

**File**: `deployment/choosing-deployment.md` (new)

**Completed**:
- ✅ Decision tree flowchart (text-based)
- ✅ Comparison matrix by use case (6x5 table)
- ✅ Comparison matrix by technical requirements (8x6 table)
- ✅ Detailed profiles for all 8 deployment options:
  - Docker Compose
  - Minikube
  - AWS EC2 Single Instance
  - AWS RKE (Production)
  - Azure AKS
  - Google Cloud Platform
  - Intel/Tiber Cloud
  - Scaleway
- ✅ Each profile includes: strengths, limitations, requirements, when to choose, cost estimates
- ✅ Decision factors by scale, budget, and team expertise
- ✅ Migration paths between deployment types
- ✅ Next steps and links to specific guides

**Also updated**: `deployment/index.md` features the choosing-deployment guide prominently with quick decision table

**Completed**: 2025-11-20

---

### Phase 4: New Content Creation ✅ COMPLETE

**Goal**: Fill critical content gaps

#### 4.1 ✅ Create RAG Guides

**Structure decision**: Created three separate RAG guides directly under `guides/` (not in a `guides/rag/` subdirectory)

**Completed files**:

1. **✅ `guides/graph-rag.md`** (nav_order: 10)
   - Complete Graph RAG guide emphasizing relationship-aware retrieval
   - What is GraphRAG and when to use it
   - Knowledge graph structure and traversal
   - Step-by-step implementation guide (load documents, extract entities, build graph, query)
   - Common patterns: entity relationships, temporal queries, comparative analysis
   - Advanced usage: controlling traversal depth, entity-focused queries
   - Troubleshooting section (incomplete graphs, poor entity extraction, slow queries)
   - Comparison with Document RAG and Ontology RAG

2. **✅ `guides/ontology-rag.md`** (nav_order: 11)
   - Complete Ontology/Structured RAG guide for schema-based extraction
   - What is OntologyRAG and when to use it
   - SDL (Schema Definition Language) examples and usage
   - Step-by-step guide (define schema, load documents, extract data, query structured data)
   - Natural language to GraphQL query conversion examples
   - Common patterns: product catalogs, financial data, contacts, events
   - Complex schemas with nested objects and arrays
   - Validation and quality control
   - Export to JSON/CSV

3. **✅ `guides/document-rag.md`** (nav_order: 12)
   - Complete Document RAG guide (mentions "basic RAG", "naive RAG", or just "RAG")
   - What is DocumentRAG and when to use it
   - Vector embeddings and semantic search explanation
   - Step-by-step guide (prepare documents, configure chunking, load documents, process, query)
   - Chunking configuration guidance (size, overlap)
   - CLI, API, and Workbench query methods
   - Understanding results: source attribution, confidence indicators
   - Troubleshooting: poor retrieval, missing context, slow queries, empty results
   - Advanced configuration: custom embedding models, retrieval tuning, collection management
   - Comparison table with GraphRAG and OntologyRAG

**Also updated**:
- ✅ `guides/index.md` - Added comprehensive RAG workflow section with all three guides
- ✅ Updated guides/index.md task finder table to include all three RAG types

**Note**: User requested specific ordering: GraphRAG → Ontology RAG → Document RAG (achieved via nav_order values)

#### 4.2 ✅ Create Security Documentation

**New directory**: ✅ `guides/security/` created

**Philosophy**: "Tell it like it is" - honest assessment of current features vs. enterprise roadmap, based on team's 20+ years cybersecurity experience

**Completed files**:

1. **✅ `guides/security/index.md`** (nav_order: 50)
   - Security philosophy emphasizing honesty and real expertise
   - Current status: strong foundations, enterprise features in development
   - What exists today: Pulsar multi-tenant separation, optional service auth, infrastructure security
   - Enterprise roadmap overview (MCP credentials, tamper-proof logging, enhanced multi-tenancy)
   - Government AI security programme validation details
   - Security recommendations by deployment type (Development, Kubernetes, Cloud)
   - Production security checklist (network, auth, data protection, monitoring, infrastructure)
   - What TrustGraph does differently: security-first architecture, real cybersec experience
   - Reporting security issues and getting help

2. **✅ `guides/security/current-features.md`** (nav_order: 1)
   - Honest documentation of available security features today
   - Multi-tenant data separation: Pulsar-based architecture, collection-based isolation
   - Service authentication: optional inter-service auth, configuration examples, limitations
   - Infrastructure security: Kubernetes deployment, Pulumi secret management, CI/CD security testing
   - Network security: K8s network policies, TLS configuration
   - Data security: encryption at rest (storage layer), encryption in transit (TLS)
   - Access control: current state (application layer responsibility), recommendations
   - Monitoring & audit: Grafana dashboards, Pulsar audit trail, gaps clearly stated
   - Government security programme validation
   - Security configuration examples (minimal/dev, basic/staging, enhanced/production)
   - Clear about what's missing and what's the user's responsibility

3. **✅ `guides/security/enterprise-roadmap.md`** (nav_order: 2)
   - Comprehensive enterprise security roadmap with development status indicators
   - Multi-layer MCP credential encryption (🔄 Active Development):
     - Per-user credential management with vault isolation
     - Multi-layer encryption (storage, transit, just-in-time decryption)
     - Credential exposure minimization design
     - Use cases: multi-tenant SaaS, enterprise, government/defense
     - Timeline: Q1-Q3 2025
   - Tamper-proof logging architecture (🔄 Active Development):
     - Blockchain-inspired immutable log design
     - Cryptographic verification and chain integrity
     - Compliance support (SOC 2, GDPR, HIPAA, government standards)
     - Timeline: Q2-Q4 2025
   - Enhanced multi-tenant security (✅ Foundation complete, 🔄 Enhancements in development):
     - Hard multi-tenancy guarantees with cryptographic isolation
     - Injection attack protection (prompt injection, tool calling manipulation)
     - Secure tool calling in agentic flows
   - Universal service authentication (✅ Partial, 🔄 Being completed):
     - Mandatory authentication for all services
     - Automatic token rotation
     - Zero-trust service mesh integration
   - Additional roadmap: RBAC, DLP, security analytics, compliance certifications
   - Enterprise security package tiers (Government/Defense, Enterprise SaaS, Enterprise On-Premise)
   - Early access and influencing the roadmap
   - Team experience and "why trust our roadmap" section

**Also updated**:
- ✅ `guides/index.md` - Added Security section with three guides listed

**Key features of security docs**:
- Honest about current state vs. planned features
- Clear timeline estimates (not commitments)
- Emphasizes team's real cybersecurity experience (Lyft, 20+ years)
- Government AI security programme validation mentioned
- MCP (Model Context Protocol) security focus for agentic systems
- Pulsar-based multi-tenant architecture as foundation
- "We don't oversell" philosophy throughout

#### 4.3 Improve Deployment Guidance

**Status**: 🎯 **Planned** (not yet started)

**Planned enhancements**:

1. **`deployment/production-considerations.md`**
   - High availability setup
   - Disaster recovery
   - Monitoring and alerting
   - Performance tuning
   - Resource sizing
   - Cost optimization

2. **`deployment/minikube.md`**
   - Add "When to use Minikube" section
   - Add "Limitations" section
   - Add "Moving to production" section

3. **`deployment/docker-compose.md`**
   - Add "When to use Docker Compose" section
   - Add resource requirements
   - Add scaling limitations

**Note**: This sub-phase is optional/deferred pending review of Phase 4 RAG and security work.

**Completed**: 2025-11-21

---

### Phase 5: Placeholder Management

**Goal**: Mark all incomplete content clearly

#### 5.1 Add WIP Callouts

**For all placeholder pages, add at top**:
```markdown
{: .wip }
> **Work in Progress**
> This page is planned but not yet complete.
> Expected completion: [DATE or "TBD"]
> Track progress: [GitHub issue link if applicable]
```

**Files requiring WIP markers** (20+ files):
- All files in `advanced/` (except index if rewritten)
- `examples/tutorials/index.md`
- `examples/integrations/index.md`
- `reference/apis/api-document-load.md`
- `guides/monitoring/index.md`
- Any other identified stubs

#### 5.2 Update Guides Index

**File**: `guides/index.md`

**Changes**:
- Remove listed categories that don't exist (Data Integration, Querying, Visualization, Migration)
- Add categories that DO exist (Agent Extraction, Object Extraction, Structured Processing)
- Add new RAG section
- Add new Security section
- Mark WIP categories clearly
- Organize logically

---

### Phase 6: Final Polish

**Goal**: Ensure consistency and quality

#### 6.1 Navigation Cleanup

- Verify all `nav_order` values are logical
- Ensure all `parent` relationships are correct
- Remove orphaned pages
- Fix duplicate nav_order conflicts

#### 6.2 Cross-References

- Add "See also" sections to related pages
- Link between API docs and guides
- Link between guides and CLI reference
- Add breadcrumb hints where helpful

#### 6.3 Link Validation

- Test all internal links
- Fix broken references
- Verify "Edit on GitHub" links work
- Check external links

#### 6.4 Style Consistency

- Consistent heading levels
- Consistent code block formatting
- Consistent callout usage
- Consistent terminology

---

## Implementation Order

### Iteration 1: Quick Wins (Day 1)
- Phase 1: Configuration & Cleanup
- Phase 5.1: Add WIP callouts to worst offenders
- Fix landing page (Phase 3.1)

### Iteration 2: Structural Fixes (Days 2-3)
- Phase 2: Content Reorganization
- Phase 5.2: Update guides index

### Iteration 3: Navigation (Days 4-5)
- Phase 3.2: Section signposting
- Phase 3.3: Deployment decision guide
- Phase 4.3: Deployment guidance improvements

### Iteration 4: Content Creation (Days 6-10)
- Phase 4.1: RAG guides (3 days)
- Phase 4.2: Security documentation (2 days)

### Iteration 5: Polish (Days 11-12)
- Phase 6: Final polish
- Review and testing

---

## Success Criteria

- [ ] No placeholder content without WIP markers
- [ ] All section indexes have clear signposting
- [ ] Landing page provides clear user journeys
- [ ] Getting Started and Overview have no overlap
- [ ] RAG guides exist and are comprehensive
- [ ] Security documentation adequate for production deployments
- [ ] Deployment decision guidance clear and actionable
- [ ] All navigation links work correctly
- [ ] GitHub edit links functional
- [ ] Clear distinction between Examples and Guides

---

## Files to Track

### Moving
- `maturity.md` → `overview/maturity.md`
- `community/` → `contributing/`
- `community/roadmap.md` → `overview/roadmap.md`
- `community/changelog/` → `reference/changelog/`

### Deleting
- `overview/feature-maturity.md` (duplicate placeholder)
- `deployment/security-considerations.md` (stub, replaced by guides/security/)
- `review.txt` (temp file)

### Creating (New Files)
- ✅ `getting-started/quickstart.md`
- ✅ `overview/introduction.md`
- ✅ `deployment/choosing-deployment.md`
- ✅ `guides/graph-rag.md` (changed: not in rag/ subdirectory)
- ✅ `guides/ontology-rag.md` (changed: not in rag/ subdirectory)
- ✅ `guides/document-rag.md` (changed: not in rag/ subdirectory)
- ✅ `guides/security/index.md`
- ✅ `guides/security/current-features.md` (changed from original plan)
- ✅ `guides/security/enterprise-roadmap.md` (changed from original plan)
- ❌ `guides/security/authentication.md` (not created - consolidated into current-features and enterprise-roadmap)
- ❌ `guides/security/network-security.md` (not created - consolidated into current-features)
- ❌ `guides/security/data-security.md` (not created - consolidated into current-features)
- ❌ `guides/security/access-control.md` (not created - consolidated into current-features)

### Rewriting (Major Changes)
- `index.md` (landing page)
- `getting-started/index.md`
- `getting-started/concepts.md`
- `overview/index.md`
- `deployment/index.md`
- `deployment/production-considerations.md`
- `guides/index.md`
- `examples/index.md`
- All other section index files

---

## Notes

- Keep git history intact - use `git mv` for moves
- Create feature branches for each phase
- Test Jekyll build after each major change
- Get stakeholder review after Phase 3
- Consider creating GitHub issues for each WIP page

---

## Questions to Resolve

1. ~~Should we remove placeholders or mark them?~~ → Mark them clearly with WIP callouts
2. ~~Create new content or just restructure?~~ → Create RAG guides, security docs, deployment guidance
3. ~~Comprehensive or incremental?~~ → Comprehensive restructure
4. What's the correct GitHub repository for edit links?
5. Should Examples section be merged into Guides entirely?
6. Timeline expectations for completion?
