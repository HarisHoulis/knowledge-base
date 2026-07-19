---
domain: engineering-culture
subdomain: observability
concept: columnar-storage-observability
title: Have you heard? Clickhouse is winning the observability wars!
sources:
  - title: "Have you heard? Clickhouse is winning the observability wars!"
    url: "https://charity.wtf/p/have-you-heard-clickhouse-is-winning"
    author: "Charity Majors"
    date: "2026-07-08"
---

# Have you heard? Clickhouse is winning the observability wars!

Charity Majors argues that Clickhouse is winning the observability wars not because it's a specific tool, but because it represents a fundamental shift to columnar storage for observability backends. She highlights how columnar storage, unlike traditional architectures, scales linearly without performance cliffs or schema lock-ins, handling high cardinality data seamlessly. However, she criticizes that many newer observability vendors built on columnar storage still mimic the old three-pillar model (metrics, logs, traces) instead of embracing a unified, context-rich data approach. She calls this 'Observability 2.0' and notes that Datadog, despite using a columnar engine called Husky, still splits data across pillars, leading to astronomical costs and lost contextual value. The key insight is that a single, wide structured event store—like the trace or canonical logs—is more powerful and cost-effective than separate pillars.

- Columnar storage (e.g., Clickhouse) enables linear scaling from 1TB to 10TB/day without architectural changes, unlike traditional systems that break down.
- Most post-2019 observability tools use columnar storage but still sell 'Datadog, but cheaper' instead of leveraging the full potential of unified storage.
- Observability 2.0 advocates for a single, context-rich data source (wide events or traces) rather than separate pillars, preserving combinatorial value of relationships.
- Datadog's architecture stores the same data multiple times (metrics, logs, traces) and charges for correlations, making it expensive and product-wise inferior.
- The real winner is columnar storage as a paradigm, not any single vendor—Clickhouse is a good open-source option, but managed services like Honeycomb also embody this approach.