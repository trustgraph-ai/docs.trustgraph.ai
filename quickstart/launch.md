---
title: Launch TrustGraph
nav_order: 3
parent: Quickstart
---

# Launch TrustGraph

Everything is configured. Time to start it up.

## Start the containers

From the directory where you unpacked the deployment bundle:

{% capture docker %}
```sh
docker-compose -f docker-compose.yaml up -d
```
{% endcapture %}

{% capture podman %}
```sh
podman-compose -f docker-compose.yaml up -d
```
{% endcapture %}

{% include code_tabs.html
   tabs="Docker,Podman"
   content1=docker
   content2=podman
%}

This pulls the container images (first time only) and starts all the
TrustGraph services in the background. The initial pull may take a few
minutes depending on your connection.

## Authenticate CLI tools

All CLI commands need a valid API token. Set it to the bootstrap token
you configured earlier:

```sh
export TRUSTGRAPH_TOKEN="${IAM_BOOTSTRAP_TOKEN}"
```

## Wait for startup

TrustGraph needs 40–120 seconds for all services to stabilise. Services
like Pulsar and Cassandra take time to initialise.

Run the system health check — it will wait and retry automatically:

{% include deployment/application-localhost/verify-system-health.md %}

Once all checks pass, you're ready to go.

## Next

[Verify it's working](verify) — confirm the LLM is connected and
the UI is accessible.
