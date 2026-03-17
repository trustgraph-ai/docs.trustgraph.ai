---
title: tg-invoke-embeddings
parent: CLI
review_date: 2027-01-01
---

# tg-invoke-embeddings

Converts text to vector embeddings.

## Synopsis

```bash
tg-invoke-embeddings TEXT [TEXT ...] [options]
```

## Description

Invokes the embeddings service to convert one or more text inputs into vector embeddings. Returns each embedding as a list of floats.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `TEXT` | One or more text strings to embed |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow ID |

## Examples

```bash
# Single text
tg-invoke-embeddings "quantum computing"

# Multiple texts
tg-invoke-embeddings "first text" "second text"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-graph-embeddings`](tg-invoke-graph-embeddings) - Search graph entities by similarity
- [`tg-invoke-document-embeddings`](tg-invoke-document-embeddings) - Search document chunks by similarity
- [`tg-invoke-row-embeddings`](tg-invoke-row-embeddings) - Search structured data by similarity
