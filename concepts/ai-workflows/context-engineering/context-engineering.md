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

In a Pragmatic Engineer podcast episode, Dex Horthy—CEO of HumanLayer and coiner of the term “context engineering”—shares practical lessons for building reliable LLM applications. He describes how his team's early experiment with fully unread AI-generated code failed within four months: production broke, models could not find the root cause, and re-onboarding took three weeks. His core advice is to keep humans in the loop where it matters, especially for design and architecture decisions, while using LLMs to speed up implementation (Orosz, 2026).

Horthy introduces key concepts like the “dumb zone”—the point at which a model's performance degrades as its context window fills up—and recommends staying well below the maximum context size. He suggests frequent, intentional compaction: compressing long, noisy contexts into Markdown documents and starting fresh sessions. He also identifies the four factors that matter in a context window: size, information quality, missing information, and trajectory. Trajectory poisoning, where a model repeats mistakes after negative feedback, signals that it is time to start a new session.

The article closes with three viable “software factory” models: turning the lights off and letting agents write unreviewed code (which Horthy tried and failed); reviewing all AI-generated code (yielding only a 30–50% productivity lift); or finding leverage by investing in planning, design, and architecture while letting agents generate code with less oversight—potentially achieving 2–3x speedups (Orosz, 2026).

- Unreviewed AI-generated code can lead to serious production issues; Horthy's team had to throw out an entire system after four months of no human code review.
- Models enter a “dumb zone” as context usage grows; larger context windows do not imply smarter models, and staying below a heuristic limit improves outcomes.
- Frequent intentional compaction—compressing context into Markdown and starting new sessions—helps manage complex projects and avoids trajectory poisoning.
- The four critical context-window factors are size, information quality, missing information, and trajectory; recognizing when a session is poisoned saves time and tokens.
- Three software-factory approaches exist: unreviewed agentic coding (risky), full human review of AI code (modest gains), and leverage-focused human oversight with limited code review (best speedups).