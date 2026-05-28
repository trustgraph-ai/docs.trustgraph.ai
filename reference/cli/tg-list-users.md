---
title: tg-list-users
parent: CLI
review_date: 2027-05-21
---

# tg-list-users

List users in the caller's workspace.

## Synopsis

```bash
tg-list-users [options]
```

## Description

Lists all users in the caller's workspace. Output is presented in a tabulated format showing user details. An optional workspace parameter can be used to list users in a different workspace.

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | Caller's workspace | Target workspace |

## Examples

```bash
# List users in the current workspace
tg-list-users

# List users in a specific workspace
tg-list-users -w research-team

# Use a specific API endpoint
tg-list-users -u https://trustgraph.example.com:8088/
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-create-user`](tg-create-user) - Create a user
- [`tg-update-user`](tg-update-user) - Update user profile fields
- [`tg-whoami`](tg-whoami) - Show the authenticated caller's user record
- [`tg-disable-user`](tg-disable-user) - Disable a user
- [`tg-delete-user`](tg-delete-user) - Delete a user permanently
