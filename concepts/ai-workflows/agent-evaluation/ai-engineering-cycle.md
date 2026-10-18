---
domain: ai-workflows
subdomain: agent-evaluation
concept: ai-engineering-cycle
title: Evals for High-Stakes AI Agents
sources:
  - title: "Evals for High-Stakes AI Agents — Doneyli De Jesus & Annabell Schäfer, Langfuse"
    url: "https://www.youtube.com/watch?v=obfPzbapMIM"
    author: "AI Engineer"
    date: "2026-10-18"
---

# Evals for High-Stakes AI Agents

Annabell Schäfer and Doneyli De Jesus of Langfuse argue that traditional monitoring is insufficient for non-deterministic AI agents. They illustrate this with a support agent that tells a user a refund was issued when the tool was never actually called: system metrics stay green and latency looks fine, so the failure only surfaces weeks later when the user complains. Because agents can claim to perform actions they did not perform, teams need continuous signals of where things go wrong rather than relying on uptime and latency dashboards.

Langfuse grew out of this gap—its founders, coming from Y Combinator, saw no equivalent of unit testing for AI applications and built an open-source platform for tracking, monitoring, and improving AI systems. The audience has since broadened from developers to industry experts collaborating with AI engineers, and more recently to coding agents that help engineers improve AI applications. The platform reports over 150,000 developers, 21 Fortune 50 companies, and more than 90 billion observations per month, with customers including Ramp, Canva, Khan Academy, and SumUp.

From working with these companies, the speakers distill an "AI engineering cycle" followed by teams that ship reliable agents. It starts with tracing—recording every step of the agent's work as a log that humans can inspect—then monitoring to identify the most interesting moments (what is failing, what is working, how the system behaves on average). Teams then build datasets of representative examples of what the system should handle and how, run experiments across variations of the system, and evaluate the results. Crucially, this is framed as a continuous loop rather than a one-time action.

- Traditional monitoring can show green status while an agent silently fails to execute a tool call and misleads the user.
- Tracing—human-inspectable logs of every agent step—is the foundation of the AI engineering cycle.
- The cycle proceeds from tracing to monitoring, dataset creation, experimentation, and evaluation, and repeats continuously.
- Langfuse positions itself as filling the missing 'unit testing' layer for non-deterministic AI applications.