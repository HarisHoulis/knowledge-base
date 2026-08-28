---
domain: engineering-culture
subdomain: performance-engineering
concept: napkin-math
title: Pushing software engineering limits with 'napkin math'
sources:
  - title: "Pushing software engineering limits with "napkin math""
    url: "https://newsletter.pragmaticengineer.com/p/pushing-software-engineering-limits"
    author: "Gergely Orosz"
    date: "Tue, 21 Jul 2026 16:52:07 GMT"
---

# Pushing software engineering limits with 'napkin math'

The article profiles Simon Eskildsen, co-founder of turbopuffer, and traces his path from high school competitive programming (IOI) to a decade at Shopify and eventually founding a startup. His IOI experience taught him to persist through hard problems and avoid getting stuck on flawed approaches, a lesson he later applied to infrastructure engineering (Orosz, 2026).

At Shopify, Simon developed "napkin math": memorizing key performance numbers (like DRAM bandwidth and S3 costs) and using quick calculations to sanity-check benchmarks and design decisions. This allowed him to identify when systems were far slower or more expensive than theoretically necessary. He also built and open-sourced toxiproxy, a fault-injection proxy for testing resilience, which was still used at Shopify 12 years later (Orosz, 2026).

These skills led to founding turbopuffer, a search/database startup, after Simon used napkin math to discover that existing search solutions were surprisingly expensive. With $8M in seed funding, Cursor became turbopuffer's first customer. The article also notes Simon's views on raising venture capital, including funding R&D and growth, but warns against ego-driven funding (Orosz, 2026).

- Napkin math is a quick-calculation technique for finding theoretical limits and challenging benchmarks.
- A decade at Shopify taught Simon to write software that ages well, with simple solutions often outlasting complex ones.
- Toxiproxy, a fault-injection proxy, was born from testing resilience and is still used at Shopify 12 years later.
- IOI competitive programming instilled persistence and the ability to avoid 'digging holes' by starting fresh when needed.
- Turbopuffer raised $8M and landed Cursor as its first customer after applying napkin math to search costs.