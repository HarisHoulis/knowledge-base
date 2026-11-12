---
domain: system-design
subdomain: observability
concept: opentelemetry-queue-tracing
title: Uncorking Queueing Bottlenecks with OpenTelemetry
sources:
  - title: "Presentation: Uncorking Queueing Bottlenecks with OpenTelemetry"
    url: "https://www.infoq.com/presentations/opentelemetry-queue-observability/"
    author: "Julian Wreford, Oli Lane"
    date: "2026-11-11"
---

# Uncorking Queueing Bottlenecks with OpenTelemetry

Oli Lane and Julian Wreford describe how Gearset replaced guesswork in its distributed asynchronous queues with OpenTelemetry tracing. They argue that traditional metrics fall short for diagnosing queueing bottlenecks, and show how tracing gives visibility into where work actually spends its time.

The talk centers on implementing user-centric SLOs based on latency distributions rather than relying on coarse aggregate metrics. This framing ties reliability targets to what users actually experience across asynchronous processing paths.

Beyond tooling, the presenters share practical debugging tips aimed at senior developers, software architects, and engineering leaders, connecting improved observability to both system reliability and team culture.

- Traditional metrics are insufficient for diagnosing distributed asynchronous queue bottlenecks; OpenTelemetry tracing fills the gap.
- User-centric SLOs should be based on latency distributions rather than aggregate metrics.
- Practical debugging techniques are offered for senior developers, architects, and engineering leaders.
- Better observability supports both system reliability and team culture.