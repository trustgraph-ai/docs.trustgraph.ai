---
layout: default
title: Parameter Types
parent: Configuration
grand_parent: Reference
nav_order: 3
permalink: /reference/configuration/parameters
---

# Parameter Type Configuration

Parameter types define the schema and constraints for configurable parameters used in flow classes. They provide a centralized, reusable way to define parameter specifications that ensure consistency and validation across TrustGraph flows.

## Overview

Parameter types are stored in TrustGraph's configuration system with the configuration type `parameter-types`. Each parameter type defines:

- **Data type**: The kind of value (string, number, integer, boolean, etc.)
- **Default value**: Value used when parameter is not specified
- **Valid values**: Enumeration of allowed values with descriptions
- **Constraints**: Validation rules (ranges, lengths, patterns, required)
- **Documentation**: Human-readable descriptions

Flow classes reference these parameter types to define which parameters they accept, and the system automatically handles default values and validation.

## Parameter Type Schema

### Basic Structure

```json
{
    "type": "string",
    "description": "Human-readable description of the parameter",
    "default": "default-value",
    "required": false
}
```

### Complete Schema

```json
{
    "type": "string|number|integer|boolean|array|object",
    "description": "Parameter description",
    "default": "any-value",
    "enum": [
        {
            "id": "value1",
            "description": "Description of value1"
        },
        {
            "id": "value2",
            "description": "Description of value2"
        }
    ],
    "minimum": 0,
    "maximum": 100,
    "minLength": 1,
    "maxLength": 255,
    "pattern": "^[a-z0-9-]+$",
    "required": true
}
```

## Fields

### type (required)

The data type of the parameter value.

**Valid types:**
- `string`: Text values
- `number`: Numeric values (floating-point)
- `integer`: Whole numbers
- `boolean`: true/false values
- `array`: Lists of values
- `object`: Structured data

**Example:**
```json
{
    "type": "string"
}
```

### description (recommended)

Human-readable explanation of the parameter's purpose and usage.

**Example:**
```json
{
    "type": "string",
    "description": "LLM model identifier for text completion"
}
```

### default (optional)

Default value used when the parameter is not explicitly provided.

**Examples:**
```json
// String default
{
    "type": "string",
    "default": "gpt-4"
}

// Number default
{
    "type": "number",
    "default": 0.7
}

// Boolean default
{
    "type": "boolean",
    "default": true
}
```

### enum (optional)

List of valid values for the parameter. Can be simple strings or objects with id and description.

**Simple enum (legacy format):**
```json
{
    "type": "string",
    "enum": ["gpt-4", "gpt-3.5-turbo", "claude-3-opus"]
}
```

**Descriptive enum (recommended):**
```json
{
    "type": "string",
    "enum": [
        {
            "id": "gpt-4",
            "description": "GPT-4 model - Most capable, higher cost"
        },
        {
            "id": "gpt-3.5-turbo",
            "description": "GPT-3.5 Turbo - Fast and cost-effective"
        },
        {
            "id": "claude-3-opus",
            "description": "Claude 3 Opus - Excellent reasoning"
        }
    ]
}
```

### minimum / maximum (optional)

Numeric constraints for `number` and `integer` types.

**Example:**
```json
{
    "type": "number",
    "description": "Temperature parameter controlling randomness",
    "minimum": 0.0,
    "maximum": 2.0,
    "default": 0.7
}
```

### minLength / maxLength (optional)

String length constraints for `string` types.

**Example:**
```json
{
    "type": "string",
    "description": "API key",
    "minLength": 32,
    "maxLength": 64
}
```

### pattern (optional)

Regular expression pattern for validating `string` types.

**Example:**
```json
{
    "type": "string",
    "description": "Model identifier",
    "pattern": "^[a-z0-9-]+$"
}
```

### required (optional)

Whether the parameter must be provided (no default will be used).

**Example:**
```json
{
    "type": "string",
    "description": "API endpoint URL",
    "required": true
}
```

**Note:** If `required` is true and no default is provided, flows must specify a value for this parameter.

## Complete Examples

### LLM Model Parameter

```json
{
    "type": "string",
    "description": "Large Language Model selection for text processing",
    "default": "gpt-4",
    "enum": [
        {
            "id": "gpt-4",
            "description": "GPT-4 - Most capable OpenAI model"
        },
        {
            "id": "gpt-3.5-turbo",
            "description": "GPT-3.5 Turbo - Fast and efficient"
        },
        {
            "id": "claude-3-opus",
            "description": "Claude 3 Opus - Advanced reasoning"
        },
        {
            "id": "mistral-large",
            "description": "Mistral Large - Open source alternative"
        }
    ],
    "required": false
}
```

### Temperature Parameter

```json
{
    "type": "number",
    "description": "Controls randomness in LLM responses (0.0 = deterministic, 2.0 = very random)",
    "default": 0.7,
    "minimum": 0.0,
    "maximum": 2.0,
    "required": false
}
```

### Chunk Size Parameter

```json
{
    "type": "integer",
    "description": "Maximum size of text chunks in characters",
    "default": 1000,
    "minimum": 100,
    "maximum": 10000,
    "required": false
}
```

### Embedding Model Parameter

```json
{
    "type": "string",
    "description": "Embedding model for vector generation",
    "default": "text-embedding-ada-002",
    "enum": [
        {
            "id": "text-embedding-ada-002",
            "description": "OpenAI Ada-002 - High quality embeddings"
        },
        {
            "id": "text-embedding-3-small",
            "description": "OpenAI Embedding-3 Small - Cost effective"
        },
        {
            "id": "text-embedding-3-large",
            "description": "OpenAI Embedding-3 Large - Highest quality"
        }
    ]
}
```

### Enable Feature Parameter

```json
{
    "type": "boolean",
    "description": "Enable advanced relationship extraction",
    "default": false
}
```

## Usage in Flow Classes

Flow classes reference parameter types in their `parameters` section:

```json
{
    "description": "Document processing with configurable LLM",
    "parameters": {
        "llm-model": {
            "type": "llm-model",
            "description": "Model for document analysis",
            "order": 1
        },
        "temperature": {
            "type": "temperature",
            "description": "Response creativity level",
            "order": 2
        },
        "chunk-size": {
            "type": "chunk-size",
            "description": "Text chunking size",
            "order": 3
        }
    },
    "class": { ... },
    "flow": { ... },
    "interfaces": { ... }
}
```

### Parameter Metadata in Flow Classes

Flow class parameter definitions include:

- **type**: Reference to parameter type name
- **description**: Override or supplement the type's description
- **order**: Display order in UI and CLI
- **controlled-by**: Parameter value is inherited from another parameter

**Example with controlled-by:**
```json
{
    "parameters": {
        "llm-model": {
            "type": "llm-model",
            "description": "Model for general processing",
            "order": 1
        },
        "rag-model": {
            "type": "llm-model",
            "description": "Model for RAG queries",
            "order": 2,
            "controlled-by": "llm-model"
        }
    }
}
```

## Parameter Resolution

When starting a flow, parameters are resolved in this order:

1. **User-provided values**: Explicit values from `tg-start-flow --param` or API
2. **Default values**: From parameter type definitions
3. **Controlled-by relationships**: Inherited from controlling parameters
4. **Required validation**: Error if required parameters are missing

### Resolution Example

Given this parameter type:
```json
{
    "type": "string",
    "default": "gpt-4",
    "enum": [...]
}
```

And this flow start command:
```bash
tg-start-flow -n my-flow -i flow1 -d "Test" --param model=claude-3-opus
```

Resolution:
1. User provided `model=claude-3-opus` → Use this value
2. If user didn't provide → Use default `gpt-4`
3. If no default and required → Error

## Managing Parameter Types

### View All Parameter Types

```bash
tg-show-parameter-types
```

### View Specific Parameter Type

```bash
tg-show-parameter-types -t llm-model
```

### List Parameter Type Names

```bash
tg-list-config-items -t parameter-types
```

### Get Parameter Type Definition

```bash
tg-get-config-item -t parameter-types -k llm-model
```

### Create or Update Parameter Type

```bash
tg-put-config-item -t parameter-types -k custom-param -v '{
    "type": "string",
    "description": "Custom parameter",
    "default": "value",
    "enum": [
        {"id": "option1", "description": "First option"},
        {"id": "option2", "description": "Second option"}
    ]
}'
```

### Delete Parameter Type

```bash
tg-delete-config-item -t parameter-types -k old-param
```

## Best Practices

### Design

1. **Descriptive Names**: Use clear, descriptive names for parameter types
2. **Reusability**: Design parameter types for reuse across multiple flow classes
3. **Sensible Defaults**: Provide appropriate defaults for common use cases
4. **Document Enums**: Include descriptions for all enum values
5. **Validate Constraints**: Use min/max and pattern constraints to prevent invalid values

### Organization

1. **Centralized Definitions**: Define parameter types once, reference everywhere
2. **Versioning**: Consider versioning strategy for parameter type changes
3. **Naming Conventions**: Use consistent naming (e.g., `llm-model`, `chunk-size`)
4. **Grouping**: Organize related parameters (e.g., all LLM params use similar patterns)

### Maintenance

1. **Backward Compatibility**: Be careful when changing parameter types
2. **Documentation**: Keep descriptions up to date
3. **Deprecation**: Mark old parameter types as deprecated before removal
4. **Testing**: Test parameter changes with existing flows

## Common Patterns

### Model Selection Pattern

```json
{
    "type": "string",
    "description": "AI model selection",
    "default": "default-model",
    "enum": [
        {"id": "model-a", "description": "Description of model A"},
        {"id": "model-b", "description": "Description of model B"}
    ]
}
```

### Numeric Range Pattern

```json
{
    "type": "number",
    "description": "Numeric parameter with range",
    "default": 0.5,
    "minimum": 0.0,
    "maximum": 1.0
}
```

### Feature Flag Pattern

```json
{
    "type": "boolean",
    "description": "Enable optional feature",
    "default": false
}
```

### Size Constraint Pattern

```json
{
    "type": "integer",
    "description": "Size parameter",
    "default": 1000,
    "minimum": 100,
    "maximum": 10000
}
```

## See Also

- [Flow Class Configuration](flow-classes) - Using parameters in flow classes
- [tg-show-parameter-types](../cli/tg-show-parameter-types) - View parameter types
- [tg-start-flow](../cli/tg-start-flow) - Start flows with parameter values
- [tg-show-flow-classes](../cli/tg-show-flow-classes) - View flow class parameters
- [Config API](../apis/api-config) - Manage parameter type definitions
