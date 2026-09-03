---
domain: ai-workflows
subdomain: llm-reasoning-effort
concept: reasoning-effort-scaling
title: Claude Fable 5.1 made me a really nice animated pelican
sources:
  - title: "Claude Fable 5.1 made me a really nice animated pelican"
    url: "https://simonwillison.net/2026/Sep/1/claude-fable-5-1/"
    date: "2026-09-01"
---

# Claude Fable 5.1 made me a really nice animated pelican

Simon Willison evaluates Anthropic's Claude Fable 5.1 using his 'pelican riding a bicycle' SVG benchmark, which he finds useful mainly for comparing reasoning effort levels within a model family. At the low and medium settings, Fable 5.1 produced simple SVGs with no visible reasoning tokens; at the high setting it added a brief reasoning summary. The xhigh setting jumped to 36,767 output tokens, cost $1.83, and produced a more detailed image, while the max setting used 65,927 tokens, cost $3.30, and generated what Willison calls the best pelican he has seen from an Anthropic model, complete with a bicycle helmet, basket, and fish.

- Claude Fable 5.1's reasoning effort settings dramatically affect output detail, cost, and latency, from near-zero reasoning at low/medium to 65,927 output tokens at max.
- For simple prompts like SVG generation, high effort can produce only marginal improvement, whereas xhigh and max can drastically change the result and cost several dollars.
- Willison found the max-level pelican notably better, but still less creative than Gemini 3.7 Flash on the same benchmark.
- Fable 5.1 sets new benchmarks like Terminal-Bench-Science, but the pelican benchmark is no longer a strong cross-model predictor of general capability.
- The max-level SVG was animated by piping it back into Fable 5.1 at high effort, producing an animated SVG for $1.37.