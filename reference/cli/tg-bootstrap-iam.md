---
title: tg-bootstrap-iam
parent: CLI
review_date: 2027-05-21
---

# tg-bootstrap-iam

Bootstrap the IAM service and obtain the initial admin API key.

## Synopsis

```bash
tg-bootstrap-iam [options]
```

## Description

Bootstraps the IAM service by creating the initial admin user and API key. This command only works when `iam-svc` is running in bootstrap mode with empty tables. It prints the initial admin user ID and API key to stdout. This is a one-time, trust-sensitive operation -- once bootstrap has completed, running the command again will fail.

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8088/` | TrustGraph API URL |

## Examples

```bash
# Bootstrap the IAM service on a fresh deployment
tg-bootstrap-iam

# Bootstrap against a specific API endpoint
tg-bootstrap-iam -u https://trustgraph.example.com:8088/

# Capture the admin API key for later use
tg-bootstrap-iam | tee bootstrap-credentials.txt
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL

## Related Commands

- [`tg-login`](tg-login) - Log in with username and password
- [`tg-create-user`](tg-create-user) - Create a user
- [`tg-create-api-key`](tg-create-api-key) - Create an API key for a user
- [`tg-create-workspace`](tg-create-workspace) - Create a workspace
