---
domain: ai-workflows
subdomain: agent orchestration
concept: game-inspired-agent-orchestration
title: AgentCraft: Turning Coding Agents Into a Strategy Game
sources:
  - title: "I Turned Coding Agents Into a Strategy Game — Ido Salomon, AgentCraft"
    url: "https://www.youtube.com/watch?v=YIVkERhy8xo"
    author: "Ido Salomon (AI Engineer)"
    date: "2026-09-27"
---

# AgentCraft: Turning Coding Agents Into a Strategy Game

Ido Salomon argues that although agents are capable of everything from "creating cat memes to B2B SaaS applications," the human remains the bottleneck: once you launch a swarm of agents, each one demands that you "control, direct, and verify" it, and doing that at scale is exhausting [1]. The fix, he suggests, is not new capability but new skills — and those skills already exist outside programming, in real-time strategy games where players manage many units at once [1].

His answer is AgentCraft, a "game-inspired orchestrator" that presents agents as units on a map. Agents (Claude Code, open-source agents, discovered on your device or created in-app) are prompted through a sidebar with voice and multimodality, while buildings on the map represent functionality such as plugin/skill management, an integrated terminal, and integrated Git [1].

The first design goal is visibility. The sidebar shows each agent, its task, what it did last time, and what it is doing now, so you can "quickly understand who needs my attention and who doesn't" [1]. The map goes further: your file system is projected onto the map, files appear as runes, and you can see which agent is working on which directory or file, then derive connections and heat maps from that activity [1]. To act on what you see, AgentCraft borrows the RTS convention of pressing spacebar to jump to whatever needs attention, letting you answer questions or approve plans quickly [1].

Salomon is explicit that visibility is a good step but not sufficient — constantly inspecting files and tools is tiring, and there are two core problems: there is too much to keep in mind, and you cannot do twenty things at once [1]. The transcript is truncated at that point.

- The human, not the model, is the bottleneck in agentic workflows: every launched agent requires control, direction, and verification, which becomes exhausting at scale.
- AgentCraft is a game-inspired orchestrator that renders agents as units on a map, with buildings representing functionality like plugins, terminal, and Git.
- Visibility is the first layer: a sidebar summarizes each agent's task and state, while a file-system map with files as runes shows which agent touched what, enabling heat maps.
- An RTS-style spacebar shortcut jumps to whichever agent needs attention, so you can answer questions or approve plans quickly.
- Visibility alone is insufficient — too much to hold in mind and an inability to do many things at once are framed as the two core remaining problems.