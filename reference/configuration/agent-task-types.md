---
title: Agent Task Types
parent: Configuration
grand_parent: Reference
nav_order: 3.5
permalink: /reference/configuration/agent-task-types
review_date: 2027-01-01
---

# Agent Task Type Configuration

Agent task types define categories of work that the agent orchestrator can recognise and handle with specialised framing. When a question arrives, the meta-router classifies it into a task type, applies domain-specific framing to the LLM context, and constrains which agent patterns are available.

## Overview

Task types allow you to:
- **Classify questions** into domain categories (e.g. research, risk assessment, summarisation)
- **Inject framing prompts** that steer the LLM's approach for that category
- **Constrain pattern selection** so that only suitable execution patterns are considered

Task types are stored in the configuration service with the type `agent-task-type` and are managed through the standard configuration CLI commands.

## JSON Structure

Each task type is a JSON object with the following fields:

```json
{
  "name": "risk-assessment",
  "description": "Due Diligence / Risk Assessment",
  "framing": "Analyse across financial, reputational, legal and operational dimensions using structured analytic techniques.",
  "valid_patterns": ["supervisor", "plan-then-execute", "react"],
  "when_to_use": "Multi-dimensional analysis requiring structured assessment"
}
```

| Property | Required | Description |
|----------|----------|-------------|
| `name` | Yes | Task type identifier, must match the config key |
| `description` | Yes | Human-readable description presented to the LLM meta-router for classification |
| `framing` | No | Domain-specific framing prompt injected into the LLM context when this task type is selected |
| `valid_patterns` | No | List of agent pattern keys that are allowed for this task type. If omitted, all patterns are available |
| `when_to_use` | No | Additional guidance for the meta-router on when to classify a question as this task type |

## Default Behaviour

If no `agent-task-type` config items are defined, the orchestrator falls back to a single task type:

```json
{
  "name": "general",
  "description": "General queries",
  "valid_patterns": ["react"],
  "framing": ""
}
```

## Managing Task Types

### Adding a Task Type

```bash
tg-put-config-item --type agent-task-type --key research --value '{
  "name": "research",
  "description": "In-depth research and investigation",
  "framing": "Conduct thorough research, cross-reference multiple sources, and provide well-evidenced conclusions.",
  "valid_patterns": ["plan-then-execute", "react"],
  "when_to_use": "Questions requiring detailed investigation across multiple topics"
}'
```

### Listing Task Types

```bash
tg-list-config-items --type agent-task-type
```

### Retrieving a Task Type

```bash
tg-get-config-item --type agent-task-type --key research
```

### Deleting a Task Type

```bash
tg-delete-config-item --type agent-task-type --key research
```

## Example Configuration

A typical deployment might define several task types:

```bash
# General-purpose queries - use ReAct for flexibility
tg-put-config-item --type agent-task-type --key general --value '{
  "name": "general",
  "description": "General queries and simple questions",
  "framing": "",
  "valid_patterns": ["react"]
}'

# Research tasks - plan first, then execute
tg-put-config-item --type agent-task-type --key research --value '{
  "name": "research",
  "description": "In-depth research and investigation",
  "framing": "Conduct thorough research, cross-reference multiple sources, and provide well-evidenced conclusions.",
  "valid_patterns": ["plan-then-execute", "react"]
}'

# Risk assessment - fan out to parallel sub-agents
tg-put-config-item --type agent-task-type --key risk-assessment --value '{
  "name": "risk-assessment",
  "description": "Due Diligence / Risk Assessment",
  "framing": "Analyse across financial, reputational, legal and operational dimensions using structured analytic techniques.",
  "valid_patterns": ["supervisor", "plan-then-execute"],
  "when_to_use": "Multi-dimensional analysis requiring structured assessment"
}'
```

## How Task Types Are Used

When the agent orchestrator receives a question:

1. The meta-router presents all configured task types (with their `description` and `when_to_use` fields) to the LLM
2. The LLM classifies the question into the most appropriate task type
3. The task type's `framing` prompt is injected into the agent's LLM context
4. Pattern selection is constrained to the task type's `valid_patterns` list
5. The meta-router selects the best pattern from the constrained set

If classification fails, the orchestrator falls back to the `general` task type with the `react` pattern.

## See Also

- [Agent Patterns](agent-patterns) - Execution pattern definitions
- [tg-invoke-agent](../cli/tg-invoke-agent) - Agent CLI
- [tg-put-config-item](../cli/tg-put-config-item) - Create and update config items
- [tg-list-config-items](../cli/tg-list-config-items) - List config items
