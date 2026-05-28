---
title: tg-enable-user
parent: CLI
review_date: 2027-05-21
---

# tg-enable-user

Re-enable a previously disabled user.

## Synopsis

```bash
tg-enable-user --user-id ID [options]
```

## Description

Re-enables a user that was previously disabled with `tg-disable-user`. Note that this does not restore any API keys that were revoked during the disable operation -- new API keys must be created separately with `tg-create-api-key`.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--user-id ID` | ID of the user to enable |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | Caller's workspace | Target workspace |

## Examples

```bash
# Re-enable a user
tg-enable-user --user-id abc123

# Re-enable and then issue a new API key
tg-enable-user --user-id abc123
tg-create-api-key --user-id abc123 --name laptop
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-disable-user`](tg-disable-user) - Disable a user
- [`tg-create-api-key`](tg-create-api-key) - Create an API key for the re-enabled user
- [`tg-update-user`](tg-update-user) - Update user profile fields
- [`tg-list-users`](tg-list-users) - List users in the workspace
