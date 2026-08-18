---
domain: system-design
subdomain: performance-modeling
concept: napkin-math
title: Pushing software engineering limits with napkin math
sources:
  - title: "Pushing software engineering limits with “napkin math”"
    url: "https://newsletter.pragmaticengineer.com/p/pushing-software-engineering-limits"
    author: "Gergely Orosz"
    date: "2026-07-21"
---

# Pushing software engineering limits with napkin math

The article profiles Simon Eskildsen, co-founder of turbopuffer, and his journey from high school programming competitions to infrastructure engineering at Shopify and founding a startup. Central to his approach is 'napkin math'—quick, back-of-the-envelope calculations based on memorized performance numbers (e.g., cost of memory, S3 bandwidth, DRAM limits) to reason about system behavior and challenge design decisions. He built and memorized a table of key metrics using flashcards, enabling him to spot when a benchmark result was orders of magnitude off from theoretical limits, and to push for simpler, more efficient solutions (Orosz, 2026).

Simon's long tenure at Shopify (eight years) taught him the value of writing software that ages well, and that simple solutions often outperform complex, multi-team efforts. This experience also led to open-source tools like Toxiproxy, a proxy for simulating network failures. Later, napkin math directly influenced the founding of turbopuffer, a search/database solution, by revealing that existing search products were far more expensive than necessary. The article also discusses Simon's views on VC funding, emphasizing that raising capital should be driven by business needs rather than ego (Orosz, 2026).

- Napkin math: use back-of-the-envelope calculations and memorized performance numbers to estimate theoretical limits and challenge questionable benchmarks.
- Long engineering tenure builds deep expertise and perspective: understanding systems deeply and learning to create simple solutions that stand the test of time.
- Failure-injection tools like Toxiproxy enable realistic resilience testing without mocking low-level drivers.
- Major engineering decisions (like database choices) should be grounded in fundamental limits, not just benchmark comparisons.
- VC funding should be justified by R&D or growth needs, not founder ego.