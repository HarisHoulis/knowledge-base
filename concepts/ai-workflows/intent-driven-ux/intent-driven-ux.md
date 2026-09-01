---
domain: ai-workflows
subdomain: intent-driven-ux
concept: intent-driven-ux
title: The End of the Static Screen: Architecting Intent-Driven UX
sources:
  - title: "The End of the Static Screen: Architecting Intent-Driven UX — Gus Iwanaga, commercetools"
    url: "https://www.youtube.com/watch?v=QrMcNe2jjt8"
    author: "AI Engineer"
    date: "2026-09-01T20:00:01+00:00"
---

# The End of the Static Screen: Architecting Intent-Driven UX

Gus Iwanaga opens by disowning his session title and showing a demo that failed: his team asked their system for a Q1 sales report four times and received four different layouts, with varying KPIs, charts, and even drifting date ranges. He argues this was not a model failure but a consequence of handing a model a component catalog and asking it to compose the experience (Iwanaga, 2026). The talk lays out a spectrum of control: shipping a fixed component where the agent only decides when to show it, versus letting the model emit markup in a sandboxed frame, which he demonstrates but declines to ship because a business cannot control what it cannot predict.

- The same query producing inconsistent layouts is an architecture problem, not just a model problem.
- The middle path: an orchestrator classifies intent, calls tools, maps results to eligible components, and broadcasts a UI spec that renders as native components against a schema.
- Atomic design was adopted with the hierarchy inverted to run from components upward to solve the arrangement problem.
- The component catalog becomes the contract between agent and interface, so every property in it matters.