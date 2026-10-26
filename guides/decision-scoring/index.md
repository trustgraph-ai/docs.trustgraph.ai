---
title: Decision Scoring
nav_order: 5
parent: Building with TrustGraph
review_date: 2026-11-01
guide_category:
  - Building with TrustGraph
guide_category_order: 5
guide_description: Use the Laya System 1 model to make fast structured decisions — choosing between options, scoring on a scale, or answering yes/no questions
guide_difficulty: intermediate
guide_time: 20 min
guide_emoji: "\U0001F3AF"
guide_banner: banner.jpg
guide_labels:
  - Decision Scoring
  - Laya
  - System 1
  - Classification
  - CLI
---

# Decision Scoring

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>A running TrustGraph deployment (v2.10 or later)</li>
<li>TrustGraph CLI tools installed</li>
<li>A running flow with the decision-scoring service</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Understand System 1 models, structure decision-scoring requests, and interpret the three output types: choice, score, and noul."
%}

**Make fast, structured decisions without calling an LLM**

> **New in TrustGraph v2.10.** Decision scoring is not available in
> v2.9 or earlier releases.

Decision scoring is integrated with the TrustGraph API gateway, so it
is accessible through both the CLI and the REST API. It is not
currently integrated with any core TrustGraph processing pipelines
(such as knowledge extraction or RAG flows) — you call it directly as
a standalone service.

## What Are System 1 Models?

The terms *System 1* and *System 2* come from cognitive psychology.
System 1 thinking is fast, intuitive, and pattern-based — the kind of
thinking you use to recognise a face or gauge someone's mood.
System 2 thinking is slow, deliberative, and logical — the kind you
use to solve a maths problem or write an essay.

Large language models (LLMs) are System 2: powerful and flexible, but
slow and expensive per call. For many real-world decisions — routing a
support ticket, triaging an alert, scoring urgency — you don't need a
full reasoning engine. You need a fast, confident classification.

That's what System 1 models are for. They are small, specialised
transformer models trained to make structured decisions in
milliseconds rather than seconds. They take a *state* (the situation)
and one or more *questions* (what to decide), and return probability
distributions over the options.

TrustGraph uses **Laya**, an open multilingual System 1 model that is
feature-equivalent to
[Jev](https://huggingface.co/Trustgraph/jev-decision-0.1). Laya runs
as an ONNX model on CPU, with no GPU required and a memory footprint
under 2 GB.

## The Three Question Types

Every decision-scoring request sends a **state** and one or more
**questions**. Each question has a type that controls how the model
interprets the options and formats the output.

| Type | Purpose | Output |
|------|---------|--------|
| **choice** | Pick one from a list | Selected option + per-option probabilities |
| **score** | Rate on an ordered scale | Expected score + per-level probabilities |
| **noul** | Answer a yes/no question | Probability of *true* (0.0–1.0) |

All three types also return a **confidence** value (how certain the
model is) and an **action probability** (how answerable the question
is given the state).

## Step-by-Step Guide

### Step 1: Structure Your State

The state is a JSON object describing the situation the model should
reason about. It can contain any fields relevant to your decision:

```json
{
  "category": "billing",
  "message": "I was overcharged last month"
}
```

The state is serialised to text and fed to the model as context. Keep
it concise — the model has a 512-token window shared between the
state, the question instructions, and the options.

### Step 2: Define Your Questions

Questions are a JSON object where each key is a question name and
each value specifies the type, criteria, and instructions.

You can ask multiple questions in a single call. All questions are
evaluated against the same state:

```json
{
  "department": {
    "type": "choice",
    "criteria": ["sales", "support", "billing"],
    "instructions": "Which department should handle this customer request?"
  },
  "urgency": {
    "type": "score",
    "criteria": ["low", "medium", "high", "critical"],
    "instructions": "How urgent is this customer issue?"
  },
  "refund_requested": {
    "type": "noul",
    "instructions": "Is the customer requesting a refund?"
  }
}
```

#### Choice Questions

Use **choice** when there is exactly one correct answer from a set of
options. The model returns the most likely option and a probability
distribution across all options.

- `criteria` — a list of option labels
- `instructions` — what the model should decide

#### Score Questions

Use **score** when the answer falls on an ordered scale. The model
returns an expected score (a weighted average across levels) and a
probability distribution. The criteria list defines the scale from
lowest (index 0) to highest.

- `criteria` — an ordered list of scale levels
- `instructions` — what the model should assess

#### Noul Questions

Use **noul** for binary yes/no determinations. The model returns a
single probability value: 0.0 means *definitely no*, 1.0 means
*definitely yes*.

- `instructions` — a statement to evaluate as true or false
- No `criteria` needed

### Step 3: Run the Scoring

Combine state and questions into a single `tg-invoke-decision-scoring`
call:

```bash
tg-invoke-decision-scoring \
  -s '{"category": "billing", "message": "I was overcharged last month"}' \
  -q '{
    "department": {
      "type": "choice",
      "criteria": ["sales", "support", "billing"],
      "instructions": "Which department should handle this customer request?"
    },
    "urgency": {
      "type": "score",
      "criteria": ["low", "medium", "high", "critical"],
      "instructions": "How urgent is this customer issue?"
    },
    "refund_requested": {
      "type": "noul",
      "instructions": "Is the customer requesting a refund?"
    }
  }'
```

For larger inputs, use files:

```bash
tg-invoke-decision-scoring -s @state.json -q @questions.json
```

### Step 4: Interpret the Results

The model returns an answer for each question:

#### Choice Result

```json
{
  "type": "choice",
  "choice": "billing",
  "probabilities": {
    "sales": 0.0,
    "support": 0.0,
    "billing": 1.0
  },
  "confidence": 0.9997,
  "action": {
    "act_probability": 1.0
  }
}
```

- **`choice`** — the selected option (highest probability)
- **`probabilities`** — probability for each option (sums to 1.0)
- **`confidence`** — how certain the model is (1.0 = maximum certainty)

Here, the model is nearly 100% confident this is a billing issue.

#### Score Result

```json
{
  "type": "score",
  "score": 2.1118,
  "legend": {
    "0": "low",
    "1": "medium",
    "2": "high",
    "3": "critical"
  },
  "probabilities": {
    "0": 0.018,
    "1": 0.1312,
    "2": 0.5718,
    "3": 0.279
  },
  "confidence": 0.2681,
  "action": {
    "act_probability": 1.0
  }
}
```

- **`score`** — expected value on the scale (weighted average of level
  indices). Here, 2.11 falls between *high* (2) and *critical* (3),
  leaning toward high.
- **`legend`** — maps index numbers to your criteria labels
- **`probabilities`** — probability for each level

Notice the lower confidence (0.27) — the model spreads probability
across *high* and *critical*, indicating genuine uncertainty about
where this falls on the scale. This is useful information: a score
result with low confidence suggests the situation could go either way.

#### Noul Result

```json
{
  "type": "noul",
  "noul": 0.0005,
  "confidence": 0.9995,
  "action": {
    "act_probability": 1.0
  }
}
```

- **`noul`** — probability that the statement is true (0.0–1.0)

Here, 0.0005 means the model is very confident the customer is *not*
requesting a refund. The message says "I was overcharged" — a
complaint, but not an explicit refund request.

### Understanding Confidence and Action Probability

Every answer includes two meta-signals:

**Confidence** measures how concentrated the probability distribution
is. High confidence means the model strongly favours one outcome; low
confidence means the probability is spread across multiple options.
For choice and score questions, confidence is derived from the entropy
of the distribution.

**Action probability** measures whether the question is answerable
given the state. A high act_probability (close to 1.0) means the
state contains enough information to make the decision. A low value
suggests the state is missing relevant context — the model can still
produce an answer, but it may be unreliable.

## Practical Patterns

### Ticket Routing

Route incoming requests to the right team without an LLM call:

```json
{
  "state": {"subject": "Login broken", "body": "Can't access my account since the update"},
  "questions": {
    "team": {
      "type": "choice",
      "criteria": ["engineering", "support", "security", "billing"],
      "instructions": "Which team should handle this ticket?"
    }
  }
}
```

### Risk Assessment

Score risk on a defined scale:

```json
{
  "state": {"transaction_amount": 15000, "country": "high-risk-region", "account_age_days": 3},
  "questions": {
    "fraud_risk": {
      "type": "score",
      "criteria": ["negligible", "low", "moderate", "high", "critical"],
      "instructions": "What is the fraud risk level for this transaction?"
    }
  }
}
```

### Content Moderation

Quick binary check before expensive processing:

```json
{
  "state": {"text": "Great product, highly recommend!"},
  "questions": {
    "contains_pii": {
      "type": "noul",
      "instructions": "Does this text contain personally identifiable information?"
    },
    "is_spam": {
      "type": "noul",
      "instructions": "Is this text spam or advertising?"
    }
  }
}
```

## When to Use Decision Scoring vs. an LLM

| Criterion | Decision Scoring (System 1) | LLM (System 2) |
|-----------|----------------------------|-----------------|
| **Speed** | Milliseconds | Seconds |
| **Cost** | CPU only, no token costs | Token costs per call |
| **Best for** | Classification, routing, triage, yes/no | Reasoning, generation, open-ended questions |
| **Output** | Structured probabilities | Free-form text |
| **Confidence** | Built-in probability + confidence | Requires prompt engineering |

Use decision scoring as a fast first pass: route, triage, or
pre-filter before calling an LLM for cases that need deeper reasoning.

## Next Steps

- **[`tg-invoke-decision-scoring`](../../reference/cli/tg-invoke-decision-scoring)** — Full CLI reference
- **[`tg-invoke-cloze`](../../reference/cli/tg-invoke-cloze)** — Cloze model classification (another System 1 approach)
- **[`tg-list-models`](../../reference/cli/tg-list-models)** — List available models
