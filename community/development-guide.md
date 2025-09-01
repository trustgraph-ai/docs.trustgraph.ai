---
title: Running TrustGraph as a developer
layout: default
nav_order: 5
parent: Community
---

# Running TrustGraph as a developer

## Target environment

TrustGraph has several 'external' components e.g. Pulsar, Cassandra that are
needed to run.  For a target environment, we use both:

- Kubernetes, deployed using a resources.yaml
- Docker/Podman deployed using docker-compose/podman-compose

So.. you're wondering how to test capability

## Things you should know

- Release branches
- It works fine with Python 3.12, there's an incompatibility with 3.13
- Packages can be built and installed, you need to run
  make update-package-versions VERSION=x.y.z
  and make sure the x.y part is correct for what you're building

## There are several ways to run code

### Target environment, locally built packages

One way to test capability is to run in the target environment, but building
packages locally.

To get running, you would 

building packages


, Kubernetes and/or Podman/Docker



- Running TrustGraph components on the 'host' so that they interact
  with running TrustGraph in a 'target' Docker/Podman environment through
  exposed ports

