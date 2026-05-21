---
title: tg-disable-user
parent: CLI
review_date: 2027-05-21
---

# tg-disable-user

Disable a user and revoke their API keys.

## Synopsis

```bash
tg-disable-user --user-id ID [options]
```

## Description

Disables a user by setting their enabled flag to false and revoking all of their API keys. This is a soft-delete operation -- the user record is retained but the user can no longer authenticate. To fully remove the user, use `tg-delete-user` instead.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--user-id ID` | ID of the user to disable |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | Caller's workspace | Target workspace |

## Examples

```bash
# Disable a user
tg-disable-user --user-id abc123

# Disable a user in a specific workspace
tg-disable-user --user-id abc123 -w research-team
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-enable-user`](tg-enable-user) - Re-enable a disabled user
- [`tg-delete-user`](tg-delete-user) - Delete a user permanently
- [`tg-update-user`](tg-update-user) - Update user profile fields
- [`tg-list-users`](tg-list-users) - List users in the workspace
- [`tg-revoke-api-key`](tg-revoke-api-key) - Revoke an individual API key
