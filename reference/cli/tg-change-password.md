---
title: tg-change-password
parent: CLI
review_date: 2027-05-21
---

# tg-change-password

Change your own password.

## Synopsis

```bash
tg-change-password [options]
```

## Description

Changes the password for the currently authenticated user. Both the current password and new password are required. If not provided on the command line, they are prompted interactively.

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `--current PASSWORD` | Prompted interactively | Current password |
| `--new PASSWORD` | Prompted interactively | New password |

## Examples

```bash
# Change password interactively (both passwords prompted)
tg-change-password

# Change password non-interactively
tg-change-password --current oldpass123 --new newpass456
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Authentication token

## Related Commands

- [`tg-login`](tg-login) - Log in with username and password
- [`tg-reset-password`](tg-reset-password) - Admin: reset another user's password
- [`tg-whoami`](tg-whoami) - Show the authenticated caller's user record
