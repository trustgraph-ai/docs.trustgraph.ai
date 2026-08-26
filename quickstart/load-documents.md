---
title: Load documents
nav_order: 5
parent: Quickstart
---

# Load documents

TrustGraph is running and the LLM is connected. Now let's give it
something to work with.

## Load sample documents

TrustGraph ships with a set of sample documents for testing. Load them
into the document library:

```sh
tg-load-sample-documents
```

This downloads the documents and adds them to TrustGraph's library.
The download may take a moment.

## Process a document

Documents in the library need to be processed — run through the
extraction pipeline — before their knowledge appears in the graph.

In the UI, go to the Workflows page and select **Document Ingestion**.
You should see the sample documents listed.

Select **Echoes of the Void** (a short document that processes
quickly). You'll see document details including a description and
tags.

Click **Submit for Processing**. The submission wizard has three steps:

1. **Select a flow** — choose the **default** flow
2. **Select a collection** — use the **default** collection
3. **Confirm** — review and click **Submit for Processing**

Once submitted, the main screen shows the document's processing
pipeline — the document flowing through extraction into the storage
backends. This is a short document and should process quickly,
depending on your LLM.

{: .note }
You can also add your own documents using the **+ Add Document** button
in the top right, but the sample documents are fine for this quickstart.

## Next

[View the knowledge graph](knowledge-graph) — see what TrustGraph
extracted.
