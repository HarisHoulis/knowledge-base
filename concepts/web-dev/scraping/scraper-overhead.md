---
domain: web-dev
subdomain: scraping
concept: scraper-overhead
title: Creepy crawlies
sources:
  - title: "Creepy crawlies"
    url: "https://simonwillison.net/2026/Sep/7/creepy-crawlies/"
    date: "2026-09-07T23:08:58+00:00"
---

# Creepy crawlies

According to the post, rendering git commits as HTML for scrapers consumes more CPU than all other legitimate access combined, including git clones. The author notes that across five geo-distributed nodes, 14 CPU cores are continuously dedicated solely to rendering commits as HTML for scrapers. This observation raises concerns for projects like Datasette, which serve a large number of crawlable web pages and may face similar overhead from automated scrapers.

- CPU spent rendering HTML for scrapers exceeds that for all legitimate access combined, including git clones.
- 14 CPU cores across 5 geo-distributed nodes are continuously used to render commits as HTML for scrapers.
- The author worries about similar scraper overhead for crawlable web projects like Datasette.