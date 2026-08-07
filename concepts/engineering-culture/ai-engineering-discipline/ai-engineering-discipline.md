---
domain: engineering-culture
subdomain: ai-engineering-discipline
concept: ai-engineering-discipline
title: AI Demands More Engineering Discipline. Not Less
sources:
  - title: "AI demands more engineering discipline. Not less"
    url: "https://charity.wtf/p/ai-demands-more-engineering-discipline"
    author: "Charity Majors"
    date: "2026-06-15"
---

# AI Demands More Engineering Discipline. Not Less

In this article, Charity Majors clarifies that her earlier piece was misread as advocating for skipping code review. She explains that AI-generated code has reached a quality level comparable to a median software engineer, making code cheap and instantly regenerable. This flips the economics of code production: code is no longer a treasured asset but a disposable artifact. She draws an analogy to the shift from handcrafted servers to immutable infrastructure, where replacement is preferred over mutation (Majors, 2026).

Majors builds on Chad Fowler's Phoenix Architectures, particularly the idea of treating application code like infrastructure: never fix a running thing; replace it. The 'deletion test' reveals that when code is precious, it's because it's the only place knowledge lives, but that's really an evaluation problem. Code should be seen as a materialized view of understanding, useful while current, disposable when stale. This reframing offloads the burden from code as permanent artifacts to continuous regeneration (Majors, 2026).

Contrary to the fear that AI reduces engineering rigor, Majors argues that AI demands more discipline, not less. Humans are poor at validation and repetitive review; our strengths lie in creativity and judgment. The shift forces engineers to focus on production observability, behavioral tests, characterization tests, and evals in production. Production becomes a stage of development, and the tools that will support this shift are still emerging, but the principles come from ops and QA domains long undervalued by software engineering (Majors, 2026).

- AI-generated code is now approximately as good as the median engineer, making code production effectively free and instant.
- The shift toward disposable code mirrors the earlier transition from pets to cattle in infrastructure management.
- Code should be treated as a materialized view of understanding, not a precious asset; it can be regenerated when stale.
- Engineers should focus on production validation, observability, and automated tests rather than manual code review as the primary quality gate.
- AI demands more engineering discipline, not less; it forces teams to embrace practices like behavioral testing and continuous evaluation.