---
domain: ai-workflows
subdomain: coding-agents
concept: vibe-coded-game-development
title: Battle Drones: A Vibe-Coded RTS Built Through Iterative Agent Prompts
sources:
  - title: "Battle Drones - a vibe coded RTS with audio-based multiplayer"
    url: "https://simonwillison.net/2026/Oct/20/battledrones/"
    author: "Simon Willison"
    date: "2026-10-20"
---

# Battle Drones: A Vibe-Coded RTS Built Through Iterative Agent Prompts

Simon Willison documents building Battle Drones, a Command & Conquer-style mobile-friendly RTS, almost entirely through prompts to coding agents (mainly Claude Code) over roughly 12 major iterations and 321 commits. He reviewed almost none of the TypeScript code, relying instead on heavy playtesting and iterative prompting; early versions used the Phaser framework and OpenAI image generation for sprites, and were recognizable as RTS games but not fun to play.

The turning point came with a single prompt—"Make it a LOT more fun"—run in Ultracode mode, where Claude Code orchestrates many subagents via dynamic workflows. The overnight run produced rebalanced gameplay, new modes, and over a thousand simulated playtests; Willison reports that undecided games after 25 minutes dropped from 14% to 0.9% and comeback wins rose from 24% to 46%. Later prompts drove a port to three.js with 3D models, a hand-designed Archipelago map encouraging Condor-dropped infantry, giant Goliath mechs, and a random map generator built within a 45-minute token-budget window.

A notable feature is agent battles: LLMs such as Claude Haiku 5.5 and GPT-6 Luna play each other through a tools plugin with fog-of-war-limited information, with recorded replays and a debug viewer. Multiplayer between nearby devices uses an audio modem, derived from his earlier Chirp Pong experiment, with a Radio Probe tool used to measure bandwidth first. Willison notes the audio multiplayer caused headaches, prompting an update adding online multiplayer.

- Iterative prompting plus playtesting, rather than code review, drove the game's improvement across 12 iterations and 321 agent commits.
- A vague "make it a LOT more fun" prompt in Ultracode mode triggered many hours of subagent work, including over a thousand simulated playtests used for rebalancing.
- Agents handled asset generation (OpenAI image API sprites), a three.js 3D port, and code-constructed 3D models.
- Agent battles let different LLMs compete via a tools plugin, with recorded replays and a debug viewer.
- Audio-based local multiplayer was prototyped from a prior experiment and validated with a bandwidth-measuring Radio Probe tool.