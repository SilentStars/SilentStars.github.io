---
layout: page
title: activities
permalink: "/activities/"
description: Summer schools, conversations, and places where I’ve shared my work.
nav: true
nav_order: 2
---


From a bioinformatics course in Copenhagen to a group project in London and a poster in Madrid, here are a few places I’ve been learning and sharing ideas.

{% assign activities = site.data.activities | sort: 'date' | reverse %}
{% assign current_year = '' %}
{% for activity in activities %}
  {% assign activity_year = activity.date | date: '%Y' %}
  {% if activity_year != current_year %}
    <h2>{{ activity_year }}</h2>
    {% assign current_year = activity_year %}
  {% endif %}
  {% include activity-entry.liquid activity=activity %}
{% endfor %}

## behind the scenes

I’ve also helped with local organising for **ISBRA 2025 in Helsinki** and **ICANN in Lugano (2023–2024)**. I review for machine learning conferences and biomedical journals, including NeurIPS 2025, ICML 2026, and NeurIPS 2026, and received **Gold Reviewer recognition at ICML 2026**.
