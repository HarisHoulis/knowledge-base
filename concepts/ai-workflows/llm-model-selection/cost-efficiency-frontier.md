---
domain: ai-workflows
subdomain: llm-model-selection
concept: cost-efficiency-frontier
title: Muse Ember: Meta's Small, Cheap Model for Agent Workloads
sources:
  - title: "Introducing Our Smallest, Most Efficient Model: Muse Ember"
    url: "https://simonwillison.net/2026/Nov/10/muse-ember/"
    author: "Simon Willison"
    date: "2026-11-10"
---

# Muse Ember: Meta's Small, Cheap Model for Agent Workloads

Meta released Muse Ember, described as its smallest and most efficient model, aimed at complex reasoning execution and the repetitive work agents do all day: tool calls, coding subtasks, routing, extraction, and long document parsing. For shorter prompts it is priced the same as GPT-6 Luna and Claude Haiku 5.5 at $0.10/million input and $0.50/million output tokens, while Claude Fable 5.2 costs 80x that at $8/$40.

Pricing gets less straightforward with longer prompts. All three cheap models support up to a million input tokens but have a threshold after which prices rise: GPT-6 Luna jumps above 272k tokens, Muse Ember above 200k, and Claude Haiku 5.5 above 100k. Taking those thresholds into account, Ember sits between the other two on price.

Simon Willison argues that comparing price-per-token no longer makes sense when reasoning tokens mean different models may use dramatically different token counts for the same problem. He points to Artificial Analysis's Intelligence Index vs. Cost per Task chart, where the Muse Ember models sit on the Pareto line—the point where improving one dimension requires giving up another. Meta makes the same claim, saying no model scores higher for less per task on the full leaderboard.

Muse Ember offers six reasoning levels: minimal, low, medium, high, xhigh, and max. In Willison's pelican-on-bicycle SVG test, the high level failed to return a full SVG, and reasoning level did not cleanly map to visual quality. The Ember results were comparable to Muse Wonder's output at 40x the price.

- Muse Ember targets agent workloads: tool calls, coding subtasks, routing, extraction, and long document parsing
- Short-prompt pricing matches GPT-6 Luna and Claude Haiku 5.5 at $0.10/$0.50 per million input/output tokens
- Long-prompt price thresholds differ: Luna >272k, Ember >200k, Haiku >100k tokens
- Price-per-token is a weak comparison when reasoning tokens vary; cost-per-task on the Artificial Analysis Pareto frontier is more useful
- Six reasoning levels exist, but level did not cleanly correlate with output quality in SVG tests