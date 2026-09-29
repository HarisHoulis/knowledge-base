---
domain: python-backend
subdomain: serverless-edge-runtimes
concept: python-workers-ga
title: Python Workers Reach GA on Cloudflare, with Questions About Cold Starts and Upstream Maintenance
sources:
  - title: "Python Workers Reach GA on Cloudflare, with Questions About Cold Starts and Upstream Maintenance"
    url: "https://www.infoq.com/news/2026/09/cloudflare-python-workers-ga/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Steef-Jan Wiggers"
    date: "2026-09-29"
---

# Python Workers Reach GA on Cloudflare, with Questions About Cold Starts and Upstream Maintenance

Cloudflare has made Python Workers generally available. The implementation is built on PEP 783 and on socket syscalls implemented over the Workers connect API (source).

The GA announcement carries no performance figures. In response, a urllib3 maintainer questioned who will support the upstream work afterwards, and Wasmer's founder asked for cold-start numbers, citing roughly 1.027 seconds from Cloudflare's own earlier post (source).

- Cloudflare's Python Workers are now generally available, built on PEP 783 and socket syscalls over the Workers connect API.
- The GA announcement includes no performance figures.
- Commenters raised two open concerns: long-term upstream maintenance support (from a urllib3 maintainer) and cold-start latency, with Wasmer's founder citing ~1.027s from an earlier Cloudflare post.