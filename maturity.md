---
title: Maturity
layout: default
nav_order: 4.5
has_children: true
parent: TrustGraph Documentation
---

# TrustGraph Maturity

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
        <td>Production-ready</td>
    </tr>
    <tr>
        <td>API gateway, REST APIs and websocket APIs</td>
        <td>Production-ready - there is presently no management of users, user permissions or API tokens</td>
    </tr>
    <tr>
        <td>Integrated knowledge extraction</td>
        <td>Production-ready</td>
    </tr>
    <tr>
        <td>Workbench UI</td>
        <td>This is intended as a demonstrator, to showcase capabilities.  Care should be taken when considering broader deployment.</td>
    </tr>
    <tr>
        <td colspan="2" style="background-color: #001020"><b>Agent features</b></td>
    </tr>
    <tr>
        <td>Agent ReAct</td>
        <td>Production-ready</td>
    </tr>
    <tr>
        <td>MCP server support</td>
        <td>Evaluation - While the capability we developed is well tested, you should have concerns about the security of the MCP ecosystem for a production environment.  This is a problem we are actively tracking.</td>
    </tr>
    <tr>
        <td colspan="2" style="background-color: #001020"><b>Graph stores</b></td>
    </tr>
    <tr>
        <td>Cassandra</td>
        <td>Production-ready.  Cassandra is not a graph store per se. TrustGraph overlays a knowledge-store schema designed to perform well at knowledge-graph queries</td>
    </tr>
    <tr>
        <td>Neo4j</td>
        <td>Pre-production - Unit testing and limited integration testing</td>
    </tr>
    <tr>
        <td>Memgraph</td>
        <td>Pre-production - Unit testing and limited integration testing</td>
    </tr>
    <tr>
        <td>FalkorDB</td>
        <td>Pre-production - Unit testing and limited integration testing</td>
    </tr>
    <tr>
        <td colspan="2" style="background-color: #001020"><b>Vector stores</b></td>
    </tr>
    <tr>
        <td>Qdrant</td>
        <td>Production-ready</td>
    </tr>
    <tr>
        <td>Milvus</td>
        <td>Pre-production - Unit testing and limited integration testing</td>
    </tr>
    <tr>
        <td>Pinecone</td>
        <td>Pre-production - Unit testing and limited integration testing</td>
    </tr>
    <tr>
        <td colspan="2" style="background-color: #001020"><b>Cloud deployments</b></td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-scaleway">Scaleway</a><br/>Kubernetes on Scaleway</td>
        <td>Pre-production - Unit testing, no integration or scale testing</td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-aks">Azure</a><br/>AKS Kubernetes on Azure</td>
        <td>Evaluation - Manually verified, tailoring would be needed for a production deploy.</td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-ec2">AWS EC2</a><br/>Docker compose on single-EC2 instance</td>
        <td>Evaluation - Manually verified, tailoring would be needed for a production deploy.</td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-gke">Google Cloud</a><br>GKE Kubernetes on GCP</td>
        <td>Pre-production - Manually verified, tailoring would be needed for a production deploy.</td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-aws-rke">RKE2 on AWS</a><br/>Deployed on an RKE2 distribution on AWS</td>
        <td>Evaluation - Manually verified, tailoring would be needed for a production deploy.</td>
    </tr>
</table>

## Repository Test Coverage

The following table lists TrustGraph repositories and their testing facilities:

<table>
    <tr>
        <th>Repository</th>
        <th>Purpose</th>
        <th>Test Facilities</th>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/trustgraph">trustgraph</a></td>
        <td>Unit, integration, contract tests on the core TrustGraph platform to assure compliance with expected behaviour and detect quality regression.</td>
        <td><a href="https://github.com/trustgraph-ai/trustgraph/actions/workflows/pull-request.yaml">pull requests pipeline</a></td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/trustgraph-templates">trustgraph-templates</a></td>
        <td>Unit and template generation tests on the template generation to assure expected behaviour in a number of configuration scenarios and to ensure continued successful operation of the configuration generation</td>
        <td><a href="https://github.com/trustgraph-ai/trustgraph-templates/actions/workflows/pull-request.yaml">pull requests pipeline</a></td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/simple-config-ui">simple config UI</a></td>
        <td>No tests currently</td>
        <td>-</td>
    </tr>
    <tr>
        <td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-scaleway">Scaleway deployment</a></td>
        <td>Unit testing the Pulumi deployment code to assure it uses the configuration correctly and deploys expected resources</td>
        <td><a href="https://github.com/trustgraph-ai/pulumi-trustgraph-scaleway/actions/workflows/pull-request.yaml">pull requests pipeline</a></td>
    </tr>
</table>

