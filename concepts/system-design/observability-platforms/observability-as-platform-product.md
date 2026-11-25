---
domain: system-design
subdomain: observability-platforms
concept: observability-as-platform-product
title: Rethinking Observability as a Platform Product
sources:
  - title: "Rethinking Observability as a Platform Product • Kasper Borg Nissen • GOTO Copenhagen 2026"
    url: "https://www.youtube.com/watch?v=PGHXYcJJVJw"
    author: "GOTO Conferences"
    date: "2026-11-24"
---

# Rethinking Observability as a Platform Product

Kasper Borg Nissen argues that organizations typically treat observability as a tooling decision—pick a vendor, deploy agents, and expect insight to follow—yet teams still face fragmented signals, rising complexity, and slow incident response. The real problem is rarely the tool itself but the absence of a shared foundation and a coherent product experience (GOTO Copenhagen 2026 talk abstract).

He reframes observability as an internal platform product, designed with clear users, sane defaults, and long-term evolution in mind. Drawing parallels to Kubernetes and platform engineering, he contends that powerful primitives are not enough: standardization, correlation, and paved paths matter more than feature lists.

OpenTelemetry is presented as the vendor-neutral foundation for structured telemetry, decoupling instrumentation from backends and enabling correlation by default. This structured approach reduces cognitive load and improves reliability while laying groundwork for AI-assisted debugging and natural-language interaction with production systems. The core message: observability is about designing a platform that makes understanding systems easier—for both humans and machines—not about collecting more data.

- Observability failures usually stem from missing shared foundations and product experience, not from the chosen tool
- Treat observability as an internal platform product with clear users, sane defaults, and long-term evolution
- Standardization, correlation, and paved paths matter more than raw feature power, echoing platform engineering lessons
- OpenTelemetry provides a vendor-neutral, structured foundation that decouples instrumentation from backends and enables correlation by default
- Structured telemetry enables AI-assisted debugging and natural-language interaction with production systems