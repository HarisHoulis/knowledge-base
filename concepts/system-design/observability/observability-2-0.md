---
domain: system-design
subdomain: observability
concept: observability-2-0
title: Have you heard? Clickhouse is winning the observability wars!
sources:
  - title: "Have you heard? Clickhouse is winning the observability wars!"
    url: "https://charity.wtf/p/have-you-heard-clickhouse-is-winning"
    author: "Charity Majors"
    date: "2026-07-08"
---

# Have you heard? Clickhouse is winning the observability wars!

Charity Majors argues that ClickHouse is winning the observability wars not merely because of its columnar storage, but because it enables a fundamentally better architecture—one that treats telemetry as unified data rather than as separate pillars (metrics, logs, and traces). She highlights Mat Duggan's experience: at 1TB/day any stack works, but at 10TB/day most become unmanageable, whereas ClickHouse scales linearly with more shards. Majors emphasizes that many newer observability vendors, despite building on columnar stores, still cargo-cult the 'three pillars' model, storing the same data multiple times and destroying its relational context, which makes telemetry worth less than the sum of its parts.

The post critiques Datadog's architecture, noting that while they do use columnar storage internally, their product still separates signals and charges for storage and correlation across datasets—a costly and product-inferior approach. Majors advocates for a single source of truth for telemetry, from which metrics, logs, and traces can be derived, arguing this is cheaper and exponentially more powerful. She notes that ClickHouse has used the term 'observability 2.0' and that the industry is slowly realizing that context-rich traces or wide events are all you need. The essay is a call for vendors to stop selling 'Datadog, but cheaper' and instead build genuinely better architecture that preserves the power of relationships in data.

- Columnar storage like ClickHouse scales linearly: 10TB/day looks like 1TB/day with more shards, unlike traditional mutating backends.
- The three pillars architecture forces storing the same telemetry in different formats, destroying valuable context and increasing costs.
- Observability should treat telemetry as a unified data set, not separate pillars; derive metrics, logs, and traces from a single source of truth.
- Newer vendors built on columnar storage still mimic Datadog's architecture and marketing, missing the opportunity to truly differentiate on product.
- The rise of AI workloads makes traces and wide structured events the most important telemetry, reinforcing the need for context-rich unified data.