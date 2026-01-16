---
title: Document RAG
nav_order: 4
parent: Common knowledge management tasks
grand_parent: How-to Guides
review_date: 2026-08-01
guide_category:
  - Common knowledge management tasks
guide_category_order: 3
guide_description: Query documents using vector embeddings and semantic similarity search using the Workbench
guide_difficulty: beginner
guide_time: 20 min
guide_emoji: 📄
guide_banner: banner.jpg
guide_labels:
  - RAG
  - Vector Search
  - Embeddings
---

# Document RAG Guide

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>TrustGraph deployed (<a href="../getting-started/quickstart">Quick Start</a>)</li>
<li>Understanding of <a href="../getting-started/concepts">Core Concepts</a></li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Load documents into TrustGraph, create Document RAG flows, and query using vector similarity search while understanding its limitations."
%}

**Query documents using vector embeddings and semantic search**

Document RAG (also called "basic RAG", "naive RAG", or simply "RAG") is the
original retrieval-augmented generation approach that uses vector embeddings
to find relevant document chunks and provides them as context to an LLM for
generating responses.

<img src="document-rag.png" alt="DocumentRAG pictorial representation"/>

Despite being introduced in 2020, many practitioners in 2023 treated basic RAG
as if it were a revolutionary breakthrough, seemingly unaware of its
well-documented limitations. The approach is straightforward: chunk your
documents, embed them, perform similarity search, and hope the LLM can make
sense of whatever fragments get retrieved.

While document RAG can work for simple use cases, it struggles with multi-hop
reasoning, fails to capture document structure, and has no mechanism for
handling contradictory information across chunks. The "naive" in "naive RAG"
is there for a reason—yet it remains surprisingly popular among those who
stopped reading the literature after the first paper.

{: .note }
> Document RAG is the most basic information retrieval flow. It can prove
> useful for some limited cases, but you should consider
> [GraphRAG](graph-rag) or [Ontology RAG](ontology-rag) for real-world
> information retrieval use-cases.

## What is Document RAG?

The essential Document RAG ingest flow consists of:
1. **Chunking** documents into smaller pieces
2. **Embedding** each chunk as a vector
3. **Storing** vectors in a vector database along with the chunks
4. **Retrieving** similar chunks based on query embedding
5. **Generating** responses using retrieved context and an LLM

The pros and cons of this approach:
- ✅ *Pro*: Quicker ingest time compared to knowledge extraction flows
- ✅ *Pro*: No token consumption on document ingest
- ⚠️ *Con*: Sentence embeddings are imprecise and limited for retrieval
  where documents contain diverse concepts
- ⚠️ *Con*: Ineffective for resolving complex questions

### When to Use Document RAG

✅ **Use Document RAG when**:
- You need semantic search over documents
- Questions can be answered from isolated passages
- You want simple, fast implementation
- Document context is self-contained in paragraphs or chunks

⚠️ **Consider alternatives when**:
- You need to understand relationships between entities
  → Use [Graph RAG](graph-rag)
- You need structured schema-based extraction
  → Use [Ontology RAG](ontology-rag)
- Answers require connecting information across documents
  → Use [Graph RAG](graph-rag)

## Prerequisites

Before starting:
- ✅ TrustGraph deployed ([Quick Start](../getting-started/quickstart))
- ✅ Understanding of [Core Concepts](../getting-started/concepts)

## Step-by-Step Guide

### Step 1: Load Your Document

TrustGraph supports multiple document formats:
- PDF files (`.pdf`)
- Text files (`.txt`)
- Markdown (`.md`)
- HTML (`.html`)

We're going to start by using a fictional maritime tracking report
which you can download at this URL:

[https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/tracking/operation-phantom-cargo.md](https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/tracking/operation-phantom-cargo.md).

- Download [the document](https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/tracking/operation-phantom-cargo.md)
- Go the 'Library' page
- Click 'Upload documents'
- Set the title: PHANTOM CARGO
- Set the Comments to: Intelligence report: Operation PHANTOM CARGO
- Set keywords: maritime, intelligence, cargo, grey arms
- Select 'Text' for the upload operation
- Click 'Select text files'
- Add the document you just downloaded
- Click Submit

<img src="load-document.png" alt="Document load dialogue"/>

### Step 2: Create a Collection

A collection is used to organise a set of related documents or data sources
into a single unit.  Retrieval operations operate across a single collection.

We'll create an 'intelligence' collection:

- Go to the 'Library' page
- Select the 'Collections' tab
- Click 'Create Collection'
- Set the ID: intelligence
- Set the name: Intelligence
- Set the description to: Intelligence analysis
- Click 'Submit'

### Step 3: Create the Flow

A flow describes the collection of processing operations.  We're going
to create a single flow for Document RAG processing.

We'll create a 'doc-rag' flow:

- Go to the 'Flows' page
- Click 'Create'
- Select the flow blueprint 'Document RAG'
- Set the ID: doc-rag
- Set the description: Document RAG
- Click 'Create'

### Step 4: Submit the Document for Processing

This pushes the document into the flow input.

There is a selection widget top right of the screen with an database icon
top left.

<img src="selection.png" alt="Selection widget"/>

Click that to open the collection/flow selector, and select the
Intelligence collection, and Document RAG, both of which you created earlier.

<img src="collection-selected.png" alt="Selection dialogue"/>

You are ready to submit the document:

- Go to the 'Library' page
- Select the PHANTOM CARGO document so that the tick box is selected
- Click 'Submit' at the bottom of the page
- Change the Processing flow to Document RAG
- Click Submit

### Step 5: Monitoring

If you want to see the document loading, you can go to Grafana at
[`http://localhost:3000`](http://localhost:3000).  The default
login user is admin, password admin.  Grafana is configured with a single
dashboard, which has a 'pub/sub backlog' graph.

<img src="monitoring.png" alt="Grafana pub/sub backlog graph"/>

The document we loaded is small, and will process very quickly, so you
should only see a 'blip' on the backlog showing that chunks were loaded
and cleared quickly.

### Step 6: Retrieval

Presently, there is no Document RAG query interface in the Workbench.

For querying Document RAG using the command line, see the [Document RAG CLI Guide](../document-rag-cli/#step-6-query-with-document-rag).

The CLI guide also includes examples demonstrating Document RAG's limitations with complex queries and multiple documents.

## Document RAG vs. Other Approaches

| Aspect | Document RAG | Graph RAG | Ontology RAG |
|--------|--------------|-----------|--------------|
| **Retrieval** | Vector similarity | Graph relationships | Schema-based |
| **Context** | Isolated chunks | Connected entities | Connected objects, properties and types |
| **Best for** | Semantic search | Complex relationships | Complex relationships + precise types |
| **Setup** | Simple | Simple | Complex |
| **Speed** | Fast | Medium | Medium |

**Use multiple approaches**: The processing flow defines the extraction
and retrieval mechanisms, so you can use multiple approaches on the same
data.

## Next Steps

### Using the CLI

For command-line workflows, see the [Document RAG CLI Guide](../document-rag-cli/).

### Explore Other RAG Types

- **[Graph RAG](../graph-rag/)** - Leverage knowledge graph relationships
- **[Ontology RAG](../ontology-rag/)** - Use structured schemas for extraction

## Related Resources

- **[Core Concepts](../../getting-started/concepts)** - Understanding embeddings and chunks
- **[Vector Search](../../getting-started/concepts#vector-embeddings)** - How semantic search works
