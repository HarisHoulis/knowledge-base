---
domain: python-backend
subdomain: browser-automation
concept: webp-screenshot-output
title: shot-scraper 1.12 adds WebP screenshot support
sources:
  - title: "shot-scraper 1.12"
    url: "https://simonwillison.net/2026/Sep/13/shot-scraper/"
    author: "Simon Willison"
    date: "2026-09-13"
---

# shot-scraper 1.12 adds WebP screenshot support

shot-scraper 1.12, Simon Willison's screenshot automation tool, adds WebP as an output format. A WebP screenshot can be taken with `shot-scraper https://simonwillison.net -o screenshot.webp --quality 80`, where the `--quality` option controls compression; omitting it produces a lossless WebP file.

According to the author, WebP screenshots are "almost always significantly smaller in file size" than equivalent JPEG or PNG files, with examples provided in the associated pull request. The feature was shipped specifically to generate the screenshot for a new commit-rewriter tool.

The release is tagged with playwright and shot-scraper.

- shot-scraper 1.12 adds WebP output, selectable via a `.webp` output filename.
- The `--quality` flag sets WebP compression quality; without it, output is lossless.
- The author reports WebP screenshots are almost always significantly smaller than JPEG or PNG equivalents.
- The feature was motivated by needing a screenshot for the author's commit-rewriter tool.