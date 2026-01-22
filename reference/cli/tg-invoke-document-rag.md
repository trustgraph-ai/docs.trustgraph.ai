---
title: tg-invoke-document-rag
parent: CLI
review_date: 2026-09-01
---

# tg-invoke-document-rag

Invokes the DocumentRAG service to answer questions using document context and retrieval-augmented generation.

## Synopsis

```bash
tg-invoke-document-rag -q QUESTION [options]
```

## Description

The `tg-invoke-document-rag` command uses TrustGraph's DocumentRAG service to answer questions by retrieving relevant document context and generating responses using large language models. This implements Retrieval-Augmented Generation (RAG) that grounds AI responses in your document corpus.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-q, --question QUESTION` | The question to answer |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow instance ID to use |
| `-U, --user USER` | `trustgraph` | User ID for context isolation |
| `-C, --collection COLLECTION` | `default` | Document collection to search |
| `-d, --doc-limit LIMIT` | `10` | Maximum number of documents to retrieve |

## Examples

### Basic Question Answering
```bash
tg-invoke-document-rag -q "What is the company's return policy?"
```

### Question with Custom Collection
```bash
tg-invoke-document-rag \
  -q "How do I configure SSL certificates?" \
  -C "technical-docs" \
  -d 5
```

### Multi-Collection Queries
```bash
# Query legal documents
tg-invoke-document-rag -q "What are the privacy requirements?" -C "legal-docs"

# Query technical documentation
tg-invoke-document-rag -q "How do I troubleshoot timeouts?" -C "tech-docs"
```

## Output Format

The command returns a JSON response:

```json
{
  "question": "What is the company's return policy?",
  "answer": "Based on the policy documents, customers can return items within 30 days...",
  "sources": [
    {
      "document": "customer-service-policy.pdf",
      "relevance": 0.92,
      "section": "Returns and Refunds"
    }
  ],
  "confidence": 0.89
}
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-graph-rag`](tg-invoke-graph-rag) - Query using knowledge graph
- [`tg-show-library-documents`](tg-show-library-documents) - List available documents
- [`tg-invoke-prompt`](tg-invoke-prompt) - Execute prompt templates

## API Integration

This command uses the [DocumentRAG API](../apis/api-document-rag) for retrieval-augmented generation.
