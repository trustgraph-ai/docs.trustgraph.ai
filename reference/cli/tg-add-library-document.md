---
title: tg-add-library-document
parent: CLI
review_date: 2026-11-30
---

# tg-add-library-document

Adds documents to the TrustGraph library with comprehensive metadata support.

## Synopsis

```bash
tg-add-library-document [options] file1 [file2 ...]
```

## Description

The `tg-add-library-document` command adds documents to the TrustGraph library system with rich metadata management. The library approach provides better document lifecycle management and processing control compared to direct document loading.

Documents added to the library can later be processed using `tg-start-library-processing`.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `files` | One or more files to add to the library |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-U, --user USER` | `trustgraph` | User identifier |

### Document Metadata

| Option | Description |
|--------|-------------|
| `--name NAME` | Document name/title |
| `--description DESCRIPTION` | Document description |
| `--id ID` | Custom document identifier (defaults to content hash) |
| `--kind MIMETYPE` | Document MIME type (auto-detected if not specified) |
| `--tags TAGS` | Comma-separated list of tags |
| `--document-url URL` | Original document source URL |
| `--keyword KEYWORDS` | Document keywords (space-separated) |

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
| `--publication-organization ORG` | Publishing organization name |
| `--publication-description DESC` | Publication description |
| `--publication-date DATE` | Publication date |
| `--publication-url URL` | Publication URL |

## Examples

### Basic Document Addition
```bash
tg-add-library-document report.pdf
```

### With Complete Metadata
```bash
tg-add-library-document \
  --name "Annual Research Report 2024" \
  --description "Comprehensive analysis of research outcomes" \
  --copyright-holder "Research Institute" \
  --copyright-year "2024" \
  --license "CC BY 4.0" \
  --tags "research,annual,analysis" \
  annual-report.pdf
```

### Multiple Documents
```bash
tg-add-library-document \
  --tags "research,2024" \
  --copyright-holder "University" \
  paper1.pdf paper2.pdf paper3.pdf
```

### With Publication Info
```bash
tg-add-library-document \
  --name "Machine Learning in Healthcare" \
  --publication-organization "Medical Journal" \
  --publication-date "2024-01-15" \
  --publication-url "https://journal.example.com/article" \
  ml-healthcare.pdf
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-library-documents`](tg-show-library-documents) - List documents in library
- [`tg-start-library-processing`](tg-start-library-processing) - Process library documents
- [`tg-remove-library-document`](tg-remove-library-document) - Remove documents from library

## API Integration

This command uses the Librarian API to add documents with metadata to the persistent library system.
