---
domain: ai-workflows
subdomain: ai-coding-agents
concept: agent-skills
title: AI Skills with Matt Pocock
sources:
  - title: "AI Skills with Matt Pocock"
    url: "https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock"
    author: "Gergely Orosz"
    date: "2026-09-17"
  - title: "Skills: grill me"
    url: "https://www.aihero.dev/skills-grill-me"
    author: "Matt Pocock"
  - title: "grilling SKILL.md"
    url: "https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md"
    author: "Matt Pocock"
---

# AI Skills with Matt Pocock

Matt Pocock — creator of Total TypeScript (over $2.5M in sales) and the AI Hero course — describes his path from voice teacher to developer to full-time technical educator, including a negotiated three-days-a-week Vercel contract he took as insurance in case his course didn't work out, and his refusal to work weekends (Pragmatic Engineer, 2026).

His current focus is reusable "skills" for coding agents. The popular "grill-me" skill, inspired by Anthropic's Thariq Shihipar, is short and simple: it instructs an agent to interview the user relentlessly. Pocock also argues that the right "leading words" change agent behavior — after reading The Pragmatic Programmer, he told an agent to build with "tracer bullets" (a golden path) instead of layer by layer, and got better code with fewer inter-layer bugs. He now mines classic software engineering books for more such words, and borrows Ousterhout's tactical-vs-strategic programming split to argue agents can handle tactical work while engineers move up to the strategic level.

Pocock frames agent-friendly codebases as "Memento-driven development": optimize for a colleague who wakes up each morning with no memory. Humans work around bad code and build memory of it; agents start fresh every session, so the readability and understandability that software fundamentals have always pushed for matters more than ever. He splits context to keep agents in their "smart zone," favors cloud agents over local ones because they run when his laptop is closed and can be made multiplayer, and has mixed feelings on TDD with agents — humans need failing tests as memory aids, but agents have longer context windows, so he asks them to produce proof their code works with or without TDD.

- Simple, short skills like "grill-me" (agent relentlessly interviews the user) can be highly effective; it was inspired by Anthropic's Thariq Shihipar.
- "Leading words" such as "tracer bullet" from The Pragmatic Programmer steer agents toward better output than default layer-by-layer construction.
- Memento-driven development: optimize codebases for an agent that starts each session with no memory, which is what software fundamentals have always aimed at.
- Cloud agents beat local ones for Pocock because they keep running after the laptop closes and can be collaborative; he also splits context to keep agents in the "smart zone."
- On TDD with agents he is ambivalent: failing tests aid human memory, but agents have longer context windows, so he asks for proof the code works either way.