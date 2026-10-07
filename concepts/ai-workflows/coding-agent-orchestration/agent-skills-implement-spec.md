---
domain: ai-workflows
subdomain: coding-agent-orchestration
concept: agent-skills-implement-spec
title: Skills repo v1.3: /pr, /implement-spec, and /retro
sources:
  - title: "New Skills! v1.3 brings /pr, /implement-spec, and /retro"
    url: "https://www.youtube.com/watch?v=BsJGo1wFTvQ"
    author: "Matt Pocock"
    date: "2026-10-05"
---

# Skills repo v1.3: /pr, /implement-spec, and /retro

Matt Pocock's v1.3 release of his skills repo adds three skills — /pr, /implement-spec, and /retro — which he describes as central to his workflow. The transcript focuses on /implement-spec, which lands large chunks of work by splitting a spec (the destination) from the tickets that implement it (the sessions). Each ticket is intended to be run in a single coding agent; trying to implement an entire spec in one agent risks entering the "dumb zone" or hitting auto-compact, so breaking work into individual tickets is described as cleaner (Pocock, 2026).

The skill addresses how to orchestrate tickets, which Pocock says has long confused users. He contrasts three approaches: the manual loop, where the user iterates through each ticket by hand ("acting like a for loop," not really workable); the deterministic loop, where a script reads each ticket and implements it itself (reliable and cheap, but complicated to set up and out of range for beginners); and the sub-agent loop, where an agent does the babysitting instead of a human. /implement-spec uses the sub-agent approach, made possible because sub-agents can now spawn sub-agents and are as capable as orchestrator agents (Pocock, 2026).

The skill has nine steps: it reads the spec and tickets, does exploration in its own sub-agent, creates an integration branch, then uses implement sub-agents to build each ticket using TDD and work trees. It merges completed work to the integration branch via a sub-agent, pings off more implement sub-agents until all work is done, calls code review on the integration branch, cleans up, and makes the PR ready for review — yielding a single PR from a large spec (Pocock, 2026). Pocock notes it parallelizes where possible: tickets are a task graph with blocking relationships rather than a list of steps, so there is always a frontier of ready tickets.

He rates the sub-agent approach as worse than a deterministic loop because that loop is deterministic and runs the same way every time, but calls /implement-spec a good way to get started with AFK (away-from-keyboard) workflows. He says he reaches for it more than expected, especially on systems without deterministic scripts or a dialed-in "software factory" (Pocock, 2026).

- v1.3 of the skills repo ships three skills: /pr, /implement-spec, and /retro.
- /implement-spec splits work into a spec (destination) and tickets (individual agent sessions) to avoid exceeding a single agent's context.
- It orchestrates tickets using sub-agents, which can now spawn their own sub-agents, as a middle ground between the manual loop and the deterministic script loop.
- Its nine-step flow reads spec and tickets, explores in a sub-agent, uses an integration branch, implements tickets via TDD and work trees, runs code review, and produces one PR.
- Tickets form a task graph with blocking relationships, giving a frontier of ready-to-parallelize work.