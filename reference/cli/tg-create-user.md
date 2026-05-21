---
title: tg-create-user
parent: CLI
review_date: 2027-05-21
---

# tg-create-user

Create a user in the caller's workspace.

## Synopsis

```bash
tg-create-user --username USER [options]
```

## Description

Creates a new user in the caller's workspace. The new user's ID is printed to stdout on success. A password is prompted interactively if not provided on the command line. Roles default to `reader` if not specified. The `--must-change-password` flag can be set to force the user to change their password on first login.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--username USERNAME` | Username for the new user |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `--password PASSWORD` | Prompted interactively | Password for the new user |
| `--name NAME` | None | Display name |
| `--email EMAIL` | None | Email address |
| `--roles ROLE [ROLE ...]` | `reader` | Roles to assign |
| `--must-change-password` | false | Force password change on first login |
| `-w, --workspace WORKSPACE` | Caller's workspace | Target workspace |

## Examples

```bash
# Create a user with default role (reader)
tg-create-user --username alice

# Create a user with full details
tg-create-user --username bob --name "Bob Smith" --email bob@example.com \
  --roles reader writer --password secret123

# Create a user who must change their password on first login
tg-create-user --username charlie --must-change-password

# Create a user in a specific workspace
tg-create-user --username dave -w research-team
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-list-users`](tg-list-users) - List users in the workspace
- [`tg-update-user`](tg-update-user) - Update user profile fields
- [`tg-disable-user`](tg-disable-user) - Disable a user
- [`tg-enable-user`](tg-enable-user) - Re-enable a disabled user
- [`tg-delete-user`](tg-delete-user) - Delete a user permanently
- [`tg-reset-password`](tg-reset-password) - Reset another user's password
