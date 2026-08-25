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

At Uber, agentic AI investments have transformed the software development lifecycle: over 70% of pull requests are now authored by local or cloud agents, contributing to a 2x year-over-year increase in lines of code per engineer (AI Engineer, 2026). The company also accelerated toil reduction through 250+ automated migrations covering 9 million lines of code. This progress was enabled by earlier technical foundations like monorepos and Bazel.

Uday Kiran Medisetty outlined six building blocks for this transformation. The first is a model gateway that enforces PII redaction, bounded latency (under 100ms for guardrails), and per-user/project/team attribution for all model requests. It now handles over 100 million requests per day across 800+ internal projects. The second is an MCP gateway that makes internal APIs and SaaS tools agent-accessible through one common entry point, with automated API crawling and token optimization strategies such as Omni MCP, CLI projection, and a code-mode skill.

- 70%+ of PRs at Uber are now authored by local or cloud agents, doubling lines of code per engineer year-over-year.
- 250+ automated migrations were handled, covering 9 million lines of code automatically.
- A model gateway centralizes model access with PII redaction, guardrails under 100ms, and per-user/project/team attribution.
- An MCP gateway simplifies agent tool access via automated API crawling and token optimization strategies like Omni MCP.
- Uber handles over 100 million model requests per day across 800+ internal projects through its model gateway.