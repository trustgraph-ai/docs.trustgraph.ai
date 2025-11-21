---
title: tg-list-collections
parent: CLI
review_date: 2025-12-20
---

# tg-list-collections

List collections for a user with their metadata.

## Synopsis

```bash
tg-list-collections [options]
```

## Description

The `tg-list-collections` command displays all collections associated with a user, showing their metadata including names, descriptions, tags, and timestamps. Collections are used to organize and isolate data within TrustGraph, allowing multiple users and projects to maintain separate data spaces.

## Options

- `-u, --api-url URL`: TrustGraph API URL (default: `$TRUSTGRAPH_URL` or `http://localhost:8088/`)
- `-U, --user USER`: User ID (default: `trustgraph`)
- `-t, --tag-filter TAG`: Filter by tags (can be specified multiple times)

## Examples

### List All Collections for Default User
```bash
tg-list-collections
```

### List Collections for Specific User
```bash
tg-list-collections -U alice
```

### Filter Collections by Tag
```bash
tg-list-collections -t research
```

### Filter by Multiple Tags
```bash
tg-list-collections -t research -t medical
```

### Using Custom API URL
```bash
tg-list-collections -u http://production:8088/ -U production-user
```

## Output Format

The command displays collections in a formatted table:

```
+------------+------------------+------------------------+------------+---------------------+---------------------+
| Collection | Name             | Description            | Tags       | Created             | Updated             |
+------------+------------------+------------------------+------------+---------------------+---------------------+
| research   | Research Project | Medical research docs  | research   | 2024-01-15 10:30:00 | 2024-01-20 14:45:00 |
| default    | Default          | Default collection     | default    | 2024-01-01 00:00:00 | 2024-01-01 00:00:00 |
+------------+------------------+------------------------+------------+---------------------+---------------------+
```

### No Collections Available
```bash
No collections found.
```

## Collection Fields

Each collection displays the following information:

- **Collection**: Unique collection identifier
- **Name**: Human-readable name
- **Description**: Detailed description of the collection's purpose
- **Tags**: Comma-separated list of tags for categorization
- **Created**: Timestamp when collection was created
- **Updated**: Timestamp of last update

## Use Cases

### Project Management
```bash
# List all research collections
tg-list-collections -t research

# Check collections for a specific team
tg-list-collections -U data-science-team
```

### Multi-Tenant Environments
```bash
# List collections for each customer
tg-list-collections -U customer-a
tg-list-collections -U customer-b
```

### Collection Discovery
```bash
# Find all collections tagged as production
tg-list-collections -t production

# List collections for audit
tg-list-collections -U admin > collections-audit.txt
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL

## Related Commands

- [`tg-set-collection`](tg-set-collection) - Create or update collection metadata
- [`tg-delete-collection`](tg-delete-collection) - Delete a collection and its data
- [`tg-load-knowledge`](tg-load-knowledge) - Load data into a specific collection

## API Integration

This command uses the [Collection Management API](../apis/api-collection) with the `list-collections` operation.

## Notes

- Collections are user-scoped; each user has their own set of collections
- Tag filtering uses AND logic when multiple tags are specified
- Timestamps are displayed in ISO format
- The default user is "trustgraph" if not specified

## Best Practices

1. **Use Descriptive Names**: Assign meaningful names to collections for easy identification
2. **Tag Consistently**: Use consistent tagging schemes across your organization
3. **Regular Audits**: Periodically review collections to identify unused ones
4. **Document Purpose**: Use clear descriptions to explain collection purposes
5. **User Separation**: Use different users for different teams or projects
