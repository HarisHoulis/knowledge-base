---
domain: ai-workflows
subdomain: coding-agents
concept: pre-commit-agent-guardrails
title: Using Pre-Commit Hooks to Steer Coding Agents
sources:
  - title: "Quoting Geoffrey Huntley"
    url: "https://simonwillison.net/2026/Oct/13/geoffrey-huntley/"
    author: "Simon Willison"
    date: "2026-10-13"
  - title: "nobody should type code by hand anymore. here's what's left."
    url: "https://ghuntley.com/agency/"
    author: "Geoffrey Huntley"
---

# Using Pre-Commit Hooks to Steer Coding Agents

Geoffrey Huntley describes a technique for enforcing coding-agent behavior through deterministic tooling rather than documentation. Rather than relying on an agent to read and follow AGENTS.md, he notes that documentation-based guidance drifts: "If the agent isn't using my diagnostics library, I could introspect and update AGENTS.md, but there's still a delta, and it'll drift."

His alternative is to encode the constraint as a pre-commit hook that inspects the git diff for direct calls to observability modules that bypass his diagnostics module. When a violation is detected, the hook fails the commit and injects a prompt instructing the agent to use the diagnostics library instead.

Huntley reports this approach works dramatically better than passive documentation, describing the result as "ten out of ten." The broader implication is that agent compliance is better achieved through automated, enforced feedback loops in the toolchain than through instructions the agent may ignore or gradually diverge from.

- Documentation like AGENTS.md drifts and leaves a delta between intended and actual agent behavior.
- A pre-commit hook can scan the git diff for direct calls to observability modules that bypass the diagnostics module.
- On violation, the hook fails the commit and injects a prompt telling the agent to use the diagnostics library.
- Huntley reports the enforced feedback loop yields a "ten out of ten" result.