---
domain: ai-workflows
subdomain: web-personalization
concept: agentic-sites
title: Agentic Sites: Building Hyper Personalized Websites
sources:
  - title: "Agentic Sites: Building Hyper Personalized Websites — Carlos Sanchez, Adobe"
    url: "https://www.youtube.com/watch?v=jebp4V0vh30"
    author: "AI Engineer"
    date: "2026-08-29T17:00:17+00:00"
---

# Agentic Sites: Building Hyper Personalized Websites

Carlos Sanchez demonstrates an agentic site that assembles itself in under two seconds for a query like "coffee machine for camping." The goal is an "audience of one" — a fully personalized page generated for a single user. The site is generated using a tool that can turn any URL into an agentic site in about an hour.

To avoid hallucinations, the system limits generation to specific blocks (hero, product list, navigation, calls to action) and grounds everything using the site's own content as a corpus. Model choice is per site, evaluated continuously for accuracy and speed; the fastest config averaged 1.1 seconds vs 4.6 for the runner-up. Sanchez argues a frontier model isn't needed because the work is choosing and arranging blocks.

The architecture includes pre-generating pages before they are requested, and letting marketers define personas. In a live demo, signals and buckets drive a "For You" page. This approach enables dynamic personalization at scale while staying grounded in brand guidelines.

- Personalization happens at the block level (hero, product list, CTA), not by generating entire pages from scratch.
- Grounding generation in the site's own corpus prevents hallucination and keeps brand guidelines intact.
- Model selection is evaluated per site for both accuracy and speed; the fastest configuration averaged 1.1 seconds versus 4.6 seconds for the runner-up.
- Frontier models are not required; the core task is choosing and arranging existing blocks.
- Any URL can be turned into an agentic site in about an hour, with pre-generated pages possible before a request arrives.