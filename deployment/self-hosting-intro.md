---
title: Introduction to Self-Hosting
nav_order: 10
parent: Deployment
review_date: 2026-01-28
guide_category:
  - Data centre
guide_banner: self-hosted-gpu.jpg
guide_category_order: 1
guide_description: Getting started with self-hosted TrustGraph deployments
guide_difficulty: beginner
guide_time: 30 min
guide_emoji: 🏠
guide_labels:
  - Self-Hosting
  - Introduction
todo: true
todo_notes: Placeholder page - content to be added.
---

# Introduction to Self-Hosting

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>Basic understanding of containerization (Docker/Podman)</li>
<li>Familiarity with command-line operations</li>
<li>Hardware capable of running large language models</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Understand the fundamentals of self-hosting TrustGraph with local GPU acceleration."
%}

