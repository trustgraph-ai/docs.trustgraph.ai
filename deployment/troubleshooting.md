---
title: Troubleshooting
nav_order: 12
parent: Deployment
grand_parent: TrustGraph Documentation
review_date: 2026-03-12
---

# Deployment troubleshooting

---

## Installation and environment

### SELinux blocking container access (Linux only)

SELinux is a default deployment on many Linux installations and may block
Docker containers from accessing configuration files.

Run this command to grant access:

```bash
chcon -Rt svirt_sandbox_file_t prometheus grafana trustgraph
```

Also apply this to any LLM-specific configuration e.g. the `vertexai`
directory.

### Processors not running

Check processor state with:

```bash
tg-show-processor-state
```

This shows the state of running processors in Prometheus.
If the list is empty or you get an error, Prometheus may not be running
or accessible.

### Configuration service not responding

Check the configuration service with:

```bash
tg-show-config
```

If you get an error, Pulsar or the configuration service may not be running.

If the output says `version 0` and shows an empty configuration,
initialisation may have failed.

---

## CLI commands not working

### Unsupported Python version

TrustGraph requires Python 3.12 or later.

### Missing `trustgraph-cli` package

If CLI commands aren't found, revisit the installation instructions:
[installation](/deployment/docker-compose#2-install-cli-tools)

### Version mismatch

Your `trustgraph-cli` package version should match the deployed TrustGraph
version. At minimum, ensure the major/minor numbers match and both versions
are declared stable.

---

## LLM invocation not working with LMStudio / Ollama

### Incorrect host URL configuration

When accessing Ollama or LMStudio running on the host from inside a container,
you must use a service address that's accessible from within containers.

**Linux with Podman:**
```
host.containers.internal
```

**Docker on Linux or Windows (not WSL):**
```
host.docker.internal
```

**WSL with Docker Desktop:**

WSL is more complex due to the host, virtualised WSL environment, and
Docker containers.

Find WSL2's IP from Windows command prompt or PowerShell:

```bash
wsl hostname -I
```

Then use that IP in your docker-compose file:

```
OLLAMA_HOST=http://[WSL2_IP]:11434
```

