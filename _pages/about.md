---
permalink: /
title: "About"
excerpt: "Academic homepage of Qinhan Hou at the University of Helsinki."
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am **Qinhan Hou** at the [University of Helsinki](https://www.helsinki.fi/en).

## Research

Research interests and current projects will be added here.

## Selected publications

{% assign selected_publications = site.publications | where: "selected", true | sort: "date" | reverse %}
{% for publication in selected_publications %}
{% include publication-entry.html publication=publication %}
{% endfor %}

[All publications]({{ "/publications/" | relative_url }}) &middot; [Google Scholar](https://scholar.google.com/citations?user=Mp2BNQsAAAAJ&hl=en)

## Learning and sharing

A few places where I’ve been learning with others and sharing my research.

{% assign recent_activities = site.data.activities | sort: "date" | reverse %}
<ul>
{% for activity in recent_activities limit:3 %}
  <li><strong><a href="{{ "/activities/" | relative_url }}#{{ activity.id | escape }}">{{ activity.short_title | escape }}</a></strong> &middot; {{ activity.date | date: "%B %Y" }} &middot; {{ activity.kind_label | escape }}<br>{{ activity.highlight | escape }}</li>
{% endfor %}
</ul>

[More from these events]({{ "/activities/" | relative_url }})

## More

- [Curriculum vitae](/cv/)
- [GitHub](https://github.com/SilentStars)
