---
title: Developer's Guide
layout: default
parent: Community
grand_parent: TrustGraph Documentation
---

# Developer Guide

This guide provides instructions for developers working on TrustGraph, covering build processes, release management, and local development.

## Community contributors

We welcome community contributions.  We love constructive discussions and
debates about AI, knowledge graphs, data sovereignty and responsible AI.
Also, how to achieve these things through good engineering.

### Philosophy

TrustGraph values:

- Radical Transparency and Open Source Accountability

  The community would prioritize complete transparency in AI
  operations, making all components inspectable, modifiable, and
  auditable. TrustGraph is "built with transparency and community
  collaboration in mind" and allows users to "easily inspect, modify,
  and extend the platform." This principle would extend beyond code to
  include decision-making processes, data handling, and algorithmic
  choices.

- Knowledge Sovereignty and Reusability

  A core tenet would be empowering users to truly own and control
  their knowledge assets. TrustGraph enables "reusable Knowledge Cores
  that can be stored, shared, and reloaded," reflecting a philosophy
  that knowledge should be portable, persistent, and under user
  control rather than locked into proprietary systems.

- Modular Interoperability Over Vendor Lock-in

  The community would champion architectural flexibility that prevents
  dependency on any single provider. TrustGraph provides "component
  flexibility" to "avoid component lock-in" and "integrates multiple
  options for all system components." This philosophy would extend to
  supporting diverse deployment environments and maintaining
  compatibility across different AI ecosystems.

- Contextual Intelligence Through Structured Relationships

  Rather than treating data as isolated fragments, the community would
  emphasize understanding information through its connections and
  relationships. TrustRAG "understands and utilizes the relationships
  between pieces of information" and leverages "automatically
  constructed Knowledge Graphs to provide richer and more accurate
  context." This represents a philosophy that meaningful AI requires
  structured, interconnected understanding.

- Collaborative Security and Distributed Trust

  The community would operate on principles of shared responsibility
  for AI safety and security, with trust built through collective
  verification rather than centralized authority. TrustGraph focuses
  on "providing a secure supply chain for AI components" while
  maintaining open-source accessibility, suggesting a model where
  security emerges from community oversight and collaborative
  validation.

- Automate everything

  We have a lot of integrating to do.

If it isn't obvious we value well-architected software.  Good software
unlocks all of the above values.  Well-architected software prizes
innovation as well as maturity.  So, we value architectural principles
which allow innovative software and experimental capability to sit alongside
robustly mature software.

### Use of git

#### Branches

- Release branches: `release/X.Y` e.g. `release/1.0`
- Feature branches: `feature/FEATURE-NAME` e.g. `feature/authentication`
- Maintenance branches: `maint/MAINT-NAME` e.g. `maint/update-pulsar-deps`
- Bugfix branches: `fix/FIX-NAME` e.g. `fix/gateway-proto-failure`

#### Tags

- Release tags: `vX.Y.Z` e.g. `v1.2.3`

## Release Management

### Release Process

1. **Prepare Git Repository**
   
   Ensure your repository is clean and ready for release.

2. **Tag the Release**
   
   Create and push a version tag:
   
   ```bash
   git tag -a v1.2.3 -m ''
   git push --tags
   ```
   
3. CI/CD pipelines deliver the results to Docker Hub

## Local Development

### Building Locally

You need a good configuration to work with.  Testing with Podman Compose
works best.  To make a configuration, either:
- be prepared to create a configuration and modify it:
  https://config-ui.demo.trustgraph.ai, or
- Study how to build configurations with the underlying template tool:
  https://github.com/trustgraph-ai/trustgraph-templates

### Building product

The core system consists of many package types, but they have different
value chains.  The service deployment is a set of containers, built to
include packages, so the target environment is a Docker Compose file
launched to execute the containers.

Whereas client-side, Python packages are enough to execute capability
which interacts with running services.

#### Building Python packages

```
make packages VERSION=x.y.z
```

This creates packages under the `dist` directory.  You can then use `pip`
to install them.

#### Building containers

```
make container VERSION=x.y.z
```

You can then use a `docker-compose.yaml` file to run them.  Such a file
can be created from the TrustGraph config utility or the
`trustgraph-templates` utility repo.

