---
title: tg-show-parameter-types
parent: CLI
review_date: 2026-04-26
---

# tg-show-parameter-types

Shows all defined parameter types used in flow blueprints.

## Synopsis

```bash
tg-show-parameter-types [options]
```

## Description

The `tg-show-parameter-types` command displays all parameter type definitions configured in TrustGraph. Parameter types define schemas and constraints for flow blueprint parameters, including data types, defaults, valid enums, and validation rules.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-T, --type TYPE` | All types | Show only the specified parameter type |

## Examples

### Show All Parameter Types
```bash
tg-show-parameter-types
```

### Show Specific Parameter Type
```bash
tg-show-parameter-types -T llm-model
```

### Using Custom API URL
```bash
tg-show-parameter-types -u http://production:8088/
```

## Output Format

Each parameter type is displayed in a table showing:
- **name**: Parameter type identifier
- **description**: Purpose of the parameter
- **type**: Data type (string, number, boolean)
- **default**: Default value
- **valid values**: Enumerated options with descriptions
- **constraints**: Validation rules (e.g., required, min/max)

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-flow-blueprints`](tg-show-flow-blueprints) - List flow blueprints
- [`tg-start-flow`](tg-start-flow) - Start flow with parameters

## API Integration

This command uses the Configuration API to retrieve parameter type definitions.
