---
domain: ai-workflows
subdomain: llm-inference-routing
concept: preference-based-routing
title: Preferences Over Benchmarks: Model Routing
sources:
  - title: "Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean"
    url: "https://www.youtube.com/watch?v=FvxY8oPoI8o"
    author: "AI Engineer"
    date: "2026-08-22T15:30:18+00:00"
---

# Preferences Over Benchmarks: Model Routing

The key design principle is transparency and customizability. Unlike black-box auto-routing, this approach lets users evaluate, customize, and improve the routing behavior without vendor lock-in, aligning with DigitalOcean's open-source values.

- There is no single best model; the right model depends on the specific request, task, cost, latency, and user preferences.
- Cost, fit, and risk are three major reasons to move away from a single-model strategy.
- DigitalOcean's router uses an open-source, purpose-built routing model that adds under 200ms overhead and allows users to define natural-language preferences and hard rules.
- The router is customizable and transparent, avoiding vendor lock-in and black-box behavior.