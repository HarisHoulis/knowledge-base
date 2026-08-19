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

Gergely Orosz interviews Simon Eskildsen, co-founder and CEO of turbopuffer, about his journey from high-school algorithmic programming to infrastructure engineering at Shopify and beyond. A central theme is “napkin math”: using rough, back-of-the-envelope calculations to estimate theoretical performance and cost limits, enabling engineers to challenge existing benchmarks and make better design decisions. Eskildsen explains how he built and memorized a table of key numbers—like DRAM bandwidth, S3 costs, and memory prices—to quickly spot when systems are orders of magnitude slower or more expensive than they should be (Orosz, 2026).

The article also covers Eskildsen’s experience at the International Olympiad for Informatics (IOI), which taught him to learn complex concepts independently and avoid “digging holes” by sticking too long with flawed approaches. At Shopify, he spent eight years on infrastructure, learning to write software that ages well and building toxiproxy, a fault-injection proxy still used in Shopify’s CI system. He also discusses the origins of his startup turbopuffer, which built a fast search product after napkin math revealed existing solutions were far costlier than necessary. Finally, the conversation touches on why founders raise venture capital—suggesting that ego often plays a larger role than business needs (Orosz, 2026).

- Napkin math—quick, order-of-magnitude calculations—helps engineers estimate theoretical performance limits and question flawed benchmarks.
- Long tenure at a company can teach durable lessons like writing software that ages well, as demonstrated by Simon Eskildsen’s eight years at Shopify.
- Building tools like toxiproxy for fault injection enables more realistic resilience testing than mocking low-level drivers.
- Competitive programming experiences like the IOI can instill perseverance and self-directed learning habits that translate to professional engineering.
- VC funding decisions are not always based on business needs; ego can be a significant factor.