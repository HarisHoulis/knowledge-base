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

Charity Majors argues that the concept of "pillars" in observability is a marketing invention rather than a technical necessity. She contrasts it with "signals," which are technical categories defined by OpenTelemetry (traces, metrics, logs, etc.). The article criticizes the multiple-pillars architecture—where each signal type is stored in its own silo—as expensive, duplicative, and cognitively taxing for engineers who must hop between tools to debug. She proposes the unified storage model (o11y 2.0), where all telemetry is stored together as wide structured events, allowing users to zoom from high-level metrics down to traces and logs without context switching (Majors, 2025).

Profiling, the current example, is a useful signal but not automatically a "pillar." Majors points out that vendors push "pillar" language to sell additional products, while the underlying technical reality is that all telemetry is just data. OpenTelemetry supports both models but fundamentally unifies signals through shared context. The article concludes that in a unified world, profiling simply means deeper zoom capability, and most teams actually need better tracing rather than a separate profiling tool (Majors, 2025).

- "Pillar" is a marketing term; "signal" is the technical term defined by OpenTelemetry.
- The multiple-pillars architecture silos data, leading to duplication, high costs, and a poor debugging experience ("bunny hopping").
- A unified storage model stores all signals together, letting users zoom in/out seamlessly from metrics to traces to logs.
- Profiling is a valid telemetry signal but not inherently a "pillar"—it becomes just another zoom level.
- OpenTelemetry does not mandate the pillars model; it can support both, but unified context is its fundamental design.