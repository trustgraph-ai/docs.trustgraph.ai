---
title: Managing Users and Workspaces
parent: Managing operations
nav_order: 2
review_date: 2026-11-01
guide_category:
  - Managing operations
guide_category_order: 2
guide_description: Create and manage users, API keys, and workspaces using CLI tools
guide_difficulty: intermediate
guide_time: 15 min
guide_emoji: "\U0001F465"
guide_banner: banner.jpg
guide_labels:
  - IAM
  - Users
  - Workspaces
  - CLI
---

# Managing Users and Workspaces

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>A running TrustGraph deployment</li>
<li>TrustGraph CLI tools installed</li>
<li>Admin-level access (API key with admin role)</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Create and manage users, API keys, roles, and workspaces using command-line tools."
%}

## Authentication

All commands require a valid authentication token with admin privileges:

```bash
export TRUSTGRAPH_TOKEN="tg_my-admin-token"
```

## Users

### Check your identity

```bash
tg-whoami
```

### Create a user

Create a new user in the current workspace:

```bash
tg-create-user \
  --username alice \
  --name "Alice Smith" \
  --email alice@example.com \
  --roles writer
```

The command prints the new user ID.  If `--password` is omitted, you
will be prompted to enter one.

Available roles:
- `reader` — read-only access within the workspace
- `writer` — read/write access within the workspace
- `admin` — access across all workspaces

You can assign multiple roles:

```bash
tg-create-user \
  --username bob \
  --roles reader writer
```

### List users

```bash
tg-list-users
```

Admins can list users in a specific workspace:

```bash
tg-list-users -w my-workspace
```

### Update a user

Update profile fields, roles, or account status:

```bash
tg-update-user \
  --user-id <user-id> \
  --name "Alice Jones" \
  --roles reader writer
```

### Disable and enable users

Disabling a user prevents login and revokes all their API keys:

```bash
tg-disable-user --user-id <user-id>
```

Re-enable a previously disabled user:

```bash
tg-enable-user --user-id <user-id>
```

### Delete a user

Permanently delete a user and all their API keys:

```bash
tg-delete-user --user-id <user-id>
```

Add `--yes` to skip the confirmation prompt.

## Passwords

### Change your own password

```bash
tg-change-password
```

You will be prompted for your current and new passwords.

### Reset a user's password (admin)

Generate a one-time temporary password for a user:

```bash
tg-reset-password --user-id <user-id>
```

The temporary password is printed to stdout.  The user will be required
to change it on next login.

## API Keys

API keys are long-lived tokens with a `tg_` prefix, used for
programmatic access, CLI tools, and integrations.

### Create an API key

```bash
tg-create-api-key \
  --user-id <user-id> \
  --name "laptop"
```

The plaintext key is printed to stdout and shown only once — store it
securely.

Optionally set an expiry date:

```bash
tg-create-api-key \
  --user-id <user-id> \
  --name "ci-pipeline" \
  --expires 2026-12-31T23:59:59Z
```

### List API keys

```bash
tg-list-api-keys --user-id <user-id>
```

### Revoke an API key

```bash
tg-revoke-api-key --key-id <key-id>
```

## Workspaces

Workspaces provide data isolation — each workspace has its own
documents, knowledge graphs, collections, and users.  See
[Workspaces & Data Isolation](../../architecture/workspaces) for details.

### List workspaces

```bash
tg-list-workspaces
```

### Create a workspace

```bash
tg-create-workspace \
  --workspace-id research \
  --name "Research Team"
```

Workspace IDs must not start with `_`.

## Login

For interactive use, you can log in with username and password to obtain
a temporary JWT token:

```bash
tg-login --username alice
```

The JWT is printed to stdout.  You can use it directly:

```bash
export TRUSTGRAPH_TOKEN=$(tg-login --username alice)
```
