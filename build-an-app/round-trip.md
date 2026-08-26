---
title: Test the round-trip
nav_order: 4
parent: Build an App
---

# Test the round-trip

Before investing time on real functionality, confirm the
edit-build-reload cycle works end to end.

## Make a small change

In the plugin directory, open `src/TemplateExplorer.tsx` and find
the "Hello, World" text:

{% raw %}
```tsx
<div style={{
  fontSize: sz(24),
  fontFamily: theme.font.sans,
  fontWeight: 600,
  color: theme.text.primary,
}}>
  Hello, World
</div>
```
{% endraw %}

Change "Hello, World" to something else — "Onboarding Bot" or
whatever you like.

## Rebuild and check

In the plugin directory:

```sh
npm run build
```

Because the UI is symlinked to the plugin's `dist/` directory, the
new build is picked up immediately. Do a hard reload (Shift-reload)
in your browser and confirm your change appears.

## Why this matters

This proves the full cycle works: edit source → build plugin →
reload UI → see the change. If this round-trip is broken, you'll
waste time debugging later when you're not sure if the problem is
your code or the build pipeline. Get it working now, and from here
on you can iterate with confidence.

## Next

[Create an ontology](ontology) — define the knowledge structure for
the onboarding bot.
