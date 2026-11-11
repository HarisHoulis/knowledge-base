---
domain: ai-workflows
subdomain: coding-agents
concept: agent-session-trace-capture
title: Every Correction You Give Your Agent Is Data
sources:
  - title: "Every Correction You Give Your Agent Is Data - Brian Douglas, Paper Compute"
    url: "https://www.youtube.com/watch?v=vg3JdjGuJwM"
    author: "AI Engineer"
    date: "2026-11-10"
---

# Every Correction You Give Your Agent Is Data

Brian Douglas argues that when engineers correct or reject an AI coding agent, that interaction is valuable training data that should be captured rather than discarded. He frames this against the loss of "reps" for junior engineers: as well-defined tasks get delegated to agents, the opportunities to level up by doing the work disappear, so the corrections themselves become the record of learning (AI Engineer, 2026).

He describes two tools: Tapes (tapes.dev), an Apache 2.0 open-source session/trace capture service, and Stereo, an execution environment that sandboxes agents to provide reproducible sessions. Together they support a self-healing infrastructure project called Sweeper Agent, which runs parallel agents (about 10 at a time, or up to ~200 Daytona sandboxes) on well-defined jobs like documentation, writing tests, and cleaning up code (AI Engineer, 2026).

The commercial layer is Paper Compute's trace capture and telemetry recording, surfaced in a Paper Console that centralizes session data across a team rather than keeping it local. Sessions can be tagged—for example, a "discard" tag marking a session an engineer rejected—so that every rejection is recorded as data. Douglas notes he still doesn't write Rust himself, despite using it daily at work, underscoring that the agent does the coding while the human's corrections carry the signal (AI Engineer, 2026).

- Corrections and rejections of agent output are valuable data and should be tagged and captured, not thrown away.
- Tapes (open-source trace capture) plus Stereo (sandboxed, reproducible execution environment) enable capturing agent sessions.
- Well-defined tasks like docs, tests, and code cleanup can be scaled to many parallel agents and sandboxes.
- Delegating work to agents removes the "reps" juniors need to level up, making captured corrections the substitute record.
- A centralized console lets teams share and tag session data rather than keeping it local to one engineer.