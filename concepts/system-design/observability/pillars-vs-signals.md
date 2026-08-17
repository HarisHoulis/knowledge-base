---
domain: system-design
subdomain: observability
concept: pillars-vs-signals
title: How many pillars of observability can you fit on the head of a pin?
sources:
  - title: "How many pillars of observability can you fit on the head of a pin?"
    url: "https://charity.wtf/p/the-pillar-is-a-lie"
    author: "Charity Majors"
    date: "2025-10-30"
---

# How many pillars of observability can you fit on the head of a pin?

Charity Majors argues that the concept of "pillars of observability" is a marketing term, not a technical one. She contrasts this with "signal," which is a technical term defined by OpenTelemetry and includes traces, metrics, logs, baggage, and (in development) profiling. The relentless debate over what constitutes a "fourth pillar" is therefore not a technical question but a vendor-driven framing to sell more siloed products (Majors, 2025).

Majors explains the two main architecture models: the multiple pillars model (observability 1.0) stores each signal type in a separate database, causing massive data duplication, high cost, and a disjointed "bunny hopping" debugging experience. The unified storage model (o11y 2.0) stores all signals together in one high-cardinality, columnar database, allowing users to zoom in and out across data like a map or PDF. She advocates for the unified model as the more efficient and lower-cognitive-load approach (Majors, 2025).

Regarding OpenTelemetry, Majors refutes the misconception that OTel is inherently pro-pillars. She cites Austin Parker's work showing that OTel unifies telemetry signals through shared context, although vendors can still choose to implement siloed storage on top. In a unified world, profiling becomes simply a finer-grained zoom level rather than a separate pillar. Majors concludes that most engineers needing profiling actually just need better tracing (Majors, 2025).

- Pillar is a marketing term; signal is the technical term used by OpenTelemetry.
- The multiple-pillars architecture silos signals, causing data duplication, high costs, and poor debugging UX.
- Unified storage (o11y 2.0) stores all signals together and enables smooth zooming across data.
- OpenTelemetry is not inherently three-pillars; it unifies signals via shared context.
- Profiling is a signal, but it is not automatically a separate pillar; most users need better tracing first.