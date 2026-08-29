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

Charity Majors argues that the concept of "pillars" of observability is a marketing construct, not a technical one. The technical term is "signal," as defined by OpenTelemetry, which currently lists traces, metrics, logs, and baggage as signal types, with profiling and events at proposal stage. Calling profiling a "fourth pillar" is a vendor framing to justify selling another siloed product, not a technical necessity. The real distinction is between architectural models: the multiple-pillars model (o11y 1.0) stores each signal type in a separate database, leading to massive data duplication and cost, while the unified storage model (o11y 2.0) stores all signals together in one highly cardinality-capable store, allowing zoom-like navigation rather than "bunny hopping" between separate tools (Majors, 2025).

The article emphasizes that OpenTelemetry itself unifies telemetry signals through shared context and does not require a pillar-based implementation, though many vendors choose to build pillar-style silos on top. Majors explains that in a unified storage world, profiling simply means being able to zoom into even finer-grained data, such as syscalls, just as tracing provides function-level insight. She concludes that engineers should focus on signals and unified data models, not pillars, and that the language of pillars mainly serves to increase vendor revenue through separate storage and query systems for each data type (Majors, 2025).

- Pillar is a marketing term; signal is the technical term used by OpenTelemetry.
- The multiple-pillars model stores each signal separately, causing data duplication and high costs; unified storage stores all signals together.
- OpenTelemetry unifies signals through shared context, but vendors can choose to implement pillar-based architectures on top.
- In a unified storage model, profiling is just a deeper zoom level into the same data, not a separate pillar.