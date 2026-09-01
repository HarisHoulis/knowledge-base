---
domain: ai-workflows
subdomain: agent-guidance
concept: adr-for-agents
title: Turn your agent on auto-pilot with ADRs
sources:
  - title: "Turn your agent on auto-pilot with ADRs"
    url: "https://www.youtube.com/watch?v=vRoqBBI51Vo"
    author: "Kent C. Dodds"
    date: "2026-08-25"
---

# Turn your agent on auto-pilot with ADRs

The video addresses the pain of repeatedly explaining product decisions to a fresh AI agent. Every new conversation requires the agent to be filled with all prior decisions, making the human the memory. This is inefficient and error-prone. The presented solution is to use Architectural Decision Records (ADRs), a traditional software practice, to capture durable decisions in the repo. ADRs contain context, the decision, consequences, and conditions for revisiting, giving agents a reliable reference. By pointing agents to ADRs—e.g., via an AGENTS.md instruction—you enable progressive disclosure and prevent agents from re-deciding or contradicting past choices. The template includes a number, title, what is being rejected, status, date, context, decision, consequences, and a 'revisit if' clause. Placing these as a 'steering veto list' in agent instructions helps agents check before proposing new primitives or surfaces, making them more autonomous while respecting prior decisions.

- Fresh AI agents lack memory of past product decisions, forcing humans to re-explain every time.
- ADRs capture the context, decision, consequences, and 'revisit if' conditions for architectural choices.
- Store ADRs in the repo and reference them in AGENTS.md as a 'steering veto list' to guide agents.
- ADRs are not immutable; they evolve, but they give agents a solid starting point and prevent accidental re-decisions.
- The ADR template includes what the team is saying 'no to,' which clarifies boundaries.