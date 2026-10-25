# Qinhan Hou — academic homepage

网站：https://silentstars.github.io/

使用 [Academic Pages](https://github.com/academicpages/academicpages.github.io) 模板，通过 GitHub Pages 发布。

## 以后怎么更新

可以直接在本对话发来新内容，让助手更新并发布。自己修改时，在 GitHub 打开对应文件，点击铅笔编辑，选择 **Commit changes**，提交到 `master` 分支。GitHub Actions 构建、发布成功后，网站会自动更新。

| 想修改的内容 | 对应文件 |
| --- | --- |
| 姓名、单位、公开邮箱、学术账号链接 | `_config.yml` |
| 首页简介、研究方向 | `_pages/about.md` |
| 导航栏目 | `_data/navigation.yml` |
| CV | `_pages/cv.md` |
| 每篇论文的标题、作者、会议和链接 | `_publications/` 中对应的 Markdown 文件 |
| 学术报告 | `_talks/` |
| 教学经历 | `_teaching/` |
| 头像 | `images/profile.svg`，或在 `_config.yml` 中设置其他图片 |
| PDF、BibTeX 等下载文件 | `files/` |

目前论文展示包含 NeurIPS 2026 主会论文和 NeurIPS 2025 NPGML Workshop 论文。主会条目采用作者确认的新标题，arXiv 链接注明为早期版本。研究方向和 CV 详情待补充。

## 新增一篇论文

在 `_publications/` 新建 `YYYY-MM-DD-short-title.md`，参考已有的两篇论文。标题、作者、摘要等写在文件开头的 YAML 区域，`---` 后是详情页正文。

```yaml
---
title: "论文标题"
collection: publications
category: conferences
permalink: /publication/unique-short-title/
date: "2026-10-25"
venue: "会议名称"
track: "Main Track"
publication_status: "Accepted at"
selected: true
authors: ["Qinhan Hou", "合作者姓名"]
excerpt: "一句话介绍这篇论文。"
arxivurl: "https://arxiv.org/abs/实际编号"
paperurl: "https://arxiv.org/pdf/实际编号"
bibtexurl: "/files/对应的引用文件.bib"
---
```

- `category: conferences` 为主会；`category: workshops` 为 Workshop。
- `selected: true` 会自动显示在首页；所有条目都会显示在 Publications 页。
- `publication_status` 可用 `Accepted at` 或 `Presented at`；`status_label: "Accepted"` 可显示录用提示。
- 主会论文的早期 arXiv 版本可用 `arxiv_label: "arXiv (earlier version)"`。
- 详情页正文可参考已有文件，使用 `publication-entry.html` 展示作者和原文入口，再补充工作介绍。
- 论文介绍组件为 `_includes/publication-entry.html`，样式为 `assets/css/publications.css`。首页和 Publications 页共用同一份论文资料。

## 发布与检查

`Deploy academic homepage` 工作流会在 `master` 有新提交后构建并部署。仓库 **Settings → Pages → Source** 使用 **GitHub Actions**。可在仓库的 **Actions** 页面查看是否发布成功。

## 本地预览

完整克隆仓库后，使用 Ruby 3.3 和 Bundler：

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve
```

## Credits

Based on Academic Pages and the Minimal Mistakes theme. The original MIT license and theme attribution are retained in `LICENSE` and the site footer.
