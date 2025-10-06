---
title: tg-set-collection
layout: default
parent: CLI
---

# tg-set-collection

Create or update collection metadata.

## Synopsis

```bash
tg-set-collection COLLECTION [options]
```

## Description

The `tg-set-collection` command creates a new collection or updates the metadata of an existing collection. Collections are used to organize and isolate data within TrustGraph, allowing multiple users and projects to maintain separate data spaces.

If the collection doesn't exist, it will be created. If it exists, the specified metadata fields will be updated.

## Arguments

### Required Arguments

- `COLLECTION`: Collection ID to create or update

### Optional Arguments

- `-u, --api-url URL`: TrustGraph API URL (default: `$TRUSTGRAPH_URL` or `http://localhost:8088/`)
- `-U, --user USER`: User ID (default: `trustgraph`)
- `-n, --name NAME`: Human-readable collection name
- `-d, --description DESCRIPTION`: Detailed description of the collection
- `-t, --tag TAG`: Collection tag (can be specified multiple times)

## Examples

### Create New Collection with Full Metadata
```bash
tg-set-collection research \
  -n "Research Project" \
  -d "Medical research document analysis" \
  -t research \
  -t medical
```

### Update Existing Collection Description
```bash
tg-set-collection research \
  -d "Updated: Medical and climate research documents"
```

### Add Tags to Collection
```bash
tg-set-collection research \
  -t research \
  -t medical \
  -t priority
```

### Create Collection for Specific User
```bash
tg-set-collection customer-data \
  -U alice \
  -n "Alice's Data" \
  -d "Customer-specific data collection"
```

### Minimal Collection Creation
```bash
tg-set-collection myproject
```

## Output Format

On successful operation, the command displays a confirmation message and metadata table:

```
Collection 'research' set successfully.
+--------------+---------------------------------------+
| Collection   | research                              |
| Name         | Research Project                      |
| Description  | Medical research document analysis    |
| Tags         | research, medical                     |
| Updated      | 2024-01-20 14:45:00                   |
+--------------+---------------------------------------+
```

## Use Cases

### Project Setup
```bash
# Create collection for new research project
tg-set-collection climate-2024 \
  -n "Climate Research 2024" \
  -d "Climate change research and analysis" \
  -t research \
  -t climate \
  -t 2024
```

### Multi-Tenant Configuration
```bash
# Set up collections for different customers
tg-set-collection acme-corp \
  -U customer-acme \
  -n "ACME Corporation" \
  -d "ACME Corp knowledge base"

tg-set-collection widgets-inc \
  -U customer-widgets \
  -n "Widgets Inc" \
  -d "Widgets Inc documentation"
```

### Collection Organization
```bash
# Organize collections by environment
tg-set-collection prod-main \
  -n "Production Main" \
  -d "Primary production data" \
  -t production

tg-set-collection dev-testing \
  -n "Development Testing" \
  -d "Development and testing data" \
  -t development
```

### Metadata Updates
```bash
# Add new tags to existing collection
tg-set-collection research \
  -t archive \
  -t completed

# Update description
tg-set-collection research \
  -d "Archived: Medical research document analysis (completed 2024)"
```

## Collection Metadata

Collection metadata includes:

- **Collection ID**: Unique identifier (specified as argument)
- **Name**: Human-readable name for display
- **Description**: Detailed explanation of collection purpose
- **Tags**: List of tags for categorization and filtering
- **Timestamps**: Created and updated timestamps (managed automatically)

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL

## Error Handling

### Connection Errors
```bash
Exception: Connection refused
```
**Solution**: Verify the API URL and ensure TrustGraph is running.

### Invalid Collection ID
```bash
Exception: Invalid collection ID format
```
**Solution**: Collection IDs should contain only alphanumeric characters, hyphens, and underscores.

## Related Commands

- [`tg-list-collections`](tg-list-collections) - List collections and their metadata
- [`tg-delete-collection`](tg-delete-collection) - Delete a collection and its data
- [`tg-load-knowledge`](tg-load-knowledge) - Load data into a specific collection

## API Integration

This command uses the [Collection Management API](../apis/api-collection) with the `update-collection` operation.

## Notes

- Collections are user-scoped; each user has their own namespace
- Metadata is optional but recommended for organization
- Tags can be used for filtering with `tg-list-collections`
- If a collection exists, only specified fields are updated; others remain unchanged
- The command creates collections implicitly if they don't exist

## Best Practices

1. **Use Descriptive IDs**: Choose meaningful collection IDs that indicate purpose
2. **Provide Clear Names**: Use human-readable names for better usability
3. **Document Purpose**: Always include descriptions explaining collection usage
4. **Tag Consistently**: Use consistent tagging schemes across your organization
5. **Plan Hierarchy**: Consider using prefixes for related collections (e.g., `prod-*`, `dev-*`)
6. **Review Regularly**: Update metadata as collection purposes evolve
