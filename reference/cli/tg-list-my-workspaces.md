---
title: tg-list-my-workspaces
parent: CLI
review_date: 2027-10-26
---

# tg-list-my-workspaces

List workspaces the current user has access to.

## Synopsis

```bash
tg-list-my-workspaces [options]
```

## Description

Lists all workspaces that the authenticated user has been granted access to. Unlike `tg-list-workspaces` (which is an admin operation listing all workspaces), this command is available to any authenticated user and shows only their own workspaces.

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8888/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

```bash
# List my workspaces
tg-list-my-workspaces

# List workspaces from a specific deployment
tg-list-my-workspaces -u https://trustgraph.example.com:8888/
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-list-workspaces`](tg-list-workspaces) - List all workspaces (admin)
- [`tg-create-workspace`](tg-create-workspace) - Create a workspace
