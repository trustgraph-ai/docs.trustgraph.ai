---
title: tg-set-prompt
parent: CLI
review_date: 2026-09-14
---

# tg-set-prompt

Sets prompt templates and system prompts for TrustGraph LLM services.

## Synopsis

```bash
# Set a prompt template
tg-set-prompt --id TEMPLATE_ID --prompt TEMPLATE [options]

# Set system prompt
tg-set-prompt --system SYSTEM_PROMPT [options]
```

## Description

The `tg-set-prompt` command configures prompt templates and system prompts used by TrustGraph's LLM services. Prompt templates contain placeholders like `{{variable}}` that are replaced with actual values when invoked. System prompts provide global context for all LLM interactions.

## Options

### Prompt Template Mode

| Option | Description |
|--------|-------------|
| `--id ID` | Unique identifier for the prompt template (required) |
| `--prompt TEMPLATE` | Prompt template text with `{{variable}}` placeholders (required) |
| `--response TYPE` | Response format - `text` or `json` (default: `text`) |
| `--schema SCHEMA` | JSON schema for structured responses (required when response is `json`) |

### System Prompt Mode

| Option | Description |
|--------|-------------|
| `--system PROMPT` | System prompt text (cannot be used with template options) |

### Common Options

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

### Basic Prompt Template
```bash
tg-set-prompt \
  --id "greeting" \
  --prompt "Hello {{name}}, welcome to {{place}}!"
```

### Question-Answer Template
```bash
tg-set-prompt \
  --id "question" \
  --prompt "Answer this question based on the context: {{question}}\n\nContext: {{context}}"
```

### JSON Response Template
```bash
tg-set-prompt \
  --id "extract-info" \
  --prompt "Extract key information from: {{text}}" \
  --response "json" \
  --schema '{"type": "object", "properties": {"name": {"type": "string"}, "age": {"type": "number"}}}'
```

### System Prompt
```bash
tg-set-prompt \
  --system "You are a helpful AI assistant. Always provide accurate, concise responses."
```

## Notes

Templates use `{{variable}}` syntax for placeholders that are replaced when the template is invoked with `tg-invoke-prompt`.

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-prompts`](tg-show-prompts) - Display configured prompts
- [`tg-invoke-prompt`](tg-invoke-prompt) - Execute a prompt template

## API Integration

This command uses the [Configuration API](../apis/api-config) to store prompt configurations.
