---
domain: ai-workflows
subdomain: ai-agent-operations
concept: tribal-dungeons
title: Tribal Dungeons of Global Shipping: AI Agents at Maersk
sources:
  - title: "Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk"
    url: "https://www.youtube.com/watch?v=dQ-_i1tZiws"
    author: "AI Engineer"
    date: "2026-08-29T17:30:21+00:00"
---

# Tribal Dungeons of Global Shipping: AI Agents at Maersk

Maersk's standard operating procedures were screenshots—sequences of images showing clicks, useless to an autonomous agent. Dmitry Buykin calls this gap 'tribal dungeons': knowledge exists but is not executable. Converting an SOP for an agent requires adding preconditions, decisions, identifiers, backend calls, validation, recovery, and evidence, negotiated with process owners because experts define the 'what' and agents define the 'how' [1].

The engineering effort lies not in the agent loop but in the refining loop around it. The corpus of procedures outweighs the runtime roughly 20 to 1, because the same shipping step differs across countries. Accuracy was earned through over 100,000 corrections in nine months, guided by heat maps that turn traces into priorities, with a single correction cell often costing a month or two. A correction only counts when it becomes an executable change—the line between an opinion and a production fix [1].

Discovery requires agent freedom, while production needs a cage. A harness exists to make dumb mistakes impossible rather than to give the model more room. Running 200 instances against legacy backends, triage and shared evidence are essential, and 'be careful' is not a guardrail [1].

- SOPs as screenshots are useless to agents; they must be translated into structured, executable procedures with validation and recovery.
- The real system is the refining loop, not the agent loop; the procedure corpus is about 20x the size of the runtime.
- Accuracy comes from continuous corrections: 100,000+ over nine months, with heat maps prioritizing failure traces.
- A correction only becomes real when it changes executable code, separating opinion from production fix.
- Discovery needs agent freedom, production needs a cage—guardrails must be structural, not verbal.