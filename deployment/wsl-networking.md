---
title: WSL networking and self-hosted models
nav_order: 1
parent: Docker / Podman Compose
review_date: 2026-03-20
---

# WSL networking

## Overview

If you are self-hosting a model on the same device you are intending
to run TrustGraph, and Windows Subsystem for Linux (WSL) is involved,
you should read this.

## Container networking

As discussed in
[Container networking and self-hosted models](container-networking),
containers have a different address space from the host in which they
are running.

<img src="podman-networking.png" alt="Podman networking diagram"/>

Things get even more complex if you are hosting a model service on
Windows using Windows Subsystem for Linux (WSL). Linux running on
Windows runs in its own virtual host with its own virtual address.
To get TrustGraph to communicate with a model service running in WSL,
TrustGraph needs to know the address of the WSL virtual machine.

## Solution 1: Use WSL2's IP address directly

From your Windows command prompt or PowerShell, find WSL2's IP:

```
wsl hostname -I
```

Then use that IP in your docker-compose file e.g.

```
OLLAMA_HOST=http://[WSL2_IP]:11434
```

## Solution 2: Configure Ollama to bind to all interfaces

In your WSL2 Ubuntu terminal, restart Ollama with:

```
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

Then from Windows, you should be able to use WSL2's IP address as above.

## Solution 3: Use Windows port forwarding

Forward the port from WSL2 to Windows localhost:

```
# Run this in Windows PowerShell as Administrator
netsh interface portproxy add v4tov4 listenport=11434 listenaddress=0.0.0.0 connectport=11434 connectaddress=[WSL2_IP]
```

Then use `host.docker.internal:11434` in your TrustGraph deployment.

## Solution 4: Move everything to WSL2

The cleanest solution is often to run Docker inside WSL2 too:

```
# In WSL2 Ubuntu
sudo apt update
sudo apt install docker.io docker-compose
sudo usermod -aG docker $USER
```

The `172.17.0.1` address you tried is Docker's default bridge gateway - that won't reach WSL2. The `host.docker.internal` also won't work because Docker Desktop on Windows doesn't automatically bridge to WSL2 services.

Try Solution 1 first - it's usually the quickest fix!

