---
title: Introduction to Context Cores
parent: Common knowledge management tasks
grand_parent: How-to Guides
nav_order: 5
review_date: 2026-06-01
guide_category:
  - Common knowledge management tasks
guide_category_order: 4
guide_description: Learn how to use cores to manage specialized knowledge domains and context
guide_difficulty: intermediate
guide_banner: banner.jpg
guide_time: 20 min
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

## Why Use Knowledge Cores?

Knowledge cores help you:

- **Organize knowledge by domain** - Keep medical knowledge separate from legal knowledge, for example
- **Improve RAG accuracy** - Queries use only relevant ontologies and context
- **Switch contexts easily** - Load different knowledge cores for different use cases
- **Share knowledge packages** - Export and import complete knowledge domains
- **Control sharing** - knowledge cores can be handled differently depending on their sensitivity

## Managing Knowledge Cores

### Viewing Available Cores

Use the CLI to list all knowledge cores:

```bash
tg-show-kg-cores
```

This displays all configured cores with their metadata.

### Creating a New Core

Create a knowledge core by defining it with configuration:

```bash
tg-put-kg-core \
  -c medical-core \
  -d "Medical knowledge and terminology"
```

### Switching Between Cores

When invoking queries, specify which core to use:

```bash
tg-invoke-graph-rag \
  -q "What are the symptoms of diabetes?" \
  -K medical-core
```

The `-K` flag specifies the knowledge core to query.

## Loading Data into a Core

Once created, populate your knowledge core with:

1. **Ontology definitions** - Define the schema using RDF/Turtle format
2. **Graph data** - Load facts and relationships
3. **Documents** - Add text documents for document RAG

Example loading triples into a specific core:

```bash
tg-load-triples \
  -K medical-core \
  -f medical-ontology.ttl
```

## Best Practices

### Keep Cores Focused

Each core should represent a single coherent knowledge domain. Avoid mixing unrelated ontologies in one core.

### Use Descriptive Names

Name cores clearly: `legal-contracts`, `product-catalog`, `customer-support` rather than `core1`, `core2`.

### Document Your Cores

Maintain documentation about:
- What knowledge is in each core
- What ontologies are used
- When it was last updated
- Who maintains it

### Version Control Ontologies

Keep your ontology definitions in version control so you can track changes and roll back if needed.

## Next Steps

Now that you understand knowledge cores, you can:

- [Load graph data into your cores](../graph-rag/)
- [Query knowledge cores with Graph RAG](../graph-rag/)
- [Define custom ontologies](../ontology-rag/)

## Related Commands

- [`tg-show-kg-cores`](../../reference/cli/tg-show-kg-cores) - List all knowledge cores
- [`tg-put-kg-core`](../../reference/cli/tg-put-kg-core) - Create or update a knowledge core
- [`tg-invoke-graph-rag`](../../reference/cli/tg-invoke-graph-rag) - Query a knowledge core
