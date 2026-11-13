---
domain: ai-workflows
subdomain: llm-pricing-and-models
concept: gemini-4-model-tiers
title: llm-gemini 0.37 and the Gemini 4 Hydrogen Release
sources:
  - title: "llm-gemini 0.37"
    url: "https://simonwillison.net/2026/Nov/12/llm-gemini/"
    author: "Simon Willison"
    date: "2026-11-12"
---

# llm-gemini 0.37 and the Gemini 4 Hydrogen Release

Simon Willison's release note for llm-gemini 0.37 covers Google's launch of Gemini 4 Hydrogen, the lowest-cost member of the Gemini 4 family. He finds Gemini 4's pricing confusing: Carbon and Argon cost the same ($2.00 input / $10.00 output per million tokens through Nov 30, 2026, doubling to $4.00/$20.00 from Dec 1), while Hydrogen is $1.50/$7.50 — only a 25% discount now, but a 75% discount after the price increase. Google justifies Argon's equal price by claiming faster responses and lower token spend per turn than Carbon.

Hydrogen is still far more expensive than comparable cheap models: Claude Haiku 5.5 and GPT-6 Luna are both $0.10/$0.50, making Hydrogen about 15x their price. Willison tested Hydrogen by having it generate pelicans and compared results across all three Gemini 4 models at three effort levels; despite the small price gap, Hydrogen's pelican quality was notably worse.

Google positions Hydrogen as a fast, disciplined execution model for everyday coding work — writing code, running tests, verifying changes — either standalone or paired with Carbon and Argon as the execution engine in multi-model workflows. Hydrogen is also the new free-tier model and will power AI features in Google Search.

- Carbon and Argon share identical pricing and both double in price on December 1, 2026; Argon is differentiated by claimed speed and lower token spend per turn.
- Hydrogen is only 25% cheaper than its siblings now but will be 75% cheaper after the December price increase.
- Hydrogen costs roughly 15x more than Claude Haiku 5.5 and GPT-6 Luna ($0.10/$0.50).
- Google positions Hydrogen as a high-efficiency execution model for everyday coding, usable standalone or alongside Carbon and Argon.
- Hydrogen is the new free-tier model and will power AI features in Google Search.