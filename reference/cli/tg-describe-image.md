---
title: tg-describe-image
parent: CLI
review_date: 2027-08-24
---

# tg-describe-image

Generates a text description of an image using the image-to-text service.

## Synopsis

```bash
tg-describe-image -i IMAGE [options]
```

## Description

The `tg-describe-image` command sends an image file to the image-to-text service and returns a text description. The image MIME type is guessed from the filename unless explicitly specified. An optional prompt can be provided to guide the description, for example to ask specific questions about the image content.

## Options

### Required Arguments

| Option | Description |
|--------|-------------|
| `-i, --image IMAGE` | Image file to describe (e.g. `photo.jpg`) |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `-u, --url URL` | `$TRUSTGRAPH_URL` or `http://localhost:8888/` | TrustGraph API URL |
| `-t, --token TOKEN` | `$TRUSTGRAPH_TOKEN` | Authentication token |
| `-w, --workspace WORKSPACE` | `$TRUSTGRAPH_WORKSPACE` or `default` | Workspace identifier |
| `-f, --flow-id FLOW` | `default` | Flow identifier |
| `-p, --prompt PROMPT` | *(none)* | Prompt to guide the description (e.g. "What is shown in this image?") |
| `-s, --system SYSTEM` | *(none)* | System prompt to use |
| `--mime-type TYPE` | *(guessed from filename)* | Image MIME type (e.g. `image/jpeg`) |

## Examples

### Basic Image Description
```bash
tg-describe-image -i photo.jpg
```

### Guided Description with Prompt
```bash
tg-describe-image -i diagram.png \
  -p "Describe the architecture shown in this diagram"
```

### Explicit MIME Type
```bash
tg-describe-image -i data/image001 --mime-type image/png
```

### With System Prompt
```bash
tg-describe-image -i chart.png \
  -s "You are a data analyst" \
  -p "What trends are visible in this chart?"
```

## Environment Variables

- `TRUSTGRAPH_URL`: Default API URL
- `TRUSTGRAPH_TOKEN`: Default authentication token
- `TRUSTGRAPH_WORKSPACE`: Default workspace identifier

## Related Commands

- [`tg-invoke-llm`](tg-invoke-llm) - Invoke the text completion LLM directly
- [`tg-invoke-agent`](tg-invoke-agent) - Invoke the agent orchestrator
