---
domain: ai-workflows
subdomain: llm-releases
concept: open-weight-frontier-models
title: Introducing Kimi K3.1 Pro
sources:
  - title: "Introducing Kimi K3.1 Pro"
    url: "https://simonwillison.net/2026/Oct/23/kimi-k31-pro/"
    author: "Simon Willison"
    date: "2026-10-23"
---

# Introducing Kimi K3.1 Pro

Moonshot released Kimi K3.1 Pro, priced at $2.00/million input tokens and $10/million output tokens in USD, matching GPT-6.1 Sol and half the price of Claude Opus 5.5. A "Highspeed" variant runs 2-3x faster at twice the price, except for input token cache hits, which are priced the same.

Moonshot's own benchmarks place Kimi roughly level with Opus 5.5 and GPT-6 Astra, beating them on a few benchmarks and coming close on others. Artificial Analysis scored Kimi at 55, ahead of Claude Fable 5.1, GPT-6 Astra, and Gemini 4 Argon (all at 53) and behind only Claude Opus 5.5 (58). Simon Willison notes this is the first time a soon-to-be open weight model has scored this highly against the frontier.

Willison tested it via the Moonshot API using the `llm openai endpoint` command added to LLM 0.32, which can run prompts against any OpenAI-compatible endpoint but doesn't log results, so he saved stdout and stderr (the reasoning trace) separately. He generated pelican-riding-a-bicycle SVGs at the three supported reasoning levels (low, medium, max) and ran fresh comparisons against Kimi K3 at the same levels.

- Kimi K3.1 Pro costs $2/M input and $10/M output tokens, matching GPT-6.1 Sol and half of Claude Opus 5.5
- A Highspeed variant is 2-3x faster at twice the price, with cache-hit input tokens priced the same
- Artificial Analysis scored it 55, ahead of Claude Fable 5.1, GPT-6 Astra, and Gemini 4 Argon (53), behind only Opus 5.5 (58)
- It is the first soon-to-be open weight model to score this highly against frontier models
- Tested via the Moonshot API using LLM's `llm openai endpoint` command with low, medium, and max reasoning levels