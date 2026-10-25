# Qinhan Hou 的学术主页

网址：https://silentstars.github.io/<br>
主题：[al-folio](https://github.com/alshedivat/al-folio) · GitHub Pages 免费托管

本地仓库放在 `/Users/qinhanhou/Sync/blog`。修改文字后提交并推送，GitHub 会自动更新网站；一般等 Actions 中的部署完成后就能看到。

## 内容改哪里

| 想更新的内容 | 文件 |
| --- | --- |
| 首页简介、研究方向、近期活动区的位置 | `_pages/about.md` |
| 论文列表和首页精选论文 | `_bibliography/papers.bib` |
| 暑校、poster 等活动 | `_data/activities.yml` |
| 教学和指导学生 | `_pages/teaching.md` |
| 网页版 CV | `_data/cv.yml` |
| 供下载的 CV | `assets/pdf/cv.pdf` |
| 邮箱、Scholar、ORCID、GitHub 链接 | `_data/socials.yml` |
| 个人照片 | `assets/img/qinhan-hou.jpg` |
| 配色和照片的网页显示比例 | `_sass/_personal.scss` |

CV 的可编辑源文件仍在 `/Users/qinhanhou/Sync/cv/general/cv.tex`。更新并生成 PDF 后，把新 PDF 放到 `assets/pdf/cv.pdf`，并同步 `_data/cv.yml` 中对应的经历。

## 加一篇论文

在 `_bibliography/papers.bib` 里复制一个现有条目，改标题、作者、年份、会议和链接即可。`selected = {true}` 会把它展示在首页；不想放首页就删掉该字段。Workshop、extended abstract、accepted main track 等状态请保留清楚。

主会论文使用新标题 *Avoiding Feature Collapse in Graph ODEs via Hysteretic Topology Evolution*。arXiv:2604.24293 仍是较早版本，因此保留相应说明。

## 写博客

在 `_posts/` 新建 `YYYY-MM-DD-title.md`。开头可以这样写，之后在分隔线下写正文：

```yaml
---
layout: post
title: "文章标题"
date: 2026-10-25
description: "一句话介绍"
tags: [graph-learning]
categories: [research]
---
```

博客目前留有真实的空状态，没有填充示例文章。`_drafts/` 中的内容不会发布。

## 保存并发布

```bash
cd /Users/qinhanhou/Sync/blog
git add .
git commit -m "Help readers find my latest research"
git push origin master
```

也可以直接在 GitHub 网页上打开相应文件，点铅笔编辑，再提交。部署状态见仓库的 Actions 标签。

## 本地预览（可选）

使用 Ruby 3.3、Bundler 和 ImageMagick：

```bash
bundle install
bundle exec jekyll serve
```

浏览器打开 http://localhost:4000/。修改 `_config.yml` 后需要重启预览。正常更新内容不需要在电脑上安装这些工具，GitHub Actions 会负责构建。

设计约定见 DESIGN.md；主题来源和更新说明见 THEME.md。
