---
domain: ai-workflows
subdomain: AI agent observability and evaluation
concept: agent-observability
title: From Vibes to Production: Evaluating and Shipping AI Agents That Work
sources:
  - title: "From Vibes to Production: Evaluating and Shipping AI Agents That Work 201 — Laurie Voss, Arize AI"
    url: "https://www.youtube.com/watch?v=F0TNSmbo5hE"
    author: "AI Engineer"
    date: "2026-10-05"
---

# From Vibes to Production: Evaluating and Shipping AI Agents That Work

Laurie Voss of Arize AI presents session 201 on closing the software development lifecycle loop for AI agents, building on the manual, small-scale monitoring covered in 101 (AI Engineer, 2026). The talk focuses on automating trace analysis and fix preparation so agent improvement can scale.

The central problem is that agents are non-deterministic: the same input may produce different results or follow different paths. As a result, code is no longer the sole source of truth; traces at scale become the source of truth for understanding average agent behavior (AI Engineer, 2026).

Traces are described as log files for AI applications. They capture every LLM call, tool call, and agent step, can be nested, and include input/output plus metadata such as cost and execution time. This tracing gives visibility into unnecessary steps, expensive actions, and unexpected latency (AI Engineer, 2026).

The talk previews using agent skills from a workshop repository to analyze traces, prepare fixes, and move toward signal—continuous automatic improvement at agent scale. It also notes that human review can become a bottleneck, motivating automation (AI Engineer, 2026).

- Agents are non-deterministic; traces, especially at scale, replace code as the source of truth for understanding behavior.
- Tracing captures every LLM call, tool call, and agent step with input/output and metadata like cost and execution time.
- Observability surfaces inefficiencies such as unnecessary actions, excessive steps, high cost, and long runtimes.
- Manual trace review creates a human bottleneck; session 201 uses agent skills to analyze traces and prepare fixes.
- The goal is continuous automatic improvement at agent scale, closing the software development lifecycle loop.