---
domain: ai-workflows
subdomain: llm-models-and-tooling
concept: gemini-4-carbon-release
title: llm-gemini 0.36 Adds Gemini 4 Carbon Support
sources:
  - title: "llm-gemini 0.36"
    url: "https://simonwillison.net/2026/Nov/10/llm-gemini/"
    author: "Simon Willison"
    date: "2026-11-10"
---

# llm-gemini 0.36 Adds Gemini 4 Carbon Support

Simon Willison's llm-gemini 0.36 release adds support for Gemini 4 Carbon, Google's newest Gemini model. Carbon was initially announced two weeks earlier for "a subset of cyber defenders" and is now generally available. Willison calls it Google's best Gemini yet, priced at $2/million input and $10/million output at launch, matching GPT-6.1 Sol and Claude Sonnet 5.5, with prices scheduled to double to $4/$20 on December 1st, matching Opus 5.5.

Willison tests the model with his recurring "pelican riding a bicycle" benchmark across low, medium, and high thinking efforts (defaulting to medium), noting that Gemini pelicans have been consistently good for a while. He also tests it in Google's Antigravity IDE with a Three.js prompt asking for a Yonkers mech animation using OpenStreetMap data, producing a standalone HTML result that he screen-captured as video.

An update notes a YouTube demo of Antigravity's /swarm feature, in which Carbon coordinated subagents to build an open-world 3D game of a pelican riding a GBike around Google's Mountain View campus, modeling assets in Blender, building the game in Three.js with WebGL shaders, and pairing procedural Web Audio effects with Lyria music.

- llm-gemini 0.36 adds support for Gemini 4 Carbon, now generally available after a limited cyber-defender preview
- Launch pricing is $2/$10 per million input/output tokens, doubling to $4/$20 on December 1st
- Willison tested pelican benchmarks at low, medium, and high thinking effort, plus a Three.js mech animation via Antigravity IDE
- A demo showed Antigravity's /swarm coordinating subagents to build a 3D game with Blender assets, Three.js, and Lyria music