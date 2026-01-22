---
title: Getting Started with Development
parent: Contributing
nav_order: 2
review_date: 2026-08-01
guide_category:
  - Contributing
guide_banner: beginning.jpg
guide_category_order: 2
guide_description: First-time developer guide — run, build, modify, and test TrustGraph locally
guide_difficulty: intermediate
guide_time: 30 min
guide_emoji: 🛠️
guide_labels:
  - Development
  - Setup
  - Building
---

# Getting Started with Development

This guide walks first-time developers through running TrustGraph, building from source, making changes, and testing them locally.

## Prerequisites

- **Python 3.13** (3.14 may work)
- **Docker** or **Podman** with Compose
- **Git**
- Other development tools as needed

## Step 1: Run TrustGraph

Before developing, get a working TrustGraph instance running locally. The easiest approach is Docker/Podman Compose.

1. Use the [Configuration UI](https://config-ui.demo.trustgraph.ai) to generate a `docker-compose.yaml` for your setup
2. Launch the system:
   ```bash
   docker-compose up -d
   ```
3. Verify it's running — check the Workbench UI or run a simple query

See [Local Deployment](../deployment/) for detailed instructions.

## Step 2: Clone and Set Up the Repository

```bash
git clone https://github.com/trustgraph-ai/trustgraph.git
cd trustgraph

# Check out the latest release branch (not main)
git checkout release/v1.8

# Create a Python virtual environment
python3 -m venv env
source env/bin/activate
```

## Step 3: Build the Packages

Update package versions to match your release branch, then build.
Replace 1.8.0 with the *exact* version of TrustGraph you are running.

```bash
make update-package-versions VERSION=1.8.0
```

This creates Python packages under `dist/`. Install them to your environment:

```bash
pip install ./trustgraph-base
pip install ./trustgraph-cli
pip install ./trustgraph-flow
```

Verify the CLI works:

```bash
tg-show-processor-state --help
```

## Step 4: Build the Containers

Build container images locally:

```bash
make container VERSION=1.8.0
```

This builds all TrustGraph containers with your local code. Use the same version number as your `docker-compose.yaml` expects.

## Step 5: Launch Your Local Build

Stop any running TrustGraph instance and relaunch with your
locally-built containers.  This performs a complete wipe and restart:

```bash
docker-compose down -v -t 0
docker-compose up -d
```

Verify the system starts correctly and the Workbench UI is accessible.

## Step 6: Make a Change

Let's make a simple change to verify the build-test cycle works. We'll
modify a log message in a processor.

Edit a file — for example, add a log line to a processor's startup:

```python
# In trustgraph-flow/trustgraph/flow/some_processor.py
log.info("Hello from my local build!")
```

## Step 7: Rebuild and Test

You don't need to rebuild everything. If you affected only the
base and flow containers, you can rebuild the subset:

```bash
make some-containers VERSION=1.8.0 CONTAINERS="flow"
```

Or rebuild all containers if unsure:

```bash
make container VERSION=1.8.0
```

## Step 8: Restart the Changed Component

Restart only the container you modified:

```bash
docker-compose down processor-name
docker-compose up -d processor-name
```

Check the logs to see your change:

```bash
docker-compose logs processor-name | grep "Hello from my local build"
```

## Running Tests

Set up the test environment:

```bash
pip install pytest pytest-cov pytest-asyncio
```

Run the test suites:

```bash
pytest tests/unit
pytest tests/integration -m 'not slow'
pytest tests/contract
```

See `TEST_STRATEGY.md` in the repository for the full testing approach.

## Next Steps

- Read [Development Workflow](developer) for git practices and working with AI assistants
- Check [Contributing Guidelines](contributing) before submitting a PR
- Join **#contributing** on [Discord](https://discord.gg/sQMwkRz5GX) for help

