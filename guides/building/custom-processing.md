---
published: false
title: Adding your own processing
nav_order: 9
parent: Building with TrustGraph
grand_parent: How-to Guides
review_date: 2026-08-01
guide_category:
  - Building with TrustGraph
guide_category_order: 9
guide_description: Extend TrustGraph with custom processing components and workflows
guide_difficulty: advanced
guide_time: 1 hr
guide_emoji: ⚙️
guide_banner: /../processing.jpg
guide_labels:
  - Custom Processing
  - Extensions
todo: true
todo_notes: This is under construction
---

# Adding your own processing

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>A running TrustGraph deployment</li>
<li>Python {{site.data.software.python-min-version}} or higher</li>
<li>Understanding of TrustGraph architecture</li>
<li>Familiarity with async Python</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Build custom processing components that extend TrustGraph with domain-specific functionality."
%}

This guide uses the [trustgraph-stix](https://github.com/trustgraph-ai/trustgraph-stix) project as a concrete example, showing how to build processors that convert cybersecurity threat reports into STIX format for knowledge graph analysis.

## Understanding Custom Processing

TrustGraph's processing architecture is built around **processors** that consume messages from queues, transform data, and produce output to other queues. Custom processing extends this with domain-specific logic.

**Key concepts:**
- **Processors** - Python classes that handle data transformation
- **Schemas** - Pulsar message formats defining data structures
- **Flow classes** - JSON configurations wiring processors together
- **Prompts** - LLM instructions for extraction and transformation

**Example use cases:**
- Domain-specific data extraction (STIX, FHIR, legal documents)
- Custom knowledge representation
- Specialized embeddings or indexing
- Integration with external systems

## Architecture Overview

A custom processing pipeline consists of three components:

1. **Processors** - Transform data (e.g., `cyber-extract`, `stix-load`)
2. **Flow class** - Defines how processors connect via queues
3. **Initialization** - Sets up prompts and flow classes at startup

```
Document → cyber-extract → STIX → stix-load → Triples + Entities → Graph
           (uses LLM)                         (maps to graph)
```

## Step 1: Define Your Schema

Schemas define the message format passed between processors using Pulsar.

Create `schema.py`:

```python
from pulsar.schema import Record, Bytes
from trustgraph.schema import Metadata

# Custom schema for STIX documents
class StixDocument(Record):
    metadata = Metadata()    # Standard TrustGraph metadata
    stix = Bytes()          # STIX bundle as bytes
```

**Key points:**
- Inherit from `pulsar.schema.Record`
- Always include `Metadata` for tracking
- Use `Bytes`, `String`, or other Pulsar types for payload

## Step 2: Create a Processor

Processors inherit from `FlowProcessor` and handle message transformation.

Create `cyber_extract/cyber_extract.py`:

```python
from trustgraph.schema import TextDocument
from trustgraph.base import FlowProcessor, ConsumerSpec, ProducerSpec
from trustgraph.base import PromptClientSpec

from your_package.schema import StixDocument

default_ident = "cyber-extract"

class Processor(FlowProcessor):

    def __init__(self, **params):
        id = params.get("id", default_ident)

        super(Processor, self).__init__(**params | {"id": id})

        # Configure input queue - receives text documents
        self.register_specification(
            ConsumerSpec(
                name="input",                  # Queue identifier
                schema=TextDocument,           # Expected message type
                handler=self.on_message        # Handler method
            )
        )

        # Configure prompt service access
        self.register_specification(
            PromptClientSpec(
                request_name="prompt-request",
                response_name="prompt-response"
            )
        )

        # Configure output queue - sends STIX documents
        self.register_specification(
            ProducerSpec(
                name="output",
                schema=StixDocument
            )
        )

    async def on_message(self, msg, consumer, flow):
        """Handle incoming message"""

        # Extract text from message
        v = msg.value()
        text = v.text.decode("utf-8")

        # Use LLM to extract structured data
        result = await flow("prompt-request").prompt(
            id="stix-extraction",
            variables={"text": text}
        )

        # Create output message
        output = StixDocument(
            metadata=v.metadata,
            stix=result.encode("utf-8")
        )

        # Send to next processor
        await flow("output").send(output)

    @staticmethod
    def add_args(parser):
        FlowProcessor.add_args(parser)

def run():
    Processor.launch(default_ident, __doc__)
```

**Key components:**

1. **ConsumerSpec** - Defines input queue and schema
2. **ProducerSpec** - Defines output queue and schema
3. **PromptClientSpec** - Enables LLM access for data extraction
4. **on_message** - Handler for each message received
5. **flow("name")** - Access to configured queues

## Step 3: Create a Transformation Processor

The second processor maps extracted data to graph entities.

Create `stix_load/stix_load.py`:

```python
from trustgraph.base import FlowProcessor, ConsumerSpec, ProducerSpec
from trustgraph.schema import Triple, Triples, EntityContext, EntityContexts, Value
from trustgraph.knowledge import Uri, Literal, IS_A, LABEL, DESCRIPTION

from your_package.schema import StixDocument

default_ident = "stix-load"

class Processor(FlowProcessor):

    def __init__(self, **params):
        id = params.get("id", default_ident)
        super(Processor, self).__init__(**params | {"id": id})

        # Input: STIX documents
        self.register_specification(
            ConsumerSpec(
                name="input",
                schema=StixDocument,
                handler=self.on_message
            )
        )

        # Output: Triples for graph storage
        self.register_specification(
            ProducerSpec(
                name="triples",
                schema=Triples
            )
        )

        # Output: Entity contexts for embeddings
        self.register_specification(
            ProducerSpec(
                name="entity-contexts",
                schema=EntityContexts
            )
        )

    async def on_message(self, msg, consumer, flow):
        """Convert STIX to graph triples"""

        v = msg.value()
        stix_data = json.loads(v.stix.decode("utf-8"))

        triples = []
        entities = []

        # Extract entities and relationships from STIX
        for obj in stix_data["objects"]:
            obj_uri = Uri(f"https://example.com/stix/{obj['id']}")
            type_uri = Uri(f"https://example.com/type/{obj['type']}")

            # Create triples
            triples.append(
                Triple(
                    s=Value(value=str(obj_uri), is_uri=True),
                    p=Value(value=IS_A, is_uri=True),
                    o=Value(value=str(type_uri), is_uri=True)
                )
            )

            if "name" in obj:
                triples.append(
                    Triple(
                        s=Value(value=str(obj_uri), is_uri=True),
                        p=Value(value=LABEL, is_uri=True),
                        o=Value(value=obj["name"], is_uri=False)
                    )
                )

                # Create entity context for embedding
                entities.append(
                    EntityContext(
                        entity=Value(value=str(obj_uri), is_uri=True),
                        context=obj["name"]
                    )
                )

        # Send triples to graph store
        await flow("triples").send(
            Triples(metadata=v.metadata, triples=triples)
        )

        # Send entity contexts for embedding
        await flow("entity-contexts").send(
            EntityContexts(metadata=v.metadata, entities=entities)
        )

    @staticmethod
    def add_args(parser):
        FlowProcessor.add_args(parser)

def run():
    Processor.launch(default_ident, __doc__)
```

**What this does:**
- Consumes STIX documents from previous processor
- Converts to graph triples (subject-predicate-object)
- Extracts entity contexts for embeddings
- Sends to graph storage and embedding queues

## Step 4: Define LLM Prompts

Create prompts for data extraction.

Create `prompts.py`:

```python
extraction_prompt = """You are extracting structured cybersecurity
threat data from text reports. Convert the following text to STIX 2.1
format JSON.

Ensure:
- Valid JSON array output
- STIX 2.1 specification compliance
- Include only high-confidence entities

Text:
{{text}}
"""
```

## Step 5: Create Flow Class Definition

Flow classes wire processors together via queues.

Create `stix-flow-class.json`:

```json
{
    "description": "Cybersecurity threat report analysis",
    "tags": ["threat-analysis", "stix", "graph-rag"],

    "flow": {
        "cyber-extract:{id}": {
            "input": "persistent://tg/flow/text-document-load:{id}",
            "prompt-request": "non-persistent://tg/request/prompt:{class}",
            "prompt-response": "non-persistent://tg/response/prompt:{class}",
            "output": "persistent://tg/flow/stix:{id}"
        },
        "stix-load:{id}": {
            "input": "persistent://tg/flow/stix:{id}",
            "triples": "persistent://tg/flow/triples-store:{id}",
            "entity-contexts": "persistent://tg/flow/entity-contexts-load:{id}"
        },
        "kg-store:{id}": {
            "triples-input": "persistent://tg/flow/triples-store:{id}",
            "graph-embeddings-input": "persistent://tg/flow/entity-contexts-load:{id}"
        }
    },

    "interfaces": {
        "document-load": "persistent://tg/flow/document-load:{id}",
        "text-load": "persistent://tg/flow/text-document-load:{id}",
        "triples-store": "persistent://tg/flow/triples-store:{id}"
    }
}
```

**Key elements:**
- `flow` section maps processor IDs to queue configurations
- `{id}` placeholder replaced with flow instance ID
- `{class}` placeholder for shared service queues
- `persistent://` queues retain messages
- `non-persistent://` queues for request/response patterns

## Step 6: Create Initialization Script

Initialize prompts and flow class at startup.

Create `init_cyberthreat.py`:

```python
from trustgraph.api import Api
import json

def initialize():
    # Connect to TrustGraph
    api = Api(url='http://localhost:8088/')
    config = api.config()

    # Load prompts
    prompts = {
        "stix-extraction": {
            "prompt": extraction_prompt,
            "model": "gemini-2.5-flash-lite"
        }
    }

    for prompt_id, prompt_data in prompts.items():
        config.set(
            type="prompt",
            key=f"template.{prompt_id}",
            value=json.dumps(prompt_data)
        )

    # Load flow class
    with open("stix-flow-class.json") as f:
        flow_class = json.load(f)

    api.flow().put_class(
        name="threat-analysis",
        definition=flow_class
    )

    print("Initialization complete")

if __name__ == "__main__":
    initialize()
```

## Step 7: Package and Deploy

Create `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "trustgraph-stix"
version = "0.1.0"
description = "STIX threat report processing for TrustGraph"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "trustgraph-base>=0.23",
]

[project.scripts]
cyber-extract = "trustgraph_stix.cyber_extract:run"
stix-load = "trustgraph_stix.stix_load:run"
tg-init-cyberthreat = "trustgraph_stix.init_cyberthreat:initialize"

[tool.setuptools.packages.find]
where = ["."]
include = ["trustgraph_stix*"]
```

Create `Containerfile`:

```dockerfile
FROM docker.io/trustgraph/trustgraph-base:latest

WORKDIR /app
COPY . /app/

RUN pip install -e .

CMD ["cyber-extract"]
```

Build container:

```bash
podman build -f Containerfile -t trustgraph-stix:latest .
```

## Step 8: Configure TrustGraph Deployment

Add processors to `docker-compose.yaml`:

```yaml
services:
  cyber-extract:
    image: trustgraph-stix:latest
    command: cyber-extract
    environment:
      PULSAR_URL: pulsar://pulsar:6650

  stix-load:
    image: trustgraph-stix:latest
    command: stix-load
    environment:
      PULSAR_URL: pulsar://pulsar:6650

  init-cyberthreat:
    image: trustgraph-stix:latest
    command: tg-init-cyberthreat
    environment:
      TRUSTGRAPH_URL: http://api-gateway:8088
    depends_on:
      - api-gateway
```

## Step 9: Start and Test

Start TrustGraph with custom processors:

```bash
docker-compose up -d
```

Wait for initialization:

```bash
tg-show-flow-classes
```

Start a flow instance:

```bash
tg-start-flow -n threat-analysis -i custom -d "Threat analysis flow"
```

Add and process a document:

```bash
tg-add-library-document \
    --identifier https://example.com/threat-report-001 \
    --name "Threat Report" \
    --kind text/plain \
    report.txt

tg-start-library-processing \
    --id processing-001 \
    --document-id https://example.com/threat-report-001 \
    --flow-id custom
```

Query results:

```bash
tg-invoke-graph-rag -q "What threat actors are mentioned?"
```

## Best Practices

**Processor design:**
- Keep processors focused on single transformations
- Use schemas for type safety
- Handle errors gracefully with try/except
- Log processing steps for debugging

**Flow configuration:**
- Use persistent queues for critical data
- Non-persistent for request/response patterns
- Connect to standard TrustGraph components (embeddings, graph storage)

**Testing:**
- Test processors independently with mock messages
- Validate schema compliance
- Test full pipeline with sample documents
- Monitor queue depths for bottlenecks

**Deployment:**
- Use containers for isolation
- Configure resource limits
- Add health checks
- Monitor processing latency

## Resources

- [trustgraph-stix repository](https://github.com/trustgraph-ai/trustgraph-stix) - Complete example
- [TrustGraph base library](https://github.com/trustgraph-ai/trustgraph) - Core processors
- [Pulsar schemas](https://pulsar.apache.org/docs/next/schema-overview/) - Message formats
