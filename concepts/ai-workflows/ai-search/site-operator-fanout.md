---
domain: ai-workflows
subdomain: ai-search
concept: site-operator-fanout
title: ChatGPT search now uses the site:operator at scale
sources:
  - title: "ChatGPT search now uses the site:operator at scale"
    url: "https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale/"
    author: "Simon Willison"
    date: "2026-08-20T23:57:32+00:00"
  - title: "ChatGPT site operator fanouts"
    url: "https://promptwatch.com/data/chatgpt-site-operator-fanouts"
  - title: "Improving GPT-5.6 Sol in ChatGPT"
    url: "https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/"
    author: "OpenAI"
  - title: "Reddit citations are dropping in ChatGPT"
    url: "https://promptwatch.com/data/reddit-citations-are-dropping-in-chatgpt"
---

# ChatGPT search now uses the site:operator at scale

Promptwatch, an automation product that tracks prompts across ChatGPT, Claude, and Gemini, observed a dramatic increase in ChatGPT Search queries containing the site: operator. The share hovered between 0.3% and 0.5% for weeks, dipped briefly to 0.15% on August 3-5, then jumped to 16-17% on August 8. This aligns with the GPT-5.6 rollout and OpenAI's August 6th announcement about making GPT-5.6 Sol more reliable with facts and focused answers. The author notes that these figures only reflect prompts with automated tracking enabled.

OpenAI obscures system prompts, but the author believes the latest search tool has a shape like search(query, recency, domains) rather than directly encouraging a site: operator. A follow-up report from Promptwatch on August 18th indicated that ChatGPT had greatly reduced the likelihood of Reddit being used in those searches. The author's attempts to confirm whether the system prompt was updated to discourage Reddit sourcing have been unsuccessful, as the most thorough leaked system prompt collection doesn't yet show relevant changes.

- ChatGPT Search queries using site: operator jumped from ~0.3-0.5% to 16-17% after GPT-5.6 rollout.
- The shift aligns with OpenAI's vague August 6th announcement about improving GPT-5.6 Sol's fact reliability.
- Promptwatch observed a corresponding drop in Reddit citations in ChatGPT searches by August 18th.
- OpenAI's system prompts remain obscured, but the search tool likely has a structured domains parameter rather than explicit site: operator use.