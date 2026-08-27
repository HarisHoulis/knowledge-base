---
domain: ai-workflows
subdomain: web-scraping-infrastructure
concept: web-scraping-layer
title: The Missing Layer in Agentic AI
sources:
  - title: "The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs"
    url: "https://www.youtube.com/watch?v=XsvUhpnHepE"
    author: "Giedrius Šteimantas"
    date: "2026-08-26T07:00:06+00:00"
---

# The Missing Layer in Agentic AI

In this talk, Giedrius Šteimantas from Oxylabs argues that agentic AI systems often miss a critical infrastructural layer for accessing the open web reliably and cost-effectively. He illustrates this with a friend's AI shopping assistant that used browser automation for everything, resulting in a slow, expensive, and unreliable product. The core principle borrowed from the scraping industry is that "cost matters": use a browser only when absolutely necessary, prefer lightweight content over heavy JavaScript pages, and validate content beyond a 200 HTTP response (Šteimantas, 2026).

- Use browser automation only when necessary; prefer lightweight HTTP requests to reduce cost and latency.
- Web scraping infrastructure provides stealth features to avoid captchas and bot detection, making agents more reliable.
- Relying on predefined deterministic website lists limits agent capabilities; scalable discovery requires a proper data-access layer.
- Cost predictability is essential for agent workflows, and scraping infrastructure helps manage it.