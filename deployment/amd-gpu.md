---
title: AMD GPU
nav_order: 11
parent: Deployment
review_date: 2026-01-28
guide_category:
  - Data centre
guide_banner: amd-gpu.jpg
guide_category_order: 2
guide_description: Self-hosting TrustGraph with vLLM on AMD GPU accelerators
guide_difficulty: advanced
guide_time: 2 - 4 hr
guide_emoji: 🔴
guide_labels:
  - AMD
  - GPU
  - vLLM
todo: true
todo_notes: Placeholder page - content to be added.
---

# Self-Hosting with vLLM and AMD GPU

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>AMD GPU with ROCm support (e.g., RX 7900 XTX, MI series)</li>
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
   goal="Deploy TrustGraph with vLLM running on AMD GPU hardware for high-performance local inference."
%}

