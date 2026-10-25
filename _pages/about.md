---
permalink: /
title: "About"
excerpt: "Qinhan Hou at the University of Helsinki, exploring graph learning, information flow and molecular data."
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I’m **Qinhan Hou**, and I work on graph machine learning at the [University of Helsinki](https://www.helsinki.fi/en). I study how information moves through graph models and how their structure and dynamics shape what they can learn.

I move between theory and experiments, working with GNNs, Graph ODEs and Graph Transformers. Recent summer schools and collaborative projects have given me opportunities to connect these interests with geometry and bioinformatics.

## Research

A few themes run through my current work:

- **Graph dynamics and information flow.** I study how node representations evolve during propagation, including [feature collapse in Graph ODEs]({{ "/publication/hysteretic-graph-odes/" | relative_url }}) and how adaptive topology can help preserve useful differences.
- **Graph structure and task locality.** I explore how [Graph Transformers](https://arxiv.org/abs/2604.22413) can match their communication to where a task’s useful information lives, from nearby neighbors to more distant parts of a graph.
- **Heterophily and graph-level learning.** My work looks at how [local motifs and mixed-frequency dynamics]({{ "/publication/heterophily-graph-level-tasks/" | relative_url }}) affect graph prediction, and how models can combine different kinds of structural signals.
- **Molecular and biological applications.** I’m interested in graph methods for molecular property prediction, and in the broader connections between deep learning and bioinformatics.

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
