---
domain: ai-workflows
subdomain: ai-search
concept: site-operator-fanout
title: ChatGPT search now uses the site:operator at scale
sources:
  - title: "ChatGPT search now uses the site:operator at scale"
    url: "https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale/"
    date: "2026-08-20"
---

# ChatGPT search now uses the site:operator at scale

Promptwatch, a product that tracks prompts across chat products, observed a dramatic increase in ChatGPT Search queries containing the `site:` operator. The share hovered between 0.3% and 0.5% for weeks, briefly dipped to 0.15% on August 3-5, then jumped to 16-17% on August 8. This aligns with the rollout of GPT-5.6 and OpenAI's August 6th announcement about making GPT-5.6 Sol in Chat more reliable with facts and providing more focused answers.

- Promptwatch data shows the percentage of ChatGPT Search fanout queries containing `site:` rose from 0.3-0.5% to 16-17% after August 8.
- The change is consistent with a staged rollout or pre-launch experiment, with a brief dip to 0.15% on August 3-5.
- OpenAI's official announcement on August 6th mentioned improvements to GPT-5.6 Sol for reliability and focused answers, though it did not specifically mention search operators.
- The author suspects the underlying search tool may use parameters like `search(query, recency, domains)` rather than directly encouraging a `site:` operator, but OpenAI's system prompts are obscured.
- A follow-up Promptwatch report on August 18th indicated ChatGPT reduced the likelihood of sourcing from Reddit, though system prompt leaks have not yet shown relevant changes.