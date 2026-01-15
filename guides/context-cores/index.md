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
guide_time: 10 min
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

<img style="max-width: 600px" src="context-cores.png" alt="Context core operations"/>

Think of knowledge cores as self-contained "knowledge packages" that can be loaded, switched, and managed independently.

## How are they used

Here's how cores are used:
- In TrustGraph, if you run a flow with 

## Why Use Knowledge Cores?

Knowledge cores help you:

- **Organize knowledge by domain** - Keep medical knowledge separate from legal knowledge, for example
- **Improve RAG accuracy** - Queries use only relevant ontologies and context
- **Switch contexts easily** - Load different knowledge cores for different use cases
- **Share knowledge packages** - Export and import complete knowledge domains

## Common Use Cases

### Domain-Specific Applications

When building applications for specific industries or fields:

- Medical diagnosis systems using medical ontologies
- Legal research tools with legal terminology
- Scientific research platforms with domain-specific taxonomies

### Multi-Tenant Systems

When serving multiple clients with different knowledge needs:

- Each client gets their own knowledge core
- Data isolation between tenants
- Customized ontologies per client

### Development and Testing

When developing and testing knowledge-based systems:

- Production knowledge core for live data
- Development core for testing new ontologies
- Staging core for validation

## Key Concepts

### Core Isolation

Each knowledge core maintains separate:
- Graph storage (triples)
- Vector embeddings
- Ontology definitions
- Configuration settings

### Core Identification

Knowledge cores are identified by a unique name. When making API calls, you specify which core to use.

### Default Core

If no core is specified, TrustGraph uses the "default" core. Most single-application deployments only need the default core.

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
