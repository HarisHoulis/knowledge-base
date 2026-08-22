---
domain: engineering-culture
subdomain: technical-estimation
concept: napkin-math
title: Pushing software engineering limits with “napkin math”
sources:
  - title: "Pushing software engineering limits with “napkin math”"
    url: "https://newsletter.pragmaticengineer.com/p/pushing-software-engineering-limits"
    author: "Gergely Orosz"
    date: "2026-07-21"
---

# Pushing software engineering limits with “napkin math”

In this article, Gergely Orosz interviews Simon Eskildsen, co-founder of turbopuffer, about the power of “napkin math” – performing quick calculations to estimate theoretical limits of computer systems. Simon developed this skill during his eight years at Shopify, where he memorized key metrics like memory costs, bandwidth, and latency using flashcards. This practice allowed him to challenge design decisions based on benchmarks by comparing actual performance to theoretical limits, such as calculating that a search query should take 10 milliseconds based on DRAM bandwidth rather than the 10 seconds a benchmark claimed (Orosz, 2026).

Simon’s early exposure to algorithmic programming through the International Olympiad for Informatics (IOI) taught him resilience and the importance of avoiding “digging holes” when stuck on a problem. At Shopify, he worked on infrastructure challenges like sharding, multi-data-center expansion, and building toxiproxy, an open-source failure injection tool. His long tenure also taught him that simple solutions often outlast large, complex ones. These experiences shaped his approach at turbopuffer, where he used napkin math to discover that existing search solutions were far more expensive than necessary, leading to a new product that attracted Cursor as its first customer (Orosz, 2026).

- Napkin math is a superpower for engineers: quickly estimating theoretical limits of hardware and costs helps challenge inefficient designs and benchmark-based decisions.
- Long tenure at one company, like Simon's 8 years at Shopify, allows deep learning about infrastructure and the value of writing software that ages well.
- IOI participation built algorithmic problem-solving skills and resilience, including the lesson to avoid getting fixated on a flawed approach and to start fresh.
- Toxiproxy, an open-source tool for simulating network failures, originated from practical testing needs at Shopify and remains in use years later.
- Raising venture capital should be driven by business needs like funding R&D or growth, not ego; Simon's startup initially succeeded without VC funding.