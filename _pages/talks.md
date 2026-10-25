---
layout: page
title: talks & posters
permalink: "/talks/"
description: A few occasions to put ideas into words and pictures.
---


## 2026

{% assign posters = site.data.activities | where: 'kind', 'poster' %}
{% for activity in posters %}{% include activity-entry.liquid activity=activity %}{% endfor %}

## 2024

**emg2vec: Self-supervised Pretraining in Electromyography-based Silent Speech Interfaces**<br>
Oral presentation · IEEE EMBC 2024 · 15–19 July 2024<br>
[Paper](https://doi.org/10.1109/EMBC53108.2024.10781736)

## 2020

**Decoding Music Genres Based on High Resolution Brain Activity Information**<br>
Oral presentation · APSIPA ASC 2020 · 7–10 December 2020
