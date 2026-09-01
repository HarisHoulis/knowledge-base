---
domain: engineering-culture
subdomain: observability
concept: pillars-are-a-lie
title: How many pillars of observability can you fit on the head of a pin?
sources:
  - title: "How many pillars of observability can you fit on the head of a pin?"
    url: "https://charity.wtf/p/the-pillar-is-a-lie"
    author: "Charity Majors"
    date: "Thu, 30 Oct 2025 05:27:38 GMT"
---

# How many pillars of observability can you fit on the head of a pin?

Charity Majors argues that the "pillars" of observability (metrics, logs, traces, etc.) are a marketing fiction, not a technical reality. The term "pillar" is used by vendors to sell siloed, separate products for each signal type, while the technical term "signal" is defined by OpenTelemetry as a type of telemetry data. OpenTelemetry currently supports traces, metrics, logs, and baggage as signals, with profiling and events at the proposal stage. Thus, profiling may be a signal, but calling it a "pillar" is purely a commercial move (Majors, 2025).

The article contrasts the multiple-pillars architecture (o11y 1.0), where each signal is stored in its own database, with the unified storage model (o11y 2.0), where all signals are stored together as wide structured events. The pillars model leads to massive data duplication, higher costs, and a "bunny hopping" user experience—jumping between metrics, logs, and traces to correlate information. The unified model lets users zoom from SLOs to detailed events to traces without switching tools, since all data is connected (Majors, 2025).

Majors clarifies that OpenTelemetry is not inherently pro-pillars; it actually unifies telemetry through shared context. In a unified world, profiling simply adds a finer zoom level, down to syscalls and kernel operations, much like Google Maps zooming from rooftops to license plates. For most users, good tracing already solves the need that profiling claims to address (Majors, 2025).

- Pillar is a marketing term; signal is a technical term defined by OpenTelemetry.
- The multiple-pillars model duplicates data across siloed stores, increasing costs and forcing users to hop between tools.
- The unified storage model (o11y 2.0) stores all signals in one database, enabling seamless zooming from metrics to traces.
- Profiling is another signal, not a new pillar; most debugging needs are met by good distributed tracing.