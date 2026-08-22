---
domain: ai-workflows
subdomain: agent-safety-operations
concept: agent-budget-not-token
title: Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic
sources:
  - title: "Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic"
    url: "https://www.youtube.com/watch?v=rbjWzZK2LU0"
    author: "Sachin Malhotra"
    date: "2026-08-22T14:00:06+00:00"
---

# Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic

Sachin Malhotra opens with a real incident: an agent tasked with cleaning up after itself accidentally deleted 200 workloads in 90 seconds, impacting 20 engineers. A filter in the pipeline evaluated to nothing, causing the selector to match everything. The agent genuinely believed it was tidying up, and nobody was malicious. Malhotra argues that the common pattern of "here's a token and here's a tool list" insufficiently scales to production work because it grants the agent unbounded power to perform irreversible actions without close oversight (Sachin Malhotra, "Give the Agent a Budget, Not a Token," 2026).

- The root cause of agent failures is not the model itself but unbounded power given to the agent for actions we aren't supervising closely.
- Narrowing token scope by removing destructive verbs is a temporary fix that ultimately fails; it's like refusing to let a new hire use any potentially dangerous tool.
- Three primitives help govern agent actions: asymmetric verbs (distinguishing easy-to-undo from hard-to-undo operations), rate limits (preventing blast radius from rapid repeated actions), and trip wires over allow lists (safety triggers rather than pre-approved-only lists).
- The 'undo test' asks whether an action can be undone; if not, it needs extra guardrails, similar to making catastrophic actions structurally out of reach for human juniors.