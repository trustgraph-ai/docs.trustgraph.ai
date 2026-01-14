---
title: tg-show-flow-blueprintes
parent: CLI
review_date: 2026-03-11
---

# tg-show-flow-blueprintes

Lists all defined flow blueprintes in TrustGraph with their descriptions and tags.

## Synopsis

```bash
tg-show-flow-blueprintes [options]
```

## Description

The `tg-show-flow-blueprintes` command displays a formatted table of all flow blueprint definitions currently stored in TrustGraph. Each flow blueprint is shown with its name, description, and associated tags.

Flow blueprintes are templates that define the structure and services available for creating flow instances. This command helps you understand what flow blueprintes are available for use.

**New in v1.4**: The command now displays configurable parameters for each flow blueprint, including their types and default values.

## Options

### Optional Arguments

- `-u, --api-url URL`: TrustGraph API URL (default: `$TRUSTGRAPH_URL` or `http://localhost:8088/`)

## Examples

### List All Flow Classes
```bash
tg-show-flow-blueprintes
```

Output:
```
+-------------------+----------------------------------+----------------------+
| name              | document-proc                    |
| description       | Document processing pipeline     |
| tags              | production, nlp                  |
| parameters        |   model: LLM model [llm-model (default: gpt-4)] |
|                   |   temperature: Response creativity [temperature (default: 0.7)] |
+-------------------+----------------------------------+----------------------+

+-------------------+----------------------------------+
| name              | data-analysis                    |
| description       | Data analysis and visualization  |
| tags              | analytics, dev                   |
| parameters        |   chunk-size: Text chunking size [chunk-size (default: 1000)] |
+-------------------+----------------------------------+----------------------+
```

### Using Custom API URL
```bash
tg-show-flow-blueprintes -u http://production:8088/
```

### Filter Flow Classes
```bash
# Show only production-tagged flow blueprintes
tg-show-flow-blueprintes | grep "production"

# Count total flow blueprintes
tg-show-flow-blueprintes | grep -c "^|"

# Show flow blueprintes with specific patterns
tg-show-flow-blueprintes | grep -E "(document|text|nlp)"
```

## Output Format

The command displays results in a formatted table with columns:

- **name**: The unique name/identifier of the flow blueprint
- **description**: Human-readable description of the flow blueprint purpose
- **tags**: Comma-separated list of categorization tags
- **parameters**: Configurable parameters with types and defaults (new in v1.4)

### Parameter Information (New in v1.4)

Parameters are displayed with:
- Parameter name and description
- Parameter type reference
- Default value from parameter type definition

Format: `  param-name: Description [param-type (default: value)]`

### Empty Results
If no flow blueprintes exist:
```
No flow blueprintes.
```

## Use Cases

### Flow Class Discovery
```bash
# Find available flow blueprintes for document processing
tg-show-flow-blueprintes | grep -i document

# List all AI-related flow blueprintes
tg-show-flow-blueprintes | grep -i "ai\|nlp\|chat\|assistant"

# Find development vs production flow blueprintes
tg-show-flow-blueprintes | grep -E "(dev|test|staging)"
tg-show-flow-blueprintes | grep "production"
```

### Flow Class Management
```bash
# Get list of flow blueprint names for scripting
tg-show-flow-blueprintes | awk 'NR>3 && /^\|/ {gsub(/[| ]/, "", $2); print $2}' | grep -v "^$"

# Check if specific flow blueprint exists
if tg-show-flow-blueprintes | grep -q "target-flow"; then
    echo "Flow blueprint 'target-flow' exists"
else
    echo "Flow blueprint 'target-flow' not found"
fi
```

### Environment Comparison
```bash
# Compare flow blueprintes between environments
echo "Development environment:"
tg-show-flow-blueprintes -u http://dev:8088/

echo "Production environment:"
tg-show-flow-blueprintes -u http://prod:8088/
```

### Reporting and Documentation
```bash
# Generate flow blueprint inventory report
echo "Flow Class Inventory - $(date)" > flow-inventory.txt
echo "=====================================" >> flow-inventory.txt
tg-show-flow-blueprintes >> flow-inventory.txt

# Create CSV export
echo "flow_class,description,tags" > flow-blueprintes.csv
tg-show-flow-blueprintes | awk 'NR>3 && /^\|/ {
    gsub(/^\| */, "", $0); gsub(/ *\|$/, "", $0); 
    gsub(/ *\| */, ",", $0); print $0
}' >> flow-blueprintes.csv
```

## Error Handling

### Connection Errors
```bash
Exception: Connection refused
```
**Solution**: Check the API URL and ensure TrustGraph is running.

### Permission Errors
```bash
Exception: Access denied to list flow blueprintes
```
**Solution**: Verify user permissions for reading flow blueprint definitions.

### Network Timeouts
```bash
Exception: Request timeout
```
**Solution**: Check network connectivity and API server status.

## Integration with Other Commands

### Flow Class Lifecycle
```bash
# 1. List available flow blueprintes
tg-show-flow-blueprintes

# 2. Get details of specific flow blueprint
tg-get-flow-blueprint -n "interesting-flow"

# 3. Start flow instance from class
tg-start-flow -n "interesting-flow" -i "my-instance"

# 4. Monitor flow instance
tg-show-flows | grep "my-instance"
```

### Bulk Operations
```bash
# Process all flow blueprintes
tg-show-flow-blueprintes | awk 'NR>3 && /^\|/ {gsub(/[| ]/, "", $2); if($2) print $2}' | \
while read class_name; do
    if [ -n "$class_name" ]; then
        echo "Processing flow blueprint: $class_name"
        tg-get-flow-blueprint -n "$class_name" > "backup-$class_name.json"
    fi
done
```

### Automated Validation
```bash
# Check flow blueprint health
echo "Validating flow blueprintes..."
tg-show-flow-blueprintes | awk 'NR>3 && /^\|/ {gsub(/[| ]/, "", $2); if($2) print $2}' | \
while read class_name; do
    if [ -n "$class_name" ]; then
        echo -n "Checking $class_name... "
        if tg-get-flow-blueprint -n "$class_name" > /dev/null 2>&1; then
            echo "OK"
        else
            echo "ERROR"
        fi
    fi
done
```

## Advanced Usage

### Flow Class Analysis
```bash
# Analyze flow blueprint distribution by tags
tg-show-flow-blueprintes | awk 'NR>3 && /^\|/ {
    # Extract tags column
    split($0, parts, "|"); 
    tags = parts[4]; 
    gsub(/^ *| *$/, "", tags);
    if (tags) {
        split(tags, tag_array, ",");
        for (i in tag_array) {
            gsub(/^ *| *$/, "", tag_array[i]);
            if (tag_array[i]) print tag_array[i];
        }
    }
}' | sort | uniq -c | sort -nr
```

### Environment Synchronization
```bash
# Sync flow blueprintes between environments
echo "Synchronizing flow blueprintes from dev to staging..."

# Get list from development
dev_classes=$(tg-show-flow-blueprintes -u http://dev:8088/ | \
  awk 'NR>3 && /^\|/ {gsub(/[| ]/, "", $2); if($2) print $2}')

# Check each class in staging
for class in $dev_classes; do
    if tg-show-flow-blueprintes -u http://staging:8088/ | grep -q "$class"; then
        echo "$class: Already exists in staging"
    else
        echo "$class: Missing in staging - needs sync"
        # Get from dev and put to staging
        tg-get-flow-blueprint -n "$class" -u http://dev:8088/ > temp-class.json
        tg-put-flow-blueprint -n "$class" -c "$(cat temp-class.json)" -u http://staging:8088/
        rm temp-class.json
    fi
done
```

### Monitoring Script
```bash
#!/bin/bash
# monitor-flow-blueprintes.sh
api_url="${1:-http://localhost:8088/}"

echo "Flow Class Monitoring Report - $(date)"
echo "API URL: $api_url"
echo "----------------------------------------"

# Total count
total=$(tg-show-flow-blueprintes -u "$api_url" | grep -c "^|" 2>/dev/null || echo "0")
echo "Total flow blueprintes: $((total - 3))"  # Subtract header rows

# Tag analysis
echo -e "\nTag distribution:"
tg-show-flow-blueprintes -u "$api_url" | awk 'NR>3 && /^\|/ {
    split($0, parts, "|"); 
    tags = parts[4]; 
    gsub(/^ *| *$/, "", tags);
    if (tags) {
        split(tags, tag_array, ",");
        for (i in tag_array) {
            gsub(/^ *| *$/, "", tag_array[i]);
            if (tag_array[i]) print tag_array[i];
        }
    }
}' | sort | uniq -c | sort -nr

# Health check
echo -e "\nHealth check:"
healthy=0
unhealthy=0
tg-show-flow-blueprintes -u "$api_url" | awk 'NR>3 && /^\|/ {gsub(/[| ]/, "", $2); if($2) print $2}' | \
while read class_name; do
    if [ -n "$class_name" ]; then
        if tg-get-flow-blueprint -n "$class_name" -u "$api_url" > /dev/null 2>&1; then
            healthy=$((healthy + 1))
        else
            unhealthy=$((unhealthy + 1))
            echo "  ERROR: $class_name"
        fi
    fi
done

echo "Healthy: $healthy, Unhealthy: $unhealthy"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL

## Related Commands

- [`tg-get-flow-blueprint`](tg-get-flow-blueprint) - Retrieve specific flow blueprint definitions
- [`tg-put-flow-blueprint`](tg-put-flow-blueprint) - Create/update flow blueprint definitions
- [`tg-delete-flow-blueprint`](tg-delete-flow-blueprint) - Delete flow blueprint definitions
- [`tg-start-flow`](tg-start-flow) - Create flow instances from classes
- [`tg-show-flows`](tg-show-flows) - List active flow instances

## API Integration

This command uses the [Flow API](../apis/api-flow) with the `list-blueprints` operation to retrieve flow blueprint listings.

## Best Practices

1. **Regular Inventory**: Periodically review available flow blueprintes
2. **Documentation**: Ensure flow blueprintes have meaningful descriptions
3. **Tagging**: Use consistent tagging for better organization
4. **Cleanup**: Remove unused or deprecated flow blueprintes
5. **Monitoring**: Include flow blueprint health checks in monitoring
6. **Environment Parity**: Keep flow blueprintes synchronized across environments

## Troubleshooting

### No Output
```bash
# If command returns no output, check API connectivity
tg-show-flow-blueprintes -u http://localhost:8088/
# Verify TrustGraph is running and accessible
```

### Formatting Issues
```bash
# If table formatting is broken, check terminal width
export COLUMNS=120
tg-show-flow-blueprintes
```

### Missing Flow Classes
```bash
# If expected flow blueprintes are missing, verify:
# 1. Correct API URL
# 2. Database connectivity
# 3. Flow blueprint definitions are properly stored
```
