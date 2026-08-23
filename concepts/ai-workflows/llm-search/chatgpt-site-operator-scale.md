---
domain: ai-workflows
subdomain: llm-search
concept: chatgpt-site-operator-scale
title: ChatGPT search now uses the site:operator at scale
sources:
  - title: "ChatGPT search now uses the site:operator at scale"
    url: "https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale/"
    author: "Simon Willison"
    date: "2026-08-20"
---

# ChatGPT search now uses the site:operator at scale

Promptwatch's automated tracking of ChatGPT prompts shows a dramatic increase in search queries containing the site: operator, jumping from about 0.3–0.5% to 16–17% around August 8, 2026, coinciding with the GPT-5.6 rollout. The data suggests a staged rollout, with a brief dip to 0.15% on August 3–5, before the surge. This aligns with OpenAI's August 6th announcement about improving GPT-5.6 Sol's factual reliability and answer focus, though OpenAI's exact implementation remains unclear due to their deliberate obscuring of system prompts.

- Promptwatch observed a spike in site: operator usage in ChatGPT search fanouts from <0.5% to 16–17% after GPT-5.6.
- The change aligns with OpenAI's vague announcement about GPT-5.6 Sol improvements on August 6th.
- The author speculates the underlying search tool may now accept a `search(query, recency, domains)` shape rather than directly encouraging `site:`.
- A follow-up report suggests ChatGPT has reduced the likelihood of Reddit citations in search results.