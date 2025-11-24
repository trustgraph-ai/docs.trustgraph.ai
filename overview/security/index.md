---
title: Security
nav_order: 50
parent: Overview
review_date: 2026-03-01
---

# Cybersecurity, Privacy and Safety

**Security foundations and enterprise roadmap for TrustGraph**

The security of TrustGraph is very important as we continue to develop
the roadmap.  The team have an extensive cybersec background, having worked
on enterprise cybersecurity teams.  The founders have 40+ years of
cybersecurity and safety engineer experience and have worked in large
public companies.

The foundations are in development for a system with all the security features
you would absolutely expect for an enterprise.  For the enterprise product,
we're going to be best-in-class.  There's more to do, particularly in the
area of large cloud and enterprise integration.

Some of the foundations are formed already: The way that we've used Pulsar to
manage separate dataflows is going to be a key data separation feature for
multi-tenant environments.  Security is often applied only to data in a store,
and TrustGraph needs to be able to demonstrate that different users' data and
credentials are kept separate.  This is complex for an MCP-enabled environment
so we're going to be able to provide some optional upgrades for the enterprise
space:

- MCP credentials maintained per-user, multi-layer encrypted to minimise
  exposure to just the point of credential invocation
- An architecture for tamper-proof loggingThe multi-tenant architecture plays
  a key role, as well as being extra layers of protection for injection
  attacks and manipulation of tool calling in agentic flows

We've worked on government AI security programmes as a means to open up
government business for challenging environments, and have done a lot of
architecture work on security infrastructure for agentic and MCP frameworks.

- Some of the services optionally have credentials enabled so that
  inter-service comms can be authenticated. This will be extended to all
  components.
- The Kubernetes infrastructure deployment patterns use Pulumi to generate
  secrets so that they only exist in deployment environments and deployment
  flows
- Deployment repos such as pulumi-trustgraph-ovhcloud have security
  infrastructure testing in CI pipelines, so that if someone accidentally
  breaks the logic about securing infrastructure components, the test will
  fail

### Enterprise Vision

- 🎯 Best-in-class multi-tenant security
- 🎯 Government/defense-grade security options
- 🎯 Full audit trail and compliance support
- 🎯 Defense-in-depth architecture
- 🎯 Zero-trust security model

