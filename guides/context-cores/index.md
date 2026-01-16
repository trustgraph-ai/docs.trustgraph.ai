---
title: Working with Context Cores
parent: Common knowledge management tasks
grand_parent: How-to Guides
nav_order: 5
review_date: 2026-06-01
guide_category:
  - Common knowledge management tasks
guide_category_order: 4
guide_description: Learn how to use cores to manage specialized knowledge domains and context using the Workbench
guide_difficulty: intermediate
guide_banner: banner.jpg
guide_time: 15 min
guide_emoji: 🤖
guide_labels:
  - Knowledge Cores
  - Context Management
  - RAG
---

# Introduction to Context Cores

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>TrustGraph instance running</li>
<li>Basic understanding of knowledge graphs and RAG concepts</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Understand what knowledge cores are, when to use them, and how to create and manage them for specialized knowledge domains."
%}

## What are Cores?

Context cores (also called knowledge cores) are a way of packaging the output of knowledge extraction.  They provide focused, domain-specific context for model operations. Each knowledge core contains:

- **Knowledge graph edges describing the relationships between entities**
- **Knowledge graph schema information describing the nature of entities**
- **Graph embeddings mapping graph entities to semantic vector space**

<img src="context-cores.png" alt="Context core operations"/>

Think of knowledge cores as self-contained "knowledge packages" that can be loaded, switched, and managed independently.

## How are they used

Here's how cores are used:
- **Creation**: In TrustGraph, when you run a flow with core
  extraction enabled, the information which goes into stores for
  retrieval algorithms is also maintained as a context core in the
  knowledge-management service.  There is one context core per
  document processed.
- **Download**: Once the processing has finished, the core can be downloaded
  using the Workbench, CLI or APIs.  The core exists as a file which can be
  stored or disk or shared with people.
- **Upload**: The core file can be presented to a TrustGraph to be reload
  to be loaded back into the knowledge-management service.  At this point
  the information held in the core is online, but not retrievable.
- **Load**: Loading a knowledge core transfers the information to stores,
  in a form which is retrievable i.e. you can ask questions using GraphRAG.

You can think of cores as having 3 states:
- **Offline**: The information exists in a core file
- **Online**: Loaded into the knowledge management core store
- **Loaded**: Loaded into retrieval stores, ready for GraphRAG and agent
  knowledge tasks.

## Why Use Context Cores?

Knowledge cores help you:

- **Organize knowledge by domain** - Keep medical knowledge separate from legal knowledge, for example
- **Improve RAG accuracy** - Queries use only relevant ontologies and context
- **Switch contexts easily** - Load different knowledge cores for different use cases
- **Share knowledge packages** - Export and import complete knowledge domains
- **Control sharing** - knowledge cores can be handled differently depending on their sensitivity


## Step-by-Step Guide

### Step 1: Load Your Document

We're going to start by using a fictional bit of cat text, we only need a
small amount of data to get going.  Fetch the text by visiting this URL:

[https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/cats/README.cats](https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/cats/README.cats)

Upload the document using the Workbench:

- Download [the document](https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/tracking/operation-phantom-cargo.md)
- Go the 'Library' page
- Click 'Upload documents'
- Set the title: README.cats
- Set the Comments to: Brief description of cats
- Set keywords: cats, animals
- Select 'Text' for the upload operation
- Click 'Select text files'
- Add the document you just downloaded
- Click Submit

<img src="load-document.png" alt="Load document dialogue"/>

### Step 2: Create a Collection

A collection is used to organise a set of related documents or data sources
into a single unit.  Retrieval operations operate across a single collection.

We'll create a 'cats' collection:

- Go to the 'Library' page
- Select the 'Collections' tab
- Click 'Create Collection'
- Set the ID: cats
- Set the name: Cats
- Set the description to: Cat information
- Click 'Submit'

### Step 3: Create the Flow

A flow describes the collection of processing operations.  We're going
to create a single flow for Graph RAG processing.

To create context cores, you need to be running a flow which contains the
**kg-store** processor.  The system ships two flow blueprints that
contain core creation: `everything` and `document-rag+graph-rag+kgcore`.
The system starts up with a single flow `default` based on the `everything`
blueprint, so that flow is able to do core building.

We'll create a `core-building` flow.

Let's take a detour via the **Flow blueprints** page.  Go to the
**Settings** page, and make sure **Flow blueprints** is selected on the
feature list.

Select **Flow blueprints** on the sidebar, and you'll see the
blueprints table.  Blueprints provide processing patterns.

<img src="flow-blueprints.png" alt="Flow blueprints table"/>

The two flows `everything` and `document-rag+graph-rag+kgcore` have
core creation in the description.

To launch a flow:
- Go to the 'Flows' page
- Click 'Create'
- Select the flow blueprint 'GraphRAG + DocumentRAG + knowledge core creation'
- Set the ID: core-building
- Set the description: Core building
- Click 'Create'

### Step 4: Submit the Document for Processing

This pushes the document into the flow input.

There is a selection widget top right of the screen with an database icon
top left.

<img src="selection.png" alt="Selection widget"/>

Click that to open the collection/flow selector, and select the
Cats collection, and core-building, both of which you created earlier.

You are ready to submit the document:

- Go to the 'Library' page
- Select the README.cats document so that the tick box is selected
- Click 'Submit' at the bottom of the page
- Change the Processing flow to **Core building**
- Click Submit

### Step 5: Monitoring

If you want to see the document loading, you can go to Grafana at
[`http://localhost:3000`](http://localhost:3000).  The default
login user is admin, password admin.  Grafana is configured with a single
dashboard.  Some useful things to monitor are:

The pub/sub backlog.  You can monitor the size of queues in Pulsar.
GraphRAG knowledge extraction causes a queue of chunks for processing in
knowledge extraction and you can see this in the backlog:

<img src="monitoring1.png" alt="Pub/sub backlog graph"/>

There is also a knowledge extraction backlog graph which helps to see
knowledge extraction if other queues are being exercised:

<img src="monitoring2.png" alt="Knowledge extraction backlog graph"/>

To gauge LLM effectiveness, there is a heatmap which shows LLM latency.
Here we can see that LLM response times for my LLM processing are in the
6 second window.

<img src="monitoring3.png" alt="LLM latency heatmap"/>

Another LLM effectiveness graph, the Token graph shows token throughput
over time, the Y-axis shows tokens/s rate.

<img src="monitoring4.png" alt="LLM token throughput graph"/>

Finally, another useful chart shows the rate limit events per second.
These are commonly seen in the text-completion process which interfaces
with the LLM.  Rate limit events are normal for a knowledge extraction
backlog.  This might particularly be helpful for you to determine whether
you need to provision more LLM bandwidth or dedicated hosting.

<img src="monitoring5.png" alt="LLM rate limit events graph"/>

The document we loaded is small, and will process very quickly, so you
should only see a 'blip' on the backlog showing that chunks were loaded
and cleared quickly.

It can take many minutes or hours to process large documents or large document
sets using GraphRAG extraction.

### Step 6: Check something is loaded

We'll check that the vector store has something loaded.

#### Workbench

- Select Vector search
- The search box enter 'cats'
- Click 'Send'

This executes a search in the vector store for graph entities which are listed
along with the graph node description and the vector similarity score.
The exact view may vary depending on the LLM model you are using and the
entities discovered by it.  If you get some results it shows that
loading has started.  If not, you'll need to work out why nothing loaded.

### Step 7: View the Knowledge Core

Now let's verify the context core has been created by viewing it in the Knowledge Cores screen.

#### Workbench

First, ensure the Knowledge Cores screen is enabled in Settings:

- Go to the **Settings** page
- Look at the **Features** section
- Find **Knowledge Cores** in the feature list
- Make sure it is enabled (checked)

Once the feature is enabled, you'll see **Knowledge Cores** in the sidebar:

- Select **Knowledge Cores** from the sidebar
- You should see a table listing the cores that have been created
- Look for a core corresponding to your document (README.cats)
- The table shows core ID, creation time, size, and status

<img src="knowledge-cores.png" alt="Knowledge Cores screen"/>

The core ID is derived from the document ID. If the core appears in the list, it means:
- The flow successfully processed the document
- The kg-store processor created the core
- The core is now available for download or loading

**Note:** knowledge cores are listed as soon as they start building.  You
should check Grafana to determine when processing of a document has
completed.

### Step 8: Download the Knowledge Core

Once processing is complete, you can download the core as a file for storage or sharing.

#### Workbench

To download a core from the Workbench:

- Make sure you are on the **Knowledge Cores** page
- Find the core in the table (i.e. the README.cats core)
- Select the core in the table by clicking the row
- Click the download button/icon for that core at the bottom of the screen
- The core will download as a file (typically with `.core` extension)
- Save the file to your local system

<img src="download-core.png" alt="Download knowledge core"/>

The downloaded file contains:
- All knowledge graph edges and relationships
- Graph schema information
- Graph embeddings
- Metadata about the core

This file can be shared with others, stored in version control, or uploaded
to different TrustGraph instances.

### Step 9: Upload the Knowledge Core

Now that you have a core file, you can upload it to make it available in the knowledge management service. Once uploaded, the core is not "online" for retrieval but available to be loaded into retrieval stores.

#### Workbench

To upload a core file using the Workbench:

- Go to the **Knowledge Cores** page
- Click the **Upload** button
- Enter a unique ID for the core, enter `https://trustgraph.ai/doc/cats-copy`
- Select the core file you previously downloaded (i.e. `readme-cats.core`)
- The core will be uploaded to the knowledge management service
- Once complete, the core appears in the Knowledge Cores table

You should now have two identical copies of the core.

<img src="upload-core.png" alt="Upload knowledge core"/>

After uploading, the core is stored in the system but not yet available for querying. You'll need to load it (Step 10) to make it available for GraphRAG queries.

<img src="knowledge-cores-2.png" alt="Upload knowledge core"/>

**Note:** Uploading a core makes it available in the knowledge
management service, but doesn't automatically load it into retrieval
stores. The core is "online" but not yet queryable.

### Step 10: Load the Knowledge Core for Retrieval

The final step is to load the core into retrieval stores, making it available for GraphRAG queries. To do this, you need to create a collection and load the core into it.

#### Workbench

First, create a new empty collection:

- Go to the **Library** page
- Select the **Collections** tab
- Click **Create Collection**
- Set the ID: `cats-copy`
- Set the name: `Cats Copy`
- Set the description: `Loaded from knowledge core`
- Click **Submit**

Now select the collection:

- Use the collection/flow selector (top right with database icon)
- Select the **cats-copy** collection

Confirm that the collection returns no results:

- Select Vector Search
- The search box enter 'cats'
- Click 'Send'
- You should see no results

Load the core:

- Go to the **Knowledge Cores** page
- Find the core you uploaded (e.g., `https://trustgraph.ai/doc/cats-copy`)
- Select the core by clicking the row
- Click the **Load** button at the bottom of the screen
- Select the **Core building** flow and press Load.
- The core will be loaded into the retrieval stores

The load may take time.

<img src="load-core.png" alt="Load knowledge core"/>

Once loaded, the knowledge from the core is now available for GraphRAG queries in the `cats-copy` collection.

### Using the CLI

For command-line workflows, see the [Working with Context Cores CLI Guide](../context-cores-cli/).

## Related Resources

- **[Graph RAG](../graph-rag/)** - Build knowledge graphs from documents
- **[Ontology RAG](../ontology-rag/)** - Use structured schemas for extraction



