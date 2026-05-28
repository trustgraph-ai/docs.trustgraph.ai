---
title: tg-create-api-key
parent: CLI
review_date: 2027-05-21
---

# tg-create-api-key

Create an API key for a user.

## Synopsis

```bash
tg-create-api-key --user-id ID --name NAME [options]
```

## Description

Creates a new API key for the specified user. The plaintext key is printed to stdout. This is the only time the full key is shown -- it cannot be retrieved again, so it must be recorded immediately. An optional expiration date can be set in ISO-8601 format.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--user-id ID` | ID of the user to create the key for |
| `--name NAME` | Descriptive name for the key (e.g. `laptop`, `ci`) |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `--expires DATETIME` | No expiry | Expiration date in ISO-8601 format |
| `-w, --workspace WORKSPACE` | Caller's workspace | Target workspace |

## Examples

```bash
# Create an API key for a user
tg-create-api-key --user-id abc123 --name laptop

# Create an API key with an expiration date
tg-create-api-key --user-id abc123 --name ci --expires 2026-12-31T23:59:59Z

# Capture the key in a variable
API_KEY=$(tg-create-api-key --user-id abc123 --name automation)
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-list-api-keys`](tg-list-api-keys) - List API keys for a user
- [`tg-revoke-api-key`](tg-revoke-api-key) - Revoke an API key
- [`tg-create-user`](tg-create-user) - Create a user
- [`tg-login`](tg-login) - Log in with username and password
