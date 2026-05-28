---
title: Changelog - TrustGraph
nav_order: 1
parent: Reference
grand_parent: TrustGraph Documentation
review_date: 2027-05-21
---

# Changelog

## v2.4 (2026-05-21)

### Major Features
- **Workspace-Based Multi-Tenancy** (#840): `workspace` replaces `user`
  as the isolation boundary for config, flows, library, and knowledge
  data:
  - All API schemas, CLI tools, and SDK methods drop the `user` field;
    workspace provides the same separation at the trusted
    `flow.workspace` layer instead of client-supplied message fields
  - Config, librarian, knowledge, and collection management operations
    scoped by workspace
  - Flow service uses closure-based topic cleanup on flow stop, with
    template analysis to distinguish per-flow, per-blueprint,
    per-workspace, and global topics — fixes a bug where stopping a flow
    could destroy the global librarian exchange
  - RabbitMQ backend adds heartbeat and blocked-connection timeout to
    catch dead connections
  - Data ownership model and IAM tech specs document the
    workspace/collection/flow hierarchy
- **IAM Service and Gateway Authentication** (#849, #851, #853, #855):
  Full identity and access management layer with authentication,
  authorisation, and capability-based access control:
  - JWT-based authentication with Ed25519 signing keys and API key
    support
  - Pluggable IAM regime via an authenticate/authorise contract,
    allowing alternative IAM implementations
  - Gateway auth middleware enforces capabilities on every request
  - Self-service user management: password changes, API key
    creation/revocation
  - Workspace CRUD with optional workspace filters
  - Mux service routing for workspace-scoped request dispatch
  - Bootstrap mode and token can be sourced from environment variables
  - New CLI tools: `tg-bootstrap-iam`, `tg-login`, `tg-create-user`,
    `tg-list-users`, `tg-disable-user`, `tg-enable-user`,
    `tg-delete-user`, `tg-change-password`, `tg-reset-password`,
    `tg-create-api-key`, `tg-list-api-keys`, `tg-revoke-api-key`,
    `tg-create-workspace`, `tg-list-workspaces`
- **Pluggable Bootstrap Framework** (#847, #863): Generic, long-running
  bootstrap processor that converges a deployment to its configured
  initial state, replacing the previous one-shot `tg-init-trustgraph`
  container:
  - Ordered initialisers with per-initialiser completion state stored in
    a reserved `__system__` workspace
  - Core initialisers: PulsarTopology, TemplateSeed, WorkspaceInit,
    DefaultFlowStart
  - Adaptive cadence: ~5s on gate failure, ~15s while converging, ~300s
    in steady state
  - Failure isolation — one initialiser's exception does not block others
  - Enterprise/third-party initialisers plug in via fully-qualified
    dotted class paths with no core code change
- **No-Auth IAM Regime** (#933): Lightweight `no-auth-svc` that permits
  all access unconditionally — no database, no bootstrap, no signing
  keys. Deploy in place of `iam-svc` for development, demos, and
  single-user setups. The gateway uses a new `authenticate-anonymous`
  operation to stay regime-agnostic: `iam-svc` rejects anonymous auth,
  `no-auth-svc` grants it with a configurable default user and workspace
- **Per-Workspace Queue Routing** (#862, #865): Workspace identity
  determined by queue infrastructure instead of message body fields,
  closing a privilege-escalation vector where a caller could spoof
  workspace in the request payload:
  - New `WorkspaceProcessor` base class discovers workspaces from config,
    creates per-workspace consumers, and manages consumer lifecycle on
    workspace create/delete events
  - Per-flow librarian clients via `LibrarianSpec`, giving each flow its
    own librarian tied to workspace-scoped request/response queues
  - Per-workspace response producers for config, flow, librarian, and
    knowledge services

### Improvements
- **Async-Safe Cassandra and Qdrant I/O** (#916): All Cassandra triples
  services rewritten with async methods and `asyncio.Lock` replacing
  `threading.local`; all six Qdrant services wrapped in
  `asyncio.to_thread`; rows services protected with locks against
  concurrent mutation
- **Ontology Selector and Domain/Range Enforcement** (#929, #848):
  Aligned similarity threshold defaults, added bypass mode for small
  ontologies, and enforced domain/range constraints in `TripleConverter`
  with subclass hierarchy support
- **Document Embeddings Core Lifecycle** (#913): Full list/get/put/
  delete/load operations for document embeddings cores across schema,
  translator, Cassandra table store, knowledge manager, gateway, REST
  API, socket client, and CLI (`tg-get-de-core`, `tg-put-de-core`)
- **Gateway Timeout Propagation** (#931): The `--timeout` flag is now
  propagated to per-service dispatchers instead of being ignored in
  favour of a hard-coded 120s value
- **Configurable Cassandra Replication Factor** (#887): New
  `CASSANDRA_REPLICATION_FACTOR` environment variable and
  `--cassandra-replication-factor` CLI argument threaded through all
  table store constructors
- **API Gateway Error Reporting** (#845): Connection failures return
  502 Bad Gateway naming the upstream URL; other exceptions include the
  message in the body and log with stack traces
- **CLI Auth Migration** (#913): `get_kg_core` and `put_kg_core` CLI
  tools migrated to `Api`/`SocketClient` with first-frame auth;
  ~600 lines of dead raw websocket code removed

### Bug Fixes
- **Pulsar Message Loss on Flow Restart** (#938): `consumer.close()`
  replaces `consumer.unsubscribe()` so the subscription cursor survives
  restarts; subscription cleanup moved to `delete_topic()` where it
  belongs
- **Stale Producers on Flow Stop** (#930): `Flow.stop()` now explicitly
  stops all producers, preventing orphaned connections to non-persistent
  Pulsar topics that caused 120s timeouts after flow restart
- **IAM Bootstrap Atomicity** (#935): Fixed half-done bootstrap state by
  using signing key existence (the last thing written) as the completion
  check, and running pre-service initialisers before opening pub/sub
  connections
- **Cassandra Pagination** (#921): `async_execute` only materialised the
  first result page; fixed to iterate all pages via `asyncio.to_thread`
- **Library API Round-Trip** (#928): Fixed 5 cascading bugs preventing
  `get_documents` → `update_document` from working (missing title
  tolerance, attribute access, datetime serialisation, empty response
  handling, dual ID keys)
- **Ontology Extractor Silent Failure** (#842): Read `.objects` (plural)
  instead of `.object` from JSONL `PromptResult`, fixing a v2.3
  regression where ontology extraction silently produced zero triples
- **API Gateway Dispatcher Eviction** (#841): Cached dispatchers are
  now evicted and stopped when their flow stops, preventing stale
  bindings that caused responses to be silently dropped after flow
  restart
- **SPARQL Empty Query** (#934): Guard against empty or whitespace-only
  LLM output in the SPARQL generator, preventing `IndexError`
- **Pulsar Log Noise** (#936): Reverted consumer receive timeout to
  2000ms (100ms generated ~200 WARN lines/sec with no benefit) and set
  the Pulsar C++ client logger to Error level
- **Workspace Initialisation Race** (#867): Config registration now runs
  before the IAM table write, preventing a stuck state when `iam-svc`
  starts before `config-svc`
- **Document-RAG Workspace** (#866): Fixed workspace routing in
  document-RAG; OpenAI text-completion processor now sets a placeholder
  token when none is configured
- **SPARQL Workspace Parameter** (#915): Removed spurious workspace
  parameter threading through the SPARQL algebra evaluator — workspace
  isolation is handled by pub/sub topic routing
- **OpenAI Rate Limit Handling** (#925): Fail fast on unrecoverable
  `RateLimitError` codes instead of retrying indefinitely
- **Publisher Resource Leak** (#886): Wrapped `pub.start()`/`pub.send()`
  in try/finally to guarantee cleanup on error
- **Flow-svc ConfigClient Restart** (#843): UUID-based subscription
  names prevent Pulsar `ConsumerBusy` on restart (v2.3 regression)
- **Bootstrap Circular Dependency** (#863): `TemplateSeed` and
  `WorkspaceInit` now run pre-gate to break the dependency cycle
- **Bare Excepts in NLTK** (#896): Replaced bare `except:` with
  specific exception types
- **Container Vulnerability Updates** (#861): Updated packages with
  known vulnerabilities in container builds

### Breaking Changes
- **User field removed**: All API schemas, CLI tools, and SDK methods
  drop the `user` field — use `workspace` for tenant isolation
- **CLI arguments**: All `tg-*` commands replace `--user` with
  `--workspace`
- **Python SDK**: `user` kwargs removed from all method signatures in
  flow, socket client, async client, explainability, and library modules
- **`tg-init-trustgraph` removed**: Replaced by the bootstrap processor
  framework
- **Authentication required**: API gateway now enforces authentication
  by default via the IAM regime; use `no-auth-svc` for unauthenticated
  access

### Infrastructure / Technical
- **Tech Specs**: New specifications for IAM protocol, capabilities
  model, bootstrap framework, no-auth regime, and data ownership model
- **Testing** (#848, #852, #916, #923, #929): Async-safe I/O tests,
  domain/range validation tests, websocket smoke test, ontology selector
  bypass tests, and upstream warning suppression

---

## v2.3 (2026-04-23)

### Major Features
- **Processor Groups** (#808, #810): Dev-time wrapper and runtime support
  for grouping related processors into managed units:
  - New `proc-group` dev tool with group definitions for control,
    embeddings, ingest, llm, rag, and storage tiers
  - Better logging and concurrency within the group runtime, with
    async Cassandra table helpers to reduce contention in storage and
    query paths
  - Processor groups are now the standard deployment shape produced by
    the configuration builder for TrustGraph 2.3: a small number of
    groupings replace the previous one-container-per-processor layout,
    saving roughly 1.5–2.5 GB of memory per installation
- **RabbitMQ Available in Configuration Builder** (#827, #779): RabbitMQ
  is now a selectable pub/sub fabric in the configuration builder for
  TrustGraph 2.3 deployments. Choosing RabbitMQ over Pulsar saves up to
  1 GB of memory per installation, in addition to the savings from
  processor groups above
- **Flow Service Lifecycle Management** (#822): Reliability and scalability
  upgrade for the pub/sub layer. Flow-scoped queue lifecycle is now owned
  by a dedicated flow service, decoupled from the config service:
  - Active flow keys restructured so queues are created and torn down in
    step with flow start/stop
  - RabbitMQ and Pulsar backends extended with lifecycle hooks; consumers,
    producers, and subscribers now bind through a shared backend interface
  - Eliminates queue leakage and stale bindings across flow restarts,
    improving stability under churn and scaling to many concurrent flows
- **Kafka Pub/Sub Backend** (#830, #833, #834) *(experimental, not for
  production use)*: Third fabric alongside Pulsar and RabbitMQ,
  demonstrating further independence from any single messaging system.
  Topics map 1:1 to Kafka topics, subscriptions map to consumer groups,
  response/notify uses unique consumer groups with correlation-ID
  filtering, and topic lifecycle is managed via `AdminClient` with
  class-based retention. Requires significant integration testing before
  production consideration.
- **Multi-architecture Container Builds** (#798, #801, #802, #805):
  All containers now published as multi-arch manifests covering both
  `amd64` and `arm64`, with ARM builds running on native ARM runners
  for speed. HuggingFace processor moved to Python 3.12 to unblock
  ARM64 support.

### Improvements
- **Reliable RabbitMQ Messaging** (#827, #779): RabbitMQ backend
  refactored to use one fanout exchange per topic instead of a shared
  topic exchange, eliminating cross-topic interference and fixing a
  request/response race condition. Chunker flow-API drift also
  resolved. RabbitMQ is now suitable as a robust production backend.
- **Agent Explainability Instrumentation** (#795, #796): Deeper
  instrumentation across the agent orchestrator and ReAct pattern,
  with envelope field naming unified across agent, GraphRAG, and
  DocumentRAG. New `provenance` helper module centralises RDF
  namespace and URI construction, and TrustGraph ontology published
  as a Turtle file (`specs/ontology/trustgraph.ttl`)
- **LLM Token Usage Exposure** (#782): Input/output token counts now
  propagate from all LLM providers through the prompt client, flow API,
  and socket clients to callers, enabling per-request cost tracking in
  agent, GraphRAG, DocumentRAG, and prompt services
- **Standardised LLM Rate-Limiting** (#835): Consistent rate-limit and
  exception handling across Cohere, Mistral, OpenAI, and vLLM providers,
  backed by a shared contract test suite
- **Domain and Range Validation** (#825): Triple extraction now validates
  extracted edges against ontology domain/range constraints, rejecting
  triples that violate the schema
- **S3 Retry with Backoff** (#829): Librarian blob operations retry with
  exponential backoff on transient S3 errors, improving resilience of
  large-document and multipart workflows
- **Deferred Optional SDK Imports** (#828, #831): Provider modules defer
  optional SDK imports to runtime, so a missing optional dependency no
  longer prevents the rest of the platform from starting
- **SPARQL CLI Error Reporting** (#794): `tg-invoke-sparql-query`
  surfaces service-side errors to the CLI instead of masking them
- **Pulsar Healthcheck Removed** (#809): `tg-verify-system-health` no
  longer requires Pulsar, matching the move to pluggable fabrics

### Bug Fixes
- **Flow-svc ConfigClient Restart** (#843): ConfigClient subscriptions
  now use unique UUID-based names, avoiding Pulsar `ConsumerBusy` errors
  when flow-svc restarts
- **API Gateway Dispatcher Eviction** (#841): Cached dispatchers are
  evicted when their flow stops, preventing stale references after flow
  lifecycle transitions
- **Ontology Extractor PromptResult** (#842): Read `.objects` (plural)
  rather than `.object` from `PromptResult`, fixing silent extraction
  failures
- **Library Queue Lifecycle** (#838): Library service queue setup/teardown
  corrected to match the new flow lifecycle model
- **Schema Migration Tail** (#777): Fixed trailing issues in the
  Metadata/EntityEmbeddings schema migration with regression tests to
  prevent reoccurrence
- **Deprecated datetime/asyncio APIs** (#816, #819): Replaced
  `datetime.utcnow()` with timezone-aware `datetime.now(timezone.utc)`
  and `asyncio.iscoroutinefunction` with `inspect.iscoroutinefunction`
  to remove deprecation warnings on recent Python versions
- **Deferred Import Test Patching** (#831): Fixed module-level names so
  tests can patch provider modules that use deferred imports
- **Prometheus Registry Pollution** (#806): Test suite no longer leaks
  metric registrations across tests; default metric registration removed
  to keep unit tests hermetic

### Infrastructure / Technical
- **Tech Specs Reorganisation** (#836): Tech-specs directory restructured
  for clarity; new specs added for flow-service queue lifecycle and
  active flow key restructure (#822)
- **Type Hints and Docstrings** (#803, #812, #817): Public functions in
  `trustgraph/base` fully type-hinted; docstrings added to public classes
- **Base Helper Module Tests** (#797): New unit test coverage for base
  helper modules
- **CI Pipeline Fixes** (#799, #800, #805): Qemu setup repaired, ARM
  container builds moved to ARM runners, multi-platform manifest build
  pipeline stabilised

---

## v2.2 (2026-04-07)

### Major Features
- **Agent Orchestrator** (#739, #743, #744, #745, #746, #747, #748, #750):
  Multi-pattern agent orchestrator with LLM-based meta-routing to select the
  appropriate execution pattern per request:
  - **Plan-then-Execute**: LLM generates a plan of steps, executes each
    sequentially, and synthesises results
  - **Supervisor**: Decomposes a question into sub-agent goals, fans out
    to parallel sub-agents, aggregates findings into a synthesis
  - **ReAct**: Existing iterative reasoning pattern (unchanged)
  - Full explainability provenance for all patterns with new RDF types
    (Decomposition, Finding, Plan, StepResult, Synthesis) and predicates
    (`tg:subagentGoal`, `tg:planStep`)
  - Analysis split into Analysis+ToolUse and Observation for finer-grained
    DAG provenance; `message_id` wired on all streaming answer chunks
  - CLI support for pattern selection:
    `tg-invoke-agent -p supervisor|plan-then-execute|react`
- **RabbitMQ Pub/Sub Backend** (#751, #752, #765): Pub/sub abstraction
  decoupled from Pulsar with RabbitMQ as an alternative backend,
  demonstrating independence from any single messaging fabric. RabbitMQ
  was selected for its significantly lower resource requirements compared
  to Pulsar. Support for additional fabrics such as Kafka is planned for
  a subsequent release.
  - Selectable via `PUBSUB_BACKEND=rabbitmq` environment variable
  - Topic exchange architecture with shared and exclusive consumer queues
  - Translator rename: `to_pulsar`/`from_pulsar` → `encode`/`decode`
    across 55+ files
  - Queue naming format changed to `CLASS:TOPICSPACE:TOPIC`
  - Subscriber resilience: automatic consumer recreation after connection
    failure
  - Thread-safe consumer model with dedicated thread pools for pika
- **SPARQL Query Service** (#754, #755): Backend-agnostic SPARQL 1.1 query
  service:
  - Parses SPARQL queries using rdflib, decomposes into triple pattern
    lookups via existing pub/sub interface
  - Supports BGP, JOIN, OPTIONAL, UNION, FILTER, BIND, VALUES, GROUP BY,
    ORDER BY, LIMIT/OFFSET, DISTINCT, and aggregates
  - Batching and streaming support for large result sets
  - Gateway integration, Python SDK method (`FlowInstance.sparql_query`),
    and CLI command (`tg-invoke-sparql-query`)
- **Universal Document Decoder** (#705): Multi-format document processing
  using the `unstructured` library:
  - Supports DOCX, XLSX, PPTX, HTML, Markdown, CSV, RTF, ODT, EPUB and
    more through a single service
  - Tables preserved as HTML markup; images stored in librarian
  - Configurable section grouping strategies (whole-document, heading,
    element-type, count, size)
  - All decoders now share the `document-decoder` ident for
    interchangeability

### Improvements
- **Inline Explainability Triples** (#763): Provenance triples now included
  directly in explain messages from GraphRAG, DocumentRAG, and Agent
  services, eliminating follow-up knowledge graph queries for
  explainability details
- **Config Push Notify Pattern** (#760): Replaced stateful pub/sub config
  broadcast with lightweight notify signal containing only version number
  and affected config types
- **Persistent WebSocket Connections** (#723): Single persistent connection
  with request multiplexing replaces per-request WebSocket connections,
  eliminating repeated TCP+WS handshakes. CLI tools converted to
  concurrent WebSocket requests
- **Auto-pull Ollama Models** (#757): Ollama provider automatically pulls
  missing models on first use
- **MCP Gateway Auth** (#721): `GATEWAY_SECRET` environment variable
  support for MCP server to API gateway authentication
- **Chunk Content ID in Explain Traces** (#708): `tg-show-explain-trace`
  now displays chunk URIs with `--show-provenance` for easy source text
  retrieval via `tg-get-document-content`
- **Prompt Queue Monitoring** (#737): New `tg-monitor-prompts` CLI tool
  for subscribing to prompt request/response queues with correlation and
  timing summaries

### Bug Fixes
- **Dispatcher Race Condition** (#715): Fixed duplicate dispatcher creation
  under concurrent coroutines causing dropped responses and permanent UI
  spinners
- **WebSocket Error Responses** (#726): Fixed missing request IDs in
  websocket multiplexer error responses causing client hangs on failed
  requests
- **OpenAI Compatibility** (#727): Use `max_completion_tokens` instead of
  deprecated `max_tokens` for newer OpenAI/Azure models; added
  `AZURE_API_VERSION` environment variable override
- **Missing Auth Header** (#724): Fixed `verify_system_status` processor
  check not including authorization header when gateway auth is enabled
- **Gateway Text Load** (#729): Accept raw UTF-8 text in `text-load`
  endpoint
- **Stray Log Messages** (#706): Removed spurious warnings from librarian
  responses arriving on shared response queues
- **Consumer Poll Timeout**: Reduced consumer poll timeout from 2000ms to
  100ms for improved responsiveness

### Breaking Changes
- **Pub/sub queue naming**: Queue format changed from topic-based to
  `CLASS:TOPICSPACE:TOPIC`; translator methods renamed from
  `to_pulsar`/`from_pulsar` to `encode`/`decode`
- **Agent schema**: Orchestration fields added (correlation, sub-agents,
  plan steps); legacy response fields (`answer`, `thought`,
  `observation`) removed
- **Config push schema**: `ConfigPush` now contains a `types` list instead
  of the full config dict; `state` queue class replaced by `flow` class

### Infrastructure / Technical
- **Testing** (#745, #749, #750): 96+ orchestrator tests covering
  aggregation, provenance, routing, explainability parsing, DAG structure,
  and callback message IDs
- **CLA Workflow** (#716, #722): Contributor License Agreement process
  via GitHub action
- **Pulsar Check Skipped** (#753): `tg-verify-system-status` no longer
  requires Pulsar when using alternative pub/sub backends

---

## v2.1 (2026-03-17)

### Major Features
- **Explainability & Provenance** (#655, #661, #677, #682, #688, #689, #693,
  #694, #697, #698): End-to-end explainability across the entire pipeline:
  - **Extract-time provenance**: Document processing now emits PROV-O triples
    tracing the lineage from documents through pages, chunks, and extracted
    edges using `prov:wasDerivedFrom` relationships
  - **Query-time explainability**: GraphRAG, DocumentRAG, and Agent queries
    record full reasoning traces (question, grounding, exploration, focus,
    synthesis stages) into a dedicated `urn:graph:retrieval` named graph
  - **Named graphs**: Knowledge is now stored across named graphs — default
    graph for facts, `urn:graph:source` for extraction provenance,
    `urn:graph:retrieval` for query-time explainability
  - **Subgraph provenance**: Extracted subgraphs are tracked with provenance
    linking edges back to their source chunks and documents
  - New CLI tools: `tg-list-explain-traces`, `tg-show-explain-trace`,
    `tg-show-extraction-provenance`
  - Explainability modes added to `tg-invoke-graph-rag`,
    `tg-invoke-document-rag`, and `tg-invoke-agent` with inline provenance
    event display
- **Value to Term Schema Redesign** (#622): Breaking redesign of the core
  wire format from `Value` (`{"v": ..., "e": true}`) to typed `Term` format:
  - IRIs: `{"t": "i", "i": "http://..."}`
  - Literals: `{"t": "l", "v": "text", "d": "datatype", "l": "lang"}`
  - Quoted triples (RDF-star): `{"t": "r", "r": {"s": ..., "p": ..., "o": ...}}`
  - Blank nodes: `{"t": "b", "d": "identifier"}`
  - Updated all processing pipelines, Cassandra indexes, serialization,
    and tests
- **Tool Services** (#655, #656, #658): Dynamically pluggable tool
  implementations for agent frameworks:
  - Base class for creating custom tool services
  - Tool service client for the ReAct agent to discover and invoke tools
    at runtime
  - Tools can be deployed independently and registered dynamically
- **Batch Embeddings** (#668, #669, #670, #671, #672, #681): Embeddings
  service redesigned for batch processing:
  - `embed()` now accepts a list of texts instead of a single text
  - Updated all embeddings providers (FastEmbed, Ollama, etc.)
  - Embeddings API now returns similarity scores
  - New CLI tools: `tg-invoke-embeddings`, `tg-invoke-graph-embeddings`,
    `tg-invoke-document-embeddings`, `tg-invoke-row-embeddings`

### Improvements
- **Incremental / Large Document Loading** (#659, #660): Multipart upload
  support for large documents:
  - S3 multipart upload with streaming retrieval
  - Upload session tracking in Cassandra with 24-hour TTL
  - New REST endpoint `GET /api/v1/document-stream` for streaming document
    content
  - New CLI tool: `tg-get-document-content`
- **Entity-Centric Graph** (#633): Redesigned graph schema for entity-centric
  storage and querying
- **Structured Data Enhancements** (#645, #646): Multi-index table support
  for structured data, removing need for manual Cassandra table modifications:
  - Row embeddings APIs exposed through gateway
  - New `row-embeddings-query` tool type for semantic search on structured
    data indexes
- **Streaming Triples** (#676): Streaming triple queries with configurable
  batch sizes for lower time-to-first-result and reduced memory overhead:
  - `tg-show-graph` updated with `--limit`, `--batch-size`, `--graph` filter,
    and `--show-graph` options
- **Graph Query CLI** (#679): New `tg-query-graph` tool for selective pattern
  matching on the triple store (by subject, predicate, object, graph) with
  auto-detection of value types
- **RDF-star Support in Turtle Export** (#676): `tg-graph-to-turtle` now
  handles quoted triples and named graph filtering
- **Enhanced GraphRAG Pipeline** (#691, #697): 4-stage GraphRAG pipeline
  with query concurrency and DocumentRAG grounding
- **Prompts JSONL Format** (#619): Support for JSONL format in prompt
  definitions
- **Entity Context Enhancement** (#629): Entity term now output alongside
  its definition in entity contexts
- **Terminology Rename** (#682): Clarified naming throughout — "provenance"
  callbacks/IDs renamed to "explain" for clarity

### Bug Fixes
- **Cassandra Schema and Graph Filter Semantics** (#680): Fixed Cassandra
  schema for named graph support and corrected graph filter semantics
- **Subscriber Queue Clogging** (#642): Fixed unexpected messages causing
  subscriber queue clogging
- **Google AI Studio** (#641, #639, #640): Fixed Google AI Studio integration,
  moved to VertexAI package to simplify dependencies
- **VertexAI SDK Migration** (#632): Migrated from deprecated Google GenAI
  library to the `google-genai` SDK
- **LLM Metrics** (#631): Fixed metric label issues across LLM providers
- **Azure LLM Model** (#657): Fixed model parameter usage in Azure LLM
  integration
- **Ontology URI Issue** (#637): Fixed ontology URI handling
- **Entity/Triple Batch Size Limits** (#635): Added batch size limits to
  prevent oversized requests
- **Pipeline Metadata ID Overwrite** (#686): Fixed metadata `id` field being
  overwritten at each processing stage
- **Null Embeddings Protection** (#627): Added guard against null embeddings
- **Graph Embeddings Service Identifier** (#648): Fixed mismatching
  `ge-query` / `graph-embeddings-query` service identifiers
- **Rate Limiting** (#638): Use `ClientError` and status code to correctly
  detect 429 rate-limit errors
- **Mistral SDK** (#687): Locked `mistralai` to `<2.0.0` to avoid a breaking
  change
- **KG Extraction** (#695): Removed `schema:subjectOf` edges from knowledge
  graph extraction

### Breaking Changes
- **Value to Term wire format**: All API clients must update to the new Term
  format (see Major Features above)
- **`tg-invoke-objects-query` renamed** to `tg-invoke-rows-query`; gateway
  service key changed from `objects` to `rows`
- **`tg-load-pdf` and `tg-load-text` removed**: Document loading is now
  handled through the library/processing pipeline
- **Metadata field**: `metadata.metadata` (subgraph) replaced by
  `metadata.root` (simple value) in export/import serialization
- **Embeddings fields**: `vectors` (plural) became `vector` (singular);
  document embeddings now reference `chunk_id` instead of inline `chunk` text
- **Graph store**: Only Cassandra is currently implemented as a graph store
  backend. Neo4j and Memgraph support is not available in this release.
- **Vector store**: Only Qdrant is currently implemented as a vector store
  backend. Milvus support is not available in this release.

### Infrastructure / Technical
- **Tech Specs**: Added technical specifications for agent explainability,
  tool services, graph contexts, extraction dataflow, and structured data
  multi-index
- **Testing** (#647, #663, #666, #696): Updated and expanded test suite for
  new Term schema, explainability, provenance, and embeddings interfaces

---

## v1.8 (2026-01-19)

### Major Features
- **API Documentation** (#612, #613, #614): Comprehensive API specifications
  and documentation:
  - REST API OpenAPI specification with full endpoint coverage
  - WebSocket AsyncAPI specification for real-time interactions
  - Python API documentation with auto-generation tooling
  - Removed legacy hand-written API documentation in favor of generated specs
- **Messaging Fabric Plugins** (#592): Plugin architecture for messaging fabric
  enabling alternative messaging backends:
  - Technology-neutral schema expressions for transport abstraction
  - Backend abstraction layer for pub/sub operations
  - Enables future support for messaging systems beyond Pulsar
  - Schema strictness improvements uncovered and fixed incorrect schema usage

### Improvements
- **Generic S3 Storage Support** (#594): Librarian blob storage refactored for
  S3-compatible stores:
  - MinIO-specific options changed to generic S3 parameters
  - Added region and SSL configuration options
  - Integrated with Garage - the configuration portal delivers integrated
    Garage
- **Storage Management Cleanup** (#595): Addressed legacy issues in storage
  management:
  - Removed legacy storage management code
  - Fixed deletion of last collection edge case
  - Storage processors now ignore data for deleted collections
- **URL Normalization** (#617): Gateway URLs now work with or without trailing
  slashes

### Bug Fixes
- **Configuration Fixes** (#616, #609, #611, #610): Multiple config-related
  fixes:
  - Fixed flows/flow key issue in config service
  - Fixed config inconsistency issues
  - Fixed flow loading problems
  - Fixed load-doc command issues
- **Streaming Fixes** (#607, #608, #602, #599): Resolved streaming-related
  issues:
  - Fixed non-streaming RAG problems
  - Fixed agent streaming tool failure
  - Fixed various streaming API issues
- **Schema Fixes** (#598, #596): Schema message improvements:
  - Fixed doc embedding schema messages
  - Fixed optionality in objects-query schema
- **Collection Management** (#597): Fixed collection existence test logic
- **Dependencies** (#606): Added missing trustgraph-base dependency

### Testing
- **Streaming Tests** (#600, #601): Added comprehensive streaming tests and
  fixed async test warnings

---

## v1.7 (2025-12-23)

### Major Features
- **Multi-Tenant Support** (#583): Basic multi-tenant infrastructure enabling
  isolated deployments:
  - Collection management migrated to config service from librarian
  - Fixed parameter name mismatches for queue customization
  - Collection storage now uses config service with push-based distribution
  - Fixed AsyncProcessor and Config Service parameter handling
  - Services can now use tenant-specific queues and configurations
- **Python API Refactor** (#577): Comprehensive Python API client enhancement
  with feature parity and streaming support:
  - Streaming interfaces for all LLM services (agent, GraphRAG, DocumentRAG,
    text completion, prompts)
  - WebSocket transport for persistent connections and multiplexing
  - Async/await support across all interfaces (REST, WebSocket, bulk, metrics)
  - Bulk import/export for triples, graph embeddings, and document embeddings
  - 60x latency improvement for streaming operations (500ms vs 30s first token)
  - Type-safe interfaces with full backward compatibility
  - CLI utilities updated to use new streaming API
- **Improved Ontology Extraction** (#576): Enhanced ontology-based knowledge
  extraction:
  - Entity normalizer for consistent entity naming
  - Simplified parser for improved extraction accuracy
  - Triple converter for better schema adherence
  - Enhanced prompt engineering for ontology extraction

### Improvements
- **System Monitoring** (#579): System startup tracker for deployment
  verification with CLI tool `tg-verify-system-status`
- **Logging Enhancements** (#586, #588): Production-grade logging infrastructure:
  - Loki logging integration for centralized log aggregation
  - Service ID added to log entries instead of module name
  - Enhanced logging strategy with structured output
- **Metrics** (#589): Added model information to metering metrics for better
  cost tracking and analysis
- **Gateway Configuration** (#584): Gateway queue overrides for flexible
  deployment topologies

### Infrastructure / Technical
- **Tech Specs**: Added comprehensive technical specifications:
  - Multi-tenant support architecture
  - Python API refactor design
  - Ontology extraction phase 2
  - Enhanced logging strategy
- **Testing**: Added comprehensive Python API client tests with streaming
  validation

---

## v1.6 (2025-12-04)

### Major Features
- **Streaming LLM Responses** (#566, #567): Comprehensive streaming support
  for LLM text completion enabling real-time token-by-token delivery:
  - Infrastructure with streaming flag in schemas, Gateway API
    (REST/WebSocket), Python API, and CLI tools.
  - Full streaming implementation across all LLM providers including
    Azure, Azure OpenAI, Bedrock, Claude, Cohere, Google AI Studio, Llamafile,
    LM Studio, Mistral, Ollama, OpenAI, TGI, Vertex AI, and vLLM
  - Backward compatible with existing non-streaming clients
  - Support for WebSocket streaming
  - Reduces time-to-first-token and improved UX for long responses
- **Streaming RAG Responses** (#568): Extended streaming support to GraphRAG
  and DocumentRAG services:
  - Token-by-token responses for knowledge graph and document retrieval queries
  - Consistent streaming UX across all TrustGraph services
  - Leverages existing PromptClient streaming infrastructure
  - Gateway support via WebSocket for real-time client applications
- **Streaming Agent Interactions** (#570): Enhanced agent framework with
  streaming support:
  - Real-time streaming of ReAct agent thought/observation/answer chunks
  - Incremental response delivery for multi-step agent workflows
  - Streaming parser for agent responses with robust error handling

### Improvements
- **Enhanced Integration Tests** (#568, #570): Comprehensive test coverage for
  streaming functionality

### Bug Fixes
- **AWS Bedrock Model Invocation** (#572): Fixed compatibility issues with
  newer Bedrock model invocation API including proper streaming support
- **Minio Library Compatibility** (#565): Fixed incompatible library change in
  Minio client for blob storage operations
- **Streaming Agent Interactions** (#570): Fixed race conditions and message
  ordering issues in streaming agent responses

### Infrastructure / Technical
- **CLI Improvements**: Enhanced CLI tools with streaming output:
  - `tg-dump-queues`: New utility for developer queue diagnostics

### Templates
  - Updates to Bedrock and Claude models to support latest models

---

## v1.5 (2025-11-23)

### New Features
- **OntoRAG: Ontology-Based Knowledge Extraction** (#523): New processor
  `kg-extract-ontology` that uses ontology objects from config to guide triple
  extraction. Includes entity contexts and integrates with ontology extractor
  from workbench.
- **MCP Authentication** (#557): Added MCP auth token header support for the
  simple authentication case.
- **Dynamic Embeddings Model Selection** (#556): Embeddings model can now be
  selected dynamically rather than being fixed.

### Bug Fixes
- **Collection deletion batch error** (#559): Fixed batch error during
  collection deletion by reducing batch size.
- **Fix hard-coded vector size** (#555): Vector store now lazy-creates
  collections with different collections for different dimension lengths.
- **Fix AgentStep schema error** (#557): Agent step argument values are now
  converted to strings to fix schema errors.
- **Remove unnecessary OpenAI parameters** (#561): Removed parameters from
  OpenAI invocation that were causing compatibility issues with
  OpenAI-compatible services.

### Infrastructure / Technical
- **Python 3.13 Support** (#553): Upgraded to Python 3.13, switched from
  cassandra-driver to scylla-driver (cassandra-driver doesn't work with
  Python 3.13).
- **Vector Store Lifecycle Tech Spec** (#555): Added technical specification
  for vector store lifecycle.
- **OntoRAG Tech Spec** (#523, #558): Added technical specification for
  ontology-based knowledge extraction and query.

### Testing
- **Ontology extraction tests** (#560): Added tests for ontology extraction.
- **Dynamic embeddings tests** (#556): Added tests for dynamic embeddings
  model selection.
- **MCP auth and agent step parsing tests** (#557): Added tests for MCP
  authentication and agent step parsing.
- **OpenAI invocation tests** (#561): Updated tests for OpenAI parameter
  changes.

---

## v1.4 (2025-10-06)

### New Features
- **Flow Configurable Parameters** (#526, #530, #531, #532, #533, #541):
  Major enhancements to flow parameter system:
  - Flow configurable parameters with dynamic settings
  - LLM dynamic settings using llm-model and llm-rag-model parameters
  - Temperature parameter support for all LLMs
  - Flow creation uses parameter defaults in API and CLI
  - Advanced parameter mode with controlled-by relationships
  - New CLI tools: tg-show-parameter-types
  - Dynamic chunking parameters
- **Structured Data Diagnosis Service** (#518, #519):
  - New structured data diagnosis service plumbed into API gateway
  - Added XML, JSON, CSV detection capabilities
  - Type detector with schema selection
- **Enhanced Collection Management** (#520, #522, #542, #544):
  - Collection metadata management and deletion capabilities
  - Librarian services integrated with collection manager
  - Collection tracking across all processors
  - Explicit collection creation/deletion (removed implicit creation)
  - Fixed collection management synchronization issues
- **User/Collection Isolation** (#509, #510):
  - Neo4j user/collection separation
  - Memgraph user/collection processing

### Improvements
- **Cassandra Performance** (#521):
  - Refactored Cassandra knowledge graph for single table
  - Multi-table implementation for performance enhancement
  - Added Cassandra collection table
- **GraphRAG Optimizations** (#527): Implemented GraphRAG optimizations with
  updated tests
- **Vector Store Enhancements** (#512): Vector stores now create collections
  on query
- **Build System** (#515): Parallel container builds
- **Logging** (#528, #543): Reduced excessive request/response logging and
  log spam

### Bug Fixes
- **Collection Management** (#544): Fixed collection management
  synchronization problems
- **Metrics** (#539, #540): Fixed label names and label issues in metrics
- **WebSocket** (#517): Fixed async websocket closure handling
- **CLI** (#529): Fixed CLI typo
- **Tests** (#534, #535): Fixed failing tests and improved LLM parameter
  test coverage
- **Object Writer** (#544): Fixed object writer management issues
- **Milvus** (#544): Updated Milvus to use ANN correctly

### API Changes
- **Gateway** (#514): Return empty embeddings list as empty list through
  gateway.
- **Parameters**: Changed `parameters` to `parameter-types` for consistency

---

## v1.3.0

### New Features
- **Structured Data Enhancements** (#492, #493, #496, #498, #500): Major improvements to structured data handling:
  - NLP query to GraphQL service for natural language database queries
  - Structured query tool integration with agent framework
  - Enhanced structured query support and object batching
  - Structured data loader CLI with auto mode functionality
  - Object import capabilities with batch processing
- **Collection Management** (#503, #511):
  - Extended use of user + collection fields throughout the system
  - Stores automatically create collections on query
- **Tool Groups** (#484): Added tool grouping functionality for better organization

### Improvements
- **GraphQL Enhancements** (#486, #489):
  - Added GraphQL table query support
  - Removed redundant GraphQL collection parameter
- **Cassandra Configuration Standardization** (#483, #488, #490):
  - Made Cassandra options (user, password, host) consistent across all utilities
  - Consolidated Cassandra configuration for better consistency
  - Refactored Cassandra operations to use common helper functions
- **API Improvements** (#513): Return empty embeddings list as empty list through gateway

### Bug Fixes
- **Vector Store Fixes** (#507): Fixed Milvus vector store integration issues
- **Document Processing** (#506): Fixed document RAG processing issues
- **Monitoring** (#502): Fixed Prometheus incorrect metric names
- **API Consistency** (#481): Fixed trustgraph-base chunks/documents confusion in the API
- **System Integration** (#494): Resolved various system integration issues
- **Import/Export** (#476): Fixed graceful shutdown for import/export operations
- **Knowledge Loading** (#472): Use collection field from request when loading knowledge core

---

## v1.2.17

### New Features
- **MCP Tool Arguments Support** (#462): Added support for Model Context Protocol (MCP) tool arguments, including agent support and additional tests
- **Anthropic Support for VertexAI** (#458): Added Anthropic model support for Google Vertex AI platform
- **Knowledge Load Utility CLI** (#456): New command-line utility for loading knowledge into the system
- **Structured Data MVP** (#452): Initial implementation of structured data handling with:
  - New schemas and architecture principles
  - Object extractor functionality
  - Cassandra object storage support
- **Knowledge Extraction via Agent Framework** (#439): 
  - Implemented KG extraction agent (kg-extract-agent)
  - Using ReAct framework (agent-manager-react)
  - Refactored ReAct manager to use traditional ReAct messages

### Improvements
- **Agent Tool Coverage** (#460): Increased ReAct tool coverage with multi-step tool invocation and reasoning tests
- **Schema Structure Refactor** (#451): Major refactoring of schema structure for better organization
- **Logging Strategy** (#444): Implemented comprehensive logging strategy, converting all print() statements to proper logging invocations
- **Build System Modernization** (#440): Migrated from setup.py to pyproject.toml for modern package infrastructure

### Bug Fixes
- **Agent Tool Resilience** (#461): 
  - Fixed incorrect tool initialization in agent service
  - Made Action parsing more resilient by handling quotation marks
- **Missing Anthropic Import** (#459): Fixed missing import for Anthropic functionality
- **Token Chunker API** (#454, #455): Fixed broken API invocation in token chunker
- **Librarian Collection Validation** (#453): Added validation for librarian collections
- **Mistral OCR** (#448, #450): 
  - Fixed Mistral OCR to use current API
  - Corrected Mistral OCR identifier to standard pdf-decoder
- **Logging Startup Issues** (#445, #446, #447): Resolved multiple logging startup problems

### Infrastructure
- **Build Dependencies** (#441, #442): Added missing build dependencies
- **Template Addition** (#463): Added new template support
- **Python Dependencies**: Updated Python dependencies to version 1.2

### Testing
- **PDF Decoder Tests**: Added comprehensive tests for PDF decoder functionality
- **MCP Arguments Tests**: Added test coverage for MCP tool arguments
- **Multi-step Reasoning Tests**: New tests for multi-step tool invocation scenarios

## v1.1.10
### New Features
- **MCP (Model Context Protocol) Support**: Added MCP server and client support (#419, #425, #426, #427, #428)
- **React Integration**: Added React call MCP functionality (#428)

### Improvements
- Documentation updates for API/CLI changes in v1.0 (#420, #421)
- Enhanced README with messaging improvements and link fixes

---

## v1.0.22
### Major Features
- **Flow API & Management**: Complete flow configuration and management system (#345, #346, #356, #357, #358)
- **Knowledge Management**: Knowledge service, library management, and core CLI tools (#367, #368, #369, #372)
- **Enhanced Gateway**: Reverse gateway functionality and improved API gateway (#416, #356)
- **Performance Improvements**: Multi-threading support for consumers and LLMs (#408, #409)

### New Integrations
- **vLLM Support**: Added vLLM integration (untested) (#410)
- **HuggingFace TGI**: Added HuggingFace Text Generation Inference support (#396)
- **Google AI Updates**: Enhanced Google AI integration (#394)

### Bug Fixes & Improvements
- Fixed command line arguments handling (#417)
- Fixed library translators (#415)
- Fixed missing script issues (#418)
- Improved token rate measurement utility (#412)
- Enhanced translator classes (#414)
- Miscellaneous fixes (#413)

---

## v0.23
### New Features
- **Knowledge Service**: Full knowledge management system with CLI tools
- **Library Management**: Document submission and library CLI functionality
- **Entity Contexts**: Import/export capabilities for entity contexts
- **Configuration Persistence**: Enhanced config management and reload mechanisms

### Infrastructure
- **Container Updates**: Upgraded to Python 3.12 (#386)
- **OCR Improvements**: Ported OCR code to new API architecture
- **Apache 2 License**: Updated licensing (#373)

### Bug Fixes
- Fixed LLM launch bugs (#377, #378)
- Fixed queue initialization issues (#381, #382)
- Fixed chunking not being enabled (#364)
- Fixed OpenAI base URL handling

---

## v0.22
### Major Features
- **Configuration Service**: Dynamic configuration management (#332, #334, #335)
- **Prompt Management**: Dynamic prompt loading and CLI commands (#338)
- **Agent Management**: Enhanced agent configuration system

### Infrastructure Changes
- Removed template directory (moved to separate repository) (#336)
- Enhanced configuration initialization (#335)
- Added config reload handler mechanism (#334)

---

## v0.21
### New Features
- **Librarian Service**: Document processing and management (#304, #305, #307, #310, #311)
- **Mistral AI Support**: Complete Mistral API integration including OCR (#313, #326)
- **LM Studio Integration**: Added LM Studio LLM hosting support (#323, #328)
- **PDF OCR**: Separate PDF OCR package with Tesseract support (#324)
- **Cassandra Integration**: Added Cassandra auth with SSL support (#318)

### Cloud & Infrastructure
- **Azure AKS**: Azure Kubernetes Service integration (#317, #319)
- **AWS Bedrock**: Inference profiles support (#314)
- **FastEmbed**: Enabled FastEmbed component (#316)

### API Improvements
- **Pulsar API Key**: Added API key support (#308)
- **Async/Sync Fixes**: Resolved async/sync loading issues (#315)
- **GraphRAG & DocRAG**: Enhanced parameters and path hops (#312)

### Bug Fixes
- Fixed broken setup.py (#320)
- Fixed async send typos (#322)
- Fixed container build issues (#325)
- Fixed missing OpenAI symbol and base URL specification (#330)
- Fixed Bedrock integration issues (#331)

