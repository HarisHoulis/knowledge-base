---
domain: system-design
subdomain: performance-estimation
concept: napkin-math
title: Pushing software engineering limits with napkin math
sources:
  - title: "Pushing software engineering limits with 'napkin math'"
    url: "https://newsletter.pragmaticengineer.com/p/pushing-software-engineering-limits"
    author: "Gergely Orosz"
    date: "2026-07-21"
---

# Pushing software engineering limits with napkin math

In this article, Gergely Orosz interviews Simon Eskildsen, co-founder of turbopuffer, about the power of "napkin math"—quick, rough calculations using memorized performance and cost numbers to sanity-check engineering decisions. Eskildsen, who started his career at Shopify after an impressive run in the International Olympiad for Informatics, developed a habit of memorizing key metrics like memory cost, S3 storage cost, and DRAM bandwidth. This enabled him to catch flawed benchmarks and challenge design choices, as he explains: when a database benchmark shows a search taking 10 seconds, napkin math might suggest it should take 10 milliseconds, revealing a problem in the implementation or benchmark (Orosz, 2026).

Eskildsen's long tenure at Shopify taught him that writing software that ages well often comes from simple solutions that outlast complex, multi-team efforts. His work on infrastructure included building toxiproxy, a proxy to simulate network failures, which is still used in Shopify's CI. The article also traces the origins of turbopuffer, where napkin math revealed that existing search solutions were far more expensive than necessary, leading to a new product that attracted Cursor as its first customer. Finally, Eskildsen shares candid thoughts on when raising venture capital makes sense—stressing that too much funding is often driven by ego rather than business needs (Orosz, 2026).

- Napkin math involves memorizing key performance and cost numbers to quickly estimate theoretical limits and spot unreasonable benchmarks.
- A long tenure at one company lets engineers internalize lessons about writing simple, durable software that ages well.
- Algorithmic competition experience taught Eskildsen to dig into concepts deeply and avoid 'digging holes' by starting over when stuck.
- Toxiproxy, built at Shopify, injects network failures to test resilience and remains in use years later.
- Napkin math can reveal when existing solutions are unnecessarily expensive, as it did for turbopuffer's search product.