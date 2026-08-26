---
title: Verify it's working
nav_order: 4
parent: Quickstart
---

# Verify it's working

The containers are running. Before loading data, let's confirm the
system is healthy and the LLM is connected.

## Test LLM connectivity

The quickest check — ask the LLM a trivial question through TrustGraph:

```sh
tg-invoke-llm '' 'What is 2 + 2?'
```

You should get a response within a few seconds. If this times out or
errors, check the [troubleshooting section](../../deployment/compose#troubleshooting)
in the compose guide.

## Connect to the UI

Open your browser and go to
[http://localhost:8888](http://localhost:8888).

You'll see a login page. Select the **API Key** tab and enter the
bootstrap token you set earlier (the value of `IAM_BOOTSTRAP_TOKEN`),
then click **Connect**.

After logging in, you should see the Workflows page showing the
available workflows. The **Workflows** button at the top right brings
you back to this page from anywhere.

## Run a prompt through the UI

Let's confirm the UI can talk to the LLM. From the Workflows page,
select **Prompt Management**.

Find the **question** prompt in the list on the left and select it.
On the right-hand side, change the **TEST** box from `{}` to:

```json
{"question": "What is 2 + 2?"}
```

Click **Run**. You should see the answer appear below.

This confirms the full stack is working: browser → UI → API gateway →
LLM → response.

## Next

[Load documents](load-documents) — load sample data and process it
into the knowledge graph.
