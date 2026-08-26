---
title: How do people use TrustGraph?
nav_order: 6
parent: Learn about TrustGraph
---

# How do people use TrustGraph?

TrustGraph is used wherever AI agents need accurate, structured
knowledge — and where you need to trust the answers they give.

## Enterprise knowledge and operations

Organisations use TrustGraph to unify fragmented knowledge — wikis,
documents, tickets, databases — into a single queryable knowledge graph.
Agents can answer questions that span multiple systems and follow
relationships across the organisation: "What's the impact of
deprecating Service X on Customer Y?"

Internal assistants built on TrustGraph understand org structure,
systems, projects, and ownership — not just text snippets. They
traverse relationships (teams → services → incidents → SLAs) to give
richer, more actionable answers than standard enterprise search.

## Security, risk, and compliance

In security operations, TrustGraph connects users, hosts, alerts,
and threat intelligence into unified threat graphs. Analysts ask
natural language questions about security posture and get answers
grounded in actual data relationships.

For compliance, regulations, policies, controls, and evidence are
modelled as a graph. When regulations change, agents can identify
which controls and assets are affected — automatically.

## Finance, strategy, and research

Financial teams use TrustGraph for M&A analysis, competitive
intelligence, and strategic planning — domains where understanding
relationships between entities matters more than finding similar
text. Research teams turn papers, patents, and lab notes into
knowledge graphs that reveal non-obvious connections across projects.

## Multi-tenant platforms

SaaS vendors embed TrustGraph as the knowledge layer for their own
products, with per-tenant knowledge cores and strict isolation. Native
multi-tenancy means each customer gets their own knowledge space with
zero cross-contamination.

## How TrustGraph compares

| Capability | Standard enterprise search | TrustGraph |
|---|---|---|
| **Core architecture** | Search indexing over documents | Context orchestration via hypergraph |
| **Context depth** | Document retrieval and vector similarity | Hyper-relational context: n-ary relationships capturing true enterprise events |
| **Context management** | Basic RBAC tied to SSO | Workspaces, Collections, and Context Cores: modular, isolated, reusable context units |
| **Agent orchestration** | Basic Q&A or simple LLM chains | HyperFlows: complex, chained agentic workflows with step-level LLM and graph config |
| **Traceability** | Logs of search queries | Real-time hypergraph traceability for all agent reasoning |
| **Compute** | API calls to proprietary LLMs | Open LLM stack: runs open models on Nvidia, AMD, or Intel hardware |
| **Deployment** | SaaS only | Self-hosted, BYOC, or SaaS |

## The common thread

These use cases share a pattern: they need **relationship-aware
retrieval** (not just text similarity), **explainability** (not just
answers), and **precision** (not just recall). That's what TrustGraph
provides.

For detailed use case descriptions with example queries, see the
[full use cases page](../../architecture/use-cases).

## Next

[Open source](open-source) — what it means that TrustGraph is fully
open source, and why that matters.
