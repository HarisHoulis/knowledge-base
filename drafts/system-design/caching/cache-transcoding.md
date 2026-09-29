---
domain: system-design
subdomain: caching
concept: cache-transcoding
title: Cloudflare Prototypes Cache Transcoding with Zstandard to Expand Effective Cache Capacity
sources:
  - title: "Cloudflare Tests Cache Transcoding to Reduce Storage Requirements"
    url: "https://www.infoq.com/news/2026/09/cloudflare-cache-transcoding/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Renato Losio"
    date: "Sun, 13 Sep 2026 10:35:00 GMT"
---

# Cloudflare Prototypes Cache Transcoding with Zstandard to Expand Effective Cache Capacity

Cloudflare has described a prototype called Cache Transcoding that compresses eligible cache content before storing it on disk (InfoQ). The approach focuses mainly on uncompressed text formats such as HTML, JSON, CSS, and JavaScript, and uses Zstandard as the compression algorithm (InfoQ).

Cloudflare estimates that Cache Transcoding could provide petabytes of additional effective cache capacity, though the company says broader testing is still needed (InfoQ).

- Cloudflare's Cache Transcoding prototype targets uncompressed text cache content, including HTML, JSON, CSS, and JavaScript (InfoQ).
- It uses Zstandard to compress eligible content before storing it on disk (InfoQ).
- Cloudflare estimates the approach could yield petabytes of additional effective cache capacity (InfoQ).
- Broader testing is still required before wider adoption (InfoQ).