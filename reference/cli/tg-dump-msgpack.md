---
title: tg-dump-msgpack
parent: CLI
review_date: 2026-01-30
---

# tg-dump-msgpack

Reads and analyzes knowledge core files in MessagePack format for diagnostic purposes.

## Synopsis

```bash
tg-dump-msgpack -i INPUT_FILE [options]
```

## Description

The `tg-dump-msgpack` command is a diagnostic utility that reads knowledge core files stored in MessagePack format and outputs their contents in JSON format or provides a summary analysis. MessagePack is a binary serialization format that TrustGraph uses for efficient storage and transfer of knowledge graph data.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-i, --input-file FILE` | Input MessagePack file to read |

### Optional Arguments

| Option | Description |
|--------|-------------|
| `-s, --summary` | Show a summary analysis of the file contents |
| `-r, --records` | Dump individual records in JSON format (default) |

## Examples

### Dump Records as JSON
```bash
tg-dump-msgpack -i knowledge-core.msgpack
```

### Show Summary Analysis
```bash
tg-dump-msgpack -i knowledge-core.msgpack --summary
```

### Save Output to File
```bash
tg-dump-msgpack -i knowledge-core.msgpack > analysis.json
```

## Output Formats

### Record Output (Default)
Outputs each record as a separate JSON object:

```json
["t", {"m": {"m": [{"s": {"v": "uri1"}, "p": {"v": "predicate"}, "o": {"v": "object"}}]}}]
["ge", {"v": [[0.1, 0.2, 0.3, ...]]}]
["de", {"metadata": {...}, "chunks": [...]}]
```

### Summary Output
With `--summary`, the command provides an analytical overview:

```
Vector dimension: 384
- NASA Challenger Report
- Technical Documentation
- Safety Engineering Guidelines
```

## Related Commands

- [`tg-get-kg-core`](tg-get-kg-core) - Retrieve knowledge cores
- [`tg-show-kg-cores`](tg-show-kg-cores) - List available knowledge cores
- [`tg-graph-to-turtle`](tg-graph-to-turtle) - Convert graph to Turtle format

## API Integration

This command reads MessagePack files directly from the filesystem.
