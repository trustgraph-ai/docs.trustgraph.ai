---
title: Introduction to the TypeScript libraries
nav_order: 6
parent: Building with TrustGraph
grand_parent: How-to Guides
review_date: 2026-08-01
guide_category:
  - Building with TrustGraph
guide_category_order: 6
guide_description: Explore TrustGraph TypeScript libraries for building web applications
guide_difficulty: intermediate
guide_time: 30 min
guide_emoji: 📘
guide_banner: typescript-intro.jpg
guide_labels:
  - TypeScript
  - Libraries
---

# Introduction to the TypeScript libraries

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>Basic TypeScript/JavaScript familiarity</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Understand the TrustGraph TypeScript libraries and choose the right one for your application."
%}

## Overview

TrustGraph provides three TypeScript/JavaScript libraries for different use cases:

| Library | Description | Use Case |
|---------|-------------|----------|
| **trustgraph-client** | Pure TypeScript WebSocket client | Backend services, CLI tools, non-React applications |
| **trustgraph-react-provider** | React Context provider wrapper | Basic React integration with direct client access |
| **trustgraph-react-state** | React hooks with Tanstack Query | Full-featured React applications with state management |

**Choosing the right library:**

- **Building a React app?** → Use `trustgraph-react-state` for the best developer experience
- **Need React Context integration?** → Use `trustgraph-react-provider` for simpler needs
- **Building without React?** → Use `trustgraph-client` for Node.js, CLIs, or vanilla JavaScript

## trustgraph-client

The core TypeScript client for TrustGraph, built on WebSockets with minimal dependencies.

**Links:**
- [GitHub Repository](https://github.com/trustgraph-ai/trustgraph-client)
- [npm Package](https://www.npmjs.com/package/trustgraph-client)

**Key features:**
- Pure TypeScript with full type safety
- WebSocket-based for streaming and non-streaming operations
- Minimal dependencies (only websocket and promises)
- No React dependency - works anywhere JavaScript runs
- Suitable for backend services, CLI tools, and non-UI applications

**Installation:**

{% capture npm_install %}
```bash
npm install trustgraph-client
```
{% endcapture %}

{% capture yarn_install %}
```bash
yarn add trustgraph-client
```
{% endcapture %}

{% capture pnpm_install %}
```bash
pnpm add trustgraph-client
```
{% endcapture %}

{% include code_tabs.html
   tabs="npm,yarn,pnpm"
   content1=npm_install
   content2=yarn_install
   content3=pnpm_install
%}

**Basic usage:**

```typescript
import { TrustGraphClient } from 'trustgraph-client';

// Create client
const client = new TrustGraphClient({
  url: 'http://localhost:8088',
  flowId: 'default'
});

// Query using Graph RAG (streaming)
const stream = client.graphRag({
  query: 'What is the scientific name for cats?',
  user: 'trustgraph',
  collection: 'default',
  streaming: true
});

for await (const chunk of stream) {
  process.stdout.write(chunk);
}
```

The client can be used in:
- Node.js backend services
- Command-line tools
- Build scripts and automation
- Browser applications without React
- Electron apps

## trustgraph-react-provider

A React Context provider that makes the TrustGraph client available throughout your component tree.

**Links:**
- [GitHub Repository](https://github.com/trustgraph-ai/trustgraph-react-provider)
- [npm Package](https://www.npmjs.com/package/trustgraph-react-provider)

**Key features:**
- Wraps `trustgraph-client` with React Context
- Provides direct access to the client instance
- Minimal abstraction - you control client interactions
- Good for simple React integrations

**Installation:**

{% capture npm_install_provider %}
```bash
npm install trustgraph-react-provider trustgraph-client
```
{% endcapture %}

{% capture yarn_install_provider %}
```bash
yarn add trustgraph-react-provider trustgraph-client
```
{% endcapture %}

{% capture pnpm_install_provider %}
```bash
pnpm add trustgraph-react-provider trustgraph-client
```
{% endcapture %}

{% include code_tabs.html
   tabs="npm,yarn,pnpm"
   content1=npm_install_provider
   content2=yarn_install_provider
   content3=pnpm_install_provider
%}

**Basic usage:**

```tsx
import { TrustGraphProvider, useTrustGraph } from 'trustgraph-react-provider';

// Wrap your app with the provider
function App() {
  return (
    <TrustGraphProvider
      url="http://localhost:8088"
      flowId="default"
    >
      <YourComponents />
    </TrustGraphProvider>
  );
}

// Access the client in components
function QueryComponent() {
  const client = useTrustGraph();

  const handleQuery = async () => {
    const stream = client.graphRag({
      query: 'What is the scientific name for cats?',
      user: 'trustgraph',
      collection: 'default',
      streaming: true
    });

    for await (const chunk of stream) {
      // Handle streaming chunks
    }
  };

  return <button onClick={handleQuery}>Query</button>;
}
```

Use this when:
- You want direct control over client interactions
- You're comfortable managing your own state
- You have simple integration needs

## trustgraph-react-state

The most React-friendly library, providing hooks built on Tanstack Query for automatic state management and caching.

**Links:**
- [GitHub Repository](https://github.com/trustgraph-ai/trustgraph-react-state)
- [npm Package](https://www.npmjs.com/package/trustgraph-react-state)

**Key features:**
- React hooks for all TrustGraph operations
- Built on Tanstack Query (React Query)
- Automatic state management (loading, error, success states)
- Intelligent caching and request deduplication
- Optimistic updates and background refetching
- Best developer experience for React applications

**Installation:**

{% capture npm_install_state %}
```bash
npm install trustgraph-react-state @tanstack/react-query
```
{% endcapture %}

{% capture yarn_install_state %}
```bash
yarn add trustgraph-react-state @tanstack/react-query
```
{% endcapture %}

{% capture pnpm_install_state %}
```bash
pnpm add trustgraph-react-state @tanstack/react-query
```
{% endcapture %}

{% include code_tabs.html
   tabs="npm,yarn,pnpm"
   content1=npm_install_state
   content2=yarn_install_state
   content3=pnpm_install_state
%}

**Basic usage:**

```tsx
import { TrustGraphProvider } from 'trustgraph-react-state';
import { useGraphRag } from 'trustgraph-react-state/hooks';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

// Create QueryClient
const queryClient = new QueryClient();

// Wrap your app with providers
function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <TrustGraphProvider
        url="http://localhost:8088"
        flowId="default"
      >
        <YourComponents />
      </TrustGraphProvider>
    </QueryClientProvider>
  );
}

// Use hooks in components
function QueryComponent() {
  const { data, isLoading, error } = useGraphRag({
    query: 'What is the scientific name for cats?',
    user: 'trustgraph',
    collection: 'default'
  });

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return <div>{data}</div>;
}
```

**Available hooks:**
- `useGraphRag` - Graph RAG queries
- `useDocumentRag` - Document RAG queries
- `useAgent` - Agent queries
- `useTextCompletion` - LLM text completion
- `useTriplesQuery` - Knowledge graph triple queries
- And more...

Each hook provides:
- `data` - Query results
- `isLoading` - Loading state
- `error` - Error state
- `refetch` - Manual refetch function
- Automatic caching and deduplication

Use this when:
- Building a full React application
- You want automatic state management
- You need caching and performance optimization
- You want the best developer experience

## Next Steps

- [Building a React application](react-app.html) - Build a complete app with `trustgraph-react-state`

