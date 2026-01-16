---
title: Working with Context Cores using CLI
parent: Advanced knowledge management
grand_parent: How-to Guides
nav_order: 5
review_date: 2026-06-01
guide_category:
  - Advanced knowledge management
guide_category_order: 4
guide_description: Use command-line tools to create, download, upload, and load knowledge cores
guide_difficulty: advanced
guide_banner: banner.jpg
guide_time: 15 min
guide_emoji: 🤖
guide_labels:
  - Knowledge Cores
  - Context Management
  - CLI
---

# Working with Context Cores Using CLI

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>TrustGraph instance running</li>
<li>Familiarity with knowledge cores concepts</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Use CLI tools to create, download, upload, and load knowledge cores for sharing and managing extracted knowledge."
%}

This guide covers the same knowledge core workflow as the [Working with Context Cores guide](../context-cores/), but using command-line tools instead of the Workbench.

**New to knowledge cores?** Read the [Working with Context Cores guide](../context-cores/) first to understand what cores are and their lifecycle (offline → online → loaded).

This guide demonstrates:
- Creating flows with core extraction enabled
- Downloading cores via CLI
- Uploading cores to other instances
- Loading cores into retrieval stores

## Step-by-Step Guide

### Step 1: Load Your Document

Download and load the example document:

```bash
wget -O README.cats https://raw.githubusercontent.com/trustgraph-ai/example-data/refs/heads/main/cats/README.cats

tg-add-library-document \
  --name "README.cats" \
  --description "Brief description of cats" \
  --tags cats,animals \
  --id https://trustgraph.ai/doc/readme-cats \
  --kind text/plain \
  README.cats
```

### Step 2: Create a Collection

Create a collection:

```bash
tg-set-collection -n Cats -d 'Cat information' cats
```

### Step 3: Create the Flow

Create a flow with the `kg-store` processor for core creation:

```bash
tg-start-flow -n document-rag+graph-rag+kgcore -i core-building -d "Core building"
```

### Step 4: Submit the Document for Processing

Submit the document for processing:

```bash
tg-start-library-processing \
    --flow-id core-building \
    --document-id https://trustgraph.ai/doc/readme-cats \
    --collection cats \
    --processing-id urn:processing-03
```

### Step 5: Monitoring (Optional)

Processing can take time. For monitoring details, see the [Working with Context Cores guide monitoring section](../context-cores/#step-5-monitoring).

### Step 6: View the Knowledge Core

List available cores:

```bash
tg-show-kg-cores
```

Output:

```
https://trustgraph.ai/doc/readme-cats
```

### Step 7: Download the Knowledge Core

Download the core as a file:

```bash
tg-get-kg-core \
  --id https://trustgraph.ai/doc/readme-cats \
  --output readme-cats.core
```

Output:

```
Got: 2 triple, 1 GE messages.
```

Verify the download:

```bash
ls -lh readme-cats.core
```
tg-dump-msgpack -i readme-cats.core
```

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

#### Command-line

To upload a core using the CLI:

```bash
tg-put-kg-core \
  --id https://trustgraph.ai/doc/readme-cats \
  --input readme-cats.core
```

The command will report progress as it uploads:

```
Put: 2 triple, 1 GE messages.
```

Verify the core was uploaded by listing all cores:

```bash
tg-show-kg-cores
```

You should see your uploaded core in the list:

```
https://trustgraph.ai/doc/readme-cats
https://trustgraph.ai/doc/cats-copy
```

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

#### Command-line

Create a new collection:

```bash
tg-set-collection \
  -n "Cats Copy" \
  -d "Loaded from knowledge core" \
  cats-copy
```

Load the core into the collection:

```bash
tg-load-kg-core \
  --id https://trustgraph.ai/doc/cats-copy \
  --collection cats-copy
```

The command will report progress as it loads the core:

```
Loading core into retrieval stores...
Loaded: 2 triple batches, 1 GE batches.
```

Verify the core is loaded by performing a GraphRAG query:

```bash
tg-invoke-graph-rag \
  -q "What do you know about cats?" \
  -C cats-copy
```

You should receive a response based on the knowledge extracted from the README.cats document.

**Note:** The core is now "loaded" - the knowledge is available in retrieval stores and can be queried using GraphRAG operations.

### API Integration

All knowledge core operations demonstrated in this guide are available through the Knowledge Management API.  For complete API documentation, see the [REST API Reference](../../reference/apis/rest.html).

**Related CLI commands:**
- [`tg-show-kg-cores`](../../reference/cli/tg-show-kg-cores) - List all knowledge cores
- [`tg-get-kg-core`](../../reference/cli/tg-get-kg-core) - Download a knowledge core
- [`tg-put-kg-core`](../../reference/cli/tg-put-kg-core) - Upload a knowledge core
- [`tg-load-kg-core`](../../reference/cli/tg-load-kg-core) - Load a core into retrieval stores



