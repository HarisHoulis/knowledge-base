---
domain: ai-workflows
subdomain: agent-context
concept: architectural-decision-records
title: Turn your agent on auto-pilot with ADRs
sources:
  - title: "Turn your agent on auto-pilot with ADRs"
    url: "https://www.youtube.com/watch?v=vRoqBBI51Vo"
    author: "Kent C. Dodds"
    date: "2026-08-25T13:41:47+00:00"
---

# Turn your agent on auto-pilot with ADRs

Starting a fresh agent conversation is painful because you have to re-explain all the product and architectural decisions made over months of work. This problem makes the human the memory, forcing them to remind the agent of every prior decision. Kent C. Dodds proposes using Architectural Decision Records (ADRs) as a traditional software solution to solve this modern AI workflow problem (Dodds, 2026).

An ADR is a document stored in the repository that records the context, the decision, the consequences, and the conditions that would trigger revisiting the decision. It includes a number, a short decision title, what is being said no to, status, and date. By pointing the agent to these records via the agent's MD file, the agent can consult a 'steering veto list' before proposing new primitives or surfaces, preventing it from re-deciding old issues or charging in an undesirable direction. This approach gives the agent a durable starting place and helps it make better product decisions autonomously (Dodds, 2026).

-  ADRs prevent agents from re-deciding past product decisions in every fresh conversation.
-  An ADR should contain context, decision, consequences, and a 'revisit if' condition.
-  Point the agent to ADRs via the agent's MD file as a steering veto list.
-  This pattern treats the human as the guide rather than the memory, enabling agent autonomy.