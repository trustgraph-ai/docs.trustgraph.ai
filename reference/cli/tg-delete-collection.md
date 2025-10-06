---
title: tg-delete-collection
layout: default
parent: CLI
---

# tg-delete-collection

Delete a collection and all its data.

## Synopsis

```bash
tg-delete-collection COLLECTION [options]
```

## Description

The `tg-delete-collection` command permanently deletes a collection and all associated data from TrustGraph. This includes documents, embeddings, knowledge graph triples, and any other data stored within the collection.

**Warning**: This operation is irreversible. All data in the collection will be permanently lost.

## Arguments

### Required Arguments

- `COLLECTION`: Collection ID to delete

### Optional Arguments

- `-u, --api-url URL`: TrustGraph API URL (default: `$TRUSTGRAPH_URL` or `http://localhost:8088/`)
- `-U, --user USER`: User ID (default: `trustgraph`)
- `-y, --yes`: Skip confirmation prompt

## Examples

### Delete Collection with Confirmation
```bash
tg-delete-collection old-research
```

The command will prompt for confirmation:
```
Are you sure you want to delete collection 'old-research' and all its data? (y/N):
```

### Delete Collection Without Confirmation
```bash
tg-delete-collection old-research -y
```

### Delete Collection for Specific User
```bash
tg-delete-collection customer-data -U alice -y
```

### Using Custom API URL
```bash
tg-delete-collection temp-data \
  -u http://production:8088/ \
  -y
```

## Output Format

### Successful Deletion
```
Collection 'old-research' deleted successfully.
```

### Cancelled Operation
```
Operation cancelled.
```

## Interactive Confirmation

By default, the command prompts for confirmation before deletion:

```
Are you sure you want to delete collection 'old-research' and all its data? (y/N):
```

Valid confirmation responses:
- `y` or `yes` (case-insensitive) - Proceed with deletion
- Any other input - Cancel operation

Use the `-y/--yes` flag to skip this prompt for automated scripts.

## What Gets Deleted

When you delete a collection, the following data is permanently removed:

- **Collection Metadata**: Name, description, tags, timestamps
- **Documents**: All documents loaded into the collection
- **Embeddings**: Document and graph embeddings
- **Knowledge Graph Data**: Triples, entities, relationships
- **Structured Data**: Any objects stored in the collection
- **Processing History**: All processing logs and metadata

## Use Cases

### Cleanup Development Collections
```bash
# Delete temporary testing collection
tg-delete-collection dev-testing -y
```

### Remove Completed Projects
```bash
# Archive and delete completed research project
# (assuming data has been backed up externally)
tg-delete-collection research-2023 -y
```

### Multi-Tenant Management
```bash
# Remove customer collection after contract end
tg-delete-collection customer-acme -U customer-acme -y
```

### Automated Cleanup Scripts
```bash
#!/bin/bash
# Delete all collections with specific tag
for collection in $(tg-list-collections -t temporary | tail -n +4 | awk '{print $2}'); do
    tg-delete-collection "$collection" -y
done
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL

## Error Handling

### Collection Not Found
```bash
Exception: Collection 'invalid-name' not found
```
**Solution**: Verify the collection ID with `tg-list-collections`.

### Permission Errors
```bash
Exception: Permission denied
```
**Solution**: Ensure you're deleting a collection owned by your user.

### Connection Errors
```bash
Exception: Connection refused
```
**Solution**: Verify the API URL and ensure TrustGraph is running.

## Safety Considerations

### Before Deletion

1. **Verify Collection**: Use `tg-list-collections` to confirm the collection ID
2. **Check Contents**: Review what data will be lost
3. **Backup Data**: Export important data before deletion
4. **Consider Alternatives**: Consider archiving instead of deleting
5. **Coordinate with Team**: Ensure no one is using the collection

### Backup Options

```bash
# Export knowledge graph data before deletion
tg-get-kg-core -U alice -c research > research-backup.ttl

# Export document embeddings
tg-save-doc-embeds -U alice -c research -f research-embeddings.json
```

## Related Commands

- [`tg-list-collections`](tg-list-collections) - List collections to verify before deletion
- [`tg-set-collection`](tg-set-collection) - Create or update collection metadata
- [`tg-get-kg-core`](tg-get-kg-core) - Export knowledge graph data before deletion
- [`tg-save-doc-embeds`](tg-save-doc-embeds) - Export document embeddings before deletion

## API Integration

This command uses the [Collection Management API](../apis/api-collection) with the `delete-collection` operation.

## Notes

- Deletion is permanent and cannot be undone
- The operation deletes all data across all TrustGraph storage systems
- Collection metadata is removed from the system
- Other users' collections are not affected
- The deletion is atomic - either all data is deleted or none

## Best Practices

1. **Always Backup**: Export important data before deletion
2. **Use Confirmation**: Avoid using `-y` flag unless in automated scripts
3. **Verify First**: Double-check collection ID with `tg-list-collections`
4. **Document Deletion**: Keep records of what was deleted and when
5. **Test in Development**: Test deletion scripts in development first
6. **Coordinate**: Notify team members before deleting shared collections
7. **Consider Archiving**: For historical data, consider archiving over deletion
8. **Audit Trail**: Maintain logs of collection deletions for compliance
