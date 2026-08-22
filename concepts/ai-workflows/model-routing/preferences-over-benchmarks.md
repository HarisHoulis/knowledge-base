---
domain: ai-workflows
subdomain: model-routing
concept: preferences-over-benchmarks
title: Preferences Over Benchmarks: Model Routing
sources:
  - title: "Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean"
    url: "https://www.youtube.com/watch?v=FvxY8oPoI8o"
    author: "AI Engineer"
    date: "2026-08-22T15:30:18+00:00"
---

# Preferences Over Benchmarks: Model Routing

The talk challenges the common instinct to select a model based on top benchmark scores, arguing that there is no single best model for all tasks. The right model depends on the actual request: the task itself, system prompts and tools, cost budget, latency requirements, and end-user preferences. The authors identify three key drivers for moving beyond one-model habits: exploding inference costs (citing companies like Walmart, Uber, and Microsoft capping usage), the overkill of using frontier models for simple tasks where smaller open models suffice, and the risk of relying on a single model with no failover when it degrades or goes down. (Archana Kamath & Tyler Gillam, 2026)

DigitalOcean's solution is an inference router built on an open-source, purpose-built routing model. Users describe their workload in natural language and set preferences such as cost, latency, quality, preferred models, or hard rules; the router then selects the appropriate model per request. This avoids vendor lock-in and black-box behavior, as users can customize, evaluate, and improve the routing. The routing model is highly efficient—under 200 milliseconds—and costs customers nothing extra. In evaluations, it even outperformed frontier models like the GPT-5 series at the routing task itself with much lower latency. (Archana Kamath & Tyler Gillam, 2026)

- Don't chase benchmark leaders; the optimal model depends on the specific request—task, system prompts, cost, latency, and user preference.
- Three forces driving multi-model adoption: cost explosion, frontier-model overkill for simple tasks, and risk of single-model failure without failover.
- DigitalOcean's router uses an open-source, purpose-built routing model that accepts natural-language task descriptions and explicit preferences to pick the best model per request.
- The routing model is fast (<200ms), costs nothing extra, and in evaluations beats frontier GPT-5 series models at the routing task itself.
- No vendor lock-in: users can customize, evaluate, and improve the router to fit their workload.