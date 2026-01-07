---
title: How-to Guides
nav_order: 7
has_children: true
parent: TrustGraph Documentation
review_date: 2026-08-01
---

# How-to Guides

<div style="border: 2px solid #4a9eff; background-color: #1e2a3a; padding: 5px 20px 20px 20px; margin: 20px 0; border-radius: 8px;" markdown="1">

## Common knowledge management tasks

{% assign guide_pages = site.pages | where: "parent", "How-to Guides" | where: "guide_category", "Common knowledge management tasks" | sort: "guide_category_order" %}
{% for guide in guide_pages %}
- [{{ guide.title }}]({{ guide.url }})
{% endfor %}

</div>

<div style="border: 2px solid #9f7aea; background-color: #2d2642; padding: 5px 20px 20px 20px; margin: 20px 0; border-radius: 8px;" markdown="1">

## Advanced knowledge management

{% assign guide_pages = site.pages | where: "parent", "How-to Guides" | where: "guide_category", "Advanced knowledge management" | sort: "guide_category_order" %}
{% for guide in guide_pages %}
- [{{ guide.title }}]({{ guide.url }})
{% endfor %}

</div>

<div style="border: 2px solid #48bb78; background-color: #1e3a2a; padding: 5px 20px 20px 20px; margin: 20px 0; border-radius: 8px;" markdown="1">

## Agentic systems

{% assign guide_pages = site.pages | where: "parent", "How-to Guides" | where: "guide_category", "Agentic systems" | sort: "guide_category_order" %}
{% for guide in guide_pages %}
- [{{ guide.title }}]({{ guide.url }})
{% endfor %}

</div>

<div style="border: 2px solid #f59e0b; background-color: #3a2e1e; padding: 5px 20px 20px 20px; margin: 20px 0; border-radius: 8px;" markdown="1">

## Managing operations

{% assign guide_pages = site.pages | where: "parent", "How-to Guides" | where: "guide_category", "Managing operations" | sort: "guide_category_order" %}
{% for guide in guide_pages %}
- [{{ guide.title }}]({{ guide.url }})
{% endfor %}

</div>

