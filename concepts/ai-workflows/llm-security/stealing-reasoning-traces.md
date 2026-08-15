---
domain: ai-workflows
subdomain: llm-security
concept: stealing-reasoning-traces
title: Stealing Reasoning Traces from Proprietary LLM APIs
sources:
  - title: "Stealing Reasoning Traces from Proprietary LLM APIs"
    url: "https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/"
    author: "Simon Willison"
    date: "2026-08-11T22:40:45+00:00"
---

# Stealing Reasoning Traces from Proprietary LLM APIs

All model providers acknowledged the report and subsequently fixed the attack, so the specific technique no longer works. However, the article underscores broader security concerns: encryption of reasoning traces is insufficient when key reuse and weaker sibling models exist, and reasoning traces themselves can be manipulated to bypass safety measures. The post concludes by linking to the original paper and Hacker News discussion, emphasizing that this is an active area of vulnerability research in AI workflows (Willison, 2026).

- Proprietary LLM APIs return encrypted chain-of-thought blocks that can be decrypted by replaying them into weaker sibling models using the same encryption key.
- The attack was demonstrated against Anthropic, OpenAI, and Google, with Claude Haiku 4.5 being the easiest target due to its support for prefilled responses.
- A prompt-injection variant can trick a model into encoding harmful instructions into its reasoning trace, which another model may then treat as trusted and follow.
- All providers have fixed the specific vulnerability, but the paper highlights the ongoing risk of reasoning-trace exfiltration and manipulation in LLM deployments.