---
title: tg-invoke-document-rag
parent: CLI
review_date: 2027-01-01
---

# tg-invoke-document-rag

Answers questions using Document RAG over the document corpus.

## Synopsis

```bash
tg-invoke-document-rag -q QUESTION [options]
```

## Description

Answers questions by retrieving relevant document chunks and generating responses using an LLM. Supports streaming output and an explainability mode that shows provenance events inline.

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
| `-f, --flow-id ID` | `default` | Flow ID |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLLECTION` | `default` | Collection identifier |
| `-d, --doc-limit N` | `10` | Maximum documents to retrieve |
| `--no-streaming` | false | Disable streaming |
| `-x, --explainable` | false | Show provenance events: Question, Exploration, Synthesis |
| `--debug` | false | Show debug output |

## Examples

```bash
# Basic query
tg-invoke-document-rag -q "What is the company's return policy?"

# With explainability
tg-invoke-document-rag -x -q "What are the privacy requirements?" -C legal-docs

# Limit documents
tg-invoke-document-rag -q "How do I configure SSL?" -d 5
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-graph-rag`](tg-invoke-graph-rag) - Graph RAG queries
- [`tg-invoke-agent`](tg-invoke-agent) - Agent Q&A
- [`tg-show-explain-trace`](tg-show-explain-trace) - Review full explainability traces
- [`tg-show-library-documents`](tg-show-library-documents) - List available documents
