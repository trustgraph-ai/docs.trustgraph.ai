---
title: tg-monitor-prompts
parent: CLI
review_date: 2027-05-21
---

# tg-monitor-prompts

Monitors prompt request/response queues and logs activity with timing.

## Synopsis

```bash
tg-monitor-prompts [options]
```

## Description

The `tg-monitor-prompts` command subscribes to prompt request and response queues, correlates them by message ID, and logs a summary of each request/response pair with elapsed time. Streaming responses are accumulated and shown once at completion. This is useful for monitoring prompt throughput, diagnosing latency issues, and observing prompt activity in real time.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `--flow FLOW` | `default` | Flow identifier to monitor |
| `--queue-type TYPE` | `prompt-rag` | Queue type to monitor |
| `--max-lines N` | `3` | Maximum lines to display per prompt/response |
| `--max-width N` | `80` | Maximum character width for displayed output |

### Pub/Sub Arguments

Standard pub/sub connection arguments are also accepted (added via `add_pubsub_args`), including the Pulsar broker URL and related connection settings.

## Examples

### Basic Monitoring
```bash
tg-monitor-prompts
```

### Monitor with Increased Output Detail
```bash
tg-monitor-prompts --flow default --max-lines 5
```

### Monitor a Specific Queue Type
```bash
tg-monitor-prompts --queue-type prompt-rag
```

### Wide Output Format
```bash
tg-monitor-prompts --max-width 120 --max-lines 10
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default pub/sub connection URL

## Related Commands

- [`tg-dump-queues`](tg-dump-queues) - Low-level multi-queue message dumper
- [`tg-invoke-prompt`](tg-invoke-prompt) - Send prompt requests
- [`tg-show-processor-state`](tg-show-processor-state) - Show processor states
