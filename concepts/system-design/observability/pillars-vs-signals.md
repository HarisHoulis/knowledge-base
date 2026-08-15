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

Charity Majors argues that the concept of "pillars" of observability is a marketing term, not a technical one, and that the only rigorous term is "signal," as defined by OpenTelemetry. She notes that OpenTelemetry currently supports traces, metrics, logs, and baggage as signals, with events and profiles at the proposal stage, but never mentions pillars at all. When vendors push pillars, they are typically preparing to sell siloed products for each signal type, multiplying costs and complexity.

Majors contrasts the multiple pillars model (observability 1.0), where each signal type is stored in a separate silo, with the unified storage model (o11y 2.0), where all signals are stored together in one database, preserving context and relationships. She explains that the pillars model forces users to hop between metrics, logs, and traces, duplicating data many times per request and hiding the connections between signals. In contrast, unified storage lets users zoom in and out smoothly—from SLOs to events to traces—without losing context.

She also addresses profiling specifically: it is a signal type, but many teams think they need profiling when they actually need better tracing. In a unified world, profiling would just allow even finer-grained zoom, down to syscalls. Finally, she clarifies that OpenTelemetry is not inherently pro-three-pillars; in fact, it unifies telemetry signals through shared distributed context, though vendors can choose to implement a siloed approach on top of it.

- Pillar is a marketing term; signal is the technical term defined by OpenTelemetry, which never mentions pillars.
- The multiple pillars model stores each signal separately, causing massive data duplication and high cost.
- The unified storage model (o11y 2.0) keeps all signals in one data store, enabling seamless zooming across metrics, logs, and traces.
- Profiling is a telemetry signal, but many users need good tracing rather than profiling; it's not necessarily a separate pillar.
- OpenTelemetry actually unifies signals via shared context, but vendors can still build three-pillar-style tools on top of it.