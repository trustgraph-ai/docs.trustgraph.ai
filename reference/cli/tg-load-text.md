---
title: tg-load-text
parent: CLI
review_date: 2026-05-03
---

# tg-load-text

Loads text documents into TrustGraph processing pipelines with rich metadata support.

## Synopsis

```bash
tg-load-text [options] file1 [file2 ...]
```

## Description

The `tg-load-text` command is a low-level operation that loads text documents directly into the processing input queue. It creates a SHA256 hash-based document ID and supports comprehensive metadata including copyright information, publication details, and keywords.

**Note**: This command pushes documents straight into the processing input queue, bypassing the librarian service. Users are advised to use `tg-add-library-document` instead, which provides better document management, tracking, and processing control through the librarian service.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `files` | One or more text files to load |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id FLOW` | `default` | Flow ID for processing |
| `-U, --user USER` | `trustgraph` | User identifier |
| `-C, --collection COLLECTION` | `default` | Collection identifier |

### Document Metadata

| Option | Description |
|--------|-------------|
| `--name NAME` | Document name/title |
| `--description DESCRIPTION` | Document description |
| `--document-url URL` | Document source URL |
| `--keyword KEYWORD` | Document keywords (can specify multiple times) |

### Copyright Information

| Option | Description |
|--------|-------------|
| `--copyright-notice NOTICE` | Copyright notice text |
| `--copyright-holder HOLDER` | Copyright holder name |
| `--copyright-year YEAR` | Copyright year |
| `--license LICENSE` | Copyright license |

### Publication Information

| Option | Description |
|--------|-------------|
| `--publication-organization ORG` | Publishing organization |
| `--publication-description DESC` | Publication description |
| `--publication-date DATE` | Publication date |

## Examples

### Load Text File
```bash
tg-load-text document.txt
```

### Load Multiple Files
```bash
tg-load-text file1.txt file2.txt file3.txt
```

### With Metadata
```bash
tg-load-text \
  --name "Research Notes" \
  --description "AI research findings" \
  --keyword "AI" --keyword "research" \
  notes.txt
```

### Complete Metadata Example
```bash
tg-load-text \
  --name "Technical Article" \
  --description "Deep learning architecture analysis" \
  --copyright-holder "Tech Publisher" \
  --copyright-year "2024" \
  --license "CC-BY-4.0" \
  --publication-organization "Journal of AI" \
  --publication-date "2024-01-15" \
  article.txt
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-load-pdf`](tg-load-pdf) - Load PDF documents
- [`tg-add-library-document`](tg-add-library-document) - Add documents to library
- [`tg-start-library-processing`](tg-start-library-processing) - Process documents

## API Integration

This command uses the [Text Load API](../apis/api-text-load) to process text files.
