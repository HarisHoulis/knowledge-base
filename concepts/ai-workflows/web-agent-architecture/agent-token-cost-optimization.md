---
domain: ai-workflows
subdomain: web-agent-architecture
concept: agent-token-cost-optimization
title: The Missing Layer in Agentic AI
sources:
  - title: "The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs"
    url: "https://www.youtube.com/watch?v=XsvUhpnHepE"
    author: "AI Engineer"
    date: "2026-08-24T23:35:46+00:00"
---

# The Missing Layer in Agentic AI

Giedrius Šteimantas, drawing on ten years of scraping at Oxylabs, argues that the real bottleneck in agentic AI is not model quality but the layer underneath that lets an agent work on the open web. He illustrates this with a friend's personal shopping agent that used browser automation at every stage, making it slow, expensive, and unreliable. A critical insight is that a 200 status code does not mean the page is real: agents often waste seventy percent of their tokens on CAPTCHAs because blocked pages still return valid-looking responses.

- Use a browser only when absolutely necessary; a search API returns compact JSON in ~700ms and under 2,000 tokens for discovery.
- For decision stages, a scraper that returns markdown and fails loudly on blocks is far cheaper and more reliable than browser automation.
- Reserve browser automation for checkout, where it is actually required, and harden it with stealth, residential proxies, and geolocation.
- Validate that the output is real before spending tokens; a 200 status code and response size are not sufficient to detect blocked content.