---
title: Cloze Model Classification
nav_order: 6
parent: Building with TrustGraph
review_date: 2026-11-01
guide_category:
  - Building with TrustGraph
guide_category_order: 6
guide_description: Train a lightweight classifier from labeled examples and use it to categorise text in milliseconds — no LLM required
guide_difficulty: intermediate
guide_time: 20 min
guide_emoji: "\U0001F3F7"
guide_banner: banner.jpg
guide_labels:
  - Cloze
  - Classification
  - System 1
  - CLI
---

# Cloze Model Classification

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>A running TrustGraph deployment (v2.10 or later)</li>
<li>TrustGraph CLI tools installed</li>
<li>A running flow with the cloze service</li>
<li>Labeled example data for your classification task</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Prepare training data, upload it as configuration, wait for auto-training, and classify text using your trained model."
%}

**Train a purpose-built classifier from your own examples**

> **New in TrustGraph v2.10.** Cloze model classification is not
> available in v2.9 or earlier releases.

Cloze model classification is integrated with the TrustGraph API
gateway, so it is accessible through both the CLI and the REST API.
It is not currently integrated with any core TrustGraph processing
pipelines — you call it directly as a standalone service.

## What Is a Cloze Model?

Like [decision scoring](../decision-scoring/), cloze classification is
a **System 1** approach: fast, pattern-based classification that runs
in a fraction of a second with no LLM token costs.

The difference is in the trade-off:

| | Decision Scoring (Laya) | Cloze Classification |
|---|---|---|
| **Training** | Pre-trained, works out of the box | You provide training examples |
| **Flexibility** | General-purpose, handles any question | Specialised — does one job well |
| **Accuracy** | Good across many tasks | Excellent on its trained task |
| **Model** | Laya (multilingual transformer) | DistilBERT (lightweight BERT) |

Decision scoring is a generalist: you describe the question at query
time and it gives you a reasonable answer. Cloze classification is a
specialist: you invest a small amount of effort training it on your
specific task, and it gives you a highly accurate answer on that task.

The underlying model is **DistilBERT**, a compact language model that
is small enough to train in around 90 seconds on CPU. It works by
learning to fill in a masked token — given "Query: *What is my account
balance?* Tool: [MASK]", it learns that `[MASK]` should be
`[TOOL_BANK]`. At inference time, it predicts the most likely label
with a confidence score.

## When to Use Cloze Classification

- **Use it when** you have a well-defined classification task with
  clear categories and can provide 8–10 examples per category.
  Typical use cases: tool routing, intent detection, ticket
  categorisation, content tagging.

- **Use decision scoring instead** when you need a general-purpose
  classifier that works without training data, or when your categories
  change frequently.

- **Use an LLM instead** when the classification requires complex
  reasoning, ambiguous categories, or explanations alongside the
  label.

## Step-by-Step Guide

### Step 1: Prepare Training Data

Create a JSON file with labeled examples. Each label needs:

- **`token`** — a unique label identifier (convention: `[TOOL_NAME]`
  or `[CATEGORY_NAME]`)
- **`seed`** — a plain-English word that hints at the label's meaning
  (used to warm-start the model's embeddings)
- **`examples`** — 8–10 representative text examples for this label

You can also set training parameters:

- **`min-accuracy`** — minimum test accuracy to accept the model
  (e.g. 0.80). If the model doesn't meet this threshold after
  training, it is rejected.
- **`epochs`** — number of training epochs (default: 20)
- **`test-split`** — fraction of examples reserved for testing
  (default: 0.2)

Here is an example for tool routing — classifying user requests to
the right tool:

```json
{
  "min-accuracy": 0.80,
  "epochs": 15,
  "test-split": 0.2,
  "labels": [
    {
      "token": "[TOOL_BANK]",
      "seed": "bank",
      "examples": [
        "What is my checking account balance?",
        "Transfer $150 to my savings account.",
        "Did my direct deposit clear this morning?",
        "Show me my recent transactions from last week.",
        "Pay my credit card bill from my checking account.",
        "What is the interest rate on my savings account?",
        "I need to dispute a charge on my debit card.",
        "Set up a recurring monthly transfer of $500.",
        "Has the wire transfer from my employer arrived yet?",
        "How much did I spend on groceries this month?"
      ]
    },
    {
      "token": "[TOOL_WEATHER]",
      "seed": "weather",
      "examples": [
        "Is it going to rain in Manchester today?",
        "What's the temperature outside right now?",
        "Give me the 7-day forecast for Tokyo.",
        "Will it snow in Denver this weekend?",
        "What is the humidity level in Miami right now?",
        "Do I need an umbrella for my commute tomorrow?",
        "How windy is it going to be this afternoon?",
        "What is the UV index in Los Angeles today?",
        "Check if there are any storm warnings in my area.",
        "What will the high and low temperatures be on Saturday?"
      ]
    },
    {
      "token": "[TOOL_EMAIL]",
      "seed": "email",
      "examples": [
        "Send the weekly status report to the engineering team.",
        "Search my inbox for messages from Sarah regarding the contract.",
        "Draft a reply to the customer feedback thread.",
        "Mark all newsletters as read.",
        "Forward the invoice from Acme Corp to the finance department.",
        "Do I have any unread messages from my manager?",
        "Compose a follow-up email to the client about the proposal.",
        "Delete all the spam in my junk folder.",
        "Archive the old project discussion thread.",
        "Attach the quarterly report and send it to the board."
      ]
    }
  ]
}
```

### Step 2: Upload Training Data

Upload the training data as a configuration item of type
`cloze-training`. The key becomes the model instance name:

```bash
cat training-data.json | \
  tg-put-config-item --type cloze-training --key tool-routing --stdin
```

```
Configuration item set: cloze-training/tool-routing
```

This triggers automatic training. The cloze service detects the new
configuration and begins training the model immediately.

### Step 3: Wait for Training

Training typically takes around 90 seconds on CPU. Poll the model
status with `tg-list-cloze-models`:

```bash
tg-list-cloze-models
```

While training is in progress:

```
tool-routing:
  State: training
```

When training completes:

```
tool-routing:
  State: ready
  Labels: [TOOL_BANK], [TOOL_WEATHER], [TOOL_EMAIL]
  Accuracy: 100.0%
  Train/Test: 48/12
```

The output shows:
- **State** — `training` or `ready`
- **Labels** — the label tokens the model learned
- **Accuracy** — classification accuracy on the held-out test set
- **Train/Test** — number of training and test examples used

If accuracy falls below your `min-accuracy` threshold, the model is
rejected and won't appear as `ready`.

### Step 4: Classify Text

Once the model is ready, classify text with `tg-invoke-cloze`:

```bash
tg-invoke-cloze -m tool-routing "Did I receive an email from my estate agent?"
```

```
Label: [TOOL_EMAIL]
Confidence: 99.77%
```

```bash
tg-invoke-cloze -m tool-routing "What is the weather in Paris?"
```

```
Label: [TOOL_WEATHER]
Confidence: 100.00%
```

The model returns the most likely label and a confidence percentage.
Inference takes a fraction of a second.

## Model Lifecycle

### Updating a Model

To update a model, upload new training data with the same key. The
service automatically retrains:

```bash
cat updated-training-data.json | \
  tg-put-config-item --type cloze-training --key tool-routing --stdin
```

The previous model continues to serve requests until the new model
finishes training.

### Removing a Model

Delete the configuration item to remove a model:

```bash
tg-delete-config-item --type cloze-training --key tool-routing
```

The model is unloaded from memory.

### Multiple Models

You can train multiple models in the same workspace, each with a
different key. Each model is independent and specialised for its own
classification task:

```bash
cat tool-routing.json | \
  tg-put-config-item --type cloze-training --key tool-routing --stdin

cat sentiment.json | \
  tg-put-config-item --type cloze-training --key sentiment --stdin

cat language-detection.json | \
  tg-put-config-item --type cloze-training --key language --stdin
```

```bash
tg-list-cloze-models
```

```
tool-routing:
  State: ready
  Labels: [TOOL_BANK], [TOOL_WEATHER], [TOOL_EMAIL]
  Accuracy: 100.0%
  Train/Test: 48/12
sentiment:
  State: ready
  Labels: [POSITIVE], [NEGATIVE], [NEUTRAL]
  Accuracy: 95.0%
  Train/Test: 24/6
language:
  State: training
```

## Writing Good Training Data

### Examples Per Label

Aim for **8–10 examples per label**. Too few and the model can't
generalise; too many and training takes longer without proportional
accuracy gains.

### Seed Words

The `seed` word gives the model a head start by initialising the new
label's embedding from a related word in DistilBERT's vocabulary.
Choose a word that captures the essence of the category:

| Label | Good Seed | Why |
|-------|-----------|-----|
| `[TOOL_BANK]` | `bank` | Direct meaning match |
| `[SENTIMENT_POSITIVE]` | `good` | Common positive word |
| `[LANG_FRENCH]` | `french` | Direct match |

### Example Diversity

Write examples that cover the range of how users might express the
same intent. Vary:
- **Phrasing** — questions, commands, statements
- **Specificity** — detailed vs. vague
- **Length** — short and long
- **Vocabulary** — formal and informal

### The min-accuracy Safety Net

Set `min-accuracy` to reject models that don't meet a quality bar.
If training data is noisy or categories overlap too much, the model
may not converge — better to catch this at training time than serve
bad predictions.

## Cloze vs. Decision Scoring vs. LLM

| Criterion | Cloze | Decision Scoring | LLM |
|-----------|-------|-----------------|-----|
| **Training required** | Yes (examples) | No | No |
| **Speed** | Sub-millisecond | Milliseconds | Seconds |
| **Accuracy** | Excellent (on trained task) | Good (general) | Good (general) |
| **Flexibility** | One task per model | Any question | Any question |
| **Cost** | CPU only | CPU only | Token costs |
| **Best for** | High-volume, fixed categories | Ad-hoc classification | Complex reasoning |

A common pattern is to use cloze models for high-volume routing (every
request hits the classifier) and decision scoring or LLMs for lower-
volume decisions that don't justify training data.

## Next Steps

- **[Decision Scoring](../decision-scoring/)** — General-purpose
  System 1 classification without training data
- **[`tg-invoke-cloze`](../../reference/cli/tg-invoke-cloze)** — Full CLI reference
- **[`tg-list-cloze-models`](../../reference/cli/tg-list-cloze-models)** — CLI reference for listing models
- **[`tg-put-config-item`](../../reference/cli/tg-put-config-item)** — CLI reference for uploading configuration
