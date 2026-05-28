---
title: tg-create-workspace
parent: CLI
review_date: 2027-05-21
---

# tg-create-workspace

Create a workspace (admin operation).

## Synopsis

```bash
tg-create-workspace --workspace-id ID [options]
```

## Description

Creates a new workspace in the system. This is a system-level operation that requires admin privileges. The workspace ID must not start with an underscore (`_`). An optional display name can be provided.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--workspace-id ID` | Workspace identifier (must not start with `_`) |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `--name NAME` | None | Display name for the workspace |

## Examples

```bash
# Create a workspace
tg-create-workspace --workspace-id research-team

# Create a workspace with a display name
tg-create-workspace --workspace-id research-team --name "Research Team"

# Create a workspace and then add a user to it
tg-create-workspace --workspace-id dev-team --name "Development Team"
tg-create-user --username alice -w dev-team
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-list-workspaces`](tg-list-workspaces) - List workspaces
- [`tg-create-user`](tg-create-user) - Create a user in a workspace
- [`tg-list-users`](tg-list-users) - List users in a workspace
- [`tg-bootstrap-iam`](tg-bootstrap-iam) - Bootstrap the IAM service
