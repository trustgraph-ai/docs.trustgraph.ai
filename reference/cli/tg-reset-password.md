---
title: tg-reset-password
parent: CLI
review_date: 2027-05-21
---

# tg-reset-password

Reset another user's password (admin operation).

## Synopsis

```bash
tg-reset-password --user-id ID [options]
```

## Description

Resets a user's password to a one-time temporary password, which is printed to stdout. The user is forced to change this temporary password on their next login. This is an administrative operation intended for account recovery or onboarding.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--user-id ID` | ID of the user whose password to reset |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | Caller's workspace | Target workspace |

## Examples

```bash
# Reset a user's password
tg-reset-password --user-id abc123

# Reset and communicate the temporary password
TEMP_PASS=$(tg-reset-password --user-id abc123)
echo "Temporary password: $TEMP_PASS"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-change-password`](tg-change-password) - Change your own password
- [`tg-create-user`](tg-create-user) - Create a user
- [`tg-update-user`](tg-update-user) - Update user profile fields
- [`tg-list-users`](tg-list-users) - List users in the workspace
