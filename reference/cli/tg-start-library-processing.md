---
title: tg-start-library-processing
parent: CLI
review_date: 2025-12-23
---

# tg-start-library-processing

Submits a library document for processing through TrustGraph workflows.

## Synopsis

```bash
tg-start-library-processing -d DOCUMENT_ID --id PROCESSING_ID [options]
```

## Description

The `tg-start-library-processing` command initiates processing of a document stored in TrustGraph's document library. This triggers workflows that extract text, generate embeddings, create knowledge graphs, and enable document search and analysis.

The processing ID must be a URI. While the value isn't presently used, a future use-case will use this identifier in the knowledge graph.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-d, --document-id ID` | Document ID from the library to process |
| `--id, --processing-id ID` | Unique identifier for this processing job (must be a URI) |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-U, --user USER` | `trustgraph` | User ID for processing context |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-i, --flow-id ID` | `default` | Flow instance to use for processing |
| `--collection COLLECTION` | `default` | Collection to assign processed data |
| `--tags TAGS` | (none) | Comma-separated tags for the processing job |

## Examples

### Basic Document Processing
```bash
tg-start-library-processing \
  -d "doc_123456789" \
  --id "urn:trustgraph:processing:001"
```

### Processing with Custom Collection
```bash
tg-start-library-processing \
  -d "doc_research_paper" \
  --id "urn:trustgraph:processing:research-001" \
  --collection "research-papers" \
  --tags "nlp,research,2023"
```

### Processing with Specific Flow
```bash
tg-start-library-processing \
  -d "doc_technical_manual" \
  --id "urn:trustgraph:processing:manual-001" \
  -i "document-analysis-flow" \
  -U "technical-team" \
  --collection "technical-docs"
```

## Processing Workflow

Document processing typically includes these steps:
1. Document retrieval from library
2. Content extraction (text, metadata)
3. Text processing (cleaning, normalization)
4. Embedding generation (vector embeddings)
5. Knowledge extraction (triples, entities)
6. Index creation (searchable content)

Different document types (PDF, text, images, structured data) may trigger different processing workflows.

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-library-documents`](tg-show-library-documents) - List library documents
- [`tg-show-library-processing`](tg-show-library-processing) - View processing status
- [`tg-stop-library-processing`](tg-stop-library-processing) - Remove processing record
- [`tg-show-flows`](tg-show-flows) - Monitor active flows

## API Integration

This command uses the [Library API](../apis/api-librarian) to initiate document processing workflows.
