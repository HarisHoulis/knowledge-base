---
domain: ai-workflows
subdomain: llm-model-releases
concept: model-release-evaluation
title: GPT-6.2 Astra and GPT-6.2 Sol: Pricing, Benchmarks and Agentic Behavior
sources:
  - title: "GPT-6.2 Astra and GPT-6.2 Sol"
    url: "https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/"
    author: "Simon Willison"
    date: "2026-11-17"
---

# GPT-6.2 Astra and GPT-6.2 Sol: Pricing, Benchmarks and Agentic Behavior

Simon Willison covers OpenAI's release of two new frontier models, GPT-6.2 Astra (for hard projects) and GPT-6.2 Sol (efficient, everyday work), available via API as gpt-6.2-astra and gpt-6.2-sol, with support shipped in LLM 0.38. Astra is priced at 80% of its predecessor 6 Astra ($8/MTok input, $40/MTok output), matching Claude Fable 5.2's pricing pattern, with cached input dropping to $0.40/million versus $1/million previously—a notable win for long agentic sessions. Sol holds steady at $2/$10, half the price of GPT-5.6 Sol.

Willison runs his standard pelican-on-a-bicycle SVG benchmark across effort levels and a newer Three.js prompt asking the model to animate Yonkers standing up as a mech and stomping through NYC boroughs using OpenStreetMap data. Neither Astra nor Sol matched Claude Fable 5.2 or Gemini 4 Carbon on the mech-morphing task. He also used Astra (Ultra) in the Codex desktop app to composite the two model outputs into a side-by-side labeled video, demonstrating agentic video-editing capability.

Reception is mixed: Astra 6.2 reportedly trails Fable 5.2 on some benchmarks, and users complain about confusing communication style. Willison cites Theo Browne's pre-release feedback letter, which describes the model managing subagents well on long tasks but then blocking to ask incomprehensible internal implementation questions—e.g., after a two-hour '/goal make a new level for Outer Wilds' session, it stalled asking which filename a reviewer writes clips to.

- GPT-6.2 Astra costs $8/$40 per MTok (80% of 6 Astra) with cached input at $0.40/million, benefiting long agentic sessions; Sol stays at $2/$10.
- Willison's pelican and Yonkers-mech benchmarks show Astra and Sol underperforming Claude Fable 5.2 and Gemini 4 Carbon on the mech-morphing task.
- Astra (Ultra) in Codex desktop successfully produced a composited side-by-side labeled video from two model outputs.
- Theo Browne's feedback highlights an agentic failure mode: models block on obscure internal implementation questions users can't answer.