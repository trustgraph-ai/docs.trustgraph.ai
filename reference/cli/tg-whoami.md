---
title: tg-whoami
parent: CLI
review_date: 2027-05-21
---

# tg-whoami

Show the authenticated caller's own user record.

## Synopsis

```bash
tg-whoami [options]
```

## Description

Displays the user record associated with the current authentication token. Shows the user's id, username, name, email, workspace, roles, enabled status, must-change-password flag, and creation timestamp.

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |

## Examples

```bash
# Show your own user record
tg-whoami

# Verify a token against a specific API
tg-whoami -u https://trustgraph.example.com:8088/

# Use an explicit token
tg-whoami -t eyJhbGciOiJIUzI1NiIs...
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-login`](tg-login) - Log in with username and password
- [`tg-update-user`](tg-update-user) - Update user profile fields
- [`tg-change-password`](tg-change-password) - Change your own password
- [`tg-list-users`](tg-list-users) - List users in the workspace
