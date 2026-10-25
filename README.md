# Qinhan Hou — academic homepage

Website: https://silentstars.github.io/

An academic website based on [Academic Pages](https://github.com/academicpages/academicpages.github.io), hosted on GitHub Pages.

## Update the content

| Content | File |
| --- | --- |
| Name, affiliation, public contact details, scholarly links | `_config.yml` |
| Biography and research interests | `_pages/about.md` |
| Navigation | `_data/navigation.yml` |
| CV | `_pages/cv.md` |
| Individual publications | `_publications/` |
| Talks and presentations | `_talks/` |
| Teaching | `_teaching/` |
| Portrait or initials | `images/profile.svg`, configured in `_config.yml` |
| PDFs and other downloads | `files/` |

Only the owner-provided name, affiliation and Google Scholar link have been populated. Research interests, positions, CV details, and individual publications await the owner's content. Template sample publications, talks, teaching, blog posts, comments and CV claims have been removed.

For a publication, add a Markdown file to `_publications/` with YAML front matter containing `title`, `collection: publications`, `category: manuscripts` (or `conferences` / `books`), `date`, `venue`, and `citation`. See the [Academic Pages documentation](https://academicpages.github.io/markdown/) for supported fields.

## Publishing

Push changes to `master`. The `Deploy academic homepage` GitHub Actions workflow builds the site with Jekyll and deploys it to Pages. In repository Settings → Pages, the source must be **GitHub Actions**.

## Local preview

Use Ruby 3.3 and Bundler:

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve
```

## Credits

Based on Academic Pages and the Minimal Mistakes theme. The original MIT license and theme attribution are retained in `LICENSE` and the site footer.
