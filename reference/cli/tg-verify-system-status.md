---
title: tg-verify-system-status
parent: CLI
review_date: 2027-05-21
---

# tg-verify-system-status

Verifies TrustGraph system health by running comprehensive checks.

## Synopsis

```bash
tg-verify-system-status [options]
```

## Description

The `tg-verify-system-status` command monitors system startup and health by running comprehensive checks across four categories: infrastructure (Pulsar, API Gateway), core services (processors, flows, prompts), data services (library), and UI. It includes intelligent retry logic with configurable timeouts, making it suitable for use in deployment scripts and CI/CD pipelines to verify that a TrustGraph instance is fully operational.

## Options

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `--pulsar-url URL` | `http://localhost:8080` | Pulsar admin URL |
| `--ui-url URL` | `http://localhost:8888` | UI URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | `$TRUSTGRAPH_WORKSPACE` or `default` | Workspace identifier |
| `--timeout SECONDS` | `120` | Global timeout in seconds |
| `--check-timeout SECONDS` | `10` | Per-check timeout in seconds |
| `--retry-delay SECONDS` | `3` | Seconds between retries |
| `-v, --verbose` | false | Show debug output |

## Examples

### Basic Health Check
```bash
tg-verify-system-status
```

### Verbose Check with Custom Timeout
```bash
tg-verify-system-status -v --timeout 300
```

### Check a Remote Instance
```bash
tg-verify-system-status \
  -u http://production:8088/ \
  --pulsar-url http://production:8080 \
  --ui-url http://production:8888
```

### Quick Check with Short Timeouts
```bash
tg-verify-system-status --timeout 30 --check-timeout 5 --retry-delay 1
```

### Use in a Deployment Script
```bash
docker compose up -d
tg-verify-system-status --timeout 180 -v
echo "System is ready"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-show-processor-state`](tg-show-processor-state) - Show processor states
- [`tg-show-flow-state`](tg-show-flow-state) - Show flow states
- [`tg-show-flows`](tg-show-flows) - List configured flows
