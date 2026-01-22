---
title: tg-load-knowledge
parent: CLI
review_date: 2026-09-26
---

# tg-load-knowledge

Loads RDF triples from RDF Turtle files into the TrustGraph knowledge graph.

## Synopsis

```bash
tg-load-knowledge -i DOCUMENT_ID [options] file1.ttl [file2.ttl ...]
```

## Description

The `tg-load-knowledge` command loads RDF triples from Turtle (TTL) format files into TrustGraph's knowledge graph. It parses Turtle files, converts them to TrustGraph's internal triple format, and imports them using WebSocket connections for efficient batch processing.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-i, --document-id ID` | Document ID to associate with the triples |
| `files` | One or more Turtle files to load |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `ws://localhost:8088/` | TrustGraph API URL (WebSocket) |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow instance ID to use |
| `-U, --user USER` | `trustgraph` | User ID for triple ownership |
| `-C, --collection COLLECTION` | `default` | Collection to assign triples |

## Examples

### Load Single File
```bash
tg-load-knowledge -i "doc123" knowledge-base.ttl
```

### Load Multiple Files
```bash
tg-load-knowledge -i "ontology-v1" \
  schema.ttl \
  instances.ttl \
  relationships.ttl
```

### Load with Custom Collection
```bash
tg-load-knowledge \
  -i "research-data" \
  -C "research-kg" \
  research-triples.ttl
```

## Turtle Format

The command supports standard RDF Turtle syntax:

```turtle
@prefix ex: <http://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

ex:Person rdf:type rdfs:Class .
ex:john rdf:type ex:Person ;
        ex:name "John Doe" ;
        ex:age "30"^^xsd:integer .
```

## Notes

The command uses WebSocket connections for efficient batch processing and includes retry logic to handle network interruptions during large data imports.

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-graph-to-turtle`](tg-graph-to-turtle) - Export graph to Turtle format
- [`tg-load-structured-data`](tg-load-structured-data) - Load structured data
- [`tg-show-graph`](tg-show-graph) - Display graph information

## API Integration

This command uses the [Knowledge Load API](../apis/api-knowledge) via WebSocket for efficient batch triple loading.
