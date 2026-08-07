---
domain: system-design
subdomain: observability
concept: contextual-telemetry
title: Your Data Is Made Powerful By Context (so stop destroying it already)
sources:
  - title: "Your Data Is Made Powerful By Context (so stop destroying it already)"
    url: "https://charity.wtf/p/your-data-is-made-powerful-by-context"
    author: "Charity Majors"
    date: "Mon, 09 Mar 2026 18:18:17 GMT"
---

# Your Data Is Made Powerful By Context (so stop destroying it already)

Charity Majors argues that observability's core problem is not culture or tooling but the data model. The dominant 'three pillars' (metrics, logs, traces) separate telemetry by signal type, destroying the relational seams that give data its value. Adding an attribute to a structured log doesn't linearly increase query power; it combinatorially multiplies it. For example, 50 fields yield 1.1 quadrillion possible combinations, making context and relationships the most valuable part of any dataset [1]. Majors contends that this destruction of context is catastrophic for software engineering use cases and especially for agentic AI validation, where precision tooling requires rich, interconnected data to find minute anomalies among billions of requests [1].

The article highlights that AI agents, like those described by Kyle Forster, often bypass traditional three-pillar observability to seek raw, pre-digested telemetry with all its connective tissue intact. Joins across silos, even by AI, cannot restore the combinatorial power of preserved context. To support agentic workflows at high change rates, production observability must prioritize speed, flexibility, tons of context, and semantic grounding via conventions. The example of a staged rollout for a credit card provider shows how a few dozen anomalous requests per day become findable only with precision tooling powered by context and cardinality. Ultimately, capturing and preserving relationships between attributes is essential—both for humans and for AI—because 'the work is making your judgment machine-readable' [1].

- Telemetry data becomes exponentially more powerful with context: 50 attributes yield 1.1 quadrillion combinations.
- The three-pillars model (metrics, logs, traces) destroys the relational seams that make data valuable.
- Precision tooling, enabled by rich context and cardinality, makes minute anomalies findable in massive request streams.
- Agentic AI validation requires high-context, high-cardinality telemetry—not just joins across siloed data.
- Preserving context and encoding human judgment into systems is critical for automated validation.