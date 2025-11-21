---
title: Core Concepts
nav_order: 1
parent: Getting Started
grand_parent: TrustGraph Documentation
---

# Core Concepts

This page covers the essential concepts you need to understand to work with TrustGraph effectively. For a deeper dive into TrustGraph's architecture and philosophy, see the [Introduction](../overview/introduction).

## Essential Terminology

As you work with TrustGraph, you'll encounter these key terms:

### Knowledge Graph
A network of interconnected entities (people, places, concepts) and their relationships. When you load a document into TrustGraph, it's automatically converted into a knowledge graph.

**Example**: A document about a company might create entities for "Company", "CEO", "Product" and relationships like "employs" and "manufactures".

### GraphRAG
Graph-enhanced Retrieval and Augmented Generation. When you ask TrustGraph a question, GraphRAG uses the knowledge graph structure to find relevant, contextually-connected information before generating an answer.

**Why it matters**: GraphRAG provides more accurate answers than traditional search because it understands how information relates.

### Vector Embeddings
Mathematical representations of text that enable semantic similarity search. TrustGraph creates embeddings for your documents so you can find conceptually similar content even if exact words don't match.

**Example**: Searching for "CEO" might also find "Chief Executive Officer" or "company leader".

### N-Triples
The format TrustGraph uses to represent graph data. Each line shows a relationship:
```
<subject> <predicate> <object> .
```

**Example**:
```
<http://trustgraph.ai/e/apple> <http://trustgraph.ai/e/founded-by> "Steve Jobs" .
```

### Flows
Processing pipelines that define how your documents are transformed into knowledge. A flow specifies:
- How to chunk documents
- What entities to extract
- Which LLM to use
- Where to store the results

### Collections
Logical groupings of documents and their associated knowledge graphs. Use collections to organize different datasets or projects.

## Key Components You'll Use

### TrustGraph CLI (`tg-*` commands)
Command-line tools for interacting with TrustGraph:
- `tg-load-pdf` - Load PDF documents
- `tg-show-graph` - View your knowledge graph
- `tg-invoke-graph-rag` - Query using GraphRAG
- `tg-show-flows` - List processing flows

### Web Workbench
Browser-based interface at `http://localhost:8888/` with:
- **Library**: Manage your documents
- **Vector Search**: Find similar content
- **Graph RAG**: Ask questions about your knowledge
- **Graph View**: Visualize relationships

### Grafana Dashboards
Monitoring interface at `http://localhost:3000/` showing:
- Processing backlog
- System performance
- Document processing status

## Understanding the Data Flow

### 1. Document Loading
```
Your PDF/Text → TrustGraph → Document Library
```
Documents are stored in TrustGraph's library, ready for processing.

### 2. Processing
```
Document → Chunking → Entity Extraction → Relationship Discovery → Knowledge Graph
```
TrustGraph breaks documents into chunks, extracts entities and relationships, and builds the knowledge graph.

### 3. Querying
```
Your Question → GraphRAG → Knowledge Graph + Vector Search → Contextual Answer
```
When you query, TrustGraph combines graph structure and semantic search to find relevant information.

## Working with Documents

### Document Formats
TrustGraph supports:
- PDF files
- Plain text (.txt)
- Markdown (.md)
- HTML

### Processing States
Documents go through these states:
1. **Loaded**: In the library, not yet processed
2. **Processing**: Being chunked and analyzed
3. **Processed**: Knowledge graph created, ready for queries

### Chunks
Large documents are split into manageable chunks for processing:
- **Chunk Size**: Typically 1000 characters
- **Overlap**: Usually 50 characters to maintain context
- **Why**: Helps LLMs process documents that exceed their context window

## Query Types

### Vector Search
Find documents based on semantic similarity:
```
Search: "artificial intelligence"
Finds: Documents about AI, ML, neural networks
```

### GraphRAG Queries
Ask questions answered using the knowledge graph:
```
Question: "Who founded Apple?"
Answer: Based on relationships in the graph
```

### Structured Queries
Query extracted structured data:
```
Query: "Show me all products priced over $100"
Returns: Structured data matching the criteria
```

## Configuration Basics

### LLM Selection
TrustGraph works with various LLM providers:
- **Local**: Ollama, LMStudio (runs on your GPU)
- **Cloud**: VertexAI, OpenAI, Anthropic

### Storage Options

**Graph Store** (stores knowledge graphs):
- Cassandra (recommended for local)
- Other graph databases

**Vector Store** (stores embeddings):
- Qdrant (recommended for local)
- Other vector databases

## Common Workflows

### Loading and Processing
```bash
# Load a document
tg-load-pdf my-document.pdf

# Start processing with a flow
tg-start-flow default-flow

# Monitor progress
tg-show-processor-state
```

### Querying
```bash
# Vector search
tg-invoke-vector-search "search term"

# GraphRAG query
tg-invoke-graph-rag "your question here"
```

### Viewing Results
```bash
# See your knowledge graph
tg-show-graph

# View flows
tg-show-flows
```

## Important Concepts for Production

### Collections
Organize your knowledge by project or dataset:
```bash
# Create a collection
tg-set-collection my-project

# Use the collection
tg-load-pdf --collection my-project document.pdf
```

### Flow Parameters
Customize how documents are processed:
- Chunk size and overlap
- Entity extraction prompts
- LLM model selection
- Output formatting

### Monitoring
Watch for:
- **Processing backlog**: Should decrease over time
- **Error rates**: Check logs if processing fails
- **Resource usage**: Ensure sufficient CPU/RAM

## Next Steps

Now that you understand the core concepts:

- **Try it out**: Follow the [Quickstart Guide](quickstart) to deploy TrustGraph
- **Hands-on practice**: Work through [First Steps](first-steps) to learn workflows
- **Deep dive**: Read the [Introduction](../overview/introduction) for architectural details
- **Production deployment**: Explore [Deployment Options](../deployment/)

## Quick Reference

| Term | What It Is | Why It Matters |
|------|------------|----------------|
| Knowledge Graph | Network of connected entities | Provides structure and context |
| GraphRAG | Graph-enhanced retrieval | More accurate than traditional search |
| Vector Embeddings | Semantic representations | Enables similarity search |
| Flow | Processing pipeline | Defines how documents become knowledge |
| Collection | Logical grouping | Organizes different datasets |
| N-Triples | Graph data format | Standard way to represent relationships |

For complete terminology, see the [Glossary](../reference/glossary) (coming soon).
