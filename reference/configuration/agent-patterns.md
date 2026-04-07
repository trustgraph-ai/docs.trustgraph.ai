---
title: Agent Patterns
parent: Configuration
grand_parent: Reference
nav_order: 3
permalink: /reference/configuration/agent-patterns
review_date: 2027-01-01
---

# Agent Pattern Configuration

Agent patterns define the execution strategies available to the agent orchestrator. The orchestrator's meta-router uses these definitions to select the most appropriate reasoning pattern for each incoming question.

## Overview

TrustGraph ships with three built-in agent patterns:

- **react** - Interleaved reasoning and action (ReAct). Iteratively thinks, selects a tool, observes the result, and repeats until it can answer. Good for open-ended, exploratory tasks.
- **plan-then-execute** - Generates a multi-step plan first, then executes each step sequentially and synthesises the results. Suited to structured, predictable tasks.
- **supervisor** - Decomposes the question into independent sub-agent goals, fans out to parallel sub-agents, and aggregates findings into a synthesis. Best for broad, multi-dimensional analysis.

Patterns are stored in the configuration service with the type `agent-pattern` and are managed through the standard configuration CLI commands.

## JSON Structure

Each pattern is a JSON object with the following fields:

```json
{
  "name": "react",
  "description": "ReACT \u2014 Reasoning + Acting",
  "when_to_use": "Adaptive, good for open-ended tasks"
}
```

| Property | Required | Description |
|----------|----------|-------------|
| `name` | Yes | Pattern identifier, must match the config key |
| `description` | Yes | Human-readable description presented to the LLM meta-router |
| `when_to_use` | No | Additional guidance for the meta-router on when to select this pattern |

## Default Behaviour

If no `agent-pattern` config items are defined, the orchestrator falls back to a single pattern:

```json
{
  "name": "react",
  "description": "Interleaved reasoning and action"
}
```

## Managing Patterns

### Adding a Pattern

```bash
tg-put-config-item --type agent-pattern --key supervisor --value '{
  "name": "supervisor",
  "description": "Fan-out to parallel sub-agents with synthesis",
  "when_to_use": "Broad questions requiring multi-dimensional analysis"
}'
```

### Listing Patterns

```bash
tg-list-config-items --type agent-pattern
```

### Retrieving a Pattern

```bash
tg-get-config-item --type agent-pattern --key react
```

### Deleting a Pattern

```bash
tg-delete-config-item --type agent-pattern --key supervisor
```

## How Patterns Are Selected

The agent orchestrator's meta-router selects a pattern in two stages:

1. **Task type identification** - The LLM classifies the incoming question into a known task type (see [Agent Task Types](agent-task-types))
2. **Pattern selection** - The LLM selects from the patterns listed in the task type's `valid_patterns` field, using each pattern's `description` and `when_to_use` to inform the decision

The selected pattern can also be specified explicitly using the `-p` flag on the CLI:

```bash
tg-invoke-agent -q "Analyse the risks" -p supervisor
```

## See Also

- [Agent Task Types](agent-task-types) - Task type definitions that constrain pattern selection
- [tg-invoke-agent](../cli/tg-invoke-agent) - Agent CLI with pattern selection
- [tg-put-config-item](../cli/tg-put-config-item) - Create and update config items
- [tg-list-config-items](../cli/tg-list-config-items) - List config items
