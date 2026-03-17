---
title: tg-invoke-graph-rag
parent: CLI
review_date: 2027-01-01
---

# tg-invoke-graph-rag

Answers questions using Graph RAG over the knowledge graph.

## Synopsis

```bash
tg-invoke-graph-rag -q "question" [options]
```

## Description

Performs graph-based Retrieval Augmented Generation (RAG) to answer questions using knowledge graph entities and relationships. Supports streaming output and an explainability mode that shows the full reasoning pipeline.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-q, --question QUESTION` | Question to answer |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id FLOW` | `default` | Flow ID |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLLECTION` | `default` | Collection identifier |

### Graph Search Parameters

| Option | Default | Description |
|--------|---------|-------------|
| `-e, --entity-limit N` | `50` | Maximum entities to retrieve |
| `--triple-limit N` | `30` | Maximum triples to retrieve |
| `-s, --max-subgraph-size N` | `150` | Maximum subgraph size |
| `-p, --max-path-length N` | `2` | Maximum path length for traversal |

### Mode Options

| Option | Default | Description |
|--------|---------|-------------|
| `--no-streaming` | false | Disable streaming (use REST mode) |
| `-x, --explainable` | false | Show provenance events: Question, Grounding, Exploration, Focus, Synthesis |
| `--debug` | false | Show debug output |

## Examples

```bash
# Basic query
tg-invoke-graph-rag -q "What is the relationship between AI and machine learning?"

# With explainability
tg-invoke-graph-rag -x -q "Who are the key researchers?"

# Custom search parameters
tg-invoke-graph-rag -q "What connections exist?" -e 100 --triple-limit 50
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-document-rag`](tg-invoke-document-rag) - Document RAG queries
- [`tg-invoke-agent`](tg-invoke-agent) - Agent Q&A
- [`tg-show-explain-trace`](tg-show-explain-trace) - Review full explainability traces
- [`tg-show-graph`](tg-show-graph) - View graph triples
