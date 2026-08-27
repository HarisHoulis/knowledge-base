---
domain: engineering-culture
subdomain: performance-estimation
concept: napkin-math
title: Pushing software engineering limits with “napkin math”
sources:
  - title: "Pushing software engineering limits with “napkin math”"
    url: "https://newsletter.pragmaticengineer.com/p/pushing-software-engineering-limits"
    author: "Gergely Orosz"
    date: "Tue, 21 Jul 2026 16:52:07 GMT"
---

# Pushing software engineering limits with “napkin math”

Simon Eskildsen, co-founder and CEO of turbopuffer, shares his journey from competitive programming in high school to nearly a decade at Shopify, where he developed the practice of “napkin math” – using rough calculations to quickly challenge performance and cost claims. His early experience at the International Olympiad for Informatics (IOI) taught him to solve algorithmic problems efficiently and avoid getting stuck in unproductive rabbit holes, a lesson he carried into his professional career (Orosz, 2026).

At Shopify, Simon spent eight years on the infrastructure team, where he learned about databases, sharding, multi-data center setups, and wrote the open-source tool Toxiproxy to simulate network failures. During this time, he built a personal table of system limits – such as memory costs, bandwidth, and latencies – and memorized the numbers with flashcards. This allowed him to spot when benchmarks were unrealistic: if a search query should take 10 milliseconds by napkin math but a benchmark says 10 seconds, then something is wrong (Orosz, 2026).

This napkin-math mindset directly led to the creation of turbopuffer. After ChatGPT's rise, Simon realized that existing search solutions were far more expensive than necessary, based on simple cost and speed calculations. He raised $8 million in seed funding and built a new kind of search engine, with Cursor as its first customer. He also reflected on the real reasons companies raise venture capital – funding R&D, growth, and often ego – and emphasized that founders should align funding with actual business needs (Orosz, 2026).

- Competitive programming (IOI) taught Simon to write fast, memory-efficient algorithms and to avoid getting stuck on flawed approaches.
- Long tenure at Shopify allowed him to learn infrastructure deeply and build tools like Toxiproxy that test system resilience.
- Napkin math – memorizing system limits and costs – enables engineers to quickly validate whether a system's performance or price is reasonable.
- Using napkin math, Simon discovered search solutions were unnecessarily expensive, leading him to start turbopuffer.
- VC funding can be driven by ego as well as business needs; founders should evaluate if raising money is truly necessary.