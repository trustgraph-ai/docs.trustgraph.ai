---
title: Running TrustGraph as a developer
layout: default
nav_order: 5
parent: Contributing
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
1. Using the configuration tool to create a docker compose / podman compose
   configuration.
2. Launch that environment, check it all works.
3. Shut the environment down
4. In the source code, `make container VERSION=x.y.z` which rebuilds the
   containers.  Use the same version number that's used in the compose file.
5. Relaunch the environment, as you did at step 2.

At this point, you have a running container set you built yourself.

If you're wanting to change a part of the system, such as a single processor,
it's possible to do this without relaunching the whole environment each time,
you could use...

1. Change the code
2. Rebuild containers / just the container you want to build.  See the
   Makefile's `some-containers` target to see how to build a partial set, or
   just one container.
3. Use e.g. `docker-compose down -v -t 0 <CONTAINER>` to stop a running
   container and
4. Use e.g. `docker-compose up -d <CONTAINER>` to start it again.

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

Say you want to modify the recursive chunker process...

The first part is to set up the development environment so that you
can run the component standalone.  This means checking out the TrustGraph
repo and installing the packages to a local environment.

#### Package environment

```
python3 -m venv env
. env/bin/activate
make update-package-versions VERSION=x.y.z
pip install ./trustgraph-base
pip install ./trustgraph-cli
pip install ./trustgraph-flow
pip install ./trustgraph-bedrock
pip install ./trustgraph-vertexai
```

The recursive chunker is a Python command called `chunker-recursive`, so
check it runs...

```
chunker-recursive --help
```

If you see help text, that means the packages are installed enough
to get things to work.

#### Replace the running component

For your test, you may not need all the packages above to be
installed.  `trustgraph-base` is always needed, `trustgraph-flow`
supplies the bulk of the remaining components.

{: .warning }
This is fiddly and hacky.  Changing the local host file
can break interactions inside and outside of containers so make a note
of anything you change so that you can back it out.

The only remaining major issue is that when you start the chunker,
it will try to connect to the Pulsar service at hostname `pulsar` port 6650.
Whereas on the host, the name `pulsar` is not known, and the Pulsar
service as available at `localhost`.  TrustGraph processes provide a
command-line parameter `--pulsar-host` to override the default Pulsar
location, however it appears that Pulsar communications incorporate
indirection mechanisms to find the various service components, and
will still use the name `pulsar` for this.

So what we do, is to add an entry to the local host file (usually /etc/hosts)
to include the line:

```
127.0.0.1 pulsar
```

This means that when any running component tries to reach out to
`pulsar`, this will cause it to try the `localhost` address.

But here's the remaining issue: The host `/etc/hosts` file may be passed
through to containers, which means that containers will be looking for
the Pulsar service in the wrong place.

In my environment, I have to make sure that the additional host entry
is NOT present when launching the TrustGraph system.  Once everything
is settled down, adding the line enables host components to interact
with Pulsar.  When I forgetfully leave the entry in place and try launching
TrustGraph in docker compose, I'm left wondering why nothing is working
until I remember I modified the hosts file.

The process to replace a running component with a local run service is thus:

1. Launch the system
2. Check it's working
3. Use `docker-compose down` to stop the container you want to replace
4. Modify the host file as described above
6. Run the service with the same command-line configuration it would use
   in docker compose
7. Check it starts, check the log for errors

You can find out what command-line form is along with any command-line
arguments are by looking in the `docker-compose.yaml` file.  You can also
use `--help` with processors. The Pulsar address is specified, but it's set
to the default so you can skip that if you want.
e.g. for the recursive chunker.

```
chunker-recursive - --chunk-size 2000 --chunk-overlap 100 --log-level DEBUG
```

### Alternative to modifying `/etc/hosts`

If you don't like the `/etc/hosts` hack, there is another way.  If you run
Pulsar in standalone mode, we can just talk to the Pulsar port from inside
a container or on the host without problems.  This means hacking the
Docker Compose file:

- Remove the `bookie` service completely.
- Remove the `zookeeper` service completely.
- Remote the `pulsar-init` service completely.
- Replace the `pulsar` service with the configuration below.
- Add a `pulsar-data` volume in the volume section at the end.
- You can remove the `zookeeper` and `bookie` volumes as they are not needed.

```
  pulsar:
    command:
    - bin/pulsar
    - standalone
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 1500M
        reservations:
          cpus: '1.0'
          memory: 1500M
    environment:
      PULSAR_MEM: -Xms600M -Xmx600M
    image: docker.io/apachepulsar/pulsar:3.3.1
    ports:
    - 6650:6650
    - 8080:8080
    restart: on-failure:100
    volumes:
    - pulsar-data:/pulsar/data
```


### Enough environment to run pytest

The process to run the pytest tests involves setting up the
packages plus a few extras...

You need a virtual environment with the packages installed...
```
python3 -m venv env
. env/bin/activate
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
