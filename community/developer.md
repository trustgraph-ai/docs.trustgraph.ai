---
title: Developer's Guide
layout: default
nav_order: 4
parent: Community
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

## Development Workflow

### Working with AI Assistants

When working with AI assistants like Claude for development.

Be aware...
- AI assistants are not perfect.  Your job is to learn their limitations
  and work with them.
- Assistants can be forgetful, so "writing things down" is a good plan.
  Submit a tech spec along with your pull request, and other people will be
  able to use AI assistants to enchance, test, and verify your work.
- Assistants can get confused with large quantities of stuff.  So get them
  to be modular. Bring things into well-defined classes and modules
  reduces the need to "know everything" at once.
- AI assistants are a little random and can 'go off-pieste' if things
  get confusing, so catch them before they do this to save yourself a bunch
  of time.
- Try to get an understanding of how things are solved in the codebase to
  prevent assistants from re-inventing the wheel regarding something that's
  already solved in the codebase.

A useful process guide:
1. **Read the Test Strategy**: Have the AI assistant read `TEST_STRATEGY.md`
   to understand testing approaches
2. **Branch from Latest Release**: Fork the repo and create a branch off the
   latest `release/vX.Y`
3. **Create Technical Specifications**: Get the assistant to write tech
   specs in `docs/tech-specs/WHATEVER.md` for new features.  It helps to be
   iterative for complex work.  Start with an empty template and add
   requirements a bit at time, and check the assistant is doing the right
   thing.  Shout on the Discord forum if you want something reviewed.
4. **Iterative Development**: Review and refine the tech spec before
   implementation.
5. **Commit the Tech Spec**: Save the specification before beginning
   implementation.
6. **Implement with Regular Commits**: Commit changes regularly to bank
   progress and enable easy rollbacks.
7. **Create Pull Requests**: Push changes and create PRs for review, do this
   as your code becomes more mature so you get an idea what the test suite
   thinks of your change.
8. **Verify Tests**: Ensure all tests pass before merging.
9. **Write Tests for New Features**: Add comprehensive tests for any new
   functionality.

### Testing Environment Setup

For local testing, set up a Python virtual environment in the trustgraph directory:

```bash
python3 -m venv env
source env/bin/activate  # On Linux/Mac
# or
env\Scripts\activate     # On Windows

pip install ./trustgraph-base
pip install ./trustgraph-cli
pip install ./trustgraph-flow
pip install ./trustgraph-vertexai
pip install ./trustgraph-bedrock

# Run tests
pytest tests -m 'not slow'
```

Note: As we use the 'trustgraph' namespace across multiple packages,
`pip install -e` seems not to work well.

**Important Notes:**
- Reinstall packages (`pip install ./package-name`) whenever code changes
- Run tests periodically to catch issues early
- AI assistants may not remember to reinstall packages, so monitor this manually

It can save time and token usage by running the tests yourself and
cut'n'pasting just the errors into the code assistant.

### Development Best Practices

- **Modular Code**: Write modular, well-architected code - this helps both AI
  assistants and human developers
- **Incremental Progress**: AI assistants aren't perfect, so encourage
  incremental changes
- **Regular Testing**: Test frequently to prevent major issues
- **Clear Specifications**: Document intentions clearly in tech specs before
  implementation
- **Solve common problems** commonly.  As well as all the old-school
  benefits, this really does save a ton of time and token usage

### Share your experiences

We love Claude and Qwen coding models, we want to hear about your experiences
too, get in Discord and share.
