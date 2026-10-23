---
domain: ai-workflows
subdomain: coding-agents
concept: single-prompt-artifact-generation
title: Quick Study: Generating a Paintbrush-Simulation Artifact from One Prompt
sources:
  - title: "Quick Study"
    url: "https://simonwillison.net/2026/Oct/23/quick-study-painter/"
    author: "Simon Willison"
    date: "2026-10-23"
---

# Quick Study: Generating a Paintbrush-Simulation Artifact from One Prompt

Simon Willison built "Quick Study," a browser tool that opens a photo and rapidly paints a version of it using a canvas element and simulated paintbrush strokes. The tool was produced by giving Claude Opus 5.5 High a single prompt asking for an artifact that performs this painting effect within a few seconds [source].

The implementation uses Sobel edge detection to drive the painting effect, and relies on no external libraries beyond Google Fonts, keeping the artifact self-contained [source]. Willison links it to a prior experiment in which Claude Fable simulated a watercolor illustration with P5.js, framing this as a continuation of prompt-driven generative art experiments [source].

- A single natural-language prompt to Claude Opus 5.5 High produced a working photo-to-painting artifact
- The tool uses Sobel edge detection with no external libraries beyond Google Fonts
- It follows an earlier experiment simulating watercolor with P5.js