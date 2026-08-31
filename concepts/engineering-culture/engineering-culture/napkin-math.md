---
domain: engineering-culture
subdomain: engineering-culture
concept: napkin-math
title: Pushing software engineering limits with “napkin math”
sources:
  - title: "Pushing software engineering limits with “napkin math”"
    url: "https://newsletter.pragmaticengineer.com/p/pushing-software-engineering-limits"
    author: "Gergely Orosz"
    date: "2026-07-21"
---

# Pushing software engineering limits with “napkin math”

The article profiles Simon Eskildsen, co-founder of turbopuffer, and his journey from a self-taught high school programmer to a senior infrastructure engineer at Shopify. A key theme is the power of “napkin math”: memorizing theoretical limits of compute, storage, and network costs, then using quick calculations to challenge benchmarks and design decisions. Eskildsen built and maintained a table of numbers—like the cost of a gigabyte of memory or S3 storage—and created flashcards to internalize them, enabling him to spot when a benchmark result was off by orders of magnitude from the theoretical optimum (Orosz, 2026).

Eskildsen’s long tenure at Shopify (nearly eight years) taught him the value of writing software that ages well, where simple solutions often outlast large, complex ones. He also built and open-sourced Toxiproxy, a network simulation tool for testing resilience. After ChatGPT took off, he applied napkin math to search infrastructure and found existing solutions were far more expensive than necessary, leading to the creation of turbopuffer. The article also covers his early life—competing in the International Olympiad in Informatics, starting a blog that caught Shopify’s attention—and his candid views on VC funding, noting that much of it is driven by ego rather than business needs (Orosz, 2026).

- Napkin math—using quick calculations from memorized theoretical limits—helps engineers challenge benchmarks and estimate true system costs and performance.
- A long tenure at one company can teach you to write software that ages well, as simple solutions often outlast large multi-team efforts.
- Building tools like Toxiproxy enables realistic failure testing by simulating network conditions without mocking low-level drivers.
- Starting a blog and documenting technical learnings can lead to unexpected career opportunities, as it did for Simon Eskildsen with Shopify.
- Applying napkin math to search infrastructure revealed that existing solutions were wastefully expensive, inspiring the creation of turbopuffer.