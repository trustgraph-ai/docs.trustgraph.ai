---
title: tg-login
parent: CLI
review_date: 2027-05-21
---

# tg-login

Log in with username and password to obtain a JWT.

## Synopsis

```bash
tg-login --username USER [options]
```

## Description

Authenticates with the TrustGraph IAM service using a username and password. On success, the resulting JWT is printed to stdout and the token expiry time is printed to stderr. The password is prompted interactively if not provided on the command line. An optional workspace can be specified to override the user's default workspace assignment.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `--username USERNAME` | Username to authenticate with |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |
| `--password PASSWORD` | Prompted interactively | User's password |
| `-w, --workspace WORKSPACE` | User's assigned workspace | Workspace to log in to |

## Examples

```bash
# Log in interactively (password prompted)
tg-login --username admin

# Log in and capture the token
export TRUSTGRAPH_TOKEN=$(tg-login --username admin --password secret)

# Log in to a specific workspace
tg-login --username admin -w my-workspace
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Set this to the output of `tg-login` for subsequent commands

## Related Commands

- [`tg-bootstrap-iam`](tg-bootstrap-iam) - Bootstrap the IAM service
- [`tg-whoami`](tg-whoami) - Show the authenticated caller's user record
- [`tg-change-password`](tg-change-password) - Change your own password
- [`tg-create-api-key`](tg-create-api-key) - Create a long-lived API key
