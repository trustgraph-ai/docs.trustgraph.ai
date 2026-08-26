---
title: Documentation Status
nav_order: 99999
---

# Pages for Review

This page automatically lists all documentation pages that have been tagged for review.

{% assign today = site.time | date: '%Y-%m-%d' %}
{% assign today_epoch = site.time | date: '%s' | plus: 0 %}
{% assign thirty_days_epoch = today_epoch | plus: 2592000 %}
{% assign review_pages = site.pages | where_exp: "page", "page.review_date" | sort: "review_date" %}

{% assign overdue = "" | split: "" %}
{% assign upcoming = "" | split: "" %}

{% for page in review_pages %}
  {% assign review_str = page.review_date | date: '%Y-%m-%d' %}
  {% assign review_epoch = page.review_date | date: '%s' | plus: 0 %}
  {% if review_str <= today %}
    {% assign overdue = overdue | push: page %}
  {% elsif review_epoch <= thirty_days_epoch %}
    {% assign upcoming = upcoming | push: page %}
  {% endif %}
{% endfor %}

{% assign todo_pages = site.pages | where: "todo", true | sort: "title" %}

{% if review_pages.size == 0 and todo_pages.size == 0 %}

✅ **No pages are currently tagged for review or marked as incomplete.**

{% else %}

{% if todo_pages.size > 0 %}
## 🚧 Incomplete Pages ({{ todo_pages.size }})

These pages need content to be written:

| Page | Section | Notes |
|------|---------|-------|
{% for page in todo_pages %}| [{{ page.title }}]({{ page.url | relative_url }}) | {{ page.parent | default: "—" }} | {{ page.todo_notes | default: "—" }} |
{% endfor %}

{% endif %}

{% if overdue.size > 0 %}
## ⚠️ Overdue ({{ overdue.size }})

| Page | Section | Review Date |
|------|---------|-------------|
{% for page in overdue %}| [{{ page.title }}]({{ page.url | relative_url }}) | {{ page.parent | default: "—" }} | **{{ page.review_date | date: '%Y-%m-%d' }}** |
{% endfor %}

{% endif %}

{% if upcoming.size > 0 %}
## 📅 Upcoming ({{ upcoming.size }})

| Page | Section | Review Date |
|------|---------|-------------|
{% for page in upcoming %}| [{{ page.title }}]({{ page.url | relative_url }}) | {{ page.parent | default: "—" }} | {{ page.review_date | date: '%Y-%m-%d' }} |
{% endfor %}

{% endif %}

---

## How to Tag Pages

### Mark a Page for Review

Add `review_date` to the front matter:

```yaml
---
title: Your Page Title
review_date: 2025-12-01
---
```

### Mark a Page as Incomplete

Add `todo: true` and optionally `todo_notes`:

```yaml
---
title: Your Page Title
todo: true
todo_notes: Add troubleshooting tips
---
```

This will display a banner at the top of the page and list it in the "Incomplete Pages" section.

To remove from these lists, delete the respective fields or set them to `null`.

{% endif %}
