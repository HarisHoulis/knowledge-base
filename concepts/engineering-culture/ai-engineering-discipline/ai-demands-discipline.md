---
domain: engineering-culture
subdomain: ai-engineering-discipline
concept: ai-demands-discipline
title: AI demands more engineering discipline. Not less
sources:
  - title: "AI demands more engineering discipline. Not less"
    url: "https://charity.wtf/p/ai-demands-more-engineering-discipline"
    author: "Charity Majors"
    date: "Mon, 15 Jun 2026 05:35:09 GMT"
---

# AI demands more engineering discipline. Not less

The article argues that AI-generated code, which has become approximately as good as that of a median software engineer with models like Opus 4.5, has turned the economics of code production upside down: code is now cheap and disposable rather than precious and durable. This shift requires greater engineering discipline, not less, particularly in validation and production practices. The author aligns with Chad Fowler's concept of "Phoenix Architectures," where code is treated as a cache—a materialized view of understanding—that should be regenerated rather than mutated, reducing entropy. She emphasizes that human brains are poor at validation and that the real rigor should move to production, using observability, behavioral tests, and evals. The key insight is that code is no longer the primary artifact; instead, the focus should be on shared understanding and production systems.

- AI-generated code (e.g., Opus 4.5) has made code production cheap and fast, shifting the bottleneck from writing to validation.
- Code should be treated as disposable and regenerable, like immutable infrastructure, rather than a precious asset to be edited in place.
- Engineering rigor must relocate to production through observability, behavioral tests, and evals, as humans are weak at quality gatekeeping.
- Adopting Phoenix Architectures (e.g., infrastructure as code principles) reduces drift and entropy by replacing rather than mutating code.