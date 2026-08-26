---
title: Prepare the configuration
nav_order: 2
parent: Quickstart
---

# Prepare the configuration

Before launching TrustGraph, you need a deployment configuration that
tells it which components to use and how to connect to your LLM.

## Generate the config

Use the
[TrustGraph Configuration Builder](https://config-ui.demo.trustgraph.ai/)
to generate your deployment configuration. The configurator selects the
newest stable version by default.

For this quickstart, use these settings:

1. **Deployment**: Docker Compose or Podman Compose (match what you have
   installed)
2. **Graph Store**: Cassandra
3. **Vector Store**: Qdrant
4. **Chunker**: Recursive
5. **LLM Model**: Choose your provider and model
6. **Output Tokens**: 4096 (safe default for most models)
7. **Customization**: Leave defaults
8. **Generate**: Click Generate, then Download the deployment bundle

{: .note }
Note the version number shown in the configurator — you'll need it
when installing CLI tools.

## Unpack the bundle

The download is a `.zip` file containing a `docker-compose.yaml` and
configuration files for TrustGraph, Grafana, Prometheus, and other
services.

Create a working directory and unpack:

```sh
mkdir -p ~/trustgraph
cd ~/trustgraph
unzip ~/Downloads/deploy.zip
```

You can verify the contents:

```sh
unzip -l deploy.zip
```

<details>
<summary>Troubleshooting: file permission issues</summary>
<div markdown="1">

Some container engines have stricter access policies. If you hit
permission errors later, try:

```sh
find garage/ loki/ prometheus/ grafana/ trustgraph/ -type f | xargs chmod 644
find garage/ loki/ prometheus/ grafana/ trustgraph/ -type d | xargs chmod 755
```

On Linux with SELinux:

```sh
sudo chcon -Rt svirt_sandbox_file_t garage/ loki/ grafana/ prometheus/ trustgraph/
```

</div>
</details>

## Install CLI tools

Install the TrustGraph CLI tools in a Python virtual environment.
Replace `2.8.x` with the version number from the configurator:

```sh
python3 -m venv env
. env/bin/activate
pip install trustgraph-cli==2.8.x
```

## Configure your LLM

{% include llm/llm-configuration-details-compose.md %}

## Set security credentials

TrustGraph creates an initial security account using the
`IAM_BOOTSTRAP_TOKEN` environment variable. This is only used on
first cold start — you can add accounts and change tokens later
through the UI.

The token must have a `tg_` prefix:

```sh
export IAM_BOOTSTRAP_TOKEN="tg_my-secret-token"
export GF_SECURITY_ADMIN_PASSWORD="my-grafana-password"
```

Replace these with your own values.

## Next

[Launch TrustGraph](launch) — start the containers.
