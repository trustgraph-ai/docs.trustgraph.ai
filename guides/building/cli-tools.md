---
title: Introduction to command-line tools
nav_order: 2.2
parent: How-to Guides
grand_parent: TrustGraph Documentation
review_date: 2026-08-01
guide_category:
  - Building with TrustGraph
guide_category_order: 2
guide_description: Learn to use TrustGraph command-line tools for document processing and knowledge graph operations
guide_difficulty: beginner
guide_time: 5 min
guide_emoji: 💻
guide_banner: /../cli.jpg
guide_labels:
  - CLI
  - Command-line
---

# Getting started with TrustGraph command-line tools

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>A running TrustGraph deployment</li>
<li>Basic command-line familiarity</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Learn to use TrustGraph command-line tools for common tasks and automation."
%}

## Command-line tools installation

The TrustGraph CLI tools are provided in the `trustgraph-cli` Python package.

The CLI tools version should match your deployed TrustGraph version. Check your deployment version and install the corresponding CLI version.

{% capture pip_install_version %}
```bash
pip install trustgraph-cli==1.8.10
```
{% endcapture %}

{% capture uv_install_version %}
```bash
uv pip install trustgraph-cli==1.8.10
```
{% endcapture %}

{% capture poetry_install_version %}
```bash
poetry add trustgraph-cli@1.8.10
```
{% endcapture %}

{% include code_tabs.html
   tabs="pip,uv,poetry"
   content1=pip_install_version
   content2=uv_install_version
   content3=poetry_install_version
%}

## Common CLI arguments

Most TrustGraph CLI tools accept these common arguments:

- `-u, --api-url API_URL` - API URL (default: `http://localhost:8088/`)
- `-t, --token TOKEN` - Authentication token (default: `$TRUSTGRAPH_TOKEN` environment variable)

Example using custom API URL:
```bash
tg-show-flows -u http://my-trustgraph-host:8088/
```

Example using authentication token:
```bash
export TRUSTGRAPH_TOKEN="your-token-here"
tg-show-flows
```

Or pass the token directly:
```bash
tg-show-flows -t "your-token-here"
```

The deployment patterns used in the deployment access the TrustGraph cluster
at `localhost`.  Docker/Podman compose expose internal service ports on
`localhost`, and the Kubernetes port-forward commands also expose services
on `localhost`.  In this configuration, the default works, and the URL does
not need to be specified.

If an API gateway key is provisioned when the system is deployed, this needs
to be specified with command-line tools in order to authenticate.  If no
gateway key is provided, then no token needs to be provided.

## Example commands

Here are a few key commands to get started:

**View running flows:**
```bash
tg-show-flows
```

Shows all active processing flows with their configurations.

**List documents in the library:**
```bash
tg-show-library-documents
```

Displays all documents that have been added to the library.

**Query the LLM directly:**
```bash
tg-invoke-llm "You are a helpful assistant" "What is 2+2?"
```

Sends a direct request to the LLM.

**Query using Graph RAG:**
```bash
tg-invoke-graph-rag -q "Tell me about cats"
```

Retrieves relevant knowledge graph information to answer questions.

For detailed documentation on these and many more commands, see [Command-line document management](document-management-cli).
