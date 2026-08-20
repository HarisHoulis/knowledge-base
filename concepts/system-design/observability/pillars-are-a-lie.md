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

Charity Majors argues that the concept of "pillars" of observability is a marketing construct, not a technical one. The technical term is "signal," as defined by OpenTelemetry, which currently supports traces, metrics, logs, and baggage, with events and profiles in development. Calling something a "pillar" is typically a vendor move to justify selling another siloed product, not a meaningful technical distinction (Majors, 2025).

Majors contrasts two architectural models: the multiple-pillars model (o11y 1.0), where each signal type is stored separately, and the unified storage model (o11y 2.0), where all signals are stored together in one database. The pillars model leads to data duplication, higher costs, and a "bunny hopping" debugging experience across different tools. The unified model allows users to zoom seamlessly from SLOs to metrics to traces to logs without losing context, because it is all the same underlying data (Majors, 2025).

OpenTelemetry is often mischaracterized as reinforcing the three-pillars model, but according to Austin Parker, OTel fundamentally unifies telemetry signals through shared distributed context. It can be used in either model, but it does not require the traditional siloed approach. In a unified world, profiling becomes just another level of zoom—down to syscalls and kernel operations—rather than a separate pillar (Majors, 2025).

- Pillar is a marketing term; signal is the technical term, with OpenTelemetry as the canonical reference.
- Profiling is a telemetry signal, but whether it's a 'pillar' is a vendor positioning question, not a technical one.
- The multiple-pillars storage model causes massive data duplication and high cost; unified storage preserves context and reduces complexity.
- OpenTelemetry unifies signals through shared context and does not mandate a three-pillars architecture.
- In a unified observability model, profiling is just a finer zoom level into the same dataset, not a separate silo.