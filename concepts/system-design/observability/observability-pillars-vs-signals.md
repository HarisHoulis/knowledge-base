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
  - title: "OpenTelemetry Signals"
    url: "https://opentelemetry.io/docs/concepts/signals/"
    author: "OpenTelemetry"
  - title: "OpenTelemetry is not three pillars"
    url: "https://www.honeycomb.io/blog/opentelemetry-is-not-three-pillars"
    author: "Austin Parker"
---

# How many pillars of observability can you fit on the head of a pin?

Charity Majors argues that the concept of 'pillars' in observability is a marketing construct, not a technical one. She distinguishes between 'pillar' as marketing terminology and 'signal' as a technical term, pointing out that OpenTelemetry defines signals like traces, metrics, logs, and baggage, with profiles and events in development. The article criticizes the 'multiple pillars' architecture model, where each signal type is stored in separate, siloed systems, leading to data duplication, high costs, and the need for engineers to 'hop' between tools to correlate information. Instead, Majors advocates for a unified storage model (o11y 2.0) where all telemetry data is stored together in one database, preserving context and enabling users to zoom from metrics to traces to logs without manual cross-referencing. She also addresses profiling, suggesting that for most users a good tracing tool is sufficient, and that profiling is just another signal type that fits into the unified model. The conclusion emphasizes that OpenTelemetry, contrary to popular belief, actually supports unified telemetry through shared context, though it can be used in a pillars-based way if vendors choose.

- Pillar is a marketing term; signal is a technical term.
- The multiple pillars model leads to data duplication and high costs.
- Unified storage (o11y 2.0) stores all signals together, enabling seamless zooming.
- OpenTelemetry unifies telemetry signals via shared context, not just three pillars.
- Profiling is a signal type, not necessarily a 'pillar'.