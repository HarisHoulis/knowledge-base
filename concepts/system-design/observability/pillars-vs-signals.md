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

Charity Majors argues that the 'pillars of observability' (logs, metrics, traces, profiling, etc.) are a marketing construct, not a technical reality. The technical term is 'signal,' as defined by OpenTelemetry. While profiling is a valid telemetry signal, calling it a 'pillar' is a vendor-driven framing designed to sell separately siloed products rather than to improve debugging (Majors, https://charity.wtf/p/the-pillar-is-a-lie).

- 'Pillar' is a marketing term; 'signal' is the technical term used by OpenTelemetry.
- The multiple-pillars storage model duplicates data across silos, driving up costs and forcing 'bunny hopping' between tools.
- A unified storage model stores all signal types together as structured data, allowing zoom-in/zoom-out navigation instead of manual cross-referencing.
- OpenTelemetry does not require a three-pillars model; it unifies signals through shared context and can support a unified storage approach.
- Profiling is a useful signal but not a 'pillar'; for most teams, good tracing may be enough.