---
domain: ai-workflows
subdomain: agentic-software-development
concept: software-factory
title: What It Actually Takes to Build a Software Factory
sources:
  - title: "What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory"
    url: "https://www.youtube.com/watch?v=vGCJ7diEtrw"
    author: "AI Engineer"
    date: "2026-09-27T15:00:02+00:00"
---

# What It Actually Takes to Build a Software Factory

Tereza Tížková (factory.com) argues that a "software factory" is a full software development cycle with autonomy — not merely code generation, but collecting signals, reacting to user feedback and logs, prioritizing, orchestrating, executing, validating, quality testing in production, and iterating, constantly improving the process and gaining new knowledge. Her team's control panel covers this entire cycle, and the concept is now being implemented for corporations like EY and Adobe.

She frames the software factory by what it is not: "not just an agent for writing code, and not even a swarm of such agents, even thousands, because generating and writing code is the easiest part compared to the rest." Engineers themselves don't spend most of their time writing code, so the real challenges lie elsewhere. While the idea dates back to ChatGPT's launch and early experiments like AutoGPT and BabyAGI, it was previously impossible due to hallucination, context-length limits, weak logical inference, and the lack of isolated environments where agents could work — problems that technology has only recently caught up with.

Three properties define the approach: be agnostic (independent of LLM choice and of how the organization already works — connecting Slack, GitHub, and existing subscriptions), be autonomous (give agents real trust, permissions, and management, entrusting them with work over long horizons; she notes the prediction of agents working a year or more without human intervention, while her own missions have already run for weeks), and pursue continuous improvement (onboarding new agents like new people, with good codebase structure, documentation, and shared knowledge).

She insists you cannot bolt a software factory onto an existing organization via consultants — you have to rebuild from the ground up, much like building a real team, or the many testing, verifying, and iterating agents "can all turn into a big mess." On model agnosticism, she cites a Coinbase CEO chart showing token spending continuing to grow while AI costs stopped rising, achieved through tricks like not forcing advanced default models on everyone and caching so prompts don't have to be filled in again every time.

- A software factory is an autonomous full SDLC loop — signals, prioritization, orchestration, validation, production testing, and iteration — not just code-generating agents or a swarm of them.
- Code generation is the easiest part; the real challenges lie in the surrounding cycle, which is why agents must be given genuine autonomy, permissions, and long time horizons.
- Three pillars: agnosticism (LLM- and workflow-independent, fitting into Slack, GitHub, and existing subscriptions), autonomy, and continuous improvement through docs, structure, and shared knowledge.
- It cannot be added mid-organization by consultants; the organization must be rebuilt from the ground up, like building a real team.
- Model agnosticism also controls cost, as illustrated by Coinbase's token-spend chart (cheaper default models, caching) rather than cutting token usage.