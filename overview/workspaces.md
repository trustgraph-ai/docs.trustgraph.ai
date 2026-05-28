---
title: Workspaces & Data Isolation
nav_order: 30
parent: Overview
grand_parent: TrustGraph Documentation
review_date: 2026-11-01
guide_category:
  - Enterprise integration
guide_category_order: 5
guide_description: How TrustGraph uses workspaces to isolate data between tenants
guide_banner: data-isolation.jpg
guide_emoji: "\U0001F512"
---

# Workspaces & Data Isolation

TrustGraph uses **workspaces** as the primary boundary for keeping data
separate. A workspace is an isolated tenancy scope in which users, flows,
configuration, documents, and knowledge graphs live. Data belonging to one
workspace is not visible to another.

## How workspaces keep data apart

Workspace isolation is enforced at multiple levels of the architecture:

- **Pub/sub queues** — workspace-scoped services use per-workspace queues.
  When two workspaces run flows with the same name, their messages travel
  on entirely separate queues. This is structural isolation — data
  separation is enforced by infrastructure, not by trusting a field in a
  message body.

- **Storage** — knowledge graphs, document libraries, embeddings, and
  configuration are all partitioned by workspace at the storage layer.
  Queries are scoped so that one workspace cannot read or write another
  workspace's data.

- **Gateway enforcement** — the API gateway resolves the workspace from
  the caller's authenticated credentials before any request reaches a
  backend service. Callers cannot specify a different workspace — identity
  determines access.

## Users and access control

TrustGraph supports two types of credential:

- **API keys** — long-lived tokens for programmatic access, CLI tools, and
  integrations. API keys have a `tg_` prefix and can optionally have an
  expiry date.
- **Username and password** — used for interactive login via the workbench.
  A successful login exchanges the credentials for a temporary JWT token
  which expires after a set period.

Each credential is bound to a workspace at the time it is issued.

In the open-source edition, the access model is deliberately simple:

- Each user is associated with a single workspace
- Users have **read/write** access to their workspace, or **admin** access
  which grants access across all workspaces
- Three built-in roles — `reader`, `writer`, and `admin` — control what
  operations a user can perform

The admin role is intended for platform operators who manage workspaces
and users. Regular users work within their assigned workspace.

## Collections and flows

Within a workspace, data is further organised by **collections** and
**flows**:

- A **collection** groups related knowledge graphs, embeddings, and
  documents together. A workspace can have multiple collections.
- A **flow** is a running data processing pipeline. Flows are owned by
  their workspace and use workspace-scoped queues for all communication.

## Enterprise access control

The workspace and IAM architecture is designed to be extensible. The
open-source edition ships a simple role-based model, but the system
supports pluggable IAM regimes. Enterprise offerings can provide:

- Multi-workspace access for a single user with per-workspace permissions
- External identity provider integration (OIDC, SAML, LDAP)
- Fine-grained, rules-based access control
- Cross-workspace administration for platform operators

See [Enterprise Offerings](enterprise) for more on the enterprise
product, and [Security](security) for the broader security architecture.
