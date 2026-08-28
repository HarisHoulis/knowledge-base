---
domain: system-design
subdomain: observability
concept: pillars-vs-signals
title: How many pillars of observability can you fit on the head of a pin?
sources:
  - title: "How many pillars of observability can you fit on the head of a pin?"
    url: "https://charity.wtf/p/the-pillar-is-a-lie"
    author: "Charity Majors"
    date: "Thu, 30 Oct 2025 05:27:38 GMT"
---

# How many pillars of observability can you fit on the head of a pin?

Charity Majors argues that "pillar" is a marketing term, not a technical one, and that observability has no fixed pillars. While profiling can be a type of telemetry signal per OpenTelemetry's definitions, calling it a "pillar" is simply a vendor strategy to sell a separate, overpriced product. She emphasizes that signals are technical, but pillars are a mental model from the 1980s that keeps engineers trapped in expensive, siloed tooling (Majors, https://charity.wtf/p/the-pillar-is-a-lie).

- Pillar is a marketing term; signal is the technical term.
- The multiple pillars model causes data duplication and forces users to "bunny hop" between tools.
- Unified storage (o11y 2.0) stores all signals together, enabling a seamless zoom-in/zoom-out debugging experience.
- OpenTelemetry actually unifies telemetry signals through shared context, despite the misconception that it supports three pillars.
- Profiling is useful mainly for syscall-level detail; most users are better served by good tracing.