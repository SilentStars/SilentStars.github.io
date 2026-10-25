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

## More

- [Curriculum vitae](/cv/)
- [GitHub](https://github.com/SilentStars)
