---
title: tg-list-workspaces
parent: CLI
review_date: 2027-05-21
---

# tg-list-workspaces

List workspaces (admin operation).

## Synopsis

```bash
tg-list-workspaces [options]
```

## Description

Lists all workspaces in the system. This is a system-level operation that requires admin privileges. Output is presented in a tabulated format showing each workspace's id, name, enabled status, and creation date.

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

```bash
# List all workspaces
tg-list-workspaces

# List workspaces from a specific endpoint
tg-list-workspaces -u https://trustgraph.example.com:8088/
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-create-workspace`](tg-create-workspace) - Create a workspace
- [`tg-create-user`](tg-create-user) - Create a user in a workspace
- [`tg-list-users`](tg-list-users) - List users in a workspace
