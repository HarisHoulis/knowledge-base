---
domain: ai-workflows
subdomain: agent-architecture
concept: agent-guardrails
title: Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan
sources:
  - title: "Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan"
    url: "https://www.youtube.com/watch?v=32nrHU6zHU8"
    author: "AI Engineer"
    date: "2026-08-29T16:30:28+00:00"
---

# Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan

Roberto Milev and Uday Kanagala argue that AI agents today are in the same position microservices were in 2015: most teams should not build multi-agent systems, and a well-structured monolith—or in this case, a single agentic loop—is usually the right starting point. Navan runs one master agent that progressively loads skills, where a skill is the unit of context and is independently pluggable and testable (Milev & Kanagala, 2026). The analogy warns against prematurely adopting complex distributed agent architectures before the foundational patterns have stabilized.

The conversation highlights how agents blur traditional authorization boundaries. When an agent is asked to book a flight whenever the fare drops below $200 and it fires two weeks later, it is unclear whether the purchase was made by the user or the agent's service account. To address this, Navan implements guardrails that run before and after every tool call rather than at the edge, capturing the goal, reasoning, and a confidence score for each action. This allows ambiguous or high-risk actions to be routed to a human for approval (Milev & Kanagala, 2026).

Because agents emit large amounts of thinking, traditional logs stop being useful. Navan uses hooks that intercept tool calls and emit structured traces, enabling debugging and observability. Testing such nondeterministic systems requires scoring trajectories of agent behavior rather than asserting exact outputs. The speakers also note that cost remains genuinely unsolved, and replay tools and emerging standards are still open problems (Milev & Kanagala, 2026).

- Agents are at a stage similar to microservices in 2015; prefer a single agent loop over premature multi-agent systems.
- Authorization blurs when agents act on behalf of users; guardrails should run before and after every tool call.
- Logs are inadequate for agent debugging; hooks and traces that capture goal, reasoning, and confidence scores are necessary.
- Nondeterministic agents should be evaluated by scoring trajectories rather than asserting fixed outputs.
- Cost, replay, and standards for agent architectures remain unsolved.