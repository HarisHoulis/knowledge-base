---
domain: ai-workflows
subdomain: coding-agents
concept: llm-3d-code-generation
title: Claude Ports a Three.js 3D Scene to Vanilla WebGL
sources:
  - title: "The Web Is More Than Enough, by Paul Ford"
    url: "https://simonwillison.net/2026/Nov/9/hn-50421091/"
    author: "Simon Willison"
    date: "2026-11-09"
---

# Claude Ports a Three.js 3D Scene to Vanilla WebGL

Simon Willison responds to Paul Ford's "The Web Is More Than Enough" by testing whether an LLM can build 3D graphics without a framework. He first created a Nudibranch-themed Fabergé Egg in Three.js (77KB), then asked Claude (Opus 5.5 Medium in regular Claude Chat) to port it to Vanilla JS in the same thread, producing a 98KB Vanilla WebGL version. The two outputs are not identical, and Willison notes he doesn't fully understand why they differed, linking the shared transcript for detail. His conclusion is that Claude Opus 5.5 is perfectly capable of 3D modeling in Vanilla JS + WebGL without Three.js. He finds the Three.js code slightly easier to read himself, but considers that minor since he rarely inspects the code for these 3D projects.

- Claude Opus 5.5 ported a Three.js 3D scene to Vanilla JS + WebGL without the library
- The Three.js original was 77KB; the Vanilla WebGL port was 98KB
- The two versions are not identical, with the differences explained in the shared Claude transcript
- Willison finds the Three.js code slightly more readable, but rarely reviews code for these 3D projects