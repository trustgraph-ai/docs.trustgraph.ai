---
title: tg-mint-token
parent: CLI
review_date: 2027-10-26
---

# tg-mint-token

Mint a JWT containing a caller-supplied user context.

## Synopsis

```bash
tg-mint-token -w WORKSPACE --user-context JSON (--user-id ID | --username NAME | --self) [options]
```

## Description

Admin operation that mints a JWT containing the specified user context. The resulting token can be used for testing policy-based query filtering or for service-to-service authentication with custom user context claims. Prints the JWT to stdout and the expiry time to stderr.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-w, --workspace WORKSPACE` | Target workspace for the minted token |
| `--user-context JSON` | User context as a JSON string |

### Subject (exactly one required)

| Option | Description |
|--------|-------------|
| `--user-id ID` | User ID (UUID) for the minted token's subject |
| `--username NAME` | Username to resolve to a user ID |
| `--self` | Mint token for the caller's own user ID |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --api-url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8888/` | API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Admin auth token (JWT or API key) |

## Examples

```bash
# Mint a token with security clearance context
tg-mint-token -w research --self \
  --user-context '{"clearance": "top-secret", "department": "cryptanalysis"}'

# Mint a token for a specific user
tg-mint-token -w production --username alice \
  --user-context '{"role": "analyst", "region": "EMEA"}'

# Use the minted token for a policy-filtered query
TOKEN=$(tg-mint-token -w default --self --user-context '{"level": "public"}')
tg-invoke-graph-rag -t "$TOKEN" -q "What projects are active?"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Admin authentication token

## Related Commands

- [`tg-login`](tg-login) - Log in to obtain a standard JWT
- [`tg-whoami`](tg-whoami) - Show the authenticated caller's user record
