---
title: tg-revoke-api-key
parent: CLI
review_date: 2027-05-21
---

# tg-revoke-api-key

Revoke an API key.

## Synopsis

```bash
tg-revoke-api-key --key-id ID [options]
```

## Description

Revokes an API key by its ID. Once revoked, the key can no longer be used for authentication. Use `tg-list-api-keys` to find the key ID before revoking.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--key-id ID` | ID of the API key to revoke |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | Caller's workspace | Target workspace |

## Examples

```bash
# Revoke an API key
tg-revoke-api-key --key-id key-abc123

# List keys first, then revoke
tg-list-api-keys --user-id abc123
tg-revoke-api-key --key-id key-xyz789
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-list-api-keys`](tg-list-api-keys) - List API keys for a user
- [`tg-create-api-key`](tg-create-api-key) - Create an API key for a user
- [`tg-disable-user`](tg-disable-user) - Disable a user (also revokes all their keys)
