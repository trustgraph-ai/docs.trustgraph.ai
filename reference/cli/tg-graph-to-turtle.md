---
title: tg-graph-to-turtle
parent: CLI
review_date: 2026-09-30
---

# tg-graph-to-turtle

Exports knowledge graph data to Turtle (TTL) format for backup, analysis, or migration.

## Synopsis

```bash
tg-graph-to-turtle [options]
```

## Description

The `tg-graph-to-turtle` command connects to TrustGraph's triple query service and exports graph triples in Turtle format. This is useful for creating backups, analyzing graph structure, migrating data, or integrating with external RDF tools.

The command queries up to 10,000 triples and outputs them in standard Turtle format to stdout, while also saving to an `output.ttl` file.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow instance ID to use |
| `-U, --user USER` | `trustgraph` | User ID for data scope |
| `-C, --collection COLLECTION` | `default` | Collection to export |

## Examples

### Basic Export
```bash
tg-graph-to-turtle
```

### Export to File
```bash
tg-graph-to-turtle > knowledge-graph.ttl
```

### Export Specific Collection
```bash
tg-graph-to-turtle -C "research-data" > research-graph.ttl
```

## Output Format

The command generates Turtle format with proper RDF syntax:

```turtle
@prefix ns1: <http://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ns1:Person rdf:type rdfs:Class .
ns1:john rdf:type ns1:Person ;
         ns1:name "John Doe" ;
         ns1:age "30" .
```

### Output Destinations

1. **stdout**: Standard output for piping or display
2. **output.ttl**: Automatically created file in current directory

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-load-knowledge`](tg-load-knowledge) - Load knowledge into graph
- [`tg-dump-msgpack`](tg-dump-msgpack) - Dump MessagePack files
- [`tg-show-graph`](tg-show-graph) - Display graph information

## API Integration

This command uses the [Triples Query API](../apis/api-triples-query) to retrieve graph data.
