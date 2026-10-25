#!/usr/bin/env python3
"""Smoke-check the generated site, including its local asset and page links."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse
import sys


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for attr in ("href", "src"):
            if attrs.get(attr):
                self.urls.append(attrs[attr])


root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
required = [
    "index.html",
    "publications/index.html",
    "activities/index.html",
    "teaching/index.html",
    "blog/index.html",
    "cv/index.html",
    "talks/index.html",
    "publication/hysteretic-graph-odes/index.html",
    "publication/heterophily-graph-level-tasks/index.html",
    "assets/img/qinhan-hou.jpg",
    "assets/pdf/cv.pdf",
    "assets/css/main.css",
    "assets/css/tailwind.css",
]
errors = []
for relative in required:
    path = root / relative
    if not path.is_file() or not path.stat().st_size:
        errors.append(f"Missing or empty: {relative}")

parsers = {}
for path in root.rglob("*.html"):
    parser = Links()
    parser.feed(path.read_text())
    parsers[path] = parser

for path, parser in parsers.items():
    relative = path.relative_to(root).as_posix()
    current_url = "/" + relative.removesuffix("index.html")
    for link in parser.urls:
        if link.startswith(("mailto:", "tel:", "data:", "javascript:")):
            continue
        target_url = urlparse(urljoin("https://silentstars.github.io" + current_url, link))
        if target_url.netloc != "silentstars.github.io":
            continue
        target = root / unquote(target_url.path).lstrip("/")
        if target.is_dir():
            target /= "index.html"
        if not target.is_file():
            errors.append(f"{relative}: broken local link {link}")
        elif target_url.fragment and target in parsers:
            fragment = unquote(target_url.fragment)
            if fragment and fragment not in parsers[target].ids:
                errors.append(f"{relative}: missing anchor {link}")

if (root / "index.html").is_file():
    home = (root / "index.html").read_text()
    for text in ["Qinhan", "Doctoral Researcher", "University of Helsinki", "IDSIA", "Deindl", "qinhan-hou.jpg"]:
        if text not in home:
            errors.append(f"Homepage missing: {text}")
if (root / "publications/index.html").is_file():
    publications = (root / "publications/index.html").read_text()
    for text in ["Avoiding Feature Collapse", "Exploring Heterophily", "Distance-Misaligned", "single-molecule dynamics", "emg2vec", "Diff-ETS", "Cross-Speaker", "Decoding Music Genres"]:
        if text not in publications:
            errors.append(f"Publications missing: {text}")
if (root / "assets/pdf/cv.pdf").is_file() and not (root / "assets/pdf/cv.pdf").read_bytes().startswith(b"%PDF-"):
    errors.append("CV download is not a PDF")

if errors:
    print("\n".join(sorted(set(errors))))
    raise SystemExit(1)
print(f"PASS: {len(required)} required outputs and links across {len(parsers)} HTML pages.")
