---
layout: page
title: blog
permalink: "/blog/"
description: Research notes and things I learn along the way.
nav: true
nav_order: 4
---


{% if site.posts.size > 0 %}
<ul class="post-list">
{% for post in site.posts %}
  <li><h3><a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a></h3><p>{{ post.description }}</p><p class="post-meta">{{ post.date | date: '%-d %B %Y' }}</p></li>
{% endfor %}
</ul>
{% else %}
A quiet corner for now. I’ll use this space for research notes, small discoveries, and ideas that deserve a little more room than a paper allows.
{% endif %}
