---
domain: system-design
subdomain: observability
concept: pillars-are-a-lie
title: How many pillars of observability can you fit on the head of a pin?
sources:
  - title: "How many pillars of observability can you fit on the head of a pin?"
    url: "https://charity.wtf/p/the-pillar-is-a-lie"
    author: "Charity Majors"
    date: "2025-10-30"
---

# How many pillars of observability can you fit on the head of a pin?

Charity Majors argues that "pillar" is a marketing term, not a technical one. The technical term is "signal," as defined by OpenTelemetry, which currently supports traces, metrics, logs, and baggage, with events and profiles proposed or in development. Therefore, asking whether profiling is a "pillar" is a marketing question, not a technical one, and the proliferation of so-called "fourth pillars" reflects vendor positioning rather than engineering reality (Majors, 2025).

Majors contrasts two observability architectures: the "multiple pillars" model, where each signal type is stored in a separate siloed database, and the "unified storage" model (o11y 2.0), where all signals are stored together in one database preserving context and relationships. The pillars model leads to data duplication, high costs, and a debugging experience of "bunny hopping" between metrics, logs, and traces. The unified model enables users to zoom in and out from SLOs to events to traces without copying IDs or lining up timestamps, because it's "the same f***ing data" (Majors, 2025).

Majors also clarifies that OpenTelemetry is not inherently a "three pillars" framework. Citing Austin Parker, she explains that OTel unifies telemetry signals through shared, distributed context, even though it can be used to feed traditional pillar-based systems if vendors choose that path. In a unified world, profiling becomes just another level of zoom, down to syscalls if needed, but most teams likely need better tracing rather than profiling (Majors, 2025).

- Pillar is a marketing term; signal is the technical term used by OpenTelemetry.
- The multiple pillars architecture silos signals into separate stores, causing data duplication, high cost, and 'bunny hopping' during debugging.
- Unified storage (o11y 2.0) stores all signals together, enabling seamless zooming from metrics to traces to logs.
- OpenTelemetry unifies signals through shared context and does not require a three-pillars architecture.
- Profiling is a signal in development, but many teams need good tracing more than profiling.