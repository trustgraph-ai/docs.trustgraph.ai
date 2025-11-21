---
title: tg-show-parameter-types
parent: CLI
review_date: 2025-11-21
---

# tg-show-parameter-types

Shows all defined parameter types used in flow classes.

## Synopsis

```bash
tg-show-parameter-types [options]
```

## Description

The `tg-show-parameter-types` command displays all parameter type definitions configured in TrustGraph. Parameter types define the schema and constraints for parameters that can be used in flow class definitions, including data types, default values, valid enums, and validation rules.

Parameter types provide a centralized way to define reusable parameter schemas that ensure consistency across flow classes.

## Options

- `-u, --api-url URL`: TrustGraph API URL (default: `$TRUSTGRAPH_URL` or `http://localhost:8088/`)
- `-t, --type TYPE`: Show only the specified parameter type

## Examples

### Show All Parameter Types
```bash
tg-show-parameter-types
```

### Show Specific Parameter Type
```bash
tg-show-parameter-types -t llm-model
```

### Using Custom API URL
```bash
tg-show-parameter-types -u http://production:8088/
```

## Output Format

The command displays each parameter type in a formatted table:

```
+----------------+-----------------------------------------------------+
| name           | llm-model                                           |
| description    | LLM model selection                                 |
| type           | string                                              |
| default        | gpt-4                                               |
| valid values   | • gpt-4 (GPT-4 model)                               |
|                | • gpt-3.5-turbo (GPT-3.5 Turbo model)               |
|                | • claude-3-opus (Claude 3 Opus model)               |
| constraints    | required                                            |
+----------------+-----------------------------------------------------+

+----------------+-----------------------------------------------------+
| name           | temperature                                         |
| description    | LLM temperature parameter for response randomness   |
| type           | number                                              |
| default        | 0.7                                                 |
| constraints    | min: 0.0, max: 2.0                                  |
+----------------+-----------------------------------------------------+

+----------------+-----------------------------------------------------+
| name           | chunk-size                                          |
| description    | Maximum size of text chunks in characters           |
| type           | integer                                             |
| default        | 1000                                                |
| constraints    | min: 100, max: 10000                                |
+----------------+-----------------------------------------------------+
```

### No Parameter Types Defined
```bash
No parameter types defined.
```

## Parameter Type Fields

Each parameter type includes:

- **name**: Unique identifier for the parameter type
- **description**: Human-readable explanation of the parameter's purpose
- **type**: Data type (string, number, integer, boolean, array, object)
- **default**: Default value used when parameter is not specified
- **valid values**: Enum of allowed values (for enum types)
- **constraints**: Validation rules (min, max, minLength, maxLength, pattern, required)

## Parameter Type Components

### Data Types

Supported parameter types:
- **string**: Text values
- **number**: Numeric values (floating-point)
- **integer**: Whole numbers
- **boolean**: true/false values
- **array**: Lists of values
- **object**: Structured data

### Enum Values

Parameters can define enums with descriptive labels:

```
valid values   | • gpt-4 (GPT-4 model)
               | • claude-3-opus (Claude 3 Opus model)
               | • mistral-large (Mistral Large model)
```

### Constraints

Common validation constraints:
- **min / max**: Numeric range limits
- **minLength / maxLength**: String length limits
- **pattern**: Regular expression validation
- **required**: Must be provided (no default)

## Use Cases

### Discover Available Parameters
```bash
# See what parameters can be configured
tg-show-parameter-types
```

### Check Parameter Defaults
```bash
# View default LLM model
tg-show-parameter-types -t llm-model
```

### Validate Flow Configuration
```bash
# Check valid values before configuring flow
tg-show-parameter-types -t embedding-model
```

### Documentation and Reference
```bash
# Generate parameter documentation
tg-show-parameter-types > parameter-reference.txt
```

## Parameter Type Definition

Parameter types are stored in the configuration system with type `parameter-types`. They follow this schema:

```json
{
    "type": "string",
    "description": "LLM model selection",
    "default": "gpt-4",
    "enum": [
        {
            "id": "gpt-4",
            "description": "GPT-4 model"
        },
        {
            "id": "gpt-3.5-turbo",
            "description": "GPT-3.5 Turbo model"
        },
        {
            "id": "claude-3-opus",
            "description": "Claude 3 Opus model"
        }
    ],
    "required": true
}
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL

## Related Commands

- [`tg-show-flow-classes`](tg-show-flow-classes) - Show flow classes and their parameters
- [`tg-start-flow`](tg-start-flow) - Start a flow with parameter values
- [`tg-show-flows`](tg-show-flows) - Show active flows and their parameter settings
- [`tg-put-config-item`](tg-put-config-item) - Create or update parameter type definitions
- [`tg-list-config-items`](tg-list-config-items) - List all parameter types

## Configuration Management

Parameter types are managed through the configuration API:

```bash
# List all parameter types
tg-list-config-items -t parameter-types

# Get a specific parameter type
tg-get-config-item -t parameter-types -k llm-model

# Create or update parameter type
tg-put-config-item -t parameter-types -k custom-param -v '{"type": "string", "default": "value"}'
```

## Parameter Usage in Flow Classes

Flow classes reference parameter types in their definitions:

```json
{
    "description": "Document processing flow",
    "parameters": {
        "model": {
            "type": "llm-model",
            "description": "LLM model to use for processing",
            "order": 1
        },
        "temperature": {
            "type": "temperature",
            "description": "Response randomness",
            "order": 2
        }
    }
}
```

When starting a flow, users can override defaults:

```bash
tg-start-flow -n document-processor -i my-flow -d "Processing" \
    --param model=claude-3-opus \
    --param temperature=0.5
```

## Best Practices

1. **Consistent Types**: Define parameter types centrally for reuse across flows
2. **Clear Descriptions**: Provide detailed descriptions for each parameter
3. **Sensible Defaults**: Set appropriate default values for common use cases
4. **Validation Rules**: Use constraints to prevent invalid configurations
5. **Enum Documentation**: Include descriptions for enum values to guide users
6. **Version Control**: Track parameter type changes over time
7. **Documentation**: Document parameter types for team reference

## See Also

- [Parameter Configuration Reference](../configuration/parameters) - Detailed parameter type schema
- [Flow Class Configuration](../configuration/flow-classes) - Using parameters in flow classes
- [Config API](../apis/api-config) - Managing parameter type definitions
