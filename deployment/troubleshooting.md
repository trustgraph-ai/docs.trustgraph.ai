---
title: Troubleshooting
nav_order: 12
parent: Deployment
grand_parent: TrustGraph Documentation
review_date: 2026-03-12
---

# Deployment troubleshooting

## Installation and environment

### TrustGraph not working

#### Are you using SELinux (Linux only)?

This is a default deployment on many Linux installations.
You may need to run a command like this to give Docker containers the
ability to access any configuration files needed for the deployment

```
chcon -Rt svirt_sandbox_file_t prometheus grafana trustgraph
```

Also apply this to any LLM-specific configuration e.g. the `vertexai`
directory.

#### Are processors running?

Try:

```
tg-show-processor-state
```

This will show the state of running processors in Prometheus.
If the list is empty or you get an error, this indicates that Prometheus may
not be running or accessible.

#### Is the configuration service running?

Try:

```
tg-show-config
```

This will show the state of the configuration service.  If you get an
error, this shows that Pulsar, or the configuration service may not be
running.

If the output says `version 0` and shows an empty configuration, it shows
that initialisation may have failed.

### TrustGraph CLI commands not working

#### Are you using a support version of Python?

(>3.12)

#### Did you install the `trustgraph-cli` package?

If not, revisit the installation instructions 
e.g. [installation](/deployment/docker-compose#2-install-cli-tools)).

#### Does your version of the `trustgraph-cli` package match the version of TrustGraph you deployed?

It's easiest to exact-match the versions, or at least ensure they major/minor
numbers match, and that both versions were declared stable.

### LLM invocation not working with LMStudio / Ollama

#### Have you configured the Ollama or LMStudio URL correctly

When accessing Ollama or LMStudio running on the host from inside
a container service, it is necessary to ensure that you use a service
address which is usable from within containers.

On Linux using Podman, containers can find the host on host.containers.internal

On Docker running directly on Linux or Windows (not WSL) containers can find the host on host.docker.internal

WSL is complicated, because you have the host, a virtualised WSL environmnet, and Docker containers.

Solving the WSL + Docker Desktop networking challenge: 

Use WSL2's IP address directly

From your Windows command prompt or PowerShell, find WSL2's IP:

wsl hostname -I

Then use that IP in your docker-compose file:

OLLAMA_HOST=http://[WSL2_IP]:11434

