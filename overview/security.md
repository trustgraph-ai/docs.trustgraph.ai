---
title: Security
nav_order: 50
parent: Overview
review_date: 2026-07-01
guide_category:
  - Enterprise integration
guide_category_order: 3
guide_description: Cybersecurity foundations, privacy protections, and enterprise security roadmap
guide_difficulty: intermediate
guide_time: 5 min
guide_emoji: 🔒
guide_banner: security.jpg
guide_labels:
  - Security
  - Enterprise
  - Compliance
todo: true
todo_notes: Revisit once MCP IAM lands in 2.5 — will need to cover authentication and authorization for MCP tool services and how they integrate with the existing IAM model
---

# Cybersecurity, Privacy and Safety

**Security architecture for TrustGraph**

The security of TrustGraph is very important as we continue to develop
the roadmap. The team have an extensive cybersec background, having worked
on enterprise cybersecurity teams. The founders have 40+ years of
cybersecurity and safety engineering experience and have worked in large
public companies.

We've worked on government AI security programmes as a means to open up
government business for challenging environments, and have done a lot of
architecture work on security infrastructure for agentic and MCP frameworks.

## Authentication

TrustGraph enforces authentication at the API gateway — the single entry
point for all external access. Internal services trust the gateway and do
not re-authenticate, keeping the architecture simple and the enforcement
point clear.

Two credential types are supported:

- **API keys** — long-lived tokens for programmatic access, CLI tools, and
  integrations. Keys are stored hashed and can be revoked individually
  without affecting other users. Keys optionally have an expiry date.
- **Username and password** — used for interactive login via the workbench.
  A successful login exchanges the credentials for a temporary JWT signed
  with Ed25519 keys. The gateway validates JWTs locally using the IAM
  service's public key — no service call needed for the authentication step.

Error responses for authentication and access control failures carry no
diagnostic detail, preventing attackers from probing which condition they
tripped. Server-side audit logging records the specific reason for
operators and post-incident forensics.

## Workspace Isolation

Workspaces are the primary boundary for data separation. Isolation is
enforced structurally at multiple levels — pub/sub queues, storage
partitioning, and gateway enforcement. See
[Workspaces & Data Isolation](workspaces) for full details.

## Access Control

The open-source edition ships a role-based access control model with three
built-in roles — `reader`, `writer`, and `admin`. Workspace scope is a
property of the grant: reader and writer capabilities are scoped to the
user's workspace, while admin capabilities span all workspaces.

The gateway gates each endpoint by capability, not by role. Authorisation
decisions are delegated to the IAM service on every request, keeping
policy logic out of the gateway.

## Infrastructure Security

- **Pulumi-generated secrets** — Kubernetes deployment patterns use Pulumi
  to generate secrets (IAM bootstrap tokens, Grafana passwords, signing
  keys) so that they only exist in deployment environments and deployment
  flows
- **CI security testing** — deployment repos such as
  pulumi-trustgraph-ovhcloud have security infrastructure testing in CI
  pipelines, so that if someone accidentally breaks the logic about
  securing infrastructure components, the test will fail

## MCP Service

{: .warning }
> The MCP server does not currently support IAM credentials. Its requests
> to the API gateway will be rejected by the authentication layer. This is
> expected to be addressed in TrustGraph 2.5.

## Enterprise IAM

TrustGraph implements rich IAM plugin interfaces, permitting use of the
basic open-source capabilities or enterprise-grade or custom services
which integrate with an enterprise's specific IAM services. The gateway
communicates with the IAM service through a well-defined contract —
enterprise offerings can replace the open-source IAM regime without
changing the gateway, the wire protocol, or the capability vocabulary.

Enterprise IAM capabilities include:

- Multi-workspace access for a single user with per-workspace permissions
- External identity provider integration (OIDC, SAML, LDAP)
- Fine-grained, rules-based access control
- MCP credentials maintained per-user, multi-layer encrypted to minimise
  exposure to just the point of credential invocation
- Tamper-proof audit logging
- Defense-in-depth protections for injection attacks and manipulation of
  tool calling in agentic flows

### Enterprise Vision

- Best-in-class multi-tenant security
- Government/defense-grade security options
- Full audit trail and compliance support
- Defense-in-depth architecture
- Zero-trust security model
