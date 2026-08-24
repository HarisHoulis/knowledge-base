---
domain: ai-workflows
subdomain: agentic-sdlc
concept: agentic-sdlc
title: Agentic SDLC at Uber
sources:
  - title: "Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber"
    url: "https://www.youtube.com/watch?v=17-YSUHo6Lk"
    author: "AI Engineer"
    date: "2026-08-21T13:00:06+00:00"
---

# Agentic SDLC at Uber

Uber's journey toward a managed software factory is driven by agentic AI. With few thousand engineers across 12 global tech sites, their investments have led to over 70% of pull requests now authored by local or cloud agents, and twice the number of lines of code per engineer year-over-year. This extends beyond coding, with more than 250 automated migrations covering 9 million lines of code, significantly reducing toil (Medisetty & Huda, 2026).

- Over 70% of PRs at Uber are authored by local or cloud agents, doubling lines of code per engineer.
- A model gateway enforces PII redaction, safety guardrails under 100ms, and per-user/project/team attribution, handling 100M+ daily requests across 800+ projects.
- An MCP gateway automatically projects internal APIs and SaaS tools into MCPs, with token-optimization patterns like Omni MCP, CLI, and a code mode skill.
- Uber completed 250+ automated migrations covering 9 million lines of code, reducing engineering toil.
- The six building blocks are at various maturity stages; the talk demonstrates an end-to-end feature build using these blocks.