---
title: Set up the dev environment
nav_order: 2
parent: Build an App
---

# Set up the dev environment

Before building a plugin, you need the TrustGraph UI running locally
in development mode. This gives you a working codebase you can modify
and see changes immediately.

## Clone the UI repo

```sh
git clone https://github.com/trustgraph-ai/trustgraph-ui.git
cd trustgraph-ui
npm install
npm run build
```

The build step compiles the built-in plugins — this is needed before
the dev server can run.

## Run the dev server

```sh
npm run dev
```

The dev server will start and tell you the port number to connect on.
Open that URL in your browser — you should see the TrustGraph UI,
running locally from your development copy.

{: .note }
The local UI still needs a running TrustGraph instance to connect to.
If you don't have one, see the [Quickstart](../quickstart/).

## Next

[Set up the plugin](plugin-setup) — clone the plugin template and
link it into the UI.
