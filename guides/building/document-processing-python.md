---
title: Document processing with Python API
nav_order: 5
parent: Building with TrustGraph
grand_parent: How-to Guides
review_date: 2026-08-01
guide_category:
  - Building with TrustGraph
guide_category_order: 5
guide_description: Submit and manage documents for processing using the Python API
guide_difficulty: intermediate
guide_time: 15 min
guide_emoji: 📄
guide_banner: ../python-doc-api.jpg
guide_labels:
  - Python
  - Documents
  - API
---

# Document processing with Python API

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>A running TrustGraph deployment</li>
<li>Python {{site.data.software.python-min-version}} or higher</li>
<li>TrustGraph Python package installed (<code>trustgraph-base</code>)</li>
<li>A running flow for document processing</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Learn to add documents to the library and submit them for processing using the TrustGraph Python API."
%}

## Overview

Document processing in TrustGraph follows a two-step workflow:

1. **Add document to library** - Upload document with metadata
2. **Start processing** - Submit document to a flow for processing

The library service (`api.library()`) provides methods for both steps.

## Adding a Document to the Library

Use `add_document()` to upload a document with metadata:

```python
from trustgraph.api import Api

# Create API client and get library service
api = Api(url='http://localhost:8088/')
library = api.library()

# Read document content
with open('my-document.txt', 'rb') as f:
    document_content = f.read()

# Add document to library
# id must be a URI (used as entity identifier in knowledge graph)
library.add_document(
    document=document_content,
    id="https://example.com/docs/my-document",
    user="trustgraph",
    title="My Document",
    comments="A sample document about cats",
    kind="text/plain",
    tags=["sample", "cats"],
    metadata=None  # Optional: list of Triple objects for additional metadata
)

print("Document added to library")
```

**Key parameters:**
- `document` - Document content as bytes
- `id` - Document URI (must be a URI, used as entity identifier in knowledge graph)
- `user` - User ID (default: "trustgraph")
- `title` - Human-readable document title
- `comments` - Description or notes about the document
- `kind` - MIME type (e.g., "text/plain", "application/pdf")
- `tags` - List of tags for organization
- `metadata` - Optional list of `Triple` objects for additional RDF metadata

## Adding Metadata with Triples

Metadata is stored as RDF triples (subject-predicate-object statements) in the knowledge graph. Use `Triple` objects to add structured metadata:

```python
from trustgraph.api import Api
from trustgraph.api.types import Triple
from trustgraph.knowledge import Uri, Literal

# Create API client and get library service
api = Api(url='http://localhost:8088/')
library = api.library()

# Read document content
with open('research-paper.pdf', 'rb') as f:
    document_content = f.read()

# Document URI (used as subject in metadata triples)
doc_id = "https://example.com/papers/research-2026"

# Create metadata triples
# Triple components can be Uri (entities/relationships) or Literal (values)
metadata = [
    # Author information
    Triple(
        s=Uri(doc_id),
        p=Uri("http://purl.org/dc/terms/creator"),
        o=Literal("Dr. Jane Smith")
    ),
    # Publication date
    Triple(
        s=Uri(doc_id),
        p=Uri("http://purl.org/dc/terms/date"),
        o=Literal("2026-01-15")
    ),
    # Subject/topic
    Triple(
        s=Uri(doc_id),
        p=Uri("http://purl.org/dc/terms/subject"),
        o=Literal("Machine Learning")
    ),
    # Related document (using Uri for object)
    Triple(
        s=Uri(doc_id),
        p=Uri("http://purl.org/dc/terms/relation"),
        o=Uri("https://example.com/papers/related-work-2025")
    ),
]

# Add document with metadata
library.add_document(
    document=document_content,
    id=doc_id,
    user="trustgraph",
    title="Research Paper on ML Techniques",
    comments="2026 research paper about machine learning",
    kind="application/pdf",
    tags=["research", "ml", "2026"],
    metadata=metadata
)

print("Document added with RDF metadata")
```

**Understanding Triple components:**
- **Subject (`s`)** - Usually the document URI (what the metadata describes)
- **Predicate (`p`)** - The relationship or property (should be a URI from a vocabulary like Dublin Core)
- **Object (`o`)** - The value (can be a `Literal` for text/numbers or `Uri` for linked entities)

Common metadata vocabularies:
- Dublin Core: `http://purl.org/dc/terms/` (creator, date, subject, etc.)
- Schema.org: `http://schema.org/` (author, datePublished, keywords, etc.)
- Custom vocabularies: Use your own URI namespace for domain-specific metadata

## Starting Document Processing

After adding a document to the library, submit it for processing:

```python
from trustgraph.api import Api

# Create API client and get library service
api = Api(url='http://localhost:8088/')
library = api.library()

# Start processing
# Both id and document_id must be URIs
library.start_processing(
    id="https://example.com/processing/my-document-2026-01",
    document_id="https://example.com/docs/my-document",
    flow="default",
    user="trustgraph",
    collection="default",
    tags=["processing", "2026"]
)

print("Document submitted for processing")
```

**Key parameters:**
- `id` - Processing record URI (must be unique)
- `document_id` - Document URI from library (must match the document's id)
- `flow` - Flow ID to use for processing (default: "default")
- `user` - User ID (default: "trustgraph")
- `collection` - Collection name for storing results (default: "default")
- `tags` - Tags for organizing processing records

## Complete Example: Add and Process a Document

This example shows the complete workflow:

```python
from trustgraph.api import Api

# Configuration
API_URL = 'http://localhost:8088/'
DOCUMENT_PATH = 'my-document.txt'
DOCUMENT_ID = "https://example.com/docs/my-document"
PROCESSING_ID = "https://example.com/processing/my-document-2026-01"

# Create API client and get library service
api = Api(url=API_URL)
library = api.library()

# Step 1: Read document content
with open(DOCUMENT_PATH, 'rb') as f:
    document_content = f.read()

# Step 2: Add document to library
library.add_document(
    document=document_content,
    id=DOCUMENT_ID,
    user="trustgraph",
    title="My Document",
    comments="A sample document for processing",
    kind="text/plain",
    tags=["sample", "2026"]
)
print(f"✓ Document added to library: {DOCUMENT_ID}")

# Step 3: Submit for processing
library.start_processing(
    id=PROCESSING_ID,
    document_id=DOCUMENT_ID,
    flow="default",
    user="trustgraph",
    collection="default",
    tags=["processing"]
)
print(f"✓ Processing started: {PROCESSING_ID}")
print(f"  Flow: default")
print(f"  Collection: default")
```

## Listing Documents and Processing Records

View documents in the library and active processing records:

```python
from trustgraph.api import Api

api = Api(url='http://localhost:8088/')
library = api.library()

# List all documents for a user
documents = library.get_documents(user="trustgraph")

print(f"Found {len(documents)} documents:")
for doc in documents:
    print(f"  • {doc.title}")
    print(f"    ID: {doc.id}")
    print(f"    Type: {doc.kind}")
    print(f"    Tags: {', '.join(doc.tags)}")
    print()

# List all processing records
processing_records = library.get_processings(user="trustgraph")

print(f"Found {len(processing_records)} processing records:")
for proc in processing_records:
    print(f"  • Processing ID: {proc.id}")
    print(f"    Document: {proc.document_id}")
    print(f"    Flow: {proc.flow}")
    print(f"    Collection: {proc.collection}")
    print()
```

## Removing Documents and Processing Records

Clean up documents and processing records when no longer needed:

```python
from trustgraph.api import Api

api = Api(url='http://localhost:8088/')
library = api.library()

# Stop processing (remove processing record)
library.stop_processing(
    id="https://example.com/processing/my-document-2026-01",
    user="trustgraph"
)
print("Processing record removed")

# Remove document from library
library.remove_document(
    user="trustgraph",
    id="https://example.com/docs/my-document"
)
print("Document removed from library")
```

**Note:** Stopping processing only removes the processing record - it does not stop in-flight processing operations (this is reserved for future functionality).

## Using URI Identifiers

Both document IDs and processing IDs must be URIs because they serve as entity identifiers in the knowledge graph:

```python
# Good URIs - these work correctly
"https://example.com/docs/my-document"
"http://trustgraph.ai/documents/cats-2026"
"urn:uuid:550e8400-e29b-41d4-a716-446655440000"

# Bad IDs - these won't work
"my-document"           # Not a URI
"docs/my-document"      # Not a URI
"123456"                # Not a URI
```

When documents are processed, TrustGraph creates knowledge graph entities using these URIs as identifiers, enabling graph queries and relationships.
