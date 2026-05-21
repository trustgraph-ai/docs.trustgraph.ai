---
title: tg-delete-user
parent: CLI
review_date: 2027-05-21
---

# tg-delete-user

Delete a user permanently.

## Synopsis

```bash
tg-delete-user --user-id ID [options]
```

## Description

Permanently deletes a user, removing the user record, username lookup, and all associated API keys. This operation cannot be undone. An interactive confirmation prompt is displayed unless the `--yes` flag is provided.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--user-id ID` | ID of the user to delete |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | Caller's workspace | Target workspace |
| `--yes` | false | Skip interactive confirmation |

## Examples

```bash
# Delete a user (with confirmation prompt)
tg-delete-user --user-id abc123

# Delete a user without confirmation (for scripting)
tg-delete-user --user-id abc123 --yes

# Delete a user in a specific workspace
tg-delete-user --user-id abc123 -w research-team --yes
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-disable-user`](tg-disable-user) - Disable a user (soft-delete)
- [`tg-create-user`](tg-create-user) - Create a user
- [`tg-list-users`](tg-list-users) - List users in the workspace
- [`tg-update-user`](tg-update-user) - Update user profile fields
