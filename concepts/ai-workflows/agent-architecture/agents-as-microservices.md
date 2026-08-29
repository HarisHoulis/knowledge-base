---
domain: ai-workflows
subdomain: agent-architecture
concept: agents-as-microservices
title: Agents Are Where Microservices Were in 2015
sources:
  - title: "Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan"
    url: "https://www.youtube.com/watch?v=32nrHU6zHU8"
    author: "AI Engineer"
    date: "2026-08-29T16:30:28+00:00"
---

# Agents Are Where Microservices Were in 2015

Roberto Milev and Uday Kanagala from Navan argue that AI agents are currently in the same position microservices were in 2015: the default advice is to avoid them unless necessary. They caution that building a single well-structured agentic loop is often preferable to orchestrating many agents, just as a monolith was preferable to premature microservices. This analogy frames their reference architecture, which centers on a master agent that progressively loads skills—where a skill is treated as the unit of context, pluggable and testable independently.

- Agents are stateful by nature, making runtime and memory first-class concerns.
- Skills serve as the unit of context, enabling modular and testable agent capabilities.
- Traditional logs fail for agents; hooks with goal, reasoning, and confidence scores are needed for observation.
- Testing nondeterministic systems requires scoring entire trajectories, not asserting exact outputs.
- Authorization blurs when an agent acts on a user's behalf, raising unresolved questions about who made a purchase.
- Cost and replay remain unsolved problems in agent operations.