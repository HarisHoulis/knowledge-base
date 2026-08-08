---
domain: ai-workflows
subdomain: context-engineering
concept: context-engineering
title: Context engineering with Dex Horthy
sources:
  - title: "Context engineering with Dex Horthy"
    url: "https://newsletter.pragmaticengineer.com/p/context-engineering-with-dex-horthy"
    author: "Gergely Orosz"
    date: "2026-07-15"
---

# Context engineering with Dex Horthy

In this Pragmatic Engineer podcast episode, Gergely Orosz interviews Dex Horthy, CEO of HumanLayer and coiner of the term "context engineering." Horthy shares practical lessons from building AI agents and talking with ~100 AI engineers, which led to his popular '12-Factor Agents' principles. He emphasizes that understanding LLM context windows is becoming a critical skill for software engineers, as models degrade when the context fills beyond a heuristic "dumb zone"—for a 1M-token model, he pushes to around 300-400K, while smaller models stop at ~100K (Orosz, 2026).

Horthy describes a failed experiment in July 2025 where AI-generated code was shipped without human review; within four months the system broke, the model couldn't find the root cause, and it took days to discover a misrouted primary key plus three weeks to re-onboard to unread code. He argues current coding models are trained to optimize SWE-bench-like benchmarks, which reward correct local fixes but can degrade codebases over time because poor architecture isn't captured by unit tests. To mitigate this, he advises frequent, intentional compaction: use one session to read code and emit a research document, a second to turn tickets into a design doc, and a third to create a plan—with a human reviewing design and architecture (Orosz, 2026).

Horthy also covers "trajectory poisoning": when a model starts saying "You're completely right!" after a mistake, it's best to start a new session, because autoregressive models can get stuck in a loop of repeated errors. He recommends focusing on four things in the context window—size, information quality, missing information, and trajectory. For "loop engineering," his team runs nightly agents that open pull requests, and humans read all of them before merging. He contrasts "token harder" (maximizing subscription usage) with "token smarter" (maximizing value with control). Finally, he outlines three software factory options: full automation (which failed for him), reviewing all AI code (30-50% productivity lift), and finding leverage while keeping humans in the loop (2-3x faster) (Orosz, 2026).

- Context engineering is about staying within the model's 'smart zone' and using techniques like context compaction to avoid degradation.
- Shipping unread AI-generated code can lead to disaster; always maintain human oversight on complex systems.
- Watch for 'trajectory poisoning'—if the model starts capitulating after mistakes, start a new session.
- Slow loops with nightly agents opening PRs are an effective way to automate code quality improvements while keeping humans in review.
- The best productivity gains come from investing in design and architecture, letting agents generate code, and selectively reviewing rather than trying to read everything.