---
domain: ai-workflows
subdomain: agent-guidance
concept: architectural-decision-records
title: Turn your agent on auto-pilot with ADRs
sources:
  - title: "Turn your agent on auto-pilot with ADRs"
    url: "https://www.youtube.com/watch?v=vRoqBBI51Vo"
    author: "Kent C. Dodds"
    date: "2026-08-25T13:41:47+00:00"
---

# Turn your agent on auto-pilot with ADRs

In this video, Kent C. Dodds (2026) addresses a common pain point in AI-assisted development: every time you start a new conversation with an agent, you must re-explain all the product decisions made over months of work. The agent has no memory of past chats, so the human becomes the memory, which is inefficient and error-prone. Dodds proposes a traditional software solution: Architectural Decision Records (ADRs) stored in the repository and referenced by the agent.

An ADR captures the context behind a decision, the decision itself, its consequences, and conditions that would prompt revisiting it. Dodds (2026) shares a template that includes a number, a short decision title, what the decision is saying no to, status, date, context, decision, consequences, and a 'revisit if' clause. These records are not set in stone; they can evolve over time but provide a durable starting point for future work.

To integrate with AI agents, Dodds recommends adding a reference to decision records in the agent's instructions (e.g., agent.md). This acts as a steering/veto list: the agent must open and review relevant ADRs before proposing new primitives or surfaces. This prevents the agent from re-deciding established choices or plowing forward in unwanted directions, making the agent more autonomous and aligned with past decisions.

- Fresh agent chats lose product context, forcing humans to act as memory.
- ADRs are durable decision documents stored in the repo.
- ADR template includes context, decision, consequences, and 'revisit if' conditions.
- Point agents to ADRs via agent.md as a steering/veto list.
- This enables agents to work autonomously without re-litigating past decisions.