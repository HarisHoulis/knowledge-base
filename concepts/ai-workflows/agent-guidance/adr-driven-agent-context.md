---
domain: ai-workflows
subdomain: agent-guidance
concept: adr-driven-agent-context
title: Turn your agent on auto-pilot with ADRs
sources:
  - title: "Turn your agent on auto-pilot with ADRs"
    url: "https://www.youtube.com/watch?v=vRoqBBI51Vo"
    author: "Kent C. Dodds"
    date: "2026-08-25T13:41:47+00:00"
---

# Turn your agent on auto-pilot with ADRs

To implement this, developers place ADRs in the repository and point agents to them via an agent.md file, describing them as a 'steering veto list' that agents must open before proposing new primitives or surfaces. This prevents agents from re-deciding past choices or proceeding in unwanted directions. The approach is a traditional software engineering practice adapted for AI workflows, enabling agents to act more autonomously while staying aligned with previously made decisions (Kent C. Dodds, 2026).

- Fresh agent conversations lack memory of past decisions, forcing developers to become the memory.
- ADRs (Architectural Decision Records) provide a durable, repo-based record of decisions.
- An ADR includes context, decision, consequences, and a 'revisit if' condition.
- Agent instructions (agent.md) can reference ADRs as a steering/veto list to guide agent behavior.
- ADRs are not immutable; they can be updated as circumstances change.