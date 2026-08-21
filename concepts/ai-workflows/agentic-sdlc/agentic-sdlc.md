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

Uber's investments in agentic AI have transformed their software development lifecycle. Over the past year, more than 70% of pull requests are now authored by local or cloud agents, and lines of code per engineer have doubled year-over-year. Additionally, they handled over 250 automated migrations, automatically moving 9 million lines of code. This acceleration was enabled by six years of foundational work on monorepos and Bazel.

- 70%+ of PRs at Uber are now authored by local or cloud agents; lines of code per engineer doubled YoY.
- The model gateway centralizes model access, enforcing PII redaction, safety guardrails, and per-project attribution under 100ms latency.
- The model gateway handles over 100 million model requests per day across 800+ internal projects.
- The MCP gateway provides a unified entry point for internal APIs and SaaS tools, with automated crawling into MCPs and token optimization strategies like Omni MCP and CLI projection.
- Over 250 automated migrations moved 9 million lines of code automatically, reducing toil.