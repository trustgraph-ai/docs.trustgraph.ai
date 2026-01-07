---
title: How-to Guides
nav_order: 7
has_children: true
parent: TrustGraph Documentation
review_date: 2026-08-01
---

# How-to Guides

<div style="border: 2px solid #4a9eff; background-color: #1e2a3a; padding: 5px 20px 20px 20px; margin: 20px 0; border-radius: 8px;">

<h2>Common knowledge management tasks</h2>

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px;">
{% assign guide_pages = site.pages | where: "parent", "How-to Guides" | where: "guide_category", "Common knowledge management tasks" | sort: "guide_category_order" %}
{% for guide in guide_pages %}
<div style="border: 1px solid #4a9eff; background-color: #0d1621; padding: 10px 15px; border-radius: 4px; flex: 1 1 200px;">
<a href="{{ guide.url }}" style="text-decoration: none; color: inherit; display: block;">{{ guide.title }}</a>
</div>
{% endfor %}
</div>

</div>

<div style="border: 2px solid #9f7aea; background-color: #2d2642; padding: 5px 20px 20px 20px; margin: 20px 0; border-radius: 8px;">

<h2>Advanced knowledge management</h2>

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px;">
{% assign guide_pages = site.pages | where: "parent", "How-to Guides" | where: "guide_category", "Advanced knowledge management" | sort: "guide_category_order" %}
{% for guide in guide_pages %}
<div style="border: 1px solid #9f7aea; background-color: #1a1529; padding: 10px 15px; border-radius: 4px; flex: 1 1 200px;">
<a href="{{ guide.url }}" style="text-decoration: none; color: inherit; display: block;">{{ guide.title }}</a>
</div>
{% endfor %}
</div>

</div>

<div style="border: 2px solid #48bb78; background-color: #1e3a2a; padding: 5px 20px 20px 20px; margin: 20px 0; border-radius: 8px;">

<h2>Agentic systems</h2>

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px;">
{% assign guide_pages = site.pages | where: "parent", "How-to Guides" | where: "guide_category", "Agentic systems" | sort: "guide_category_order" %}
{% for guide in guide_pages %}
<div style="border: 1px solid #48bb78; background-color: #0d2118; padding: 10px 15px; border-radius: 4px; flex: 1 1 200px;">
<a href="{{ guide.url }}" style="text-decoration: none; color: inherit; display: block;">{{ guide.title }}</a>
</div>
{% endfor %}
</div>

</div>

<div style="border: 2px solid #f59e0b; background-color: #3a2e1e; padding: 5px 20px 20px 20px; margin: 20px 0; border-radius: 8px;">

<h2>Managing operations</h2>

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px;">
{% assign guide_pages = site.pages | where: "parent", "How-to Guides" | where: "guide_category", "Managing operations" | sort: "guide_category_order" %}
{% for guide in guide_pages %}
<div style="border: 1px solid #f59e0b; background-color: #221a10; padding: 10px 15px; border-radius: 4px; flex: 1 1 200px;">
<a href="{{ guide.url }}" style="text-decoration: none; color: inherit; display: block;">{{ guide.title }}</a>
</div>
{% endfor %}
</div>

</div>

