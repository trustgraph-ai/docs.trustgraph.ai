---
title: tg-invoke-graph-rag
parent: CLI
review_date: 2026-05-27
---

# tg-invoke-graph-rag

Uses Graph RAG to answer questions using knowledge graph data.

## Synopsis

```bash
tg-invoke-graph-rag -q "question" [options]
```

## Description

The `tg-invoke-graph-rag` command performs graph-based Retrieval Augmented Generation (RAG) to answer questions using structured knowledge from the knowledge graph. Retrieves relevant entities and relationships to provide contextually accurate answers.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-q, --question QUESTION` | Question to answer using graph knowledge |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id FLOW` | `default` | Flow ID to use |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLLECTION` | `default` | Collection identifier |

### Graph Search Parameters

| Option | Default | Description |
|--------|---------|-------------|
| `-e, --entity-limit LIMIT` | `50` | Maximum entities to retrieve |
| `-t, --triple-limit LIMIT` | `30` | Maximum triples to retrieve |
| `-s, --max-subgraph-size SIZE` | `150` | Maximum subgraph size |
| `-p, --max-path-length LENGTH` | `2` | Maximum path length for traversal |

## Examples

### Basic Graph RAG Query
```bash
tg-invoke-graph-rag -q "What is the relationship between AI and machine learning?"
```

### With Custom Parameters
```bash
tg-invoke-graph-rag \
  -q "Who are the key researchers in this field?" \
  -e 100 \
  -t 50
```

### Specific Flow and Collection
```bash
tg-invoke-graph-rag \
  -q "What connections exist between these entities?" \
  -f research-flow \
  -C academic-papers
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-document-rag`](tg-invoke-document-rag) - Query using document RAG
- [`tg-load-kg-core`](tg-load-kg-core) - Load knowledge into flow
- [`tg-show-graph`](tg-show-graph) - View graph triples

## API Integration

This command uses the Graph RAG API to perform knowledge graph queries with retrieval-augmented generation.
