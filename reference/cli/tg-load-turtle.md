---
title: tg-load-turtle
parent: CLI
review_date: 2027-05-21
---

# tg-load-turtle

Loads triples into the knowledge graph from Turtle (RDF) files.

## Synopsis

```bash
tg-load-turtle -f FLOW_ID --document-id DOC_ID [options] FILE [FILE ...]
```

## Description

The `tg-load-turtle` command parses Turtle (RDF) files using rdflib and imports the triples into the TrustGraph knowledge graph via the bulk API. This allows you to load externally produced RDF data into TrustGraph for querying and retrieval.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-f, --flow-id FLOW_ID` | Flow identifier for the import |
| `--document-id DOC_ID` | Identifier for the loaded triples |
| `FILE [FILE ...]` | One or more Turtle (.ttl) files to load |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | `$TRUSTGRAPH_WORKSPACE` or `default` | Workspace identifier |
| `-C, --collection COLLECTION` | `default` | Collection identifier |

## Examples

### Load a Single Turtle File
```bash
tg-load-turtle -f default --document-id "research-triples" data.ttl
```

### Load Multiple Files into a Collection
```bash
tg-load-turtle \
  -f default \
  --document-id "ontology-import" \
  -C ontologies \
  schema.ttl classes.ttl properties.ttl
```

### Load from a Remote Instance
```bash
tg-load-turtle \
  -u http://production:8088/ \
  -f default \
  --document-id "external-data" \
  external-graph.ttl
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-graph-to-turtle`](tg-graph-to-turtle) - Export knowledge graph to Turtle format
- [`tg-load-knowledge`](tg-load-knowledge) - Load knowledge into graph
- [`tg-show-graph`](tg-show-graph) - Display graph triples
- [`tg-query-graph`](tg-query-graph) - Query the knowledge graph
