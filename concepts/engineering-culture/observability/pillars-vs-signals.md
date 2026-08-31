---
domain: engineering-culture
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

Charity Majors argues that the concept of "pillars" in observability is a marketing construct, not a technical one. She distinguishes "pillar" from "signal," citing OpenTelemetry's definition of signals (traces, metrics, logs, baggage, events, profiles) as the technical canonical term. The article criticizes the "multiple pillars" architecture model (o11y 1.0), where each signal type is stored separately, leading to massive data duplication, high costs, and a frustrating "bunny hopping" debugging experience across siloed tools. Majors contrasts this with the "unified storage model" (o11y 2.0), where all signals are stored together in a single high-cardinality database, allowing users to zoom in and out from SLOs to traces to logs without context-switching. She asserts that profiling is simply another signal type, not a new pillar, and in a unified world it would provide even finer resolution (down to syscalls) rather than a separate silo. She also addresses OpenTelemetry's role, noting Austin Parker's argument that OTel fundamentally unifies signals through shared distributed context, even though vendors can implement it in a pillars-based way.

- Pillar is a marketing term; signal is a technical term defined by OpenTelemetry.
- The multiple pillars model duplicates data across silos, inflating costs and making debugging difficult.
- Unified storage (o11y 2.0) stores all signals together, enabling seamless zoom-in from metrics to traces.
- Profiling is a signal, not a fourth pillar; in a unified architecture it adds finer-grained visibility.
- OpenTelemetry supports unified context but can be used with either architecture model.