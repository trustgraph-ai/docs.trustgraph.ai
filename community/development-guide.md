---
title: Running TrustGraph as a developer
layout: default
nav_order: 5
parent: Community
---

This is a WORK IN PROGRESS!

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

To get running, you would follow this process:
1) Using the configuration tool to create a docker compose / podman compose
   configuration.
2) Launch that environment, check it all works.
3) Shut the environment down
4) In the source code, `make container VERSION=x.y.z` which rebuilds the
   containers.  Use the same version number that's used in the compose file.
5) Relaunch the environment, as you did at step 2).

At this point, you have a running container set you built yourself.

If you're wanting to change a part of the system, such as a single processor,
it's possible to do this without relaunching the whole environment each time,
you could use...

1) Change the code
2) Rebuild containers / just the container you want to build.  See the
   Makefile's `some-containers` target to see how to build a partial set, or
   just one container.
3) Use e.g. `docker-compose down -v -t 0 <CONTAINER>` to stop a running
   container and
4) Use e.g. `docker-compose up -d <CONTAINER>` to start it again.

### Changing the command line

You're typically running the command line

- Running TrustGraph components on the 'host' so that they interact
  with running TrustGraph in a 'target' Docker/Podman environment through
  exposed ports

### Enough environment to run pytest

The process to run the pytest tests involves setting up the
packages plus a few extras...

You need a virtual environment with the packages installed...
```
python3 -m venv env
```

And then install the packages.  Make the version number match the
release branch you have checked out, and then install some pacakges...

```
make update-package-versions VERSION=x.y.z
pip install ./trustgraph-base
pip install ./trustgraph-cli
pip install ./trustgraph-flow
pip install ./trustgraph-bedrock
pip install ./trustgraph-vertexai
```

That installs all the packages which currently have tests running
against them.

Install the test extras:

```
pip install pytest pytest-cov pytest-asyncio
```

You should then be able to run tests...
```
pytest tests/unit
pytest tests/integration -m 'not slow'
pytest tests/contract
```

See `TEST_STRATEGY.md` for the test strategy.  If you want a coder
assistant to add tests, it's a good idea to get the coding assistant
to read that file.
