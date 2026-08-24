---
domain: engineering-culture
subdomain: engineering-practices
concept: napkin-math
title: Pushing software engineering limits with “napkin math”
sources:
  - title: "Pushing software engineering limits with “napkin math”"
    url: "https://newsletter.pragmaticengineer.com/p/pushing-software-engineering-limits"
    author: "Gergely Orosz"
    date: "2026-07-21"
---

# Pushing software engineering limits with “napkin math”

The article profiles Simon Eskildsen, co-founder and CEO of turbopuffer, tracing his path from high school programming competitions to nearly a decade at Shopify’s infrastructure team. It emphasizes how long tenure helped him learn deep infrastructure concepts and write software that ages well, noting that simple solutions often outlast complex, multi-team RFC-driven ones (Orosz, 2026).

Central to Simon’s approach is “napkin math”: maintaining a table of theoretical limits and costs—such as DRAM bandwidth, S3 costs, and memory prices—and memorizing these numbers via flashcards. This allowed him to challenge design decisions based on benchmarks, as in a search query that theoretically should take 10 milliseconds but was benchmarked at 10 seconds, revealing a flaw in the benchmark or implementation (Orosz, 2026).

At Shopify, Simon built and open-sourced Toxiproxy, a failure-injection proxy that simulates network latency and downtime, which still runs in Shopify’s CI system years later. He later founded turbopuffer after using napkin math to discover that existing search solutions were far more expensive than necessary. Cursor became a key early customer after Simon helped with their search and database needs. The article also discusses reasons to raise venture capital, including funding R&D and growth, while cautioning against ego-driven funding (Orosz, 2026).

- Long tenure at one company can teach infrastructure depth and how to write software that ages well; simple solutions often outperform complex ones.
- Napkin math—memorizing hardware limits and costs—enables quick theoretical estimates that expose flawed benchmarks and expensive designs.
- Toxiproxy, built at Shopify, is a failure-injection proxy for testing resilience and was open-sourced in 2014.
- Napkin math led to founding turbopuffer because existing search solutions were unnecessarily costly.
- Raise VC funding for R&D and growth, not for ego.