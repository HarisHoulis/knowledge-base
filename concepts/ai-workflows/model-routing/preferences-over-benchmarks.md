---
domain: ai-workflows
subdomain: model-routing
concept: preferences-over-benchmarks
title: Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean
sources:
  - title: "Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean"
    url: "https://www.youtube.com/watch?v=FvxY8oPoI8o"
    author: "AI Engineer"
    date: "2026-08-22T15:30:18+00:00"
---

# Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean

The talk argues that choosing a single 'best' model based on public benchmarks is the wrong instinct. Instead, model routing—selecting a model per request based on task, cost, latency, and user preference—is emerging as a critical discipline. The authors identify three drivers: exploding costs, task-model fit (frontier models are often overkill), and risk of relying on a single model for failover. They emphasize that no public leaderboard can encode the right choice because it depends on the actual request, system prompts, tools, and end-user needs (Archana Kamath & Tyler Gillam, 2026).

DigitalOcean's inference router is presented as an open-source solution that avoids black-box behavior. It runs through an open proxy and a purpose-built routing model, allowing users to describe preferences in natural language and set hard rules. The router picks the right model per request in under 200ms at no extra cost, and in evaluations it beats frontier models like the GPT-5 series on the routing task itself with lower latency. This approach emphasizes customization, evaluation, and improvement without vendor lock-in (Archana Kamath & Tyler Gillam, 2026).

- There is no single best model; the right model depends on the individual request's task, cost constraints, latency needs, and end-user preferences.
- Model routing addresses cost explosion, task-model fit, and the risk of depending on one model for production failover.
- DigitalOcean's router is open source, fast (<200ms), and lets users define natural-language preferences and hard rules to pick a model per request.
- The routing model outperforms frontier models at the routing task itself while adding no extra cost to customers.
- The key design principle is transparency: routing should be customizable, evaluable, and improvable, avoiding the black-box problem.