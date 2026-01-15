---
title: tg-show-prompts
parent: CLI
review_date: 2026-05-16
---

# tg-show-prompts

Displays all configured prompt templates and system prompts in TrustGraph.

## Synopsis

```bash
tg-show-prompts [options]
```

## Description

The `tg-show-prompts` command displays all prompt templates and the system prompt currently configured in TrustGraph. This includes template IDs, prompt text, response types, and JSON schemas for structured responses.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Display All Prompts
```bash
tg-show-prompts
```

### Using Custom API URL
```bash
tg-show-prompts -u http://production:8088/
```

## Output Format

The command displays prompts in formatted tables:

```
System prompt:
+---------+--------------------------------------------------+
| prompt  | You are a helpful AI assistant. Always provide  |
|         | accurate, concise responses. When uncertain,     |
|         | clearly state your limitations.                  |
+---------+--------------------------------------------------+

greeting:
+---------+--------------------------------------------------+
| prompt  | Hello {{name}}, welcome to {{place}}!           |
+---------+--------------------------------------------------+

extract-info:
+----------+-------------------------------------------------+
| prompt   | Extract key information from: {{text}}         |
| response | json                                            |
| schema   | {"type": "object", "properties": {...}}        |
+----------+-------------------------------------------------+
```

### Template Information

For each template, the output shows:
- **prompt**: The template text with variable placeholders (e.g., `{{name}}`)
- **response**: Response format (`text` or `json`)
- **schema**: JSON schema for structured responses (when response type is `json`)

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-set-prompt`](tg-set-prompt) - Configure prompt templates
- [`tg-invoke-prompt`](tg-invoke-prompt) - Execute a prompt template

## API Integration

This command uses the [Configuration API](../apis/api-config) to retrieve prompt configurations.
