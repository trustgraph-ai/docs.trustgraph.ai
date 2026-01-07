---
title: Deployment
nav_order: 4
has_children: true
parent: TrustGraph Documentation
review_date: 2025-12-29
---

# Deployment

<div style="border: 2px solid #06b6d4; background-color: #1e3a3f; padding: 5px 20px 20px 20px; margin: 20px 0; border-radius: 8px;">

<h2>Deployment decisions</h2>

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px;">
{% assign deployment_pages = site.pages | where: "parent", "Deployment" | sort: "guide_category_order" %}
{% for guide in deployment_pages %}
{% if guide.guide_category contains "Deployment decisions" %}
<div style="border: 1px solid #06b6d4; background-color: #0d1f23; padding: 0; border-radius: 4px; flex: 1 1 200px; overflow: hidden;">
<a href="{{ guide.url }}" style="text-decoration: none; color: inherit; display: block;">
{% if guide.guide_banner %}
<div style="width: 100%; height: 180px; background-image: url('{{ guide.url | replace: 'index.html', '' }}{{ guide.guide_banner }}'); background-size: cover; background-position: center; position: relative;">
<div style="position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.85), rgba(0,0,0,0.4)); padding: 15px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 5px;">
{% if guide.guide_emoji %}<span style="font-size: 2em; filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.8));">{{ guide.guide_emoji }}</span>{% endif %}
<strong style="font-size: 1.1em; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">{{ guide.title }}</strong>
</div>
<div style="font-size: 0.85em; color: #06b6d4; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">
{% if guide.guide_difficulty %}{{ guide.guide_difficulty }}{% endif %}{% if guide.guide_difficulty and guide.guide_time %} • {% endif %}{% if guide.guide_time %}{{ guide.guide_time }}{% endif %}
</div>
</div>
</div>
{% else %}
<div style="padding: 10px 15px 0 15px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 5px;">
{% if guide.guide_emoji %}<span style="font-size: 2em;">{{ guide.guide_emoji }}</span>{% endif %}
<strong style="font-size: 1.1em;">{{ guide.title }}</strong>
</div>
<div style="font-size: 0.85em; color: #06b6d4;">
{% if guide.guide_difficulty %}{{ guide.guide_difficulty }}{% endif %}{% if guide.guide_difficulty and guide.guide_time %} • {% endif %}{% if guide.guide_time %}{{ guide.guide_time }}{% endif %}
</div>
</div>
{% endif %}
<div style="padding: 10px 15px;">
{% if guide.guide_description %}<div style="font-size: 0.9em; margin-top: 8px; opacity: 0.9;">{{ guide.guide_description }}</div>{% endif %}
{% if guide.guide_labels %}<div style="display: flex; flex-wrap: wrap; gap: 5px; margin-top: 10px;">{% for label in guide.guide_labels %}<span style="font-size: 0.75em; padding: 2px 8px; background-color: rgba(6, 182, 212, 0.2); border: 1px solid #06b6d4; border-radius: 3px; white-space: nowrap;">{{ label }}</span>{% endfor %}</div>{% endif %}
</div>
</a>
</div>
{% endif %}
{% endfor %}
</div>

</div>

<div style="border: 2px solid #48bb78; background-color: #1e3a2a; padding: 5px 20px 20px 20px; margin: 20px 0; border-radius: 8px;">

<h2>Standalone deployment</h2>

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px;">
{% assign deployment_pages = site.pages | where: "parent", "Deployment" | sort: "guide_category_order" %}
{% for guide in deployment_pages %}
{% if guide.guide_category contains "Standalone deployment" %}
<div style="border: 1px solid #48bb78; background-color: #0d2118; padding: 0; border-radius: 4px; flex: 1 1 200px; overflow: hidden;">
<a href="{{ guide.url }}" style="text-decoration: none; color: inherit; display: block;">
{% if guide.guide_banner %}
<div style="width: 100%; height: 180px; background-image: url('{{ guide.url | replace: 'index.html', '' }}{{ guide.guide_banner }}'); background-size: cover; background-position: center; position: relative;">
<div style="position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.85), rgba(0,0,0,0.4)); padding: 15px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 5px;">
{% if guide.guide_emoji %}<span style="font-size: 2em; filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.8));">{{ guide.guide_emoji }}</span>{% endif %}
<strong style="font-size: 1.1em; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">{{ guide.title }}</strong>
</div>
<div style="font-size: 0.85em; color: #48bb78; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">
{% if guide.guide_difficulty %}{{ guide.guide_difficulty }}{% endif %}{% if guide.guide_difficulty and guide.guide_time %} • {% endif %}{% if guide.guide_time %}{{ guide.guide_time }}{% endif %}
</div>
</div>
</div>
{% else %}
<div style="padding: 10px 15px 0 15px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 5px;">
{% if guide.guide_emoji %}<span style="font-size: 2em;">{{ guide.guide_emoji }}</span>{% endif %}
<strong style="font-size: 1.1em;">{{ guide.title }}</strong>
</div>
<div style="font-size: 0.85em; color: #48bb78;">
{% if guide.guide_difficulty %}{{ guide.guide_difficulty }}{% endif %}{% if guide.guide_difficulty and guide.guide_time %} • {% endif %}{% if guide.guide_time %}{{ guide.guide_time }}{% endif %}
</div>
</div>
{% endif %}
<div style="padding: 10px 15px;">
{% if guide.guide_description %}<div style="font-size: 0.9em; margin-top: 8px; opacity: 0.9;">{{ guide.guide_description }}</div>{% endif %}
{% if guide.guide_labels %}<div style="display: flex; flex-wrap: wrap; gap: 5px; margin-top: 10px;">{% for label in guide.guide_labels %}<span style="font-size: 0.75em; padding: 2px 8px; background-color: rgba(72, 187, 120, 0.2); border: 1px solid #48bb78; border-radius: 3px; white-space: nowrap;">{{ label }}</span>{% endfor %}</div>{% endif %}
</div>
</a>
</div>
{% endif %}
{% endfor %}
</div>

</div>

<div style="border: 2px solid #9f7aea; background-color: #2d2642; padding: 5px 20px 20px 20px; margin: 20px 0; border-radius: 8px;">

<h2>Global cloud</h2>

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px;">
{% assign deployment_pages = site.pages | where: "parent", "Deployment" | sort: "guide_category_order" %}
{% for guide in deployment_pages %}
{% if guide.guide_category contains "Global cloud" %}
<div style="border: 1px solid #9f7aea; background-color: #1a1529; padding: 0; border-radius: 4px; flex: 1 1 200px; overflow: hidden;">
<a href="{{ guide.url }}" style="text-decoration: none; color: inherit; display: block;">
{% if guide.guide_banner %}
<div style="width: 100%; height: 180px; background-image: url('{{ guide.url | replace: 'index.html', '' }}{{ guide.guide_banner }}'); background-size: cover; background-position: center; position: relative;">
<div style="position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.85), rgba(0,0,0,0.4)); padding: 15px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 5px;">
{% if guide.guide_emoji %}<span style="font-size: 2em; filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.8));">{{ guide.guide_emoji }}</span>{% endif %}
<strong style="font-size: 1.1em; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">{{ guide.title }}</strong>
</div>
<div style="font-size: 0.85em; color: #9f7aea; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">
{% if guide.guide_difficulty %}{{ guide.guide_difficulty }}{% endif %}{% if guide.guide_difficulty and guide.guide_time %} • {% endif %}{% if guide.guide_time %}{{ guide.guide_time }}{% endif %}
</div>
</div>
</div>
{% else %}
<div style="padding: 10px 15px 0 15px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 5px;">
{% if guide.guide_emoji %}<span style="font-size: 2em;">{{ guide.guide_emoji }}</span>{% endif %}
<strong style="font-size: 1.1em;">{{ guide.title }}</strong>
</div>
<div style="font-size: 0.85em; color: #9f7aea;">
{% if guide.guide_difficulty %}{{ guide.guide_difficulty }}{% endif %}{% if guide.guide_difficulty and guide.guide_time %} • {% endif %}{% if guide.guide_time %}{{ guide.guide_time }}{% endif %}
</div>
</div>
{% endif %}
<div style="padding: 10px 15px;">
{% if guide.guide_description %}<div style="font-size: 0.9em; margin-top: 8px; opacity: 0.9;">{{ guide.guide_description }}</div>{% endif %}
{% if guide.guide_labels %}<div style="display: flex; flex-wrap: wrap; gap: 5px; margin-top: 10px;">{% for label in guide.guide_labels %}<span style="font-size: 0.75em; padding: 2px 8px; background-color: rgba(159, 122, 234, 0.2); border: 1px solid #9f7aea; border-radius: 3px; white-space: nowrap;">{{ label }}</span>{% endfor %}</div>{% endif %}
</div>
</a>
</div>
{% endif %}
{% endfor %}
</div>

</div>

<div style="border: 2px solid #4a9eff; background-color: #1e2a3a; padding: 5px 20px 20px 20px; margin: 20px 0; border-radius: 8px;">

<h2>European Cloud Providers</h2>

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px;">
{% assign deployment_pages = site.pages | where: "parent", "Deployment" | sort: "guide_category_order" %}
{% for guide in deployment_pages %}
{% if guide.guide_category contains "European Cloud Providers" %}
<div style="border: 1px solid #4a9eff; background-color: #0d1621; padding: 0; border-radius: 4px; flex: 1 1 200px; overflow: hidden;">
<a href="{{ guide.url }}" style="text-decoration: none; color: inherit; display: block;">
{% if guide.guide_banner %}
<div style="width: 100%; height: 180px; background-image: url('{{ guide.url | replace: 'index.html', '' }}{{ guide.guide_banner }}'); background-size: cover; background-position: center; position: relative;">
<div style="position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.85), rgba(0,0,0,0.4)); padding: 15px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 5px;">
{% if guide.guide_emoji %}<span style="font-size: 2em; filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.8));">{{ guide.guide_emoji }}</span>{% endif %}
<strong style="font-size: 1.1em; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">{{ guide.title }}</strong>
</div>
<div style="font-size: 0.85em; color: #4a9eff; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">
{% if guide.guide_difficulty %}{{ guide.guide_difficulty }}{% endif %}{% if guide.guide_difficulty and guide.guide_time %} • {% endif %}{% if guide.guide_time %}{{ guide.guide_time }}{% endif %}
</div>
</div>
</div>
{% else %}
<div style="padding: 10px 15px 0 15px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 5px;">
{% if guide.guide_emoji %}<span style="font-size: 2em;">{{ guide.guide_emoji }}</span>{% endif %}
<strong style="font-size: 1.1em;">{{ guide.title }}</strong>
</div>
<div style="font-size: 0.85em; color: #4a9eff;">
{% if guide.guide_difficulty %}{{ guide.guide_difficulty }}{% endif %}{% if guide.guide_difficulty and guide.guide_time %} • {% endif %}{% if guide.guide_time %}{{ guide.guide_time }}{% endif %}
</div>
</div>
{% endif %}
<div style="padding: 10px 15px;">
{% if guide.guide_description %}<div style="font-size: 0.9em; margin-top: 8px; opacity: 0.9;">{{ guide.guide_description }}</div>{% endif %}
{% if guide.guide_labels %}<div style="display: flex; flex-wrap: wrap; gap: 5px; margin-top: 10px;">{% for label in guide.guide_labels %}<span style="font-size: 0.75em; padding: 2px 8px; background-color: rgba(74, 158, 255, 0.2); border: 1px solid #4a9eff; border-radius: 3px; white-space: nowrap;">{{ label }}</span>{% endfor %}</div>{% endif %}
</div>
</a>
</div>
{% endif %}
{% endfor %}
</div>

</div>

<div style="border: 2px solid #f59e0b; background-color: #3a2e1e; padding: 5px 20px 20px 20px; margin: 20px 0; border-radius: 8px;">

<h2>Data centre</h2>

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px;">
{% assign deployment_pages = site.pages | where: "parent", "Deployment" | sort: "guide_category_order" %}
{% for guide in deployment_pages %}
{% if guide.guide_category contains "Data centre" %}
<div style="border: 1px solid #f59e0b; background-color: #221a10; padding: 0; border-radius: 4px; flex: 1 1 200px; overflow: hidden;">
<a href="{{ guide.url }}" style="text-decoration: none; color: inherit; display: block;">
{% if guide.guide_banner %}
<div style="width: 100%; height: 180px; background-image: url('{{ guide.url | replace: 'index.html', '' }}{{ guide.guide_banner }}'); background-size: cover; background-position: center; position: relative;">
<div style="position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.85), rgba(0,0,0,0.4)); padding: 15px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 5px;">
{% if guide.guide_emoji %}<span style="font-size: 2em; filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.8));">{{ guide.guide_emoji }}</span>{% endif %}
<strong style="font-size: 1.1em; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">{{ guide.title }}</strong>
</div>
<div style="font-size: 0.85em; color: #f59e0b; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">
{% if guide.guide_difficulty %}{{ guide.guide_difficulty }}{% endif %}{% if guide.guide_difficulty and guide.guide_time %} • {% endif %}{% if guide.guide_time %}{{ guide.guide_time }}{% endif %}
</div>
</div>
</div>
{% else %}
<div style="padding: 10px 15px 0 15px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 5px;">
{% if guide.guide_emoji %}<span style="font-size: 2em;">{{ guide.guide_emoji }}</span>{% endif %}
<strong style="font-size: 1.1em;">{{ guide.title }}</strong>
</div>
<div style="font-size: 0.85em; color: #f59e0b;">
{% if guide.guide_difficulty %}{{ guide.guide_difficulty }}{% endif %}{% if guide.guide_difficulty and guide.guide_time %} • {% endif %}{% if guide.guide_time %}{{ guide.guide_time }}{% endif %}
</div>
</div>
{% endif %}
<div style="padding: 10px 15px;">
{% if guide.guide_description %}<div style="font-size: 0.9em; margin-top: 8px; opacity: 0.9;">{{ guide.guide_description }}</div>{% endif %}
{% if guide.guide_labels %}<div style="display: flex; flex-wrap: wrap; gap: 5px; margin-top: 10px;">{% for label in guide.guide_labels %}<span style="font-size: 0.75em; padding: 2px 8px; background-color: rgba(245, 158, 11, 0.2); border: 1px solid #f59e0b; border-radius: 3px; white-space: nowrap;">{{ label }}</span>{% endfor %}</div>{% endif %}
</div>
</a>
</div>
{% endif %}
{% endfor %}
</div>

</div>
