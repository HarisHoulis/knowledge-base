---
domain: system-design
subdomain: observability
concept: self-hosted-observability
title: Wrangling Telemetry at Scale: A Guide to Self-Hosted Observability
sources:
  - title: "Presentation: Wrangling Telemetry at Scale: A Guide to Self-Hosted Observability"
    url: "https://www.infoq.com/presentations/self-hosted-observability-stack-tradeoffs/"
    author: "Colin Douch"
    date: "2026-10-28"
---

# Wrangling Telemetry at Scale: A Guide to Self-Hosted Observability

Colin Douch presents battle-tested strategies for building and scaling self-hosted observability stacks, drawing on experience running telemetry infrastructure at scale. The talk focuses on correlating the three core telemetry signals—metrics, structured logs, and distributed traces—using open-source tooling rather than commercial SaaS platforms.

The stack centers on well-known open-source components: Prometheus and VictoriaMetrics for metrics, and Jaeger for distributed tracing. Douch frames the decision to self-host primarily around avoiding SaaS vendor lock-in, and treats the resulting engineering trade-offs as the central theme of the presentation rather than an afterthought.

Rather than a single-tool walkthrough, the talk is positioned as a guide to the operational and architectural choices involved in owning your observability pipeline—how the tools fit together, how signals are correlated, and what costs and complexity come with that control.

- Self-hosting observability avoids SaaS vendor lock-in but introduces real engineering trade-offs
- Correlating metrics, structured logs, and distributed traces is the core challenge at scale
- Open-source tooling like Prometheus, VictoriaMetrics, and Jaeger forms the basis of the stack
- The talk emphasizes battle-tested, practical strategies over theoretical architecture