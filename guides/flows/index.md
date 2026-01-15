---
title: Introduction to Flows
parent: Common knowledge management tasks
grand_parent: How-to Guides
nav_order: 6
review_date: 2026-06-01
guide_category:
  - Common knowledge management tasks
guide_category_order: 5
guide_description: Learn how to use flows to orchestrate knowledge processing pipelines
guide_difficulty: intermediate
guide_banner: banner.jpg
guide_time: 15 min
guide_emoji: 🔄
guide_labels:
  - Flows
  - Pipelines
  - Processing
---

# Introduction to Flows

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>TrustGraph instance running</li>
<li>Basic understanding of knowledge processing concepts</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Understand what flows are, how they orchestrate processing pipelines, and how to create and manage them for different use cases."
%}

## What are Flows?

Flows are configurable processing pipelines in TrustGraph that orchestrate how data moves through various processing stages. A flow defines:

- **Processing steps** - The sequence of operations to perform on data
- **Data transformations** - How data is extracted, enriched, and structured
- **Integration points** - How different services and models work together
- **Output destinations** - Where processed results are stored

<img style="max-width: 600px" src="flows.png" alt="Flow processing pipeline"/>

Think of flows as assembly lines for knowledge - raw data enters one end, moves through various processing stations, and emerges as structured knowledge.

## Why Use Flows?

Flows help you:

- **Automate knowledge extraction** - Process documents and data without manual intervention
- **Standardize processing** - Ensure consistent handling across all inputs
- **Scale operations** - Handle large volumes of data efficiently
- **Customize pipelines** - Adapt processing for different data types and use cases

## Common Use Cases

### Document Processing Pipelines

When extracting knowledge from documents:

- Text extraction → chunking → embedding → storage
- PDF parsing → entity extraction → graph creation
- Multi-format ingestion with unified processing

### Real-Time Data Enrichment

When processing streaming data:

- Event ingestion → classification → relationship extraction
- Data validation → enrichment → knowledge graph updates
- Continuous monitoring and knowledge updates

### Custom Workflows

When building specialized processing:

- Domain-specific extraction rules
- Multi-stage validation and verification
- Integration with external APIs and services

## Key Concepts

### Flow Classes

Flow classes define the template or blueprint for a flow. They specify:
- What processing steps are included
- Which models and services to use
- Configuration parameters

### Flow Instances

Flow instances are running flows based on a flow class. You can:
- Start and stop flow instances
- Monitor their status
- View processing metrics

### Flow ID

Each flow has a unique identifier used when making API calls or CLI commands.

### Default Flow

If no flow is specified, TrustGraph uses the "default" flow configured for your instance.

## Managing Flows

### Viewing Available Flows

List all configured flows:

```bash
tg-show-flows
```

This displays flow IDs, status, and configuration details.

### Viewing Flow Classes

See available flow templates:

```bash
tg-show-flow-classes
```

### Starting a Flow

Activate a flow instance:

```bash
tg-start-flow -f my-processing-flow
```

### Stopping a Flow

Deactivate a running flow:

```bash
tg-stop-flow -f my-processing-flow
```

### Creating Custom Flows

Define a new flow class with custom configuration:

```bash
tg-put-flow-class \
  -f custom-flow \
  -c flow-config.json
```

## Flow Configuration

Flows are configured using JSON that specifies:

```json
{
  "steps": [
    {
      "name": "extract",
      "processor": "text-extractor",
      "config": {...}
    },
    {
      "name": "embed",
      "processor": "embedder",
      "config": {...}
    }
  ]
}
```

## Common Flow Patterns

### Linear Pipeline

Data flows sequentially through processing steps:
Input → Extract → Transform → Store

### Branching Pipeline

Data is processed through multiple parallel paths:
Input → {Path A, Path B, Path C} → Merge → Store

### Conditional Processing

Processing adapts based on data characteristics:
Input → Classify → Route to appropriate processor → Store

## Best Practices

### Keep Flows Focused

Each flow should handle a specific type of processing. Create separate flows for different data types or use cases.

### Monitor Performance

Track flow metrics to identify bottlenecks:
- Processing time per step
- Error rates
- Throughput

### Handle Errors Gracefully

Configure error handling:
- Retry logic for transient failures
- Dead letter queues for problematic data
- Logging for debugging

### Version Your Flows

Maintain flow configurations in version control:
- Track changes over time
- Roll back problematic updates
- Document flow evolution

### Test Before Production

Validate new flows with test data:
- Verify output quality
- Check performance characteristics
- Ensure error handling works

## Debugging Flows

When flows aren't working as expected:

1. **Check flow status** - Ensure the flow is running
2. **Review logs** - Look for error messages
3. **Verify configuration** - Check processor settings
4. **Test with sample data** - Isolate the problem

## Next Steps

Now that you understand flows, you can:

- [Process documents with Document RAG](../document-rag/)
- [Build custom processing pipelines](../../reference/extending)
- [Monitor flow performance](../monitoring/)

## Related Commands

- [`tg-show-flows`](../../reference/cli/tg-show-flows) - List all flows and their status
- [`tg-start-flow`](../../reference/cli/tg-start-flow) - Start a flow instance
- [`tg-stop-flow`](../../reference/cli/tg-stop-flow) - Stop a running flow
- [`tg-show-flow-classes`](../../reference/cli/tg-show-flow-classes) - View flow templates
- [`tg-put-flow-class`](../../reference/cli/tg-put-flow-class) - Create or update a flow class
