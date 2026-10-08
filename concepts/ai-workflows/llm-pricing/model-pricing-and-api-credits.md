---
domain: ai-workflows
subdomain: llm-pricing
concept: model-pricing-and-api-credits
title: Claude Haiku 5.5: Pricing, Tokenizer Changes, and New API Credits
sources:
  - title: "Claude Haiku 5.5"
    url: "https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/"
    author: "Simon Willison"
    date: "2026-10-07"
---

# Claude Haiku 5.5: Pricing, Tokenizer Changes, and New API Credits

Anthropic released Claude Haiku 5.5, a fast, low-cost model priced at $0.10/$0.50 per million input/output tokens up to 100,000 tokens, matching OpenAI's GPT-6 Luna. Beyond 100,000 tokens the price rises 5x to $0.50/$2.50, while Luna's increase at 272,000 tokens only goes to $0.20/$0.75, making Luna a better deal for larger workloads. The previous Haiku 4.5 was priced at $1/$5 and was showing its age after almost a year.

Haiku 5.5 uses a new, less generous tokenizer: the same long prompt consumes roughly 1.25x as many tokens compared to Haiku 4.5, representing a hidden price increase. The model does not allow disabling reasoning and defaults to medium effort; testing with the llm-anthropic plugin showed a low-effort pelican SVG cost 0.0936 cents and took 7 seconds, while a max-effort one took 5 minutes 9 seconds and cost 3.3826 cents.

Anthropic also halved the price of cache reads for Sonnet 5.5 and introduced monthly API credits for Max and Team subscribers: $100/month for Max 5x, $200 for Max 20x, and up to $500 pooled for Team. Credits are claimed via Settings -> Billing, match the subscription cost, do not roll over, and auto-reload can be disabled so API requests stop when the balance runs out. OpenAI still allows using a Codex subscription for personal API use, which remains a better deal for heavy API users.

- Haiku 5.5 matches GPT-6 Luna's $0.10/$0.50 pricing up to 100,000 tokens, but costs 5x more beyond that while Luna only rises to $0.20/$0.75 at 272,000 tokens.
- The new tokenizer uses about 1.25x more tokens for the same prompt than Haiku 4.5, a hidden price increase.
- Reasoning cannot be disabled and defaults to medium; low-effort generation is cheap and fast while max effort can take minutes.
- Anthropic halved Sonnet 5.5 cache read prices and added monthly API credits for Max and Team subscribers ($100-$500), which do not roll over.