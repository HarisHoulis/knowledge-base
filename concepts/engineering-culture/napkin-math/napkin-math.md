---
domain: engineering-culture
subdomain: napkin-math
concept: napkin-math
title: Pushing software engineering limits with “napkin math”
sources:
  - title: "Pushing software engineering limits with “napkin math”"
    url: "https://newsletter.pragmaticengineer.com/p/pushing-software-engineering-limits"
    author: "Gergely Orosz"
    date: "2026-07-21"
---

# Pushing software engineering limits with “napkin math”

The article profiles Simon Eskildsen, a self-taught engineer who went from competing in the International Olympiad for Informatics (IOI) to an eight-year tenure at Shopify. His algorithmic training taught him to write correct, fast, and memory-efficient code, and his early blog—covering topics like his IOI experience and his broken iPhone—eventually caught the attention of a Shopify recruiter, landing him an infrastructure role (Orosz, 2026).

At Shopify, Eskildsen developed a practice he calls “napkin math”: maintaining a table of approximate numbers for costs and performance limits (e.g., $2 per gigabyte of memory, 100 GB/s DRAM bandwidth) and memorizing them with flashcards. This let him quickly evaluate engineering decisions by comparing observed benchmarks against theoretical ceilings, often revealing that systems were far slower or costlier than necessary (Orosz, 2026).

The article also covers his work building toxiproxy, a failure-injection proxy that remains in Shopify's CI years later, and highlights the benefits of long tenure: learning to write software that ages well and gaining deep infrastructure expertise. Finally, it describes how napkin math informed the founding of his startup turbopuffer, where he found that existing search solutions were unnecessarily expensive, and discusses pragmatic reasons for raising venture capital beyond ego (Orosz, 2026).

- Self-directed learning and algorithmic competitions like the IOI can build a strong engineering foundation even without a CS degree.
- Long tenure at one company allows engineers to develop deep infrastructure knowledge and learn to write software that outlasts multi-team projects.
- Napkin math—memorizing rough costs and performance limits—helps engineers challenge benchmarks and catch inefficiencies quickly.
- Tools like toxiproxy demonstrate how practical, open-sourced solutions can have lasting impact within an organization.