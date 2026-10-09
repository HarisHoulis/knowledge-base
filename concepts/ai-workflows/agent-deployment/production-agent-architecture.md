---
domain: ai-workflows
subdomain: agent-deployment
concept: production-agent-architecture
title: Brains vs Hands: How to Run AI Agents Safely in Production
sources:
  - title: "Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya"
    url: "https://www.youtube.com/watch?v=NaOkR3VSfR4"
    author: "AI Engineer"
    date: "2026-10-08"
---

# Brains vs Hands: How to Run AI Agents Safely in Production

Viren Baraiya argues that agents in production are not just chatbots but include background workers, scheduled agents, event-driven agents, long-term coordinators, and multi-agent systems. He notes that at a recent conference most attendees were already launching agents in production, signaling rapid adoption. The core analogy is to microservices: an agent should be treated as an application, not a single component, following a single-responsibility principle where a shell coordinates multiple specialized agents to achieve a business goal.

The shell acts as the application wrapper that controls agent execution and combines deterministic and non-deterministic parts. The LLM provides non-determinism through reasoning and planning, but determinism must be enforced where it matters—such as payments or restarting a Kubernetes cluster—so that the sequence of steps is predictable every time. The shell connects to databases, internal systems, corporate systems, humans in the control loop, and tools via API or MCP.

Baraiya emphasizes that one agent should not be responsible for many things, as that risks hallucinations. Instead, multiple agents communicate through choreography or orchestration, each with a clear responsibility, and the shell provides the deterministic workflow that governs their execution.

- Agents in production span background workers, scheduled agents, event-driven agents, long-term coordinators, and multi-agent systems—not just chatbots.
- Treat an agent as an application, analogous to microservices: use a shell that coordinates specialized agents under a single-responsibility principle.
- Separate deterministic and non-deterministic parts: LLM reasoning is non-deterministic, but critical workflows like payments or cluster restarts must remain deterministic.
- Avoid overloading a single agent with many responsibilities to reduce hallucinations; use multi-agent communication via choreography or orchestration.