---
domain: engineering-culture
subdomain: engineering-practices
concept: napkin-math
title: Pushing software engineering limits with “napkin math”
sources:
  - title: "Pushing software engineering limits with “napkin math”"
    url: "https://newsletter.pragmaticengineer.com/p/pushing-software-engineering-limits"
    author: "Gergely Orosz"
    date: "Tue, 21 Jul 2026 16:52:07 GMT"
---

# Pushing software engineering limits with “napkin math”

The article profiles Simon Eskildsen, co-founder of turbopuffer, and his journey from high school programming competitions to infrastructure engineering at Shopify. Central to his success is “napkin math”: quick, rough calculations to estimate the theoretical limits of systems, such as DRAM bandwidth, S3 costs, and memory prices (Orosz, 2026). This practice allowed him to challenge design decisions based on benchmarks that were orders of magnitude off the theoretical optimum, revealing that many solutions were far more expensive or slower than necessary (Orosz, 2026).

Eskildsen’s background in the International Olympiad for Informatics taught him persistence and self-study, while his nearly decade-long tenure at Shopify exposed him to large-scale infrastructure problems and the value of simple, long-lasting solutions (Orosz, 2026). His creation of toxiproxy, a failure-injection proxy, exemplifies his approach to testing resilience without mocking low-level drivers (Orosz, 2026). The article also covers the origins of turbopuffer, which emerged after napkin math showed that existing search solutions were unnecessarily costly, and his pragmatic view on venture capital funding (Orosz, 2026).

- Napkin math involves memorizing key performance and cost numbers to quickly estimate theoretical limits and challenge flawed benchmarks.
- Long tenure at Shopify taught the importance of writing software that ages well, with simple solutions often outlasting complex multi-team designs.
- Competitive programming instilled a habit of deep self-study and persistence, which proved invaluable in engineering.
- Toxiproxy was developed to simulate network failures and test resilience without mocking low-level drivers, and it remains in use years later.
- Turbopuffer was founded after napkin math revealed that existing search solutions were far more expensive than theoretically necessary.