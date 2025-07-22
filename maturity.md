---
title: Maturity
layout: default
nav_order: 4.5
has_children: true
parent: TrustGraph Documentation
---

# TrustGraph Maturity

If you want to know more about feature maturity, come discuss at the
TrustGraph Discord.  See [Support](community/support)

## Feature Maturity

The following table lists TrustGraph features and their current maturity status:

<table>
    <tr>
        <th>Feature</th>
        <th>Maturity Status</th>
    </tr>
    <tr>
        <td colspan="2" style="background-color: #001020"><b>Core capability</b></td>
    </tr>
    <tr>
        <td>GraphRAG + DocumentRAG</td>
        <td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
    </tr>
    <tr>
        <td>API gateway, REST APIs and websocket APIs</td>
        <td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready - there is presently no management of users, user permissions or API tokens</td>
    </tr>
    <tr>
        <td>Integrated knowledge extraction</td>
        <td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
    </tr>
    <tr>
        <td>Workbench UI</td>
        <td style="background-color: #1a4e6d; color: #e8f4fd;">🔬 Demonstrator - This is intended as a demonstrator, to showcase capabilities.  Care should be taken when considering broader deployment if matters such as authentication, access control and user separation are important.</td>
    </tr>
    <tr>
        <td colspan="2" style="background-color: #001020"><b>Agent features</b></td>
    </tr>
    <tr>
        <td>Agent ReAct</td>
        <td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
    </tr>
    <tr>
        <td>MCP server support</td>
        <td style="background-color: #1a4e6d; color: #e8f4fd;">🔬 Evaluation - While the capability we developed is well tested, you should have concerns about the security of the MCP ecosystem for a production environment.  This is a problem we are actively tracking.</td>
    </tr>
    <tr>
        <td colspan="2" style="background-color: #001020"><b>Graph stores</b></td>
    </tr>
    <tr>
        <td>Cassandra</td>
        <td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready.  Cassandra is not a graph store per se. TrustGraph overlays a knowledge-store schema designed to perform well at knowledge-graph queries</td>
    </tr>
    <tr>
        <td>Neo4j</td>
        <td style="background-color: #6d4e0c; color: #fff4d6;">⚠️ Pre-production - Unit testing and limited integration testing</td>
    </tr>
    <tr>
        <td>Memgraph</td>
        <td style="background-color: #6d4e0c; color: #fff4d6;">⚠️ Pre-production - Unit testing and limited integration testing</td>
    </tr>
    <tr>
        <td>FalkorDB</td>
        <td style="background-color: #6d4e0c; color: #fff4d6;">⚠️ Pre-production - Unit testing and limited integration testing</td>
    </tr>
    <tr>
        <td colspan="2" style="background-color: #001020"><b>Vector stores</b></td>
    </tr>
    <tr>
        <td>Qdrant</td>
        <td style="background-color: #2d5a3d; color: #d4f4dd;">✅ Production-ready</td>
    </tr>
    <tr>
        <td>Milvus</td>
        <td style="background-color: #6d4e0c; color: #fff4d6;">⚠️ Pre-production - Unit testing and limited integration testing</td>
    </tr>
    <tr>
        <td>Pinecone</td>
        <td style="background-color: #6d4e0c; color: #fff4d6;">⚠️ Pre-production - Unit testing and limited integration testing</td>
    </tr>
    <tr>
        <td colspan="2" style="background-color: #001020"><b>Cloud deployments</b></td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-scaleway">Scaleway</a><br/>Kubernetes on Scaleway</td>
        <td style="background-color: #6d4e0c; color: #fff4d6;">⚠️ Pre-production - Unit testing, no integration or scale testing</td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-aks">Azure</a><br/>AKS Kubernetes on Azure</td>
        <td style="background-color: #1a4e6d; color: #e8f4fd;">🔬 Evaluation - Manually verified, tailoring would be needed for a production deploy.</td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-ec2">AWS EC2</a><br/>Docker compose on single-EC2 instance</td>
        <td style="background-color: #1a4e6d; color: #e8f4fd;">🔬 Evaluation - Manually verified, tailoring would be needed for a production deploy.</td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-gke">Google Cloud</a><br>GKE Kubernetes on GCP</td>
        <td style="background-color: #6d4e0c; color: #fff4d6;">⚠️ Pre-production - Manually verified, tailoring would be needed for a production deploy.</td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-aws-rke">RKE2 on AWS</a><br/>Deployed on an RKE2 distribution on AWS</td>
        <td style="background-color: #1a4e6d; color: #e8f4fd;">🔬 Evaluation - Manually verified, tailoring would be needed for a production deploy.</td>
    </tr>
</table>

## Repository Test Coverage

The following table lists TrustGraph repositories and their testing facilities:

<table>
    <tr>
        <th rowspan="2">Repository</th>
        <th colspan="3">Regime</th>
        <th rowspan="2">Results</th>
    </tr>
    <tr>
        <th>Unit</th>
        <th>Integration</th>
        <th>Operations</th>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/trustgraph">trustgraph</a><br/>core system</td>
        <td style="text-align: center;">✅</td>
        <td style="text-align: center;">✅</td>
        <td style="text-align: center;">❌</td>
        <td><a href="https://github.com/trustgraph-ai/trustgraph/actions/workflows/pull-request.yaml">pipeline</a></td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/trustgraph-templates">trustgraph-templates</a><br/>deployment configurations</td>
        <td style="text-align: center;">✅</td>
        <td style="text-align: center;">✅</td>
        <td style="text-align: center;">❌</td>
        <td><a href="https://github.com/trustgraph-ai/trustgraph-templates/actions/workflows/pull-request.yaml">pipeline</a></td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/simple-config-ui">config UI</a></td>
        <td style="text-align: center;">❌</td>
        <td style="text-align: center;">❌</td>
        <td style="text-align: center;">❌</td>
        <td>&nbsp;</td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-scaleway">Scaleway</a><br/>Automated deployment package</td>
        <td style="text-align: center;">✅</td>
        <td style="text-align: center;">❌</td>
        <td style="text-align: center;">❌</td>
        <td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-scaleway/actions/workflows/pull-request.yaml">pipeline</a></td>
    </tr>
</table>

