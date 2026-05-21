---
title: tg-dump-queues
parent: CLI
review_date: 2027-05-21
---

# tg-dump-queues

Multi-queue Pulsar message dumper for debugging TrustGraph message flows.

## Synopsis

```bash
tg-dump-queues [pubsub-options] [-o LOG_FILE] QUEUE [QUEUE ...]
```

## Description

The `tg-dump-queues` command monitors multiple Pulsar queues simultaneously and logs all messages to a file with timestamps and pretty-printed formatting. It uses TrustGraph's Subscriber abstraction for pub/sub compatibility, making it a low-level debugging tool that connects directly to the pub/sub backend. This is useful for diagnosing message flow issues, inspecting queue contents, and verifying that processors are producing expected output.

## Options

### Positional Arguments

| Argument | Description |
|----------|-------------|
| `QUEUE [QUEUE ...]` | One or more queue names to monitor |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-o, --output LOG_FILE` | None | Path to a log file for captured messages |

### Pub/Sub Arguments

Standard pub/sub connection arguments are also accepted (added via `add_pubsub_args`), including the Pulsar broker URL and related connection settings.

## Examples

### Monitor a Single Queue
```bash
tg-dump-queues my-queue
```

### Monitor Multiple Queues
```bash
tg-dump-queues prompt-request prompt-response graph-rag
```

### Log Output to File
```bash
tg-dump-queues -o debug-log.txt prompt-request prompt-response
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default pub/sub connection URL

## Related Commands

- [`tg-monitor-prompts`](tg-monitor-prompts) - Monitor prompt request/response activity with timing
- [`tg-dump-msgpack`](tg-dump-msgpack) - Examine MessagePack file contents
- [`tg-show-processor-state`](tg-show-processor-state) - Show processor states
