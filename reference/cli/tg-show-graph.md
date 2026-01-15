---
title: tg-show-graph
parent: CLI
review_date: 2026-03-28
---

# tg-show-graph

Displays knowledge graph triples (edges) from TrustGraph.

## Synopsis

```bash
tg-show-graph [options]
```

## Description

The `tg-show-graph` command queries the knowledge graph and displays up to 10,000 triples (subject-predicate-object relationships) in human-readable format. Useful for exploring knowledge graph contents and understanding entity relationships.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id FLOW` | `default` | Flow ID to query |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLLECTION` | `default` | Collection identifier |

## Examples

### Display All Graph Triples
```bash
tg-show-graph
```

### Query Specific Flow
```bash
tg-show-graph -f research-flow
```

### Query User's Collection
```bash
tg-show-graph -U researcher -C medical-papers
```

### Using Custom API URL
```bash
tg-show-graph -u http://production:8088/
```

## Output Format

Triples are displayed in subject-predicate-object format:

```
<Person1> <hasName> "John Doe"
<Person1> <worksAt> <Organization1>
<Organization1> <hasName> "Acme Corporation"
<Document1> <createdBy> <Person1>
<Document1> <hasTitle> "Research Report"
```

### Triple Components

- **Subject**: Entity the statement is about (URI in angle brackets)
- **Predicate**: Relationship or property (URI in angle brackets)
- **Object**: Value or target entity (URI or literal in quotes)

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-load-kg-core`](tg-load-kg-core) - Load knowledge core into flow
- [`tg-invoke-graph-rag`](tg-invoke-graph-rag) - Query knowledge graph
- [`tg-show-kg-cores`](tg-show-kg-cores) - List available knowledge cores

## API Integration

This command uses the Knowledge API to retrieve RDF triples from the active knowledge graph.
