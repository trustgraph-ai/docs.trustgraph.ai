---
title: Explainable AI with TypeScript
nav_order: 10
parent: Building with TrustGraph
grand_parent: How-to Guides
review_date: 2026-08-01
guide_category:
  - Building with TrustGraph
guide_category_order: 10
guide_description: Build an application that traces AI answers back to their source documents using TrustGraph's explainability API
guide_difficulty: intermediate
guide_time: 45 min
guide_emoji: "\U0001F50D"
guide_banner: explainable-ai.jpg
guide_labels:
  - TypeScript
  - Explainability
  - Provenance
  - RDF
---

# Explainable AI with TypeScript

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>A running TrustGraph deployment with documents loaded</li>
<li>Node.js 18 or higher</li>
<li>Familiarity with the <code>@trustgraph/client</code> library (see <a href="typescript-libraries.html">TypeScript Libraries</a>)</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Build a Node.js application that sends an agent query, receives explainability events, and traces every piece of the answer back to its source document, page, and text chunk."
%}

When an AI system answers a question, you often want to know: *where did
that answer come from?* TrustGraph's explainability API answers this by
emitting structured provenance events alongside the AI response. Each event
carries RDF triples that describe exactly what happened at each stage of the
retrieval pipeline.

In this guide, you'll build a command-line application that:

1. Sends a question to the TrustGraph agent
2. Receives and parses explainability events in real time
3. Traces knowledge graph edges back to source documents
4. Fetches the original text from those source chunks

The complete source code is available at
[trustgraph-ai/trustgraph/dev-tools/explainable-ai](https://github.com/trustgraph-ai/trustgraph/tree/master/dev-tools/explainable-ai).

## How explainability works

When you call the agent API with an `onExplain` callback, TrustGraph emits
a series of **explain events** as the query is processed. Each event has:

- **`explainId`** - A URI identifying this pipeline step
- **`explainGraph`** - The named graph where provenance triples are stored
- **`explainTriples`** - An array of RDF triples describing what happened

The triples use the [W3C PROV Ontology](https://www.w3.org/TR/prov-o/)
combined with TrustGraph's own namespace to form a provenance chain.
The event types you'll encounter are:

| Event type | What it represents |
|---|---|
| **AgentQuestion** | The initial user query |
| **Analysis / ToolUse** | Agent deciding which tool to invoke |
| **GraphRagQuestion** | A sub-query sent to the Graph RAG pipeline |
| **Grounding** | Concepts extracted from the query for graph traversal |
| **Exploration** | Entities discovered during knowledge graph traversal |
| **Focus** | The selected knowledge graph edges used as context |
| **Synthesis** | The answer synthesised from retrieved context |
| **Observation** | The tool result returned to the agent |
| **Conclusion / Answer** | The agent's final answer |

These events link together via `prov:wasDerivedFrom`, forming a chain from
the final answer all the way back to the source documents.

## Step 1: Create the project

```bash
mkdir explainable-ai
cd explainable-ai
npm init -y
npm install @trustgraph/client
```

Add `"type": "module"` to `package.json` so Node.js treats `.js` files as
ES modules (required for `import` syntax):

```json
{
  "name": "explainable-ai",
  "version": "1.0.0",
  "type": "module",
  "dependencies": {
    "@trustgraph/client": "^1.7.2"
  }
}
```

Create `index.js` and add the imports and configuration:

```javascript
import { createTrustGraphSocket } from '@trustgraph/client';

const USER = "trustgraph";
const QUESTION = "Tell me about the author of the document";
const SOCKET_URL = "ws://localhost:8088/api/v1/socket";
```

## Step 2: Connect and get API handles

The `createTrustGraphSocket` function creates a WebSocket connection and
returns a `BaseApi` instance. From this, you get two handles:

- **`flow`** - for AI operations (agent, RAG, text completion) and
  knowledge graph queries
- **`librarian`** - for fetching stored document content

```javascript
const client = createTrustGraphSocket(USER, undefined, SOCKET_URL);

const flow = client.flow("default");
const librarian = client.librarian();
```

## Step 3: Define RDF constants

Explain events use standard RDF predicates alongside TrustGraph's own
namespace. Define the ones you'll need for parsing:

```javascript
const RDF_TYPE    = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type";
const RDFS_LABEL  = "http://www.w3.org/2000/01/rdf-schema#label";
const PROV_DERIVED = "http://www.w3.org/ns/prov#wasDerivedFrom";

const TG_GROUNDING   = "https://trustgraph.ai/ns/Grounding";
const TG_CONCEPT     = "https://trustgraph.ai/ns/concept";
const TG_EXPLORATION = "https://trustgraph.ai/ns/Exploration";
const TG_ENTITY      = "https://trustgraph.ai/ns/entity";
const TG_FOCUS       = "https://trustgraph.ai/ns/Focus";
const TG_EDGE        = "https://trustgraph.ai/ns/edge";
const TG_CONTAINS    = "https://trustgraph.ai/ns/contains";
```

A useful helper checks whether a set of triples assigns a given RDF type
to an ID:

```javascript
const isType = (triples, id, type) =>
    triples.some(t => t.s.i === id && t.p.i === RDF_TYPE && t.o.i === type);
```

## Step 4: Send the agent query

The `flow.agent()` method sends a question and provides streaming callbacks
for the agent's reasoning process, plus an `onExplain` callback for
explainability events:

```javascript
let thought = "";
let obs = "";
let ans = "";
const explainEvents = [];

await flow.agent(
    QUESTION,

    // Think: agent reasoning / chain-of-thought
    (chunk, complete, messageId, metadata) => {
        thought += chunk;
        if (complete) {
            console.log("\nThinking:", thought, "\n");
            thought = "";
        }
    },

    // Observe: tool results returned to the agent
    (chunk, complete, messageId, metadata) => {
        obs += chunk;
        if (complete) {
            console.log("\nObservation:", obs, "\n");
            obs = "";
        }
    },

    // Answer: the agent's final response
    (chunk, complete, messageId, metadata) => {
        ans += chunk;
        if (complete) {
            console.log("\nAnswer:", ans, "\n");
            ans = "";
        }
    },

    // Error
    (error) => {
        console.error("Error:", error);
    },

    // Explain: explainability events with RDF triples
    (explainEvent) => {
        explainEvents.push(explainEvent);
    }
);
```

Each streaming callback receives chunks of text. Set `complete` to true on
the final chunk for each message. The explain callback fires for each
pipeline step, delivering the `explainId` and `explainTriples`.

**Why collect explain events?** The explain callback is synchronous, but
processing the events fully requires async queries (label resolution,
provenance lookups). We collect them during streaming and process them
after the agent finishes.

## Step 5: Parse explain events inline

While you can't do async work inside the callback, you can print a useful
summary immediately. Each event's triples include `rdf:type` assertions
that identify the pipeline step:

```javascript
const printExplainInline = (explainEvent) => {
    const { explainId, explainTriples } = explainEvent;
    if (!explainTriples) return;

    // Extract RDF types for this event
    const types = explainTriples
        .filter(t => t.s.i === explainId && t.p.i === RDF_TYPE)
        .map(t => t.o.i);

    // Show short type names (e.g. "Grounding" instead of full URI)
    const shortTypes = types
        .map(t => t.split("/").pop().split("#").pop())
        .join(", ");
    console.log(`  [explain] ${shortTypes}`);

    // Grounding events: show the seed concepts for graph traversal
    if (isType(explainTriples, explainId, TG_GROUNDING)) {
        const concepts = explainTriples
            .filter(t => t.s.i === explainId && t.p.i === TG_CONCEPT)
            .map(t => t.o.v);
        console.log(`    Grounding concepts: ${concepts.join(", ")}`);
    }

    // Exploration events: show entity count
    if (isType(explainTriples, explainId, TG_EXPLORATION)) {
        const count = explainTriples
            .filter(t => t.s.i === explainId && t.p.i === TG_ENTITY).length;
        console.log(`    Entities: ${count} found`);
    }
};
```

Call this from your explain callback before pushing:

```javascript
(explainEvent) => {
    printExplainInline(explainEvent);
    explainEvents.push(explainEvent);
}
```

This gives you real-time visibility into the pipeline as it runs:

```
  [explain] Entity, Question, AgentQuestion
  [explain] Entity, Analysis, ToolUse
  [explain] Entity, Question, GraphRagQuestion
  [explain] Entity, Grounding
    Grounding concepts: author, document
  [explain] Entity, Exploration
    Entities: 45 found
  [explain] Entity, Focus
  [explain] Entity, Synthesis, Answer
```

## Step 6: Resolve labels for URIs

Entities and predicates in the triples are identified by URI. To display
human-readable names, query the knowledge graph for `rdfs:label`:

```javascript
const resolveLabels = async (uris) => {
    const labels = new Map();
    await Promise.all(uris.map(async (uri) => {
        try {
            const results = await flow.triplesQuery(
                { t: "i", i: uri },
                { t: "i", i: RDFS_LABEL },
            );
            if (results.length > 0) {
                labels.set(uri, results[0].o.v);
            }
        } catch (e) {
            // No label found, fall back to URI
        }
    }));
    return labels;
};
```

Collect all URIs that need labels from the explain events:

```javascript
const collectUris = (events) => {
    const uris = new Set();
    for (const { explainId, explainTriples } of events) {
        if (!explainTriples) continue;

        // Entity URIs from Exploration events
        if (isType(explainTriples, explainId, TG_EXPLORATION)) {
            for (const t of explainTriples) {
                if (t.s.i === explainId && t.p.i === TG_ENTITY)
                    uris.add(t.o.i);
            }
        }

        // Subject, predicate, and object URIs from Focus edge triples
        if (isType(explainTriples, explainId, TG_FOCUS)) {
            for (const t of explainTriples) {
                if (t.p.i === TG_EDGE && t.o.t === "t") {
                    const tr = t.o.tr;
                    if (tr.s.t === "i") uris.add(tr.s.i);
                    if (tr.p.t === "i") uris.add(tr.p.i);
                    if (tr.o.t === "i") uris.add(tr.o.i);
                }
            }
        }
    }
    return uris;
};
```

With labels resolved, URIs like `http://trustgraph.ai/e/richard-j.-aldrich`
become `Richard J. Aldrich`.

## Step 7: Extract knowledge graph edges

**Focus** events contain the knowledge graph triples that were selected as
context for the RAG answer. These are stored as
[RDF-star](https://w3c.github.io/rdf-star/cg-spec/editors_draft.html)
triple terms - a triple nested inside another triple's object position:

```
focusId  --selectedEdge-->  edge:0
edge:0   --edge-->          <<subject, predicate, object>>
```

In the JavaScript client, triple terms have type `"t"` with a `tr` field
containing the nested `{s, p, o}`:

```javascript
const collectEdgeTriples = (events) => {
    const edges = [];
    for (const { explainId, explainTriples } of events) {
        if (!explainTriples) continue;
        if (isType(explainTriples, explainId, TG_FOCUS)) {
            for (const t of explainTriples) {
                if (t.p.i === TG_EDGE && t.o.t === "t")
                    edges.push(t.o.tr);
            }
        }
    }
    return edges;
};
```

## Step 8: Trace edges back to source documents

Each knowledge graph edge can be traced back through a provenance chain to
the original document text. The chain uses `prov:wasDerivedFrom` and
TrustGraph's `contains` predicate:

```
subgraph  --contains-->        <<edge triple>>     (RDF-star triple term)
subgraph  --wasDerivedFrom-->  chunk               (text chunk)
chunk     --wasDerivedFrom-->  page                (document page)
page      --wasDerivedFrom-->  document            (original document)
```

To resolve this chain, query the knowledge graph at each step:

```javascript
const resolveEdgeSources = async (edgeTriples) => {
    const iri = (uri) => ({ t: "i", i: uri });
    const sources = new Map();

    await Promise.all(edgeTriples.map(async (tr) => {
        const key = JSON.stringify(tr);
        try {
            // Step 1: Find the subgraph containing this edge triple.
            // Uses an RDF-star triple term as the query object.
            const subgraphResults = await flow.triplesQuery(
                undefined,
                iri(TG_CONTAINS),
                { t: "t", tr },
            );
            if (subgraphResults.length === 0) return;
            const subgraph = subgraphResults[0].s.i;

            // Step 2: subgraph -> chunk
            const chunkResults = await flow.triplesQuery(
                iri(subgraph), iri(PROV_DERIVED),
            );
            if (chunkResults.length === 0) return;
            const chunk = chunkResults[0].o.i;

            // Step 3: chunk -> page
            const pageResults = await flow.triplesQuery(
                iri(chunk), iri(PROV_DERIVED),
            );
            if (pageResults.length === 0) return;
            const page = pageResults[0].o.i;

            // Step 4: page -> document
            const docResults = await flow.triplesQuery(
                iri(page), iri(PROV_DERIVED),
            );
            const document = docResults.length > 0
                ? docResults[0].o.i : undefined;

            sources.set(key, { subgraph, chunk, page, document });
        } catch (e) {
            // Query failed, skip this edge
        }
    }));

    return sources;
};
```

**What this does:**

1. Queries `? contains <<triple>>` using the edge as an RDF-star triple
   term to find which subgraph contains it
2. Walks the `wasDerivedFrom` chain: subgraph -> chunk -> page -> document
3. Returns a map keyed by the serialised edge triple

## Step 9: Fetch source text from the librarian

The chunk URI (e.g. `urn:chunk:319e0102-...`) is a universal identifier
that ties together three things:

- **Provenance** - the chunk entity in the knowledge graph with metadata
  (character offset, chunk index, etc.)
- **Content** - the original text, stored in the librarian
- **Embeddings** - the vector in the document embeddings store

To fetch the text, call `librarian.streamDocument()` with the chunk URI.
The content is returned as base64-encoded text:

```javascript
const fetchChunkText = (chunkUri) => {
    return new Promise((resolve, reject) => {
        let text = "";
        librarian.streamDocument(
            chunkUri,
            (content, chunkIndex, totalChunks, complete) => {
                text += content;
                if (complete) resolve(text);
            },
            (error) => reject(error),
        );
    });
};
```

Decode the base64 when displaying:

```javascript
const b64 = await fetchChunkText(chunkUri);
const text = Buffer.from(b64, "base64").toString("utf-8");
```

## Step 10: Put it all together

After the agent query completes, run the post-processing pipeline:

```javascript
// Resolve provenance for each knowledge graph edge
const edgeTriples = collectEdgeTriples(explainEvents);
const edgeSources = await resolveEdgeSources(edgeTriples);

// Collect and resolve labels for all URIs
const uris = collectUris(explainEvents);
for (const src of edgeSources.values()) {
    if (src.chunk) uris.add(src.chunk);
    if (src.page) uris.add(src.page);
    if (src.document) uris.add(src.document);
}
const labels = await resolveLabels([...uris]);
const label = (uri) => labels.get(uri) || uri;
```

Then display the results. For example, printing knowledge graph edges with
their source provenance:

```javascript
for (const { explainId, explainTriples } of explainEvents) {
    if (!explainTriples) continue;
    if (!isType(explainTriples, explainId, TG_FOCUS)) continue;

    const termValue = (term) =>
        term.t === "i" ? label(term.i) : (term.v || "?");

    const edges = explainTriples
        .filter(t => t.p.i === TG_EDGE && t.o.t === "t")
        .map(t => t.o.tr);

    for (const tr of edges) {
        console.log(`  ${termValue(tr.s)} -> ${termValue(tr.p)} -> ${termValue(tr.o)}`);
        const src = edgeSources.get(JSON.stringify(tr));
        if (src) {
            const parts = [];
            if (src.chunk) parts.push(label(src.chunk));
            if (src.page) parts.push(label(src.page));
            if (src.document) parts.push(label(src.document));
            console.log(`    Source: ${parts.join(" -> ")}`);
        }
    }
}
```

Finally, close the connection:

```javascript
client.close();
process.exit(0);
```

## Run the example

```bash
node index.js
```

You'll see output like:

```
================================================================================
TrustGraph Explainability API Demo
================================================================================
Connected, sending query...

  [explain] Entity, Question, AgentQuestion
  [explain] Entity, Analysis, ToolUse
  [explain] Entity, Question, GraphRagQuestion
  [explain] Entity, Grounding
    Grounding concepts: author, document
  [explain] Entity, Exploration
    Entities: 45 found
  [explain] Entity, Focus
  [explain] Entity, Synthesis, Answer

Thinking: I need to find information about the author of a document...

Observation: The document "Beyond the vigilant state" is by Richard J. Aldrich...

Answer: The author of the document is Richard J. Aldrich.

================================================================================
Knowledge Graph Edges
================================================================================
  Richard J. Aldrich -> definition -> An author whose work includes...
    Source: Chunk 1 -> Page 14 -> Beyond the vigilant state
  Richard J. Aldrich -> is -> person
    Source: Chunk 1 -> Page 10 -> Beyond the vigilant state

================================================================================
Sources
================================================================================

  [1] Beyond the vigilant state / Page 14 / Chunk 1
  ----------------------------------------------------------------------
    Aldrich has published extensively on intelligence, transparency
    and the media. His work includes an article titled Regulation by
    Revelation in Known Knowns: British and American Intelligence ...
```

Every piece of the answer is traceable: which knowledge graph edges
informed the response, which document chunks those edges came from,
and the actual text of those chunks.

## Understanding the RDF triple format

Triples in explain events use a compact JSON format:

```javascript
{
  s: { t: "i", i: "http://trustgraph.ai/e/richard-j.-aldrich" },  // subject (IRI)
  p: { t: "i", i: "http://www.w3.org/2004/02/skos/core#definition" },  // predicate (IRI)
  o: { t: "l", v: "An author who..." },  // object (literal)
  g: "urn:graph:retrieval"  // named graph
}
```

Term types:
- `"i"` (IRI) - a URI identifier, value in field `i`
- `"l"` (literal) - a string value, value in field `v`
- `"t"` (triple) - an RDF-star triple term, nested triple in field `tr`

## Next steps

- **React integration** - Use the explain callback with `useAgent` from
  `@trustgraph/react-state` to build an interactive explainability UI
- **Graph RAG explainability** - The `graphRagStreaming` and
  `documentRagStreaming` methods also accept an `onExplain` callback,
  producing the same provenance events without the agent layer
- **Visualisation** - Use the `prov:wasDerivedFrom` links between explain
  events to build a provenance graph visualisation
- **Filtering** - Use the RDF types to filter events by pipeline stage,
  showing only the steps relevant to your users
