---
title: tg-load-sample-documents
parent: CLI
review_date: 2026-05-15
---

# tg-load-sample-documents

Loads predefined sample documents into TrustGraph library for testing and demonstration purposes.

## Synopsis

```bash
tg-load-sample-documents [options]
```

## Description

The `tg-load-sample-documents` command loads a curated set of sample documents into TrustGraph's document library. These documents include academic papers, government reports, and reference materials that demonstrate TrustGraph's capabilities and provide data for testing and evaluation.

The command downloads documents from public sources and adds them to the library with comprehensive metadata including RDF triples for semantic relationships.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-U, --user USER` | `trustgraph` | User ID for document ownership |

## Examples

### Load Sample Documents
```bash
tg-load-sample-documents
```

### Load with Custom User
```bash
tg-load-sample-documents -U "demo-user"
```

## Sample Documents

The command loads the following sample documents:

### 1. NASA Challenger Report
- **Title**: Report of the Presidential Commission on the Space Shuttle Challenger Accident, Volume 1
- **Topics**: Safety engineering, space shuttle, NASA
- **Use Case**: Technical document processing and safety analysis

### 2. Old Icelandic Dictionary
- **Title**: A Concise Dictionary of Old Icelandic
- **Topics**: Language, linguistics, Old Norse, grammar
- **Publication**: 1910, Clarendon Press
- **Use Case**: Historical document processing and linguistic analysis

### 3. US Intelligence Threat Assessment
- **Title**: Annual Threat Assessment of the U.S. Intelligence Community - March 2025
- **Topics**: National security, cyberthreats, geopolitics
- **Use Case**: Current affairs analysis and security research

### 4. Intelligence and State Policy
- **Title**: The Role of Intelligence and State Policies in International Security
- **Topics**: Intelligence, international security, state policy
- **Publication**: Cambridge Scholars Publishing, 2021
- **Use Case**: Academic research and policy analysis

### 5. Globalization and Intelligence
- **Title**: Beyond the Vigilant State: Globalisation and Intelligence
- **Topics**: Intelligence, globalization, security
- **Use Case**: Comparative intelligence studies

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-library-documents`](tg-show-library-documents) - List library documents
- [`tg-add-library-document`](tg-add-library-document) - Add custom documents
- [`tg-start-library-processing`](tg-start-library-processing) - Process documents

## API Integration

This command uses the [Library API](../apis/api-librarian) to add documents and associated metadata.
