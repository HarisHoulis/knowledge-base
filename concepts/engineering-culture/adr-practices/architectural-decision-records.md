---
domain: engineering-culture
subdomain: adr-practices
concept: architectural-decision-records
title: Turn your agent on auto-pilot with ADRs
sources:
  - title: "Turn your agent on auto-pilot with ADRs"
    url: "https://www.youtube.com/watch?v=vRoqBBI51Vo"
    author: "Kent C. Dodds"
    date: "2026-08-25T13:41:47+00:00"
---

# Turn your agent on auto-pilot with ADRs

In this video, Kent C. Dodds addresses the common pain point of repeating product decisions to AI agents every time a new conversation begins. The decisions made over months of development are often trapped in old chat logs, forcing the developer to act as the memory. He argues that relying on comments or searching past chats is not a durable pattern.

His solution is to use Architectural Decision Records (ADRs), a traditional software practice. ADRs are stored in the repo and referenced in the agent's instructions (e.g., AGENTS.md). They provide a structured way to capture context, the decision itself, and its consequences, so agents can consult them before making changes.

Dodds provides a template for ADRs, including a number, short title, what the team is saying no to, status, date, context, decision, consequences, and a 'revisit if' condition. He emphasizes that ADRs are not set in stone but evolve over time. By pointing agents to these records, developers can steer agents away from re-deciding past questions or heading in undesired directions (Kent C. Dodds, 2026).

- Store durable product decisions as Architectural Decision Records (ADRs) in the repo.
- Reference ADRs in the agent's instructions (like AGENTS.md) so agents read them before acting.
- Include context, decision, consequences, and a 'revisit if' condition to enable progressive evolution.
- ADRs help prevent agents from re-deciding old questions or proceeding in unwanted directions.