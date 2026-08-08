---
domain: ai-workflows
subdomain: agentic-game-development
concept: one-shot-game-generation
title: One-shotting a Raccoon Heist game using Claude Fable 5
sources:
  - title: "One-shotting a Raccoon Heist game using Claude Fable 5"
    url: "https://simonwillison.net/2026/Aug/5/raccoon-heist/"
    author: "Simon Willison"
    date: "2026-08-05"
---

# One-shotting a Raccoon Heist game using Claude Fable 5

In this post, Simon Willison revisits a 2022 tweet where GPT-3 generated a description of "Raccoon Heist" and DALL-E produced concept art. He then used Claude Fable 5 running in Claude Code for web to build a fully playable 3D browser game from that tweet's images alone, with a simple prompt encouraging the agent to work independently and commit frequently. The agent used Three.js, generated textures via OpenAI's gpt-image-2 API, and deployed previews through GitHub Pages branches, allowing Willison to watch the game evolve in real time (Willison, 2026).

The agent produced a surprisingly complete game: a low-poly raccoon heist game with guards, a scent-tracking dog, procedural WebAudio music, and mobile touch controls. It also wrote its own build log in notes.md and used Playwright to catch and fix real bugs, such as mobile canvas sizing and a broken win-screen button. Willison highlights the agent's code for the dog NPC and notes that the workflow of committing to a branch and using GitHub Pages made iterative previewing seamless.

Despite the technical achievement, Willison argues the game itself is mediocre: it lacks team mechanics (the two other raccoons are decorative), is too easy, and becomes boring after collecting all items. He concludes that while agents are impressive at generating game prototypes, designing games that are genuinely fun remains a uniquely human skill—but recommends game development as a low-risk, fun way to explore the capabilities of AI agents (Willison, 2026).

- Claude Fable 5, given only a tweet's screenshots and a prompt, built a full 3D browser game using Three.js, OpenAI image generation, and GitHub Pages for preview.
- The workflow of prompting the agent to 'commit and push as often as possible' to a branch enabled near-real-time iterative previewing.
- The agent autonomously implemented features, wrote tests, and fixed real bugs (e.g., mobile canvas sizing, invisible tap-blocking UI).
- The resulting game was technically solid but not fun—lacking team mechanics and depth—showing that game design remains a challenge for AI.
- AI agent game jams are recommended as an accessible way to explore agent capabilities and push their limits.