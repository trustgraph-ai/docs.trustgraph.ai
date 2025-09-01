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

So... you're wondering how to develop code and test it?

## Things you should know

- Release branches - don't develop against master, use
  a branch like `release/v1.2` as the base.  Release branches always
  contain the latest code used to build containers so are a relatively
  stable branch to start building on.  Note that the latest release branch
  may contain unstable changes, so you may want to use the latest stable
  release.
- It works fine with Python 3.12, there's an incompatibility with 3.13, due
  to cassandra-driver having problems in some environments.  We're tracking
  this to work out when to move to 3.13 or later.
- Packages can be built and installed, you need to run
  make update-package-versions VERSION=x.y.z
  and make sure the x.y part is correct for what you're building
- It's possible to run code on the host and have to interact with a
  container environment.

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

You're typically running the command line on the 'host' so that they interact
with running TrustGraph in a 'target' Docker/Podman environment through
exposed ports.  If so, you have the packages installed locally, and you
can just use `pip install` to update the packages from checked-out code.
Make sure you ran `make update-package-versions VERSION=x.y.z` so that the
packages install.

### Running a component on the host

You have components running in docker, but want to test an existing
processor or support component on the host so that it interacts with the
docker environment.  This is possible.

The first complication is that the addressing scheme on your host doesn't
match what's happening inside the container environment, and this
is particularly relevant to how Pulsar works.

{: .warning }
This can be fiddly to work through.  Changing the local host file
can break interactions inside and outside of containers so make a note
of anything you change so that you can back it out.

Say you want to modify the recursive chunker process...

The development process would be

1) Download a docker compose configuration
2) Launch that environment, check it all works
3) Check out the source code of TrustGraph

You're typically running the command line on the 'host' so that they interact
with running TrustGraph in a 'target' Docker/Podman environment through
exposed ports.  If so, you have the packages installed locally, and you
can just use `pip install` to update the packages from checked-out code.
Make sure you ran `make update-package-versions VERSION=x.y.z` so that the
packages install.

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
