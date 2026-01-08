---
title: Container networking and self-hosted models
nav_order: 1
parent: Docker / Podman Compose
review_date: 2026-03-20
guide_category:
  - Standalone deployment
guide_category_order: 1
guide_description: Easiest way to get TrustGraph running locally with Docker or Podman for development and testing
guide_difficulty: beginner
guide_time: 30 - 60 min
guide_emoji: 🐳
guide_banner: /../podman.png
guide_labels:
  - Docker
  - Local
  - Quick Start
---


# WSL networking

## Overview

### A word on networking and self-hosting

If you are self-hosting a model on the same device you are intending
to run TrustGraph, you will need to understand how to get TrustGraph
to talk to your model service.

<details>

<summary>Networking discussion for self-hosted models</summary>

<div markdown="1">
If you are intending to self-host a model, you may need to
understand how the Docker or Podman networking affects getting
TrustGraph to interact with your model service.  This is more of an
issue if you are intending to host the model on the same device as you
are running TrustGraph.
</div>

<div markdown="1">
Typically when you get two programs to talk to each other, and they are
running on the same host, you tell one program, the other is running at
address `localhost`.  This is a name for the special address `127.0.0.1`.
This means: the network traffic doesn't go out on a physical network, but
is communicated to another service on the same device.  That only works
when the two programs are running directly on the host.
</div>

<div markdown="1">
Say you are building a React app, and running it in debug mode and want
to interact with it using the browser you might get your browser to talk to
the URL `http://localhost:5173/`.  This means, connect to port 5173 on
this device.
</div>

<div markdown="1">
The diagram below illustrates how container
networking operates on a host.
</div>

<img src="podman-networking.png" alt="Podman networking diagram"/>

<div markdown="1">
The container engine creates a network space for containers, so that
containers appear to talk to each across a network.  Containers talk to
each other by using their own network address.  Containers can also
talk to services on the host using a special address for the host.
To a container, `localhost` and `127.0.0.1` direct communication to
*that same container*.
</div>

<div markdown="1">
This is important because when TrustGraph containers want to talk to
a model service running on the host.  This is the red arrow on the diagram
above.  To talk to the model service, you need to give the TrustGraph
services the address of the host.  The host address address in Podman
and Docker are given below.
</div>

<div markdown="1">

| Container engine | Host address |
|----------|-------------|
| **Podman** | `host.containers.internal` |
| **Docker** | `host.docker.internal` |

</div>

<div markdown="1">
Example: you run Ollama on the host and want to connect from TrustGraph.
On the host, you can access Ollama as `http://localhost:11434`.
From TrustGraph on Docker, you need to access the service as
`http://host.docker.internal:11434/`.
</div>

<div markdown="1">
Things get even more complex if you are hosting a model service on Windows
using Windows Subsystem for Linux (WSL). Linux running on Windows runs in its own virtual host with its own virtual address.
</div>

<div markdown="1">
Solution 1: Use WSL2's IP address directly
From your Windows command prompt or PowerShell, find WSL2's IP:

wsl hostname -I


Then use that IP in your docker-compose file:

OLLAMA_HOST=http://[WSL2_IP]:11434



Solution 2: Configure Ollama to bind to all interfaces
In your WSL2 Ubuntu terminal, restart Ollama with:

OLLAMA_HOST=0.0.0.0:11434 ollama serve


Then from Windows, you should be able to use WSL2's IP address as above.

Solution 3: Use Windows port forwarding
Forward the port from WSL2 to Windows localhost:

# Run this in Windows PowerShell as Administrator
netsh interface portproxy add v4tov4 listenport=11434 listenaddress=0.0.0.0 connectport=11434 connectaddress=[WSL2_IP]


Then use localhost:11434 in your docker-compose.

Solution 4: Move everything to WSL2
The cleanest solution is often to run Docker inside WSL2 too:

# In WSL2 Ubuntu
sudo apt update
sudo apt install docker.io docker-compose
sudo usermod -aG docker $USER



The 172.17.0.1 address you tried is Docker's default bridge gateway - that won't reach WSL2. The host.docker.internal also won't work because Docker Desktop on Windows doesn't automatically bridge to WSL2 services.

Try Solution 1 first - it's usually the quickest fix!
</div>

</details>

