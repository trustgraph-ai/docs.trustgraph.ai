---
title: tg-invoke-llm
parent: CLI
review_date: 2026-12-02
---

# tg-invoke-llm

Invokes the text completion service with custom system and user prompts.

## Synopsis

```bash
tg-invoke-llm "system prompt" "user prompt" [options]
```

## Description

The `tg-invoke-llm` command provides direct access to the Large Language Model (LLM) text completion service. Specify both a system prompt (which sets the AI's behavior and context) and a user prompt (the actual query or task) for complete control over LLM interaction.

Useful for custom AI tasks, prompt experimentation, and direct LLM integration without RAG or agent frameworks.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `system` | System prompt that defines the AI's role and behavior |
| `prompt` | User prompt containing the actual query or task |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-f, --flow-id FLOW` | `default` | Flow ID to use |

## Examples

### Basic Question Answering
```bash
tg-invoke-llm "You are a helpful assistant." "What is the capital of France?"
```

### Code Generation
```bash
tg-invoke-llm \
  "You are an expert Python programmer." \
  "Write a function to calculate the Fibonacci sequence."
```

### Creative Writing
```bash
tg-invoke-llm \
  "You are a creative writer specializing in science fiction." \
  "Write a short story about time travel in 200 words."
```

### Technical Documentation
```bash
tg-invoke-llm \
  "You are a technical writer who creates clear, concise documentation." \
  "Explain how REST APIs work in simple terms."
```

### Using Specific Flow
```bash
tg-invoke-llm \
  "You are a medical expert." \
  "Explain the symptoms of type 2 diabetes." \
  -f medical-flow
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token

## Related Commands

- [`tg-invoke-prompt`](tg-invoke-prompt) - Use predefined prompt templates
- [`tg-invoke-agent`](tg-invoke-agent) - Invoke agent with tools
- [`tg-set-prompt`](tg-set-prompt) - Configure prompt templates

## API Integration

This command uses the Text Completion API to generate responses using the configured LLM service.
