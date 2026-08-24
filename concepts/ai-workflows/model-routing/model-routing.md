---
domain: ai-workflows
subdomain: model-routing
concept: model-routing
title: Preferences Over Benchmarks: Model Routing
sources:
  - title: "Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean"
    url: "https://www.youtube.com/watch?v=FvxY8oPoI8o"
    author: "AI Engineer"
    date: "2026-08-22T15:30:18+00:00"
---

# Preferences Over Benchmarks: Model Routing

This talk by Archana Kamath and Tyler Gillam of DigitalOcean challenges the common practice of selecting models based on public benchmark leaderboards. They argue that there is no single best model for every job; the right model depends on the specific request, including the task type, required latency, cost constraints, and end-user expectations. The authors highlight three forces pushing organizations away from the one-model habit: exploding costs, overkill from using frontier models for simple tasks, and the reliability risk of depending on a single model. They advocate for model routing as a solution, where a router intelligently selects the best model per request based on user-defined priorities such as cost, latency, and quality.

- Benchmarks are insufficient for model selection because they cannot encode the full context of a real request, including task, tools, cost, latency, and user preferences.
- Cost control is a major driver for routing: companies like Walmart, Uber, and Microsoft are capping usage to manage inference bills.
- Model routing reduces risk by providing failover: if one model degrades, traffic can be shifted to another, avoiding single points of failure.
- DigitalOcean's open-source router uses a specialized routing model that is fast (under 200ms) and does not incur extra cost, allowing customization without vendor lock-in.