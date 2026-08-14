---
domain: engineering-culture
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

Charity Majors argues that the 'pillars of observability' framing is a marketing construct, not a technical one. She distinguishes between 'pillar,' which vendors use to sell siloed products, and 'signal,' which is a precise term defined by OpenTelemetry. Profiling is a type of telemetry signal, not necessarily a new pillar. Majors contends that the multiple-pillars model stores the same data in separate databases, causing duplication, high cost, and a fragmented 'bunny hopping' debugging experience. A unified storage model—where all signals are stored together and metrics, logs, and traces are derived from one dataset—lets engineers zoom from SLOs down to events without copying IDs or matching timestamps. She quotes Austin Parker explaining that OpenTelemetry unifies signals through shared context and does not require a three-pillars architecture. In a unified world, profiling simply adds finer-grained zoom (e.g., syscalls) rather than a separate product. Majors concludes that most teams claiming to need profiling actually need better tracing (Majors, 2025).

- 'Pillar' is a marketing term; 'signal' is the technical term (Majors, 2025).
- OpenTelemetry currently supports traces, metrics, logs, and baggage as signals, with events and profiles at proposal/development stage (as cited in Majors, 2025).
- The multiple-pillars architecture stores each signal separately, leading to data duplication, higher cost, and a disjointed debugging workflow (Majors, 2025).
- Unified storage (o11y 2.0) keeps all telemetry in one place, letting engineers zoom in and out without 'bunny hopping' between tools (Majors, 2025).
- OpenTelemetry does not mandate a three-pillars model; it unifies signals through shared context (Majors, 2025).