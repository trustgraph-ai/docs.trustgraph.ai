---
title: Intel GPU
nav_order: 11
parent: Deployment
review_date: 2026-01-28
guide_category:
  - Data centre
guide_banner: intel-ai.jpg
guide_category_order: 2
guide_description: Self-hosting TrustGraph with vLLM on Intel GPU accelerators
guide_difficulty: advanced
guide_time: 2 - 4 hr
guide_emoji: 🔴
guide_labels:
  - GPU
  - vLLM
  - Intel Arc
todo: true
todo_notes: Placeholder page - content to be added.
---

# Self-Hosting with vLLM and Intel GPU

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>Intel GPU with ??? support (e.g., Intel Arc B60)</li>
<li>ROCm drivers installed</li>
<li>Docker or Podman with GPU passthrough configured</li>
<li>Python {{site.data.software.python-min-version}}+ for CLI tools</li>
<li>Basic command-line familiarity</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Deploy TrustGraph with vLLM running on Intel GPU hardware for high-performance local inference."
%}

