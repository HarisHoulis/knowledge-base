---
domain: engineering-culture
subdomain: engineering-practices
concept: napkin-math
title: Pushing software engineering limits with 'napkin math'
sources:
  - title: "Pushing software engineering limits with "napkin math""
    url: "https://newsletter.pragmaticengineer.com/p/pushing-software-engineering-limits"
    author: "Gergely Orosz"
    date: "Tue, 21 Jul 2026 16:52:07 GMT"
---

# Pushing software engineering limits with 'napkin math'

The article profiles Simon Eskildsen, co-founder of turbopuffer, and his journey from competitive programming to infrastructure engineering at Shopify. Simon credits his high school participation in the International Olympiad for Informatics (IOI) for teaching him to write correct, fast, and memory-efficient code, and for instilling resilience when facing difficult problems. At Shopify, his nearly decade-long tenure on the infrastructure team exposed him to large-scale challenges like sharding, multi-data-center expansion, and building tools like toxiproxy to test system resilience. One key lesson he highlights is that long tenure helps you learn to write software that ages well, often preferring simple solutions that outlast complex, multi-team designs (Orosz, 2026, https://newsletter.pragmaticengineer.com/p/pushing-software-engineering-limits).

The core concept of the article is "napkin math"—a practice Simon developed at Shopify to quickly estimate theoretical limits of computer operations. He maintains a table of key numbers (e.g., cost per gigabyte of memory, S3 storage, DRAM bandwidth) and memorizes them with flashcards. This allows him to challenge design decisions based on benchmarks, by calculating what the theoretical performance or cost should be and comparing it to the benchmark results. If a benchmark says an operation takes 10 seconds but napkin math suggests it should take 10 milliseconds, one of them is likely wrong. This method helped Simon spot inefficiencies and make better engineering decisions (Orosz, 2026).

Napkin math directly influenced the founding of turbopuffer. After ChatGPT's rise, context windows were small and fast search was critical for AI applications, but existing search solutions were surprisingly expensive. Using napkin math, Simon discovered they were far more expensive than necessary, leading him to build a new search product. The company raised $8M in seed funding, with Cursor as their first customer. The article also explores broader insights, such as the reasons for raising venture capital (funding R&D, growth, or ego) and the importance of not relying solely on benchmarks when making technical decisions (Orosz, 2026).

- Napkin math is a powerful tool: memorizing key cost/performance numbers lets you quickly compute theoretical limits and challenge flawed benchmarks.
- Long tenure at a company can be beneficial: Simon's nearly decade at Shopify taught him to write software that ages well, often preferring simple solutions over complex ones.
- Competitive programming (IOI) built a strong foundation: it taught algorithmic thinking, resilience, and how to learn complex topics independently.
- Simple, robust tools can have lasting impact: toxiproxy, built at Shopify, remains used 12 years later and demonstrates the value of creating practical solutions.
- VC funding isn't always necessary upfront: turbopuffer built a new product with seed funding, and Simon notes that funding decisions should be driven by business needs, not ego.