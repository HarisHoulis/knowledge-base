---
domain: system-design
subdomain: observability
concept: observability-signals-vs-pillars
title: How many pillars of observability can you fit on the head of a pin?
sources:
  - title: "How many pillars of observability can you fit on the head of a pin?"
    url: "https://charity.wtf/p/the-pillar-is-a-lie"
    author: "Charity Majors"
    date: "2025-10-30"
---

# How many pillars of observability can you fit on the head of a pin?

Charity Majors argues that "pillar" is a marketing term, not a technical one, while "signal" is the precise term used in OpenTelemetry (traces, metrics, logs, baggage, with events and profiles in proposal stage) ([source](https://charity.wtf/p/the-pillar-is-a-lie)). Vendor talk of pillars usually signals an imminent pitch for another siloed signal type, and the multiple-pillars model (o11y 1.0) stores each signal separately, causing massive data duplication and forcing engineers to hop between metrics, logs, and traces to debug.

The unified storage model (o11y 2.0) stores all telemetry in one high-cardinality columnar store, preserving context and enabling users to zoom from SLOs to individual events without copying IDs or aligning timestamps. This reduces cost and cognitive load. Profiling is a telemetry signal, but not necessarily a "pillar"; in a unified model, it becomes a deeper zoom level, down to syscalls. OpenTelemetry itself unifies signals through shared context, but vendors can choose to implement pillar-based systems on top of it.

- "Pillar" is a marketing term; "signal" is the technical term used by OpenTelemetry.
- Multiple-pillars architecture stores each signal in separate silos, causing duplication and costly tool-hopping.
- Unified storage architecture keeps all signals in one database, enabling zoom in/out without losing context.
- Profiling is a type of telemetry signal, not a new pillar; it's just a deeper zoom level in a unified model.
- OpenTelemetry unifies signals via shared context, but vendors often build pillar-style products on top of it.