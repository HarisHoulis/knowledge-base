---
domain: ai-workflows
subdomain: llm-agents
concept: agent-convergence-failure
title: Steve Yegge on Gas Town and Opus 4.7 Tic
sources:
  - title: "Quoting Steve Yegge"
    url: "https://simonwillison.net/2026/Aug/4/steve-yegge/#atom-everything"
    author: "Simon Willison"
    date: "2026-08-04"
  - title: "The Shape of Things to Come"
    url: "https://yegge.ai/essays/the-shape-of-things-to-come/"
    author: "Steve Yegge"
    date: "2026"
---

# Steve Yegge on Gas Town and Opus 4.7 Tic

Steve Yegge's essay 'The Shape of Things to Come' describes the failure of his coding agent Gas Town when upgrading to Opus 4.7. Gas Town had been reusable up to 4.6, but the new model introduced a persistent 'just two more things' tic that prevented the agent from ever converging on a final state. Instead of completing work, the agent continually proposed additional modifications to Gas Town itself, effectively burning down the project. This anecdote highlights a common failure mode in LLM-based agents: the inability to stop refining and reach a stable, deployable state. Simon Willison quotes this passage on his blog, noting the implications for coding agents and LLM behavior in real-world workflows.

- Gas Town was a reusable coding agent, but only used to build itself.
- Opus 4.7 introduced a 'just two more things' tic that prevented convergence.
- The tic caused the agent to endlessly fiddle with Gas Town itself, not do real work.
- The issue persisted, leading to Gas Town's effective abandonment.
- This illustrates a critical challenge in LLM agent reliability: ensuring task completion without runaway refinement.