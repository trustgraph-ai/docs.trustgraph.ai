---
title: tg-query-graph
parent: CLI
review_date: 2027-01-01
---

# tg-query-graph

Query the triple store with pattern matching.

## Synopsis

```bash
tg-query-graph [-s SUBJECT] [-p PREDICATE] [-o OBJECT] [-g GRAPH] [options]
```

## Description

Selectively queries the triple store by specifying any combination of subject, predicate, object, and named graph. Values are auto-detected as IRIs, literals, or quoted triples.

Auto-detection rules:
- Starts with `http://`, `https://`, `urn:`, or wrapped in `<>` -> IRI
- Starts with `<<` and ends with `>>` -> quoted triple
- Anything else -> literal

## Options

### Triple Filters

| Option | Description |
|--------|-------------|
| `-s, --subject VALUE` | Subject filter (auto-detected) |
| `-p, --predicate VALUE` | Predicate filter (auto-detected as IRI) |
| `-o, --object VALUE` | Object filter (IRI, literal, or `<<quoted triple>>`) |
| `--object-type TYPE` | Override object type: `iri`, `literal`, `triple` |
| `--object-datatype DATATYPE` | Datatype for literal object (e.g., `xsd:integer`) |
| `--object-language LANG` | Language tag for literal object (e.g., `en`) |
| `-g, --graph VALUE` | Named graph filter |

### Quoted Triple Filters

Build object as a quoted triple using explicit fields (alternative to `-o "<<s p o>>"`):

| Option | Description |
|--------|-------------|
| `--qt-subject VALUE` | Quoted triple subject |
| `--qt-subject-type TYPE` | Override: `iri`, `triple` |
| `--qt-predicate VALUE` | Quoted triple predicate (always IRI) |
| `--qt-object VALUE` | Quoted triple object |
| `--qt-object-type TYPE` | Override: `iri`, `literal`, `triple` |
| `--qt-object-datatype DATATYPE` | Datatype for qt-object literal |
| `--qt-object-language LANG` | Language tag for qt-object literal |

### Output Options

| Option | Default | Description |
|--------|---------|-------------|
| `--format FORMAT` | `space` | Output format: `space`, `pipe`, `json`, `jsonl` |
| `-H, --headers` | false | Show column headers (for space/pipe formats) |

### Standard Parameters

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow ID |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLL` | `default` | Collection identifier |
| `-l, --limit N` | `1000` | Maximum results |
| `-b, --batch-size N` | `20` | Streaming batch size |

## Examples

```bash
# Query by subject
tg-query-graph -s "http://example.org/entity"

# Query by predicate
tg-query-graph -p "http://www.w3.org/2000/01/rdf-schema#label"

# Query literal with language tag
tg-query-graph -o "Marie Curie" --object-language en

# Query quoted triple
tg-query-graph -o "<<http://ex.org/s http://ex.org/p http://ex.org/o>>"

# Query provenance graph as JSON
tg-query-graph -g "urn:graph:source" --format json
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-graph`](tg-show-graph) - Dump all graph triples
- [`tg-graph-to-turtle`](tg-graph-to-turtle) - Export graph to Turtle format
- [`tg-show-extraction-provenance`](tg-show-extraction-provenance) - Show document provenance hierarchy
