---
layout: about
title: about
permalink: "/"
subtitle: Doctoral Researcher · <a href="https://www.helsinki.fi/en">University of
  Helsinki</a>
profile:
  align: right
  image: qinhan-hou.jpg
  image_circular: false
selected_papers: true
social: true
announcements:
  enabled: false
latest_posts:
  enabled: false
---


I’m **Qinhan Hou**, a doctoral researcher at the University of Helsinki. I study how information moves through graph models, and how the structure of a graph shapes what a model can learn.

My work moves between theory and experiments with **graph neural networks, Graph ODEs, and Graph Transformers**. I’m especially interested in what happens as information travels farther: when it helps, when useful differences disappear, and how a model can adapt its connections to the task.

Before Helsinki, I worked with **Jürgen Schmidhuber’s group at the Swiss AI Lab IDSIA**, developing machine learning methods for EMG-based silent speech interfaces. At **Uppsala University’s Deindl Lab**, I worked on computational tools for single-molecule biophysics. These experiences keep me curious about the meeting point of learning methods and biological data.

I hold an MSc in Computer Science from Uppsala University and a BEng in Software Engineering from Tianjin University. Away from my day-to-day research, I enjoy learning with others through summer schools, teaching, and collaborative projects.

## research

- **Graph dynamics and information flow.** How can continuous-depth models preserve useful differences between nodes? In our [Graph ODE work]({{ '/publication/hysteretic-graph-odes/' | relative_url }}), we study feature collapse and let the graph topology evolve along with its features.
- **Structure and task locality.** How far should a model look? I explore [Graph Transformer training](https://arxiv.org/abs/2604.22413) that adapts to the distances at which a task’s useful information lives.
- **Heterophily and graph-level learning.** I study how [local motifs and mixed-frequency dynamics]({{ '/publication/heterophily-graph-level-tasks/' | relative_url }}) shape graph prediction, including molecular property prediction.
- **Learning from biological signals.** My earlier work spans self-supervised learning for silent speech and computational analysis of single-molecule dynamics. I’m interested in bringing these biological questions into conversation with graph learning.

## learning and sharing

A few recent stops along the way:

{% assign recent_activities = site.data.activities | sort: 'date' | reverse %}
<ul class="recent-activities">
{% for activity in recent_activities limit:3 %}
  <li><span class="activity-date">{{ activity.date | date: '%b %Y' }}</span><div><a href="{{ '/activities/' | relative_url }}#{{ activity.id }}">{{ activity.short_title }}</a><p>{{ activity.highlight }}</p></div></li>
{% endfor %}
</ul>

[More from these events]({{ '/activities/' | relative_url }}) · [Teaching & supervision]({{ '/teaching/' | relative_url }}) · [CV]({{ '/cv/' | relative_url }})
