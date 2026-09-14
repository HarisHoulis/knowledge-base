---
domain: ai-workflows
subdomain: agent-security
concept: securing-bash-executing-agents
title: We let an AI agent execute Bash and lived to talk about it — Sarah Sanders, PostHog
sources:
  - title: "We let an AI agent execute Bash and lived to talk about it — Sarah Sanders, PostHog"
    url: "https://www.youtube.com/watch?v=4lXks428C9o"
    author: "AI Engineer"
    date: "2026-09-14T16:00:00+00:00"
---

# We let an AI agent execute Bash and lived to talk about it — Sarah Sanders, PostHog

Sarah Sanders, a context engineer at PostHog, describes the security work behind the PostHog Wizard: an agentic CLI tool that reads your codebase, installs the right SDK, instruments events, and builds dashboards — compressing an hour or two of setup into five to six minutes with free inference. The tool is deliberately an agent rather than just a good prompt or an invokable skill, because participating fully in an agent loop is the whole product experience. It recently hit 8,000 runs per week, and the team is considering making it the default way to install PostHog.

That ambition triggered the security question: an agent with shell access is, in Sanders' framing, the "malware starter pack" — close to what you'd hand a piece of malware if you were feeling generous. She walks through the anatomy of the Wizard: task-specific models, steering prompts, a set of tools, an in-house context engine ("the wizard's brain", sometimes described as markdown in a trench coat) that produces consistent results across runs, a terminal UI built with Ink, and a security scanner called the Warlock that she built while investigating the risks of shipping an agent to production.

The talk's core lesson is about layered defense-in-depth for agents, and specifically that prompts are not security. Sanders classifies the original posture as "layer zero" — just prompts that suggest what the agent should do and steer it — which she explicitly calls not security at all. The next step was layer one, an allow list of permitted commands, which she began auditing and found warranted scrutiny.

Only the first layers of that progression are covered in the available transcript; the remaining lessons are framed as the things that kept her up at night and the tooling (the Warlock) she built in response.

- The PostHog Wizard is an agentic CLI that reads your codebase, installs the right SDK, instruments events, and builds dashboards — turning 1-2 hours of setup into ~5-6 minutes, now at ~8,000 runs per week.
- Building an agent is the product, not a gimmick: prompts or invokable skills don't deliver the same developer experience as a CLI that can take part in an agent loop.
- An agent that can run commands is effectively the "malware starter pack" — its toolset resembles what you'd hand malware — so shipping one demands a real threat model.
- Threat models fall out of the anatomy of the agent: models, prompts, tools, context engine, terminal UI, plus a purpose-built security scanner (the Warlock).
- Prompts are not security: PostHog's original "layer zero" was only prompts steering the agent, with an allow list as the first real (and audited) control layer.