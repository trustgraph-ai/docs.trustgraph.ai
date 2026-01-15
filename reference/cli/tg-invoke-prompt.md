---
title: tg-invoke-prompt
parent: CLI
review_date: 2026-05-08
---

# tg-invoke-prompt

Invokes the LLM prompt service using predefined prompt templates with variable substitution.

## Synopsis

```bash
tg-invoke-prompt [options] template-id [variable=value ...]
```

## Description

The `tg-invoke-prompt` command invokes TrustGraph's LLM prompt service using predefined prompt templates. Templates contain placeholder variables in the format `{{variable}}` that are replaced with values provided on the command line.

This provides a structured way to interact with language models using consistent, reusable prompt templates for specific tasks like question answering, text extraction, analysis, and more.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `template-id` | Prompt template identifier (e.g., `question`, `extract-definitions`) |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id ID` | `default` | Flow instance ID to use |
| `variable=value` | (none) | Template variable assignments (can specify multiple times) |

## Examples

### Basic Question Answering
```bash
tg-invoke-prompt question \
  text="What is artificial intelligence?" \
  context="AI research field"
```

### Extract Definitions
```bash
tg-invoke-prompt extract-definitions \
  document="Machine learning is a subset of AI..." \
  terms="machine learning,neural networks"
```

### Text Summarization
```bash
tg-invoke-prompt summarize \
  text="$(cat document.txt)" \
  max_length="200"
```

### With Custom Flow
```bash
tg-invoke-prompt analysis \
  -f "research-flow" \
  data="$(cat research-data.json)" \
  focus="trends"
```

## Variable Substitution

Templates use `{{variable}}` placeholders that are replaced with command-line values:

```bash
# Template: "Good {{time}}, {{name}}!"
tg-invoke-prompt greeting name="Alice" time="morning"
# Result: "Good morning, Alice!"
```

Variables can contain:
- Simple text values
- File contents via `$(cat file.txt)`
- Command output via `$(command)`

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-show-prompts`](tg-show-prompts) - Display configured prompts
- [`tg-set-prompt`](tg-set-prompt) - Configure prompt templates
- [`tg-invoke-llm`](tg-invoke-llm) - Invoke LLM directly

## API Integration

This command uses the [Prompt API](../apis/api-prompt) to execute prompt templates with variable substitution.
