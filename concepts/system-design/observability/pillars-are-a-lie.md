---
domain: system-design
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

Charity Majors argues that the concept of observability 'pillars' is a marketing term, not a technical one. The technical term is 'signal', as defined by OpenTelemetry. Vendors label features like profiling as a 'fourth pillar' to justify higher prices, but this has no technical meaning. The real distinction is between two architectural models: the multiple pillars model (each signal type in siloed storage) and the unified storage model (all signals in one database). The pillars model causes data duplication, high costs, and a poor debugging experience where engineers must 'hop' between tools. Unified storage allows zooming from SLOs down to individual events without switching contexts. OpenTelemetry does not mandate the three-pillar approach; it actually unifies signals through shared context. Profiling, while a valid signal, is often not what engineers need—most need better tracing. Ultimately, pillars are a lie; data is data.

- Pillar is a marketing term; signal is the technical term, and profiling is a valid signal type.
- The multiple pillars architecture leads to data duplication and high costs; unified storage is the modern alternative.
- Unified storage lets you zoom from metrics to traces to logs seamlessly, reducing cognitive load.
- OpenTelemetry does not enforce the pillars model; it treats everything as unified data with shared context.