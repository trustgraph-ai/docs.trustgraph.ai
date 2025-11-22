---
title: Ontologies
parent: Configuration
grand_parent: Reference
nav_order: 2.5
permalink: /reference/configuration/ontologies
review_date: 2026-08-01
---

# Ontology Configuration

Ontologies define the semantic structure for knowledge extraction in [Ontology RAG](../../guides/ontology-rag/). They provide a schema of classes, properties, and relationships that guide how TrustGraph extracts structured knowledge from unstructured text.

## Overview

Ontologies in TrustGraph are based on OWL (Web Ontology Language) concepts and define:
- **Classes** - Types of entities (e.g., Sensor, Observation, Person)
- **Object Properties** - Relationships between entities (e.g., observes, hasResult)
- **Datatype Properties** - Attributes with literal values (e.g., startTime, hasSimpleResult)
- **Metadata** - Namespace definitions and ontology documentation

Ontologies are stored in TrustGraph's configuration system with the configuration type `ontology` and are managed through the standard configuration CLI commands.

## Ontology Sources

TrustGraph works with two ontology formats, each with specific tooling requirements:

### OWL Ontologies (Standard Format)

Standard OWL ontologies in Turtle (`.ttl`), RDF/XML, or other RDF serializations can **only** be imported through the Workbench Ontology Editor. The editor converts these to TrustGraph's native JSON format during import.

Common sources for OWL ontologies:
- W3C standard ontologies (SOSA/SSN, PROV-O, FOAF)
- Domain-specific ontologies (schema.org, Dublin Core)
- Custom ontologies created with tools like Protégé

### Native JSON Format

TrustGraph stores ontologies internally in a JSON format that closely follows OWL structure. The TrustGraph config API and CLI tools work **only** with this native JSON format.

You can obtain native JSON ontologies by:
- Exporting from the Workbench after importing an OWL ontology
- Creating programmatically
- Downloading pre-converted ontologies

**Workflow**: To use an OWL ontology with CLI tools, first import it via the Workbench, then export the native JSON format.

## Native JSON Structure

### Top-Level Structure

```json
{
  "metadata": { ... },
  "classes": { ... },
  "objectProperties": { ... },
  "datatypeProperties": { ... }
}
```

### Metadata Section

The metadata section contains ontology documentation and namespace definitions:

```json
{
  "metadata": {
    "name": "Ontology Name",
    "description": "Human-readable description",
    "version": "1.0",
    "created": "2024-01-15",
    "modified": "2024-06-20T10:30:00Z",
    "creator": "Author Name",
    "namespace": "http://example.org/ontology/",
    "namespaces": {
      "owl": "http://www.w3.org/2002/07/owl#",
      "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
      "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "http://example.org/ontology/"
    }
  }
}
```

| Property | Description |
|----------|-------------|
| `name` | Display name for the ontology |
| `description` | Detailed description of the ontology's purpose |
| `version` | Version identifier |
| `created` | Creation date |
| `modified` | Last modification timestamp |
| `creator` | Author or organization |
| `namespace` | Primary namespace URI |
| `namespaces` | Prefix-to-URI mappings for referenced vocabularies |

### Classes Section

Classes define entity types. Each class is keyed by a local identifier:

```json
{
  "classes": {
    "Sensor": {
      "uri": "http://www.w3.org/ns/sosa/Sensor",
      "type": "owl:Class",
      "rdfs:label": [
        {"value": "Sensor or Observer", "lang": "en"}
      ],
      "rdfs:subClassOf": "System"
    },
    "System": {
      "uri": "http://www.w3.org/ns/sosa/System",
      "type": "owl:Class",
      "rdfs:label": [
        {"value": "System", "lang": "en"}
      ]
    },
    "Observation": {
      "uri": "http://www.w3.org/ns/sosa/Observation",
      "type": "owl:Class",
      "rdfs:label": [
        {"value": "Observation", "lang": "en"}
      ],
      "rdfs:subClassOf": "Execution"
    }
  }
}
```

| Property | Required | Description |
|----------|----------|-------------|
| `uri` | Yes | Full URI identifier for the class |
| `type` | Yes | Always `owl:Class` |
| `rdfs:label` | Yes | Array of labels with language tags |
| `rdfs:subClassOf` | No | Parent class (local key reference) |

### Object Properties Section

Object properties define relationships between entities:

```json
{
  "objectProperties": {
    "observes": {
      "uri": "http://www.w3.org/ns/sosa/observes",
      "type": "owl:ObjectProperty",
      "rdfs:label": [
        {"value": "observes", "lang": "en"}
      ]
    },
    "hasResult": {
      "uri": "http://www.w3.org/ns/sosa/hasResult",
      "type": "owl:ObjectProperty",
      "rdfs:label": [
        {"value": "has result", "lang": "en"}
      ]
    },
    "madeBySensor": {
      "uri": "http://www.w3.org/ns/sosa/madeBySensor",
      "type": "owl:ObjectProperty",
      "rdfs:label": [
        {"value": "made by sensor or observer", "lang": "en"}
      ]
    }
  }
}
```

| Property | Required | Description |
|----------|----------|-------------|
| `uri` | Yes | Full URI identifier for the property |
| `type` | Yes | Always `owl:ObjectProperty` |
| `rdfs:label` | Yes | Array of labels with language tags |

### Datatype Properties Section

Datatype properties define attributes with literal values:

```json
{
  "datatypeProperties": {
    "startTime": {
      "uri": "http://www.w3.org/ns/sosa/startTime",
      "type": "owl:DatatypeProperty",
      "rdfs:range": "xsd:string",
      "rdfs:label": [
        {"value": "start time", "lang": "en"}
      ],
      "rdfs:comment": "The value would usually be encoded using xsd:dateTime"
    },
    "hasSimpleResult": {
      "uri": "http://www.w3.org/ns/sosa/hasSimpleResult",
      "type": "owl:DatatypeProperty",
      "rdfs:range": "xsd:string",
      "rdfs:label": [
        {"value": "has simple result", "lang": "en"}
      ]
    }
  }
}
```

| Property | Required | Description |
|----------|----------|-------------|
| `uri` | Yes | Full URI identifier for the property |
| `type` | Yes | Always `owl:DatatypeProperty` |
| `rdfs:range` | No | Expected datatype (e.g., `xsd:string`, `xsd:dateTime`) |
| `rdfs:label` | Yes | Array of labels with language tags |
| `rdfs:comment` | No | Additional documentation |

## Managing Ontologies

### Loading via Workbench (Recommended)

The Workbench provides an ontology editor that can import standard OWL ontologies:

1. Enable the Ontology Editor in Settings → Feature Switches
2. Navigate to the Ontologies page
3. Click 'Import Ontology'
4. Select your OWL file (Turtle, RDF/XML, etc.)
5. Click 'Import'

The editor allows you to explore and modify the ontology structure before saving.

### Loading via CLI

Load a native JSON ontology:

```bash
cat ontology.json | tg-put-config-item --type ontology --key my-ontology --stdin
```

Or with inline JSON:

```bash
tg-put-config-item --type ontology --key my-ontology --value '{
  "metadata": {
    "name": "My Ontology",
    "namespace": "http://example.org/ontology/"
  },
  "classes": { ... },
  "objectProperties": { ... },
  "datatypeProperties": { ... }
}'
```

### Listing Ontologies

```bash
tg-list-config-items --type ontology
```

### Retrieving an Ontology

```bash
tg-get-config-item --type ontology --key my-ontology
```

### Deleting an Ontology

```bash
tg-delete-config-item --type ontology --key my-ontology
```

## Using Ontologies in Flows

Ontologies are used with Ontology RAG flow classes. When creating a flow, specify which ontology to use:

```bash
tg-start-flow -n onto-rag -i my-flow -d "Ontology RAG with custom ontology"
```

The flow class determines which ontology is applied during knowledge extraction. See [Flow Classes](flow-classes) for configuration details.

## Complete Example

Here's a minimal but complete ontology for tracking observations:

```json
{
  "metadata": {
    "name": "Simple Observation Ontology",
    "description": "Basic ontology for tracking observations and sensors",
    "version": "1.0",
    "namespace": "http://example.org/obs/",
    "namespaces": {
      "owl": "http://www.w3.org/2002/07/owl#",
      "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "obs": "http://example.org/obs/"
    }
  },
  "classes": {
    "Sensor": {
      "uri": "http://example.org/obs/Sensor",
      "type": "owl:Class",
      "rdfs:label": [{"value": "Sensor", "lang": "en"}]
    },
    "Observation": {
      "uri": "http://example.org/obs/Observation",
      "type": "owl:Class",
      "rdfs:label": [{"value": "Observation", "lang": "en"}]
    },
    "Location": {
      "uri": "http://example.org/obs/Location",
      "type": "owl:Class",
      "rdfs:label": [{"value": "Location", "lang": "en"}]
    }
  },
  "objectProperties": {
    "madeBy": {
      "uri": "http://example.org/obs/madeBy",
      "type": "owl:ObjectProperty",
      "rdfs:label": [{"value": "made by", "lang": "en"}]
    },
    "atLocation": {
      "uri": "http://example.org/obs/atLocation",
      "type": "owl:ObjectProperty",
      "rdfs:label": [{"value": "at location", "lang": "en"}]
    }
  },
  "datatypeProperties": {
    "timestamp": {
      "uri": "http://example.org/obs/timestamp",
      "type": "owl:DatatypeProperty",
      "rdfs:range": "xsd:dateTime",
      "rdfs:label": [{"value": "timestamp", "lang": "en"}]
    },
    "value": {
      "uri": "http://example.org/obs/value",
      "type": "owl:DatatypeProperty",
      "rdfs:range": "xsd:string",
      "rdfs:label": [{"value": "value", "lang": "en"}]
    }
  }
}
```

## Best Practices

### Ontology Design

1. **Start with existing ontologies** - Use established standards like SOSA/SSN, schema.org, or Dublin Core where applicable
2. **Keep it focused** - Include only classes and properties relevant to your extraction needs
3. **Use meaningful labels** - Labels are used by the LLM during extraction; clear labels improve accuracy
4. **Define hierarchies** - Use `rdfs:subClassOf` to create class hierarchies that aid extraction

### Namespace Management

1. **Use standard prefixes** - Follow conventions (owl, rdf, rdfs, xsd)
2. **Define a primary namespace** - Use the `namespace` field for your ontology's base URI
3. **Include all referenced namespaces** - Ensure all prefixes used in URIs are defined

### Knowledge Extraction

1. **Match domain vocabulary** - Class and property names should align with terminology in your documents
2. **Balance specificity** - Too many classes may fragment extraction; too few may lose precision
3. **Test with sample documents** - Validate that the ontology captures the relationships you need

## See Also

- [Ontology RAG Guide](../../guides/ontology-rag/) - Complete tutorial for using ontologies
- [tg-put-config-item](../cli/tg-put-config-item) - Create and update ontologies
- [tg-get-config-item](../cli/tg-get-config-item) - Retrieve ontology definitions
- [tg-list-config-items](../cli/tg-list-config-items) - List all ontologies
- [Flow Classes](flow-classes) - Configure flows to use ontologies
- [Schemas](schemas) - Structured data schemas (different from ontologies)

