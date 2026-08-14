---
domain: ai-workflows
subdomain: agent-design
concept: raising-the-floor
title: Designing Agents (The Floor Is the Frontier)
sources:
  - title: "Designing Agents (The Floor Is the Frontier)"
    url: "https://www.youtube.com/watch?v=jHMiYtjoJfA"
    author: "Ben Hylak"
    date: "2026-08-12T18:00:34+00:00"
---

# Designing Agents (The Floor Is the Frontier)

The talk also critiques the lack of continual learning in production. Despite the conference track's theme, few real-world systems explicitly perform continual learning; instead, the frontier is designing evaluation and feedback loops that handle a moving model landscape—new models, new harnesses, and tool integrations break traditional eval suites (Ben Hylak, 2026).

- Traditional chatbot-era evals (e.g., 1,000 Q&A examples) are largely irrelevant for agent deployments; teams rarely build such datasets.
- Agents exhibit creative, tool-driven behavior that can be both powerful and dangerous, requiring evaluation for open-ended autonomy.
- 'Raising the floor' is about improving baseline agent reliability, not chasing benchmarks.
- Production agents are already used in high-stakes domains like finance, healthcare, and defense, making robustness critical.
- Continual learning is not yet common in real-world agent systems; the focus is on robust evaluation across model changes.