---
title: Backup & Restore
parent: Advanced Topics
review_date: 2026-03-01
---

# Backup & Restore

## Recovery Options

TrustGraph makes use of standard storage mechanisms, which come with
their own backup options:

- Neo4j: https://neo4j.com/docs/operations-manual/current/backup-restore/
- Memgraph: https://memgraph.com/docs/database-management/backup-and-restore
- Qdrant: https://qdrant.tech/documentation/database-tutorials/create-snapshot/
- MinIO: https://docs.min.io/enterprise/aistor-object-store/operations/failure-and-recovery/
- Cassandra: https://cassandra.apache.org/doc/4.0/cassandra/operating/backups.html
- Milvus: https://milvus.io/docs/milvus_backup_overview.md

When planning for backup/restore it may not be enough just to make sure
you have a copy of the database, but also to consider the recovery
window in the event of a disaster, and so planning for a resilient
deployment with multiple copies and a number of recovery points should be
a part of an operational deployment plan.

The storage products used by TrustGraph can be deployed in enterprise
offerings which provide for greater resilience and site reliability.

## Knowledge Cores

Another option to retain the state of your TrustGraph-extracted knowledge
is to use knowledge cores which can be self-managed and loaded back into
the system to load into the same state.

## Enterprise Support

Operational support for TrustGraph is available from KnowNext at
[https://knownext.io](https://knownext.io).

