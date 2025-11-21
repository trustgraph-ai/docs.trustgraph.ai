---
title: Graph RAG
layout: default
nav_order: 10
parent: How-to Guides
grand_parent: TrustGraph Documentation
---

# Graph RAG Guide

**Query knowledge graphs using relationship-aware retrieval**

Graph RAG is TrustGraph's advanced retrieval approach that leverages knowledge graph relationships to provide contextually-rich, relationship-aware answers. Unlike basic RAG that retrieves isolated chunks, Graph RAG understands how entities connect and retrieves related information across the graph structure.

## What is Graph RAG?

Graph RAG combines:
1. **Knowledge Graphs**: Entities and their relationships
2. **Vector Embeddings**: Semantic similarity search
3. **Graph Traversal**: Following relationship paths
4. **Contextual Assembly**: Building comprehensive context from connected information

### How Graph RAG Works

```
Query → Entity Identification → Graph Traversal → Context Assembly → LLM Generation
```

1. **Identify relevant entities** in your query
2. **Find those entities** in the knowledge graph
3. **Traverse relationships** to gather connected information
4. **Assemble context** from related entities and relationships
5. **Generate answer** using rich, relationship-aware context

### Graph RAG vs. Document RAG

| Aspect | Document RAG | Graph RAG |
|--------|--------------|-----------|
| **Retrieval** | Vector similarity only | Relationships + vectors |
| **Context** | Isolated chunks | Connected entities |
| **Understanding** | Semantic match | Structural relationships |
| **Answers** | Text-based | Context-aware |
| **Best for** | Simple lookups | Complex questions |
| **Hallucinations** | More prone | Significantly reduced |

## When to Use Graph RAG

✅ **Use Graph RAG when**:
- Questions require understanding relationships
- Answers need context from multiple documents
- You need to connect disparate information
- Reducing hallucinations is critical
- Questions involve "how are X and Y related?"

⚠️ **Consider alternatives when**:
- Simple keyword search is sufficient → Use [Document RAG](document-rag)
- Need structured typed data → Use [Ontology RAG](ontology-rag)
- Documents are completely independent

## Prerequisites

Before starting:
- ✅ TrustGraph deployed ([Quick Start](../getting-started/quickstart))
- ✅ Documents loaded and processed
- ✅ Knowledge graph built (happens automatically during processing)
- ✅ Understanding of [knowledge graphs](../getting-started/concepts#knowledge-graph)

## Step-by-Step Guide

### Step 1: Verify Knowledge Graph Exists

Check that your documents have been processed into a knowledge graph:

```bash
# View knowledge graph contents
tg-show-graph
```

**Expected output** (N-Triples format):
```
<http://trustgraph.ai/e/apple> <http://trustgraph.ai/e/founded-by> "Steve Jobs" .
<http://trustgraph.ai/e/apple> <http://www.w3.org/2000/01/rdf-schema#label> "Apple Inc" .
<http://trustgraph.ai/e/iphone> <http://trustgraph.ai/e/manufactured-by> <http://trustgraph.ai/e/apple> .
```

If no output, process documents first:
```bash
tg-start-flow default-flow
```

### Step 2: Understand Your Knowledge Graph

**View graph structure**:
```bash
# See all triples
tg-show-graph | head -50
```

**Common relationship types**:
- `founded-by`: Company → Person
- `located-in`: Entity → Location
- `part-of`: Component → Parent
- `related-to`: Generic relationships
- `rdfs:label`: Entity name
- `skos:definition`: Entity definition

### Step 3: Query Using Graph RAG

#### CLI Method

**Basic query**:
```bash
tg-invoke-graph-rag "What companies did Steve Jobs found?"
```

**Query with collection**:
```bash
tg-invoke-graph-rag --collection tech-history "How is Apple related to Pixar?"
```

**Complex relationship query**:
```bash
tg-invoke-graph-rag "What products are manufactured by companies founded by Steve Jobs?"
```

#### API Method

**Endpoint**: `/api/graph-rag`

**Request**:
```json
{
  "query": "What companies did Steve Jobs found?",
  "collection": "tech-history",
  "max_hops": 2
}
```

**Response**:
```json
{
  "answer": "Steve Jobs founded Apple Inc. in 1976 and later founded NeXT Computer...",
  "entities": [
    {
      "entity": "Steve Jobs",
      "type": "Person",
      "relationships": [...]
    }
  ],
  "triples": [
    {
      "subject": "Apple Inc",
      "predicate": "founded-by",
      "object": "Steve Jobs"
    }
  ]
}
```

#### Workbench Method

1. Navigate to **Graph RAG** tab
2. Enter your question
3. Click **Submit**
4. View answer with relationship context
5. Click **Graph View** to visualize entities and relationships

### Step 4: Visualize the Knowledge Graph

**In Workbench**:
1. Go to **Graph RAG** or **Vector Search** tab
2. Submit a query
3. Click **Graph View** button
4. Interact with the graph:
   - Click nodes to see entity details
   - Click edges to see relationship types
   - Zoom and pan to explore

**View specific entities**:
```bash
# Search for specific entity
tg-show-graph | grep "Steve Jobs"
```

### Step 5: Refine Queries for Better Results

**Start broad, then narrow**:
```bash
# Broad exploration
tg-invoke-graph-rag "What topics are in this knowledge graph?"

# Focused question
tg-invoke-graph-rag "What are the key relationships between Apple and its founders?"

# Multi-hop relationship
tg-invoke-graph-rag "What products are connected to Steve Jobs through multiple companies?"
```

**Use relationship-aware phrasing**:
- ✅ "How is X related to Y?"
- ✅ "What connects A and B?"
- ✅ "What are the relationships between...?"
- ❌ "Tell me about X" (better for Document RAG)

## Understanding Graph RAG Results

### Entity Extraction

Graph RAG identifies entities in your query:
- **People**: Steve Jobs, Tim Cook
- **Organizations**: Apple, Google
- **Products**: iPhone, MacBook
- **Concepts**: Innovation, Technology
- **Locations**: Cupertino, California

### Relationship Traversal

Graph RAG follows relationships:
- **Direct**: A → B (1-hop)
- **Indirect**: A → B → C (2-hop)
- **Multi-path**: A → B ← C (converging paths)

### Context Assembly

Graph RAG assembles context from:
- **Entity properties**: Names, definitions, types
- **Direct relationships**: Immediate connections
- **Related entities**: Connected through relationships
- **Relationship chains**: Multi-hop paths

## Common Patterns

### Entity Relationship Questions

```bash
# Direct relationship
tg-invoke-graph-rag "Who founded Apple?"

# Reverse relationship
tg-invoke-graph-rag "What companies were founded by Steve Jobs?"

# Multi-entity relationships
tg-invoke-graph-rag "What do Apple and Microsoft have in common?"
```

### Temporal Queries

```bash
tg-invoke-graph-rag "What happened after Apple was founded?"
tg-invoke-graph-rag "What products came before the iPhone?"
```

### Comparative Analysis

```bash
tg-invoke-graph-rag "Compare the founding stories of Apple and Google"
tg-invoke-graph-rag "What are the differences between X and Y?"
```

### Chain of Relationships

```bash
tg-invoke-graph-rag "How is the iPhone connected to Steve Jobs?"
tg-invoke-graph-rag "What path connects person A to company B?"
```

## Advanced Usage

### Controlling Traversal Depth

**Maximum hops** determines how far to traverse:

```bash
# Short traversal (1-2 hops) - faster, more focused
tg-invoke-graph-rag --max-hops 1 "Direct relationships only"

# Deep traversal (3-4 hops) - slower, more comprehensive
tg-invoke-graph-rag --max-hops 3 "Complex multi-step relationships"
```

**Guidelines**:
- **1 hop**: Direct relationships only
- **2 hops**: Standard (recommended default)
- **3-4 hops**: Complex questions, may be slower
- **5+ hops**: Very comprehensive, potentially slow

### Entity-Focused Queries

Query specific to known entities:

```bash
tg-invoke-graph-rag "Tell me everything about <entity_name>"
tg-invoke-graph-rag "What are all relationships of <entity_name>?"
```

### Combining with Document RAG

Use both approaches:

```bash
# Graph RAG for relationships
tg-invoke-graph-rag "How are X and Y connected?"

# Document RAG for details
tg-invoke-document-rag "What are the detailed specifications of Y?"
```

## Troubleshooting

### Empty or Poor Results

**Problem**: Graph RAG returns minimal or no results

**Solutions**:
- Verify graph exists: `tg-show-graph`
- Check entity extraction: Look for entities in graph output
- Rephrase query to mention specific entities
- Ensure documents were fully processed
- Check for processing errors: `tg-show-processor-state`

### Irrelevant Relationships

**Problem**: Retrieved relationships not relevant

**Solutions**:
- Use more specific entity names in query
- Reduce max_hops to focus on direct relationships
- Rephrase query to be more precise
- Check if relationships exist: `tg-show-graph | grep "entity"`

### Slow Queries

**Problem**: Graph RAG takes too long

**Solutions**:
- Reduce max_hops (fewer traversals)
- Limit collection scope
- Optimize graph database configuration
- Consider using [Document RAG](document-rag) for simpler queries

### Missing Relationships

**Problem**: Expected relationships not found

**Solutions**:
- Verify entities extracted: `tg-show-graph | grep "entity_name"`
- Check entity extraction prompt in flow configuration
- Improve source document quality
- Use more descriptive text about relationships

## Graph RAG Configuration

### Entity Extraction

Configure entity extraction in your flow:

```yaml
entity_extraction:
  prompt: |
    Extract entities and their relationships from this text.
    Focus on: people, organizations, products, locations, concepts.
```

### Relationship Types

Customize relationship extraction:

```yaml
relationship_types:
  - founded-by
  - located-in
  - manufactured-by
  - part-of
  - related-to
```

### Graph Store

Configure graph database (Cassandra by default):

```yaml
graph_store:
  type: cassandra
  keyspace: trustgraph
  replication: 3
```

## Graph RAG Best Practices

### Query Formulation

**Good queries**:
- ✅ Mention specific entities
- ✅ Ask about relationships
- ✅ Use verbs like "connect", "relate", "link"
- ✅ Be specific about what you're looking for

**Poor queries**:
- ❌ Too vague ("tell me about things")
- ❌ No entities mentioned
- ❌ Better suited for Document RAG

### Knowledge Graph Quality

**Improve graph quality**:
- Use well-structured source documents
- Ensure clear entity mentions
- Include explicit relationship descriptions
- Use consistent terminology
- Avoid ambiguous pronouns

### Performance Optimization

- Start with 2-hop max for most queries
- Use collection scoping to reduce graph size
- Index frequently queried entities
- Monitor query performance in Grafana

## Comparing RAG Approaches

### When to Use Each

| Scenario | Best Approach |
|----------|---------------|
| "What is X?" | Document RAG |
| "How is X related to Y?" | **Graph RAG** |
| "Extract all products" | Ontology RAG |
| "Summarize document" | Document RAG |
| "Connect A to B" | **Graph RAG** |
| "Find entities of type X" | Ontology RAG |

### Combining Approaches

**Use sequentially**:
1. Graph RAG to find related entities
2. Document RAG to get detailed content
3. Ontology RAG to extract structured data

**Example workflow**:
```bash
# Find relationships
tg-invoke-graph-rag "What companies are related to Apple?"

# Get details
tg-invoke-document-rag "Detailed information about Apple's products"

# Extract structured data
tg-invoke-objects-query "Get all product entities"
```

## Next Steps

### Explore Other RAG Types

- **[Document RAG](document-rag)** - Simple semantic search
- **[Ontology RAG](ontology-rag)** - Structured schema-based extraction

### Advanced Topics

- **[Structured Processing](structured-processing/)** - Work with extracted objects
- **[Agent Extraction](agent-extraction)** - AI-powered extraction workflows
- **[Custom Algorithms](../advanced/custom-algorithms)** - Build custom extraction logic

### API Integration

- **[Graph RAG API](../reference/apis/api-graph-rag)** - API reference
- **[CLI Reference](../reference/cli/tg-invoke-graph-rag)** - Command details
- **[Examples](../examples/)** - Working code samples

## Related Resources

- **[Knowledge Graphs](../getting-started/concepts#knowledge-graph)** - Understanding graphs
- **[Architecture](../overview/architecture)** - How Graph RAG fits in
- **[N-Triples Format](../getting-started/concepts#n-triples)** - Graph data format
- **[Troubleshooting](../deployment/troubleshooting)** - Common issues
