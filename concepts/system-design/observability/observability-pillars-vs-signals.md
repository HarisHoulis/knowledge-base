---
domain: system-design
subdomain: observability
concept: observability-pillars-vs-signals
title: How many pillars of observability can you fit on the head of a pin?
sources:
  - title: "How many pillars of observability can you fit on the head of a pin?"
    url: "https://charity.wtf/p/the-pillar-is-a-lie"
    author: "Charity Majors"
    date: "2025-10-30"
---

# How many pillars of observability can you fit on the head of a pin?

Charity Majors argues that the concept of "pillars" in observability is a marketing term, not a technical one. The technical term is "signal," as defined by OpenTelemetry, which currently includes traces, metrics, logs, and baggage, with events and profiles at proposal/development stage. The word "pillar" is absent from OpenTelemetry's documentation, highlighting that pillar-based thinking is not rooted in technical reality (Majors, 2025).

Majors contrasts two architectural models: the multiple pillars model (observability 1.0) and the unified storage model (o11y 2.0). The former stores each signal type in separate silos, leading to massive data duplication, high costs, and a poor "bunny hopping" user experience where engineers manually correlate data across metrics, logs, and traces. The latter stores all signals together in one database, preserving context and enabling a smooth zoom-in/zoom-out experience. She notes that most industry giants use the pillars model, while newer companies like Honeycomb use unified storage (Majors, 2025).

Majors clarifies that engineers using "pillars" colloquially is fine, but when vendors push the term, it usually signals intent to sell more siloed products. She also addresses OpenTelemetry, citing Austin Parker to show that OTel fundamentally unifies telemetry signals through shared context, though it does not require this. Profiling, she suggests, is just another type of signal—another level of zoom in a unified storage world, not necessarily a separate pillar (Majors, 2025).

- Pillar is a marketing term; signal is the technical term.
- The multiple pillars model causes data duplication, high costs, and inefficient debugging workflows.
- Unified storage (o11y 2.0) stores all telemetry together, allowing seamless zooming from SLOs to events to traces.
- OpenTelemetry supports unified telemetry by design, not necessarily three pillars.
- Profiling is a signal type, and in a unified storage model it becomes just another zoom level.