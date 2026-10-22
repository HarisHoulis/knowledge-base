---
domain: ai-workflows
subdomain: agent-architecture
concept: actor-model-for-agents
title: Actors for Agents: Patterns for Production AI
sources:
  - title: "Presentation: Actors for Agents: Patterns for Production AI"
    url: "https://www.infoq.com/presentations/actors-for-production-ai-agents/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Manju Rajashekhar"
    date: "2026-10-22"
---

# Actors for Agents: Patterns for Production AI

Manju Rajashekhar argues that production AI agents should be treated as distributed systems, and that the actor model provides the runtime primitives needed to make them resilient beyond fragile demos. Rather than ad-hoc orchestration, agents gain explicit state ownership and message passing as first-class design elements.

The talk covers write-through state, so that agent state is persisted as it changes, and supervision boundaries, which isolate and manage failures across the agent system. These patterns address continuations and mutable execution graphs—the dynamic, branching control flow that agentic workflows exhibit in practice.

Together these ideas frame agentic workflows as an architecture problem: failures, resumptions, and changing execution paths are handled through actor-style isolation and supervision rather than brittle glue code.

- Treat production AI agents as distributed systems rather than demos
- Use the actor model for state ownership and message passing
- Apply write-through state to persist agent state as it changes
- Use supervision boundaries to manage failures and continuations
- Support mutable execution graphs in agentic workflows