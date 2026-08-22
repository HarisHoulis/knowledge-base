---
domain: system-design
subdomain: observability
concept: observability-pillars-vs-signals
title: How many pillars of observability can you fit on the head of a pin?
sources:
  - title: "How many pillars of observability can you fit on the head of a pin?"
    url: "https://charity.wtf/p/the-pillar-is-a-lie"
    author: "Charity Majors"
    date: "Thu, 30 Oct 2025 05:27:38 GMT"
---

# How many pillars of observability can you fit on the head of a pin?

Charity Majors argues that the concept of 'pillars' of observability is a marketing term, not a technical one. She contrasts it with 'signal,' which is defined by OpenTelemetry as a type of remotely transmitted data. While engineers may colloquially use 'pillar' to mean signal type, vendors use it to sell siloed products, reinforcing an outdated and expensive architecture model.

- The 'pillars' metaphor is marketing; 'signal' is the technical term defined by OpenTelemetry.
- The multiple-pillars model stores each signal type in separate silos, causing data duplication and high costs.
- Unified storage (o11y 2.0) treats all telemetry as the same data, allowing seamless zooming from metrics to traces to logs.
- OpenTelemetry actually supports unified context, though it can be used in a pillars-style architecture.
- Profiling is a signal, not necessarily a pillar, and is often unnecessary if good tracing is available.