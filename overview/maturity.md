---
title: Maturity
nav_order: 5
parent: Overview
review_date: 2026-08-01
guide_category:
  - Enterprise integration
guide_category_order: 2
guide_description: Production readiness, feature stability, and deployment status for enterprise use
guide_difficulty: beginner
guide_time: 10 min
guide_emoji: 📊
guide_banner: maturity.jpg
guide_labels:
  - Production
  - Stability
  - Enterprise
---

# TrustGraph Maturity

This page summarizes the maturity and test coverage of TrustGraph features, integrations, and reference deployments. Use it to assess production readiness for your use case.

## Status Levels

| Status | Meaning |
|--------|---------|
| ✅ **Production-ready** | End-to-end tested, recommended for production use |
| ⚠️ **Pre-production** | Tested but limited scale/coverage; use with caution |
| 🔬 **Evaluation** | Suitable for demos, trials, and evaluation only |
| ❌ **Not covered** | No formal support or testing |

---

## At a Glance

**Can I run this in production?** Here's the quick summary:

- ✅ **Core GraphRAG, Ontology RAG, and DocumentRAG** — Production-ready on Cassandra, Neo4j, and Memgraph
- ✅ **Qdrant vector search** — Production-ready; Milvus and Pinecone in pre-production
- ✅ **Agent ReAct framework** — Production-ready for agent workflows
- ✅ **Kubernetes deployments** — Production-ready on Scaleway and OVHcloud with full e2e test suites
- ⚠️ **Other cloud platforms** — Azure AKS, GCP GKE, AWS in evaluation/pre-production; tailoring required
- 🔬 **Workbench UI** — Intended as a demonstrator - you would want to develop or customise for your use-case

---

## Feature Maturity

<table>
<thead>
<tr>
<th>Category</th>
<th>Capability</th>
<th>Status</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="6"><strong>Core</strong></td>
<td>GraphRAG</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td></td>
</tr>
<tr>
<td>Ontology RAG</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td></td>
</tr>
<tr>
<td>DocumentRAG</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td></td>
</tr>
<tr>
<td>API Gateway / REST / WebSocket</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td>No built-in user/permissions/token management</td>
</tr>
<tr>
<td>Integrated knowledge extraction</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td></td>
</tr>
<tr>
<td>Workbench UI</td>
<td style="background-color: #1a4e6d; color: #e8f4fd;">🔬 Demonstrator</td>
<td>Intended as a demonstrator - you would want to develop or customise for your use-case</td>
</tr>
<tr>
<td rowspan="2"><strong>Agents</strong></td>
<td>Agent ReAct</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td></td>
</tr>
<tr>
<td>MCP server support</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td>Production ready, but MCP ecosystem security might give you concerns</td>
</tr>
</tbody>
</table>

---

## Platform & Storage Maturity

### Graph Stores

<table>
<thead>
<tr>
<th>Store</th>
<th>Status</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cassandra</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td>Not a graph store per se; TrustGraph overlays a knowledge-store schema optimized for graph queries</td>
</tr>
<tr>
<td>Neo4j</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td>Since v1.4</td>
</tr>
<tr>
<td>Memgraph</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td>Since v1.4</td>
</tr>
<tr>
<td>FalkorDB</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td>Unit testing and limited integration testing</td>
</tr>
</tbody>
</table>

### Vector Stores

<table>
<thead>
<tr>
<th>Store</th>
<th>Status</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Qdrant</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td>Default and recommended vector store</td>
</tr>
<tr>
<td>Milvus</td>
<td style="background-color: #6d4e0c; color: #fff4d6;">⚠️ Pre-production</td>
<td>Does not receive regular testing</td>
</tr>
<tr>
<td>Pinecone</td>
<td style="background-color: #6d4e0c; color: #fff4d6;">⚠️ Pre-production</td>
<td>Does not receive regular testing</td>
</tr>
</tbody>
</table>

### Cloud Deployments

<table>
<thead>
<tr>
<th>Platform</th>
<th>Type</th>
<th>Status</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-scaleway">Scaleway</a></td>
<td>Kubernetes</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td>Full e2e test suite in CI pipeline</td>
</tr>
<tr>
<td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-ovhcloud">OVHcloud</a></td>
<td>Kubernetes</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td>Full e2e test suite in CI pipeline</td>
</tr>
<tr>
<td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-gke">Google Cloud (GKE)</a></td>
<td>Kubernetes</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td>Manually verified; tailoring needed for production</td>
</tr>
<tr>
<td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-aks">Azure (AKS)</a></td>
<td>Kubernetes</td>
<td style="background-color: #1a4e6d; color: #e8f4fd;">🔬 Evaluation</td>
<td>Receives limited testing</td>
</tr>
<tr>
<td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-aws-rke">AWS (RKE2)</a></td>
<td>Kubernetes</td>
<td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
<td>Manually verified; tailoring needed for production</td>
</tr>
<tr>
<td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-ec2">AWS EC2</a></td>
<td>Docker Compose</td>
<td style="background-color: #1a4e6d; color: #e8f4fd;">🔬 Evaluation</td>
<td>Single-instance deployment; likely not suitable for production use</td>
</tr>
</tbody>
</table>

---

## Repository & Testing Coverage

<table>
<thead>
<tr>
<th>Repository</th>
<th>Scope</th>
<th>Testing</th>
<th>CI Pipeline</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/trustgraph-ai/trustgraph">trustgraph</a></td>
<td>
Core system functionality and contracts<br/>
~1500 unit tests<br/>
~250 integration tests<br/>
~100 contract tests
</td>
<td>✅ unit<br/>✅ integration<br/>✅ e2e</td>
<td><a href="https://github.com/trustgraph-ai/trustgraph/actions">pipeline</a></td>
</tr>
<tr>
<td><a href="https://github.com/trustgraph-ai/workbench-ui">workbench-ui</a></td>
<td>Workbench UI demonstrator application</td>
<td>✅ unit<br/>✅ integration</td>
<td><a href="https://github.com/trustgraph-ai/workbench-ui/actions">pipeline</a></td>
</tr>
<tr>
<td><a href="https://github.com/trustgraph-ai/trustgraph-templates">trustgraph-templates</a></td>
<td>Verification that deployment configurations build correctly and contain the correct features</td>
<td>✅ unit<br/>✅ integration<br/>✅ e2e</td>
<td><a href="https://github.com/trustgraph-ai/trustgraph-templates/actions">pipeline</a></td>
</tr>
<tr>
<td><a href="https://github.com/trustgraph-ai/simple-config-ui">config UI</a></td>
<td>Configuration UI</td>
<td></td>
<td><a href="https://github.com/trustgraph-ai/simple-config-ui/actions">pipeline</a></td>
</tr>
<tr>
<td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-scaleway">Scaleway</a></td>
<td>Cloud resources deployed as expected</td>
<td>✅ unit<br/>✅ integration<br/>✅ e2e<br/>✅ security</td>
<td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-scaleway/actions">pipeline</a></td>
</tr>
<tr>
<td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-ovhcloud">OVHcloud</a></td>
<td>Cloud resources deployed as expected</td>
<td>✅ unit<br/>✅ integration<br/>✅ e2e<br/>✅ security</td>
<td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-ovhcloud/actions/workflows/pull-request.yaml">pipeline</a></td>
</tr>
</tbody>
</table>

---

## Notes

- **Bleeding edge**: Newest features may not yet have full test coverage; check the changelog for details.

## Questions?

For questions about production readiness or specific deployment scenarios, join the [TrustGraph Discord](https://discord.gg/sQkVqqPB) or see [Getting Help](../contributing/help-and-resources).
