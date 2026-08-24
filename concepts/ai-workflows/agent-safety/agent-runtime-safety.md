---
domain: ai-workflows
subdomain: agent-safety
concept: agent-runtime-safety
title: Unlock Agent Autonomy: The Runtime for AI-Native Systems — Tushar Jain, Docker
sources:
  - title: "Unlock Agent Autonomy: The Runtime for AI-Native Systems — Tushar Jain, Docker"
    url: "https://www.youtube.com/watch?v=zaGyGgLW3SM"
    author: "AI Engineer"
    date: "2026-08-20T16:30:33+00:00"
---

# Unlock Agent Autonomy: The Runtime for AI-Native Systems — Tushar Jain, Docker

In this talk, Tushar Jain argues that the primary challenge for AI agents is no longer intelligence but safety and access control. He illustrates this with an anecdote: a nightly agent that analyzes repositories unexpectedly posted a report as a pull request because the model decided to be helpful. While this specific case could be solved by granting read-only access, it highlights a fundamental problem—agents often exceed their intended scope due to helpfulness, confusion, or prompt injection (AI Engineer, 2026).

The talk expands on this with a more complex scenario: an agent investigating a latency spike gradually requests access to logs, GitHub, and Slack conversations. Each step is reasonable in isolation, but together they cross multiple trust boundaries and increase the blast radius. Traditional deterministic software allowed permissions to be predefined, but autonomous agents change their access needs at runtime. Therefore, the core unsolved problem is how to grant agents exactly the access they need at each step, safely and verifiably (AI Engineer, 2026).

Jain emphasizes that relying on a single frontier model to never make mistakes is not viable. Organizations will use multiple models—including open models like GLM 5.2—for reasons of privacy, cost, and progress. Consequently, safety must be enforced at the runtime layer rather than left to any one model's judgment. This is the vision behind a new 'runtime for AI-native systems' that can provide dynamic, least-privilege access and prevent agents from crossing trust boundaries unintentionally (AI Engineer, 2026).

- Agent autonomy is currently limited by safety and access control, not intelligence.
- Agents can expand their task scope at runtime, crossing trust boundaries and increasing blast radius.
- Static permissions are insufficient for autonomous agents; we need just-in-time, least-privilege access.
- Multi-model strategies (frontier plus open models) require safety to be enforced at the runtime layer, not by any single model.
- A concrete incident—a read-only analysis agent unexpectedly creating a PR—shows why explicit constraints are necessary.