---
title: Clustering
parent: Advanced Topics
grand_parent: TrustGraph Documentation
review_date: 2026-03-01
---

# Clustering

## Standard Configuration

The base configurations deployed by the TrustGraph configuration
portal consists optimised for a smaller footprint.  We want to deploy
a configuration which can easily be tailed for performance and resilience
while keeping the footprint low to make it easier for an evaluation to be
performed.

## Clustering Options

To enable a more performant or resilient footprint, you might consider:

- Using a hosted cloud environment, such as [Scaleway](/deployment/scaleway)
  or [OVHcloud](/deployment/ovhcloud) can provide a platform with a fully
  supported Kubernetes platform.
- Modifying the configuration to deploy multiple copies of containers is
  a way to improve operational endurance in the face of failures.
  - All of the TrustGraph parallelise processing when deployed as multiple
    instances.
  - Pulsar supports federated deployment of Zookeeper, Bookkeeper and
    Pulsar brokers
  - Neo4j and Memgraph offer mirrored and federated configurations to
    improve resilience and performance.
  - Cassandra can be federated and optimised for multi-data-center and
    multi-region resilience.
  - Qdrant supports federated configurations.

## Enterprise Support

Operational support for TrustGraph is available from KnowNext at
[https://knownext.io](https://knownext.io).  Support includes
continuous testing of the customer's configuration, and dedicated
site reliability and operational support packages.

