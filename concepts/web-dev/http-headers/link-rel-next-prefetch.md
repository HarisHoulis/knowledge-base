---
domain: web-dev
subdomain: http-headers
concept: link-rel-next-prefetch
title: Datasette #3046: Don't Serve link rel=next HTTP Headers to Firefox for HTML Pages
sources:
  - title: "datasette #3046: Don't serve link: rel=next HTTP headers to Firefox for HTML pages"
    url: "https://simonwillison.net/2026/Nov/7/link-rel-next/"
    author: "Simon Willison"
    date: "2026-11-07"
---

# Datasette #3046: Don't Serve link rel=next HTTP Headers to Firefox for HTML Pages

Datasette pages were serving an HTTP `link` header pointing to the next page of results, e.g. `link: <...?_next=...>; rel="next"`. This caused Firefox to prefetch that next page, so a small fraction of visitors triggered unnecessary data fetching and full server-side page renders that were then discarded (Simon Willison, 2026).

The behavior traces to a Firefox bug open for 24 years, and an early comment on that issue links to Willison's own 2002 blog post complaining about the same prefetching feature—a detail he had entirely forgotten. The fix in issue #3046 is to stop serving the `link: rel=next` header to Firefox for HTML pages.

- Serving `link: rel=next` HTTP headers causes Firefox to prefetch the next page
- Prefetching wastes bandwidth and forces Datasette to render pages that get thrown away
- The underlying Firefox behavior has an issue open for 24 years
- Fix: don't serve the header to Firefox for HTML pages