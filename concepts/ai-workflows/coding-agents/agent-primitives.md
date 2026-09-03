---
domain: ai-workflows
subdomain: coding-agents
concept: agent-primitives
title: Your Coding Agent Needs Better Primitives
sources:
  - title: "Your Coding Agent Needs Better Primitives"
    url: "https://www.youtube.com/watch?v=kbmv3HIuKyk"
    author: "Kent C. Dodds"
    date: "2026-07-15T14:51:04+00:00"
---

# Your Coding Agent Needs Better Primitives

Kent C. Dodds argues that poor AI agent output is usually a symptom of poor system design, not an incapable agent. The more an agent has to guess or invent its own primitives, the lower the quality and safety of the final result. Primitives are the smallest meaningful units of a system; they let agents compose behavior without re-implementing core mechanics (Dodds, 2026).

- Great agent outcomes depend on well-built system primitives, not just the agent's model or prompting.
- Primitives span UI components/tokens, API resources/verbs, data entities/relationships, infrastructure, executable tools, workflows, and authentication/authorization.
- Without solid primitives, agents improvise, leading to inconsistent UI, duplicated logic, guessed data relationships, dangerous infrastructure changes, and insecure permissions.
- Primitives should be explicitly designed up front; agents can help build them, but humans must be intentional about avoiding overlap.
- Product engineers' scarce work is now systems design: creating a safe, efficient environment for agents to operate in.