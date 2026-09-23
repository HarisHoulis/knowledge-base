---
domain: ai-workflows
subdomain: llm-pricing
concept: llm-price-war
title: Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a New Price War
sources:
  - title: "Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war"
    url: "https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/"
    author: "Simon Willison"
    date: "2026-09-22"
---

# Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a New Price War

On consecutive days in September 2026, xAI released Grok 4.7 and Xiaomi released MiMo v2.6 Flash/Pro, followed by Anthropic's Claude Opus 5.5 and, an hour later, OpenAI's GPT-6 Sol and GPT-6 Luna. The headline story is pricing: GPT-6 Luna lands at $0.10/M input and $0.50/M output, half the price of GPT-5.6 Luna, and GPT-6 Sol halves the price of GPT-5.6 Sol. Because GPT-5.6 already has a scheduled 25% price increase for November, GPT-6 is effectively half the price of the promotional pricing for the previous generation. With GPT-5.6 Terra priced identically to GPT-6 Sol, any remaining reason to use Terra "just evaporated".

Claude Opus 5.5 cuts the price that Opus 4.5 through Opus 5 all shared ($5/M input, $25/M output) by 20% to $4/M and $20/M, with cache reads falling 60% -- significant for long agentic conversations where 90%+ of input tokens are processed at cached prices. Anthropic frames the release as a response to feedback on communication style, saying it is cheaper per token than Opus 5.0 while reaching the intelligence of Fable 5.1 across every effort level. The top tier is untouched by the war: GPT-6 Astra and Claude Fable 5.1 remain at $10/M input and $50/M output.

Model behavior remains uneven. In the author's pelican-riding-a-bicycle test, Opus 5.5 at "max" thinking failed to return a response twice, exhausting its 128,000 maximum output tokens while still reasoning about the SVG, at a cost of $2.56 and nearly 20 minutes each failure -- suggesting "max" is effectively useless if it over-thinks to breaking point on a trivial prompt. Fable 5.1 on max did not over-think and produced the best pelican seen from any Anthropic model. GPT-6 Sol and Claude Opus 5.5 are now the author's default models in Codex and Claude Code, and the Datasette Agent demo at agent.datasette.io has been upgraded to GPT-6 Luna, which appears fast and competent at SQL and at building HTML/JavaScript for Datasette Apps.

Anthropic says Sonnet 5.5 and Haiku 5.5 are coming soon, raising the question of whether Haiku can regain price competitiveness at the low end: current Haiku 4.5 is $1/$5 while GPT-6 Luna is one tenth of that.

- GPT-6 Luna at $0.10/M input and $0.50/M output is half the price of GPT-5.6 Luna and among the cheapest models OpenAI has released, beaten only by GPT-4.1 Nano and GPT-5 Nano.
- Claude Opus 5.5 drops Opus pricing 20% to $4/$20 per million tokens and cuts cache-read prices 60%, which matters for agentic conversations where 90%+ of input tokens hit the cache.
- The price war hits the mid tier only: GPT-6 Astra and Claude Fable 5.1 stay at $10/$50.
- Opus 5.5 at "max" thinking burned through its 128,000 output-token limit twice while reasoning about a pelican SVG, costing $2.56 and ~20 minutes per failure.
- Anthropic has Sonnet 5.5 and Haiku 5.5 coming, with Haiku 4.5 at $1/$5 facing GPT-6 Luna at one tenth the price.