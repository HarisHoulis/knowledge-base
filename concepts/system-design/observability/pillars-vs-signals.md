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

Charity Majors argues that “pillar” is a marketing term, not a technical one, and that “signal” is the correct technical term. She points to OpenTelemetry’s Signals documentation, which defines traces, metrics, logs, and baggage as signal types and never mentions pillars. The constant debates over whether profiling or errors are the “fourth pillar” are really just vendors trying to charge more for separate products (Majors, 2025).

Majors contrasts two architecture models: the “multiple pillars” model, which stores each signal type in its own silo, and the “unified storage” model (o11y 2.0), which stores all signals together as wide structured events. The pillars model leads to data duplication, higher costs, and a “bunny hopping” debugging experience, while the unified model lets users zoom in and out from SLOs to traces without losing context. She cites Austin Parker to show that OpenTelemetry actually unifies telemetry through shared context, even if vendors often implement it in a pillars-style way (Majors, 2025).

On profiling specifically, Majors says that in a unified storage world profiling is just another zoom level, like going from rooftops to license plates in Google Maps. She also shares that Honeycomb’s research found most teams who think they need profiling actually need better tracing, since profiling is only necessary for syscall-level detail (Majors, 2025).

- Pillar is a marketing term; signal is a technical term—and OpenTelemetry defines signal types without pillars.
- The multiple-pillars model silos data, causes duplication, and increases cost; the unified storage model treats data as data and stores it once.
- Unified observability enables zooming from metrics/SLOs down to individual events and traces without hopping between tools.
- OpenTelemetry is not inherently tied to the three-pillars model; it unifies signals through shared context.
- Profiling is a signal, but most teams need good tracing first; profiling is only for syscall-level resolution.