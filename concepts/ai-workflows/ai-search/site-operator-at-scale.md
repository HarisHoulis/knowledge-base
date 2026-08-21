---
domain: ai-workflows
subdomain: ai-search
concept: site-operator-at-scale
title: ChatGPT search now uses the site:operator at scale
sources:
  - title: "ChatGPT search now uses the site:operator at scale"
    url: "https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale/"
    author: "Simon Willison"
    date: "2026-08-20T23:57:32+00:00"
---

# ChatGPT search now uses the site:operator at scale

Promptwatch's automated tracking of ChatGPT search prompts revealed a dramatic increase in the use of the `site:` operator, jumping from 0.3-0.5% of fanout queries to 16-17% around August 8, 2026, coinciding with the GPT-5.6 rollout. This shift aligns with OpenAI's vague announcement about making GPT-5.6 Sol more reliable with facts and providing more focused answers, but OpenAI has actively obscured their system prompts, making direct verification difficult. The change suggests ChatGPT's search tool may now internally structure queries with a `domains` parameter rather than encouraging users to use `site:` directly. A follow-up report from Promptwatch on August 18 indicated a notable reduction in Reddit citations within these searches, though no corresponding system prompt change has been confirmed in leaked collections.

- Promptwatch data shows ChatGPT Search's fanout queries with `site:` operator jumped from ~0.4% to 16-17% on August 8, 2026.
- This change aligns with the GPT-5.6 rollout and OpenAI's announcement of more factual and focused answers.
- OpenAI obscures system prompts, but the search tool likely uses a `domains` parameter internally rather than explicit `site:` prompts.
- Reddit citations in ChatGPT search appear to have dropped significantly around August 18, per Promptwatch.