---
domain: engineering-culture
subdomain: observability
concept: pillars-vs-signals
title: Observability Pillars Are a Lie: Signals Are the Real Technical Term
sources:
  - title: "How many pillars of observability can you fit on the head of a pin?"
    url: "https://charity.wtf/p/the-pillar-is-a-lie"
    author: "Charity Majors"
    date: "Thu, 30 Oct 2025 05:27:38 GMT"
---

# Observability Pillars Are a Lie: Signals Are the Real Technical Term

Charity Majors argues that the notion of "pillars" of observability is a marketing construct, not a technical one. She explains that "signal" is the technical term, citing OpenTelemetry documentation, while "pillar" is a colloquialism that vendors use to justify selling siloed, expensive tools. The foundational distinction is between the multiple-pillars architecture (storing each signal type separately) and the unified storage model (storing all signals together as structured data), which she associates with observability 2.0.

- Pillar is a marketing term; signal is a technical term.
- Vendors use pillar language to sell siloed data storage, increasing cost and complexity.
- Unified storage model treats all telemetry as one dataset, enabling seamless zooming from metrics to traces.
- OpenTelemetry unifies signals through shared context, despite common misperception that it enforces three pillars.
- Profiling is a signal type, not inherently a fourth pillar; most users needing profiling actually need better tracing.