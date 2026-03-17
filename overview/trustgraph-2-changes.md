---
title: TrustGraph 2 Changes
nav_order: 100
parent: Overview
---

# TrustGraph 2 Changes

**From knowledge graphs to a full context backend for AI agents**

Since the v1.8 release, TrustGraph has undergone a significant evolution.
TrustGraph 2 pushes the platform forward in three directions:

- **Transparency** — full provenance and explainability, from source
  document to final answer.
- **Scale** — batch processing, streaming pipelines, and incremental
  document loading for production workloads.
- **Extensibility** — a pluggable tool service architecture that lets
  teams add new agent capabilities without touching the core platform.

## Explainability

One of the most significant additions is end-to-end explainability.
When TrustGraph answers a question, you can now trace the full reasoning
chain — from the final response, through the knowledge graph edges that
informed it, all the way back to the original source document, page, and
text chunk.

Three complementary provenance layers make this possible:

- **Extraction-time provenance** records the transformation chain as
  documents are ingested.  Every step — page extraction, text chunking,
  knowledge graph triple extraction — is tracked with parent-child
  relationships.
- **Query-time explainability** captures the reasoning pipeline as
  GraphRAG queries execute: which edges were retrieved, why the model
  selected each edge, and how the final answer was synthesised.
- **Agent explainability** extends this to the ReACT agent framework.
  Each iteration of the agent's think-act-observe cycle is recorded.

All provenance metadata follows the W3C PROV-O ontology, stored in
dedicated named graphs.  See [Explainability](explainability/) for the
full details.

### CLI tools for exploration

- **tg-list-explain-traces** — list all query sessions with their
  questions and timestamps.
- **tg-show-explain-trace** — display the complete reasoning chain for a
  given session.
- **tg-show-document-hierarchy** — browse the document-to-page-to-chunk
  hierarchy after ingestion.
- **tg-invoke-graph-rag --explainable** — run a query and stream
  explainability events in real time.

## Performance at Scale

### Batch embeddings processing

Embeddings generation has been redesigned to process multiple texts in
a single API call.  For a typical corpus of a thousand document chunks,
processing times drop from minutes to seconds.

### Incremental document loading

Large documents no longer need to fit in memory.  The new pipeline
supports chunked uploads with real-time progress feedback, resumable
transfers, page-by-page PDF extraction, and incremental chunking.

### Streaming triples

Knowledge extraction now emits results progressively as they are
generated, reducing end-to-end latency and memory pressure.
Configurable batch size limits prevent any single extraction from
overwhelming downstream processors.

### Query concurrency

Database and embeddings query services now support configurable
concurrency limits, allowing you to tune parallelism to match your
infrastructure.

### Entity-centric graph storage

The Cassandra graph storage model has been redesigned around an
entity-centric architecture.  The previous multi-table approach has been
consolidated into a streamlined two-table schema that reduces write
amplification and eliminates N+1 query problems for label resolution.
See [Storage](storage/) for details.

## Pluggable Tool Services

A tool service architecture makes it easy to extend the ReACT agent with
new capabilities without modifying core TrustGraph code.

A tool service is a standalone microservice that the agent can invoke
during its reasoning process.  You define the service interface and tool
descriptor, deploy the service, and the agent can immediately start
using it.  This enables:

- **Custom data lookups** — connect the agent to internal databases,
  APIs, or search systems.
- **Domain-specific operations** — add calculation engines, validation
  services, or specialised processing.
- **Flexible configuration** — the same service implementation can power
  multiple differently-configured tools.
- **Independent deployment** — tool services deploy and scale
  independently from the core platform.

A base class handles all the messaging plumbing, so implementing a new
tool service is a matter of writing a single `invoke` method.

## Structured Data Support

TrustGraph now supports structured, tabular data alongside documents and
knowledge graphs.  You can extract structured records from unstructured
documents, load pre-structured data from CSV files or databases, and
query across both graph and structured data using natural language.

Row-level embeddings bring semantic search to structured data — finding
records using fuzzy, meaning-based matching rather than requiring exact
queries.

## Broader Platform Improvements

### RDF 1.2 alignment

The core data model now properly supports IRIs, blank nodes, typed
literals with XSD datatypes and language tags, quoted triples (RDF-star),
and named graphs.  This is the foundation that makes the explainability
features possible.

### Updated LLM integrations

- Google VertexAI migrated to the current `google-genai` SDK.
- Azure integration now supports model selection and improved error
  diagnostics.

### Reliability improvements

- Message queue subscriber resilience — unexpected messages no longer
  cause queue congestion.
- Rate limiting with proper HTTP 429 detection across LLM providers.
- Pipeline metadata handling fixes to prevent data loss during
  multi-stage processing.
- Null embedding protection for edge cases in vector operations.
- Improved CLI diagnostics for easier operational troubleshooting.

## Upgrading from TrustGraph 1.x

The upgrade to TrustGraph 2 involves a data model migration and data
re-ingestion.  The new data model unlocks all of the features described
on this page — named graphs, explainability, structured data, and the
performance improvements from entity-centric storage.
