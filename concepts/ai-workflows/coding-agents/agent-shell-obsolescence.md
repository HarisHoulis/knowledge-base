---
domain: ai-workflows
subdomain: coding-agents
concept: agent-shell-obsolescence
title: Smarter Models Killed the Harness: What's Left of the Agent Shell
sources:
  - title: "Smarter Models Killed the Harness. Here's What's Left — Jediah Katz, SpaceX"
    url: "https://www.youtube.com/watch?v=7Y4sbZgBdnc"
    author: "AI Engineer"
    date: "2026-10-19"
---

# Smarter Models Killed the Harness: What's Left of the Agent Shell

Jediah Katz, an engineer on Cursor's agent shell who moved to SpaceX via the Cursor acquisition, traces the evolution of the "agent shell" (also called harness) from prompt engineering in early 2023 to context engineering by mid-2025, and finally to shell engineering as the industry term. He defines the shell as the model's "eyes and hands"—connecting users, the model, computers, and third-party services like MCP—and splits it into two levels: an execution level (where the agent loop runs and state is stored, built much like traditional software) and a context/orchestration level (which models are called, when, and what context they see, including prompts, tools, and memory compression), the latter being the "Wild West" where he works most.

- The agent shell/harness evolved from prompt engineering (2023) to context engineering (mid-2025) to shell engineering, split into execution and context/orchestration levels.
- Berkeley testing of seven leading models found harness choice had no significant impact on SWE-bench Lite scores, and Apple/EPFL found custom harnesses made little difference on MLE-bench.
- Fancy harnesses no longer add intelligence: models have learned to explore codebases, work persistently, and verify their own work, making patching tricks like small edit models obsolete.
- The harness makes itself obsolete through a data flywheel, as models absorb the skills harnesses once supplied.