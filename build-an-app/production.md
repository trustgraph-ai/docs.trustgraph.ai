---
title: Go to production
nav_order: 12
parent: Build an App
---

# Go to production

Your plugin works in the dev environment. To deploy it for real,
you need to get the plugin file and configuration into the
TrustGraph UI container. The cleanest approach is to build a
derived container image.

## Build the plugin

In the plugin directory, run a final build:

```sh
npm run build
```

The output is `dist/onboarding.iife.js` — this is the single file
you need to deploy.

## Prepare the configuration

You'll need a `components.json` that includes your plugin. Start
from the default configuration — you can extract it from the base
image:

```sh
docker run --rm trustgraph/trustgraph-ui:latest \
  cat /usr/lib/python3.12/site-packages/trustgraph_ui/ui/config/components.json \
  > components.json
```

Edit the file to add your plugin entry:

```json
{
  "id": "onboarding",
  "title": "Onboarding Bot",
  "icon": "△",
  "paletteKey": "cyan",
  "description": "Office onboarding and 'who knows what?' bot.",
  "url": "/plugins/onboarding.iife.js",
  "globalName": "TemplatePlugin"
}
```

You can also remove any built-in components you don't need — the
file is just a JSON array of tab groups.

## Build a derived container

Create a `Dockerfile` that layers your plugin and configuration
on top of the base TrustGraph UI image:

```dockerfile
FROM trustgraph/trustgraph-ui:latest

COPY dist/onboarding.iife.js \
  /usr/lib/python3.12/site-packages/trustgraph_ui/ui/plugins/

COPY components.json \
  /usr/lib/python3.12/site-packages/trustgraph_ui/ui/config/
```

Build and run it:

```sh
docker build -t my-trustgraph-ui .
```

Then use `my-trustgraph-ui` in place of `trustgraph/trustgraph-ui`
in your deployment configuration.

## Alternative: volume mounts

If you'd rather not build a custom image, you can mount the plugin
and config into the container at runtime:

```sh
docker run \
  -v ./dist/onboarding.iife.js:/usr/lib/python3.12/site-packages/trustgraph_ui/ui/plugins/onboarding.iife.js \
  -v ./components.json:/usr/lib/python3.12/site-packages/trustgraph_ui/ui/config/components.json \
  trustgraph/trustgraph-ui:latest
```

This is useful for quick testing but a derived image is more
portable and easier to deploy.

{: .note }
The container paths above are correct at the time of writing.
If they change in a future release, check the TrustGraph UI
container for the current locations.

## Next

[What next?](what-next) — ideas for where to go from here.
