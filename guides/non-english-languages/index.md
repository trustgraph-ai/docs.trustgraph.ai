---
title: Working with non-English languages
nav_order: 10
parent: Common knowledge management tasks
grand_parent: How-to Guides
review_date: 2026-08-01
guide_category:
  - Common knowledge management tasks
guide_category_order: 10
guide_description: Context graphs are language-sensitive, and can easily be
  built in any language, provided that you have access to an LLM which
  is proficient in your preferred language
guide_difficulty: intermediate
guide_time: 30 min
guide_banner: language.jpg
guide_emoji: 🌍
guide_labels:
  - Multilingual
  - Internationalization
  - Context Graph
---

# Working with non-English languages

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>TrustGraph deployed (<a href="../getting-started/quickstart">Quick Start</a>)</li>
<li>Understanding of <a href="../getting-started/concepts">Core Concepts</a></li>
<li>An LLM with proficiency in your target language</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Build a context graph from non-English documents and query it in your preferred language."
%}

TrustGraph uses an LLM to extract knowledge and build context graphs from your
documents. To work in a non-English language, you simply need a model that is
proficient in your preferred language. Most modern LLMs support multiple
languages, so building a context graph in French, German, Japanese or any
other widely-used language is straightforward.
