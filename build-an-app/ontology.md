---
title: Create an ontology
nav_order: 5
parent: Build an App
---

# Create an ontology

Before writing any UI code, we need to define the knowledge structure
that will power the onboarding bot. That means creating an ontology.

## How we build ontologies

Traditionally, ontology development is a specialist discipline — a
knowledge engineer interviews domain experts, maps out the concepts
and relationships, and iterates through formal design processes. It
works, but it's slow and requires scarce expertise.

We take a different approach: **use a code assistant to generate
ontologies**. Instead of the traditional model where an expert
interviews people and designs the ontology, we turn the tables — a
human who understands the domain leads a code assistant through the
process. You describe what you need in plain language, the assistant
generates the OWL ontology, and you iterate until it captures the
right structure.

You don't need to be an ontology expert. You just need to know your
domain.

This is a good point to bring a code assistant into your project.
We work with Claude Code and Kimi K2 — pick your favourite assistant
or have fun trying something new. If you don't have access to a code
assistant, there's a ready-made ontology at the end of this page.

## Start with use cases

Before jumping into ontology generation, start by talking to your
code assistant about the problem space. Describe the scenario — an
office onboarding bot that helps people find out who owns what, how
to get access, and how approval processes work — and ask it to
suggest some use cases and workflows.

This doesn't take long, and it grounds the rest of the conversation
in concrete things the ontology needs to support. Without this step,
you'll end up with an ontology that looks reasonable but doesn't
actually answer the questions people ask.

Claude Code came up with the following use cases when we ran this
process:

- **Service ownership**: "Who owns the payment gateway service?"
- **Access approval**: "Who can approve my access to the data
  warehouse?"
- **Spend approval**: "I'm raising an IT request with a £5k spend —
  who approves it?"
- **Role-based tooling**: "I just joined as a data engineer — what
  tools do I need access to?"
- **Escalation**: "My request is stuck — who do I escalate to?"

## Break down the concepts

Next, having identified use cases, ask the code assistant to break
down the concepts — what entity types and relationships are needed
to support those queries.

From our use cases, it identified entity types like **Person**,
**Role**, **Team**, **Service**, **Process**, and **ApprovalStep**
— with relationships connecting them: who belongs to which team,
which team owns which service, which roles require access to which
services, and how approval chains work including spend thresholds.

At this point it's worth mentioning to the code assistant that
you'll be building a knowledge graph, so it's important to capture
objects and relationships between objects — these are the core
concepts that make a knowledge graph queryable.

The ontology also needs **properties** — attributes like a person's
name, a service's description, or a spend threshold amount.
Generally this is detail you can work out later and it can often be
resolved during ontology generation. It's up to you whether you want
to go through a separate design step for properties — for more
complex ontologies it might be worth doing.

This is all worth reviewing before generating the ontology. If the
concepts don't cover your use cases, iterate now — it's much easier
to fix at this stage than after you've generated data.

## Generate the ontology

TrustGraph uses **OWL** (Web Ontology Language) ontologies, typically
written in **Turtle** format — a compact, readable RDF syntax.
OWL provides the formal vocabulary for defining classes,
relationships, and properties. Turtle is a text format that's easy
to read and edit.

A key feature of how TrustGraph uses ontologies: **the ontology will
be read by an LLM** during knowledge extraction. The LLM needs to
understand what each class and relationship means in order to extract
the right knowledge from documents. This means it's important to
include all the documentation and semantics needed for the LLM to
do its job.

Specifically, prompt the code assistant to include `rdfs:label` and
`rdfs:comment` properties for **everything** in the ontology — every
class, every object property, every data property. Without these,
the LLM sees machine-readable identifiers but has no context for
what they mean.

Once you're happy with the concepts, ask the code assistant to
generate the ontology. A prompt like this works well:

> Generate an OWL ontology in Turtle format for an office onboarding
> and service ownership domain. It should include classes for:
> Person, Role, Team, Department, Service (internal tools and
> platforms), Process (IT requests, access requests, procurement),
> ApprovalStep (stages in an approval chain with spend thresholds),
> and Channel (communication channels like Slack).
>
> Key relationships: Person hasRole Role, Person memberOf Team,
> Team owns Service, Role requiresAccess Service, Process hasStep
> ApprovalStep, ApprovalStep approvedBy Role, ApprovalStep
> spendLimit (a value), Team managedBy Person.
>
> This ontology will be read by an LLM during knowledge extraction,
> so include rdfs:label and rdfs:comment on every class, object
> property, and data property. The labels and comments should be
> clear enough for an LLM to understand what each concept means.

Review the output — check that the entity types and relationships
make sense for the queries you want to support. Iterate with the
assistant if anything is missing or wrong.

{: .highlight }
**Don't have a code assistant?** Use our
[ready-made ontology](https://raw.githubusercontent.com/trustgraph-ai/demo-onboarding/refs/heads/master/onboarding.ttl) and skip to the next step.

## Next

[Load the ontology](load-ontology) — load it into TrustGraph and
check it looks right.
