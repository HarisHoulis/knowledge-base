---
domain: ai-workflows
subdomain: llm-tooling
concept: gemini-model-lineup-pricing
title: llm-gemini 0.38 and the Confusing Gemini 4 Neon Pricing
sources:
  - title: "llm-gemini 0.38"
    url: "https://simonwillison.net/2026/Nov/18/llm-gemini/"
    author: "Simon Willison"
    date: "2026-11-18"
---

# llm-gemini 0.38 and the Confusing Gemini 4 Neon Pricing

Simon Willison releases llm-gemini 0.38 to support Google's newly announced Gemini 4 Neon model. He notes that the Gemini 4 lineup's pricing has become even more confusing than before: the previous lineup of Hydrogen, Argon, and Carbon had Argon and Carbon at the same price, with Hydrogen at 3/4 of that price until December 1st, when the other two double and Hydrogen drops to 1/4.

The Neon announcement effectively pretends Argon doesn't exist, leaving a lineup of Carbon, Neon, and Hydrogen from most to least expensive. Because Carbon is currently at half price, Neon ($3/million input, $15/million output) is actually the most expensive right now, followed by Carbon ($2/$10) and Hydrogen ($1.50/$7.50); Willison expects this to make more sense once Carbon doubles to $4/$20 on December 1st.

He tested Neon's low, medium, and high reasoning levels with his pelican-riding-a-bicycle benchmark, dropped Argon from his Gemini 4 comparison grid, and found the Neon pelicans look better than Hydrogen and worse than Carbon. He also ran his recurring "yonkers-rising" three.js mech prompt against Neon at "extra" effort in Google Antigravity.

- llm-gemini 0.38 adds support for Google's Gemini 4 Neon model
- Gemini 4 pricing is confusing: Neon is currently the most expensive despite Carbon being positioned as top-tier, due to Carbon's temporary half-price discount
- Carbon doubles to $4/$20 on December 1st, which should restore the intended price ordering
- Pelican benchmark places Neon quality between Hydrogen and Carbon