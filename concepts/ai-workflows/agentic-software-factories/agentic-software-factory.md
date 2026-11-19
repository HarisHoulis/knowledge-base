---
domain: ai-workflows
subdomain: agentic-software-factories
concept: agentic-software-factory
title: Software Factories and Code Reviews with Harjot Gill
sources:
  - title: "Software factories and code reviews with Harjot Gill"
    url: "https://newsletter.pragmaticengineer.com/p/software-factories-and-code-reviews"
    author: "Gergely Orosz"
    date: "2026-11-18"
---

# Software Factories and Code Reviews with Harjot Gill

Harjot Gill, founder and CEO of CodeRabbit, describes running an "AI-pilled" software factory where agents generate the bulk of engineering output: he shipped over 5,000 pull requests in a month at a monthly AI run rate of roughly $250,000, with a team of about 40 engineers (Gergely Orosz, The Pragmatic Engineer). Much of this work is "janitorial" — improving CI, fixing flaky tests, refining caching — with agents steered during commutes and evenings; examples include a Rust write-ahead log on object stores (the agent ran for six weeks, now in production), migrating services to Bun over a weekend, and building a new CI system after a $13M/year quote pushed them to build their own with agents in a week at 50% less cost.

Gill argues agents must be able to "hill climb" by verifying their own work, using layers including formal models like TLA+ and Lean (TLA+ surfaced race conditions code review missed), local deterministic simulations that fuzz concurrent interleavings, emulated real APIs, dev environments, and staged production rollouts with feature flags that agents observe before widening. He believes human code review of agent-generated code is dead; instead engineers review releases (multiple PRs) and spend more time on planning and final assets. Quality is backed by a "review exempt list" of trusted devs who can push without review, paired with a strike system that revokes that trust when a dev causes outages.

CodeRabbit stopped investing in fine-tuning models because frontier models move too fast to maintain their own. Teams use "war rooms" where engineers, product, and designers gather to steer agents from prototype to working product. Gill's hiring criteria emphasize agency, breadth, and systems thinking, and his unconventional job ad invited candidates who had shipped 1,000+ non-slop PRs in 30 days or played 500+ hours of strategy games like Civilization or Factorio, reflecting parallels between running dozens of agents and playing strategy games. Orosz notes the approach is an outlier — most companies spend $200-$2,000 per dev per month on AI — and that massive spend can be justified for dev-tool startups as a form of R&D that speeds time-to-market, though the "Dracula effect" of agent-driven drain and disturbed sleep is real.

- Agents generate most output at CodeRabbit: 5,000+ PRs/month at ~$250K monthly AI spend with ~40 engineers, much of it janitorial CI/test/caching work.
- Agents need verification loops to "hill climb": formal methods (TLA+, Lean), deterministic simulations, emulated APIs, dev environments, and staged rollouts.
- Human review shifts from individual PRs to releases and planning; a review-exempt list with a strike system ties production trust to accountability.
- Fine-tuning models is no longer worthwhile as frontier models advance too fast; war rooms let cross-functional teams steer agents together.
- Hiring favors agency, breadth, and systems thinking, with strategy-game experience seen as analogous to orchestrating many parallel agents.