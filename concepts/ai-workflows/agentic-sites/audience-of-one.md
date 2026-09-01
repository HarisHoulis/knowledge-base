---
domain: ai-workflows
subdomain: agentic-sites
concept: audience-of-one
title: Agentic Sites: Building Hyper Personalized Websites
sources:
  - title: "Agentic Sites: Building Hyper Personalized Websites — Carlos Sanchez, Adobe"
    url: "https://www.youtube.com/watch?v=jebp4V0vh30"
    author: "Carlos Sanchez"
    date: "2026-08-29T17:00:17+00:00"
---

# Agentic Sites: Building Hyper Personalized Websites

Agentic sites are websites that assemble themselves in real time for each visitor, targeting what Carlos Sanchez describes as an 'audience of one'. In a live demo, a request for a camping coffee machine generates a fully personalized page with product listings, customized copy, and tips in under two seconds. The tool can also transform any URL into an agentic site in about an hour, producing context-aware content such as a side-by-side conference comparison for the AI Engineer site. This approach aims to deliver the marketer's long-sought personalized experience, but at scale and cost-effectively (source: Carlos Sanchez, AI Engineer).

To avoid hallucinations, very little content is actually generated from scratch. The site itself acts as a strict corpus for retrieval-augmented generation, grounding every output in brand guidelines and existing content. Only selected blocks—hero, product list, navigation, calls to action—change dynamically. Model selection is per site and continuously evaluated for both accuracy and speed, ensuring pages generate quickly; the fastest configuration averaged 1.1 seconds versus 4.6 seconds for the runner-up. Sanchez emphasizes that frontier models are unnecessary because the task is centered on choosing and arranging pre-designed blocks, not writing an entire page from nothing (source: Carlos Sanchez).

- Agentic sites generate pages tailored to a specific query and user in under two seconds, targeting an 'audience of one'.
- Only dynamic blocks (hero, products, nav, CTA) are generated; all output is grounded in the site's own content to avoid hallucination.
- LLM choice is per site, evaluated for both accuracy and speed; the fastest setup reached 1.1 seconds vs 4.6 seconds for the alternative.
- Frontier models are not required, as the core work is selecting and arranging content blocks rather than generating everything.
- Any URL can be turned into an agentic site in about an hour, as demonstrated by generating a conference comparison for AI Engineer's site.