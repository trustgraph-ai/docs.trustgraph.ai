---
title: tg-load-pdf
parent: CLI
review_date: 2026-04-17
---

# tg-load-pdf

Loads PDF documents into TrustGraph for processing and analysis.

## Synopsis

```bash
tg-load-pdf [options] file1.pdf [file2.pdf ...]
```

## Description

The `tg-load-pdf` command is a low-level operation that loads PDF documents directly into the processing input queue. The command extracts content, generates document metadata, and makes the documents available for processing by other TrustGraph services.

Each PDF is assigned a unique identifier based on its content hash, and comprehensive metadata can be attached including copyright information, publication details, and keywords.

**Note**: This command pushes documents straight into the processing input queue, bypassing the librarian service. Users are advised to use `tg-add-library-document` instead, which provides better document management, tracking, and processing control through the librarian service.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `files` | One or more PDF files to load |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow instance ID to use |
| `-U, --user USER` | `trustgraph` | User ID for document ownership |
| `-C, --collection COLLECTION` | `default` | Collection to assign document |

### Document Metadata

| Option | Description |
|--------|-------------|
| `--name NAME` | Document name/title |
| `--description DESCRIPTION` | Document description |
| `--identifier ID` | Custom document identifier |
| `--document-url URL` | Source URL for the document |
| `--keyword KEYWORD` | Document keywords (can specify multiple times) |

### Copyright Information

| Option | Description |
|--------|-------------|
| `--copyright-notice NOTICE` | Copyright notice text |
| `--copyright-holder HOLDER` | Copyright holder name |
| `--copyright-year YEAR` | Copyright year |
| `--license LICENSE` | Copyright license |

### Publication Details

| Option | Description |
|--------|-------------|
| `--publication-organization ORG` | Publishing organization |
| `--publication-description DESC` | Publication description |
| `--publication-date DATE` | Publication date |

## Examples

### Load Single PDF
```bash
tg-load-pdf document.pdf
```

### Load Multiple Files
```bash
tg-load-pdf report1.pdf report2.pdf manual.pdf
```

### With Metadata
```bash
tg-load-pdf \
  --name "Technical Manual" \
  --description "System administration guide" \
  --keyword "technical" --keyword "manual" \
  technical-manual.pdf
```

### Complete Metadata Example
```bash
tg-load-pdf \
  --name "Research Paper" \
  --description "AI Research Publication" \
  --copyright-holder "University Press" \
  --copyright-year "2024" \
  --license "CC-BY-4.0" \
  --publication-organization "Academic Publisher" \
  --publication-date "2024-01-15" \
  research-paper.pdf
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-add-library-document`](tg-add-library-document) - Add documents to library
- [`tg-start-library-processing`](tg-start-library-processing) - Process documents
- [`tg-load-text`](tg-load-text) - Load text files

## API Integration

This command uses the [PDF Decoder API](../apis/api-document-load) to process PDF files.
