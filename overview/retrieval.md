---
title: Information retrieval
nav_order: 1.5
parent: Overview
---

# Information Retrieval

TrustGraph supports multiple retrieval strategies to provide context to LLM
queries. The approach you choose has a significant impact on the quality
and accuracy of responses.

## Graph RAG

This is where we started in 2023.  Graph RAG is TrustGraph's flagship
retrieval mechanism. Rather than treating documents as opaque text blobs,
Graph RAG extracts structured knowledge and stores it in a knowledge graph
alongside vector embeddings of entities.  TrustGraph engineers were working
on GraphRAG before it was 'cool'.

### Overview

At a high level, document chunks are processed through knowledge extraction
to produce both a knowledge graph and graph embeddings for semantic search.

<img src="retrieval-graph-rag.png">

### Ingestion

The ingestion pipeline processes documents through several stages:

1. **Chunking**: Documents are split into manageable chunks for processing
2. **Knowledge extraction**: An LLM extracts entities and relationships from each chunk, producing knowledge subgraphs
3. **Graph loading**: The extracted subgraphs are loaded into the knowledge graph
4. **Entity determination**: Entities are identified with their semantic meaning
5. **Embedding**: Entities are embedded into vector space
6. **Vector store loading**: Embeddings are stored for similarity search

<img src="retrieval-graph-rag-ingest.png">

### Retrieval

When a question is asked, the retrieval process works as follows:

1. **Question embedding**: The question is converted to a vector embedding
2. **Vector query**: The embedding is used to find semantically relevant nodes in the vector store
3. **Graph traversal**: Starting from relevant nodes, the knowledge graph is traversed to extract a contextual subgraph
4. **LLM invocation**: The knowledge subgraph provides structured context to the LLM, which generates the answer

This approach provides precise, relationship-aware context rather than
raw text snippets.

<img src="retrieval-graph-rag-retrieval.png">

## Ontology RAG

You have probably heard of GraphRAG before.  Ontology RAG, much less likely.
So, let's cover the basics.

### Ontologies

Ontologies are structured frameworks that formally define the concepts,
relationships, and rules within a specific domain of knowledge. They provide a
standardised vocabulary and logical structure for representing how entities
relate to each other, enabling both humans and computers to share a consistent
understanding of complex information.  It's like a database schema, but
for human knowledge.

In knowledge engineering, ontologies have a bad reputation - they are complex,
take years to create, and people often have massive disagreements about what
ontologies are there to do.  Biologists famously disagree about what
constitutes a 'cell'.

But this isn't to say there's 'flaw' - there's nothing broken about ontology
technology.  The real issue is that human knowledge is a profoundly complex
experience.  When we try to classify human knowledge, we can't eliminate the
fundamental human experiences which come with trying to make sense of the
world around us.

So, don't give up too soon, bringing ontologies into information retrieval
produces some awesome results.

### Ontology RAG

Ontology RAG extends Graph RAG by incorporating domain ontologies to guide
knowledge extraction. This approach is particularly valuable when working
with specialised domains that have well-defined conceptual structures.
For many use-cases, Ontology extraction results in much improved retrieval
results.

Early attempts at using ontologies in knowledge extraction attempted to
guide extraction by loading the full ontology into an LLM context window.
Here be dragons: Good ontologies are big, and this can easily flood the
context window.  In a nutshell, the TrustGraph approach is to apply
the GraphRAG algorithm itself to ontologies stored as graph - an information
retrieval operation is used to work out the correct subset of ontology
components to use for knowledge extraction.

The process begins by selecting relevant ontology components based on the
document chunks being processed. This ontology subset then guides the
knowledge extraction process, ensuring that extracted entities and
relationships conform to the domain model. The result is a more consistent and
semantically precise knowledge graph, with embeddings that align with the
ontological structure.

<img src="retrieval-ontology-rag.png">

When this technique is widely adopted by all the AI frameworks, remember
TrustGraph was pioneering this capability in 2025.

## Document RAG

Document RAG is the traditional approach that dominated early RAG
implementations circa 2020. It remains available in TrustGraph for
completeness, but represents a significantly less sophisticated approach
compared to Graph RAG.

The process is straightforward: document chunks are embedded directly and
stored in a vector database. At query time, similar chunks are retrieved
based on embedding similarity and passed to the LLM as context.

<img src="retrieval-doc-rag.png">

While simple to implement, Document RAG has fundamental limitations:

- **No relationship awareness**: Retrieved chunks are isolated text fragments with no understanding of how concepts relate to each other
- **Context window pollution**: Raw text chunks consume token budget inefficiently compared to structured knowledge
- **Semantic drift**: Embedding similarity often retrieves superficially related content rather than genuinely relevant information
- **Poor multi-hop reasoning**: Questions requiring synthesis across multiple facts perform poorly when context is fragmented text

For most use cases, Graph RAG or Ontology RAG will deliver substantially
better results.
