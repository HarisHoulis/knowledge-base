---
domain: ai-workflows
subdomain: agentic-engineering-practices
concept: skills-as-judgment
title: Scale the Judgment, Not the Model
sources:
  - title: "Scale the Judgment, Not the Model — Andrew Orobator, Reddit"
    url: "https://www.youtube.com/watch?v=6MudaeKdBSk"
    author: "Andrew Orobator"
    date: "2026-09-27"
---

# Scale the Judgment, Not the Model

Andrew Orobator, an Android engineer at Reddit, argues that the model was never the real bottleneck — the judgment around it is (Orobator, AI Engineer). Swapping in a smarter model yields only a slightly better answer, but removing tests, inspections, and reviews makes the whole thing fall apart. "A model is raw talent, and judgment is organization." Meanwhile teams still burn human creativity and attention on manual maintenance, such as a recurring "war meeting" whose only purpose is deleting outdated experiments.

The judgment already exists — it lives in scars, postmortems, and the most experienced reviewers — but it doesn't scale because it's locked in one person's head. The concrete example: ask a senior engineer to clear a feature flag and they first run a chain of questions — is the deployment frozen, what about the flag next to it, which team owns it. That set of questions *is* the judgment, the most valuable thing in the building, yet it surfaces once during code verification and then disappears, so the next person learns only from their own mistakes.

Orobator frames a skill as institutional judgment made enforceable — a recorded set of judgments the agent plays back rather than guesses, letting a junior engineer work with ten-year-old instincts at hand. He borrows Minsky's 1986 notion of the K-line (knowledge line): the configuration of mind that solved a problem and was reused for the next one; a skill is a K-line for a codebase. Skills are not documentation: agents are drowning in facts, and what they lack is knowing which facts are important and which decisions are dangerous — documentation preserves facts, skills preserve judgments.

Because refactoring or feature work outlives a single session and the context window clears every time, the other half is recording the work itself: the plan, the solution, what was already tried, and the surprises along the way. In a work journal, a new session with a fresh agent and zero memory takes one word — "continue" — and the agent reads the log and picks up at stage seven of nine. Orobator says this very talk was written that way, with a new agent resuming from the work log rather than needing re-explanation.

- The model is not the bottleneck; judgment around the model is. A smarter model gives a slightly better answer, but removing tests, inspections, and reviews makes everything fall apart.
- Institutional judgment lives in scars, postmortems, and senior reviewers, but is trapped in individual heads — encoding it lets one reviewer's taste direct thousands of changes they never touch.
- A skill is institutional judgment made enforceable — a K-line (Minsky, 1986) for a codebase — and differs from documentation: docs preserve facts, skills preserve which facts matter and which decisions are dangerous.
- Because context windows clear between sessions, a work journal recording the plan, solution, attempted approaches, and surprises lets a fresh agent resume with a single "continue".