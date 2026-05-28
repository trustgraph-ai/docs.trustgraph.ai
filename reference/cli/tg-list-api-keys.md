---
title: tg-list-api-keys
parent: CLI
review_date: 2027-05-21
---

# tg-list-api-keys

List the API keys for a user.

## Synopsis

```bash
tg-list-api-keys --user-id ID [options]
```

## Description

Lists all API keys belonging to the specified user. Output is presented in a tabulated format showing each key's id, name, prefix, created date, last used date, and expiration date.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--user-id ID` | ID of the user whose keys to list |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | Caller's workspace | Target workspace |

## Examples

```bash
# List API keys for a user
tg-list-api-keys --user-id abc123

# List keys in a specific workspace
tg-list-api-keys --user-id abc123 -w research-team
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-create-api-key`](tg-create-api-key) - Create an API key for a user
- [`tg-revoke-api-key`](tg-revoke-api-key) - Revoke an API key
- [`tg-list-users`](tg-list-users) - List users in the workspace
