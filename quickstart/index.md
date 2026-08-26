---
title: Quickstart
nav_order: 200
has_children: true
---

# Quickstart

Get TrustGraph running and see it work with your own eyes. By the end
of this guide you'll have a working instance, loaded data, queried a
knowledge graph, and seen explainability in action.

## What you're going to do

1. **Launch TrustGraph** using Docker Compose or Podman Compose on a
   single machine — a laptop, workstation, or cloud instance
2. **Load documents** and process them into a knowledge graph
3. **Query with Graph RAG** and see how answers trace back to sources
4. **Use ontologies** to control what knowledge gets extracted
5. **Run SPARQL queries** against structured knowledge
6. **Explore the graph** visually in the Context Graph viewer

The whole thing takes under 30 minutes.

## What you'll need

- A machine with **12GB+ RAM and 8 CPUs** available for TrustGraph — a
  16GB laptop will work if nothing else heavy is running
- **Docker Engine** or **Podman** installed
- **Python 3** for CLI tools
- **Access to an LLM** — a cloud API key (OpenAI, Anthropic, Google
  VertexAI, AWS Bedrock) or a local model via Ollama
- Basic command-line familiarity

If Docker Compose on a single machine isn't right for your situation,
see the [deployment options](../../deployment/) for Kubernetes,
cloud platforms, and other approaches. This quickstart focuses on the
simplest path to get you running.

## Next

[Prepare the configuration](prepare) — generate your deployment config.
