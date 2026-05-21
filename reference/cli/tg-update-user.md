---
title: tg-update-user
parent: CLI
review_date: 2027-05-21
---

# tg-update-user

Update a user's profile fields.

## Synopsis

```bash
tg-update-user --user-id ID [options]
```

## Description

Updates one or more profile fields for a user: name, email, roles, enabled status, and must-change-password flag. The username is immutable and cannot be changed. Only the fields provided on the command line are updated; omitted fields are left unchanged.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--user-id ID` | ID of the user to update |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `--name NAME` | Unchanged | Display name |
| `--email EMAIL` | Unchanged | Email address |
| `--roles ROLE [ROLE ...]` | Unchanged | Roles to assign |
| `--enabled yes/no` | Unchanged | Whether the user is enabled |
| `--must-change-password yes/no` | Unchanged | Force password change on next login |
| `-w, --workspace WORKSPACE` | Caller's workspace | Target workspace |

## Examples

```bash
# Update a user's display name and email
tg-update-user --user-id abc123 --name "Alice Johnson" --email alice@example.com

# Change a user's roles
tg-update-user --user-id abc123 --roles reader writer admin

# Disable a user via the update command
tg-update-user --user-id abc123 --enabled no

# Force a user to change their password
tg-update-user --user-id abc123 --must-change-password yes
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-create-user`](tg-create-user) - Create a user
- [`tg-list-users`](tg-list-users) - List users in the workspace
- [`tg-whoami`](tg-whoami) - Show the authenticated caller's user record
- [`tg-disable-user`](tg-disable-user) - Disable a user
- [`tg-enable-user`](tg-enable-user) - Re-enable a disabled user
- [`tg-delete-user`](tg-delete-user) - Delete a user permanently
