---
domain: system-design
subdomain: observability
concept: head-based-sampling
title: How Eve Online Leverages Head Based Sampling to Observe "Fun"
sources:
  - title: "Presentation: How Eve Online Leverages Head Based Sampling to Observe "Fun""
    url: "https://www.infoq.com/presentations/eve-observability-head-sampling/"
    author: "Nicholas Herring"
    date: "2026-10-13"
---

# How Eve Online Leverages Head Based Sampling to Observe "Fun"

Nicholas Herring presents how EVE Online approaches distributed tracing and observability across a 20-year-old MMO architecture. The talk focuses on the challenges of maintaining visibility into a high-throughput, real-time game simulation while controlling telemetry costs and avoiding performance degradation.

Herring discusses leveraging head-based sampling alongside dynamic exponential moving average (EMA) and deterministic sampling techniques. These approaches are used to maintain high system fidelity in the observability data while keeping telemetry overhead manageable under the load of real-time game simulations.

The presentation frames observability around the goal of observing "fun" — using sampling strategies to capture meaningful signals from a long-lived, distributed system without letting tracing itself become a performance or cost burden.

- EVE Online applies head-based sampling to distributed tracing in a 20-year-old MMO architecture
- Dynamic EMA and deterministic sampling techniques complement head-based sampling
- Sampling strategies balance high system fidelity against telemetry cost control
- The approach aims to avoid performance degradation under high-throughput real-time game simulations