---
domain: ai-workflows
subdomain: agent-architecture
concept: agentic-guardrails
title: Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan
sources:
  - title: "Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan"
    url: "https://www.youtube.com/watch?v=32nrHU6zHU8"
    author: "AI Engineer"
    date: "2026-08-29T16:30:28+00:00"
---

# Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan

Roberto Milev and Uday Kanagala, speaking at AI Engineer, frame the current state of AI agents as analogous to microservices in 2015: a promising but often over-applied pattern. They caution that teams should not reach for multi-agent systems if a well-structured single agent can suffice. Navan therefore runs one master agent that dynamically loads skills, treating each skill as a self-contained unit of context that can be developed and tested independently (source: YouTube).

The talk emphasizes that agents are stateful by nature, which breaks traditional logging and authorization models. Because an agent may act on behalf of a user or a service account, the question of who authorized a purchase becomes ambiguous. Navan addresses this by placing guardrails before and after every tool call, and by using hooks to capture the agent's goal, reasoning, and a confidence score for each step. This allows uncertain actions to be routed to a human for approval (source: YouTube).

Testing nondeterministic agent systems requires a shift from asserting specific outputs to scoring entire trajectories. Logs are insufficient because agents generate too much intermediate reasoning. Finally, the speakers note that cost remains genuinely unsolved, though replay and emerging standards may help address it (source: YouTube).

- Agents are where microservices were in 2015; prefer a single agent or well-structured monolith before adopting multi-agent architectures.
- Use one master agent with pluggable skills as the unit of context, enabling independent testing and evolution.
- Guardrails must run before and after every tool call, not just at the edge, to handle authorization and statefulness.
- Logs break for agents; use hooks, traces, and confidence scores to route uncertain outputs to humans.
- Test nondeterministic systems by scoring trajectories rather than asserting exact outputs, and expect cost to remain unsolved.