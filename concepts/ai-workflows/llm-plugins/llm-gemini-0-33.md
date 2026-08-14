---
domain: ai-workflows
subdomain: llm-plugins
concept: llm-gemini-0-33
title: llm-gemini 0.33: Gemini 3.7 Flash Support
sources:
  - title: "llm-gemini 0.33"
    url: "https://simonwillison.net/2026/Aug/13/llm-gemini/"
    author: "Simon Willison"
    date: "2026-08-13"
---

# llm-gemini 0.33: Gemini 3.7 Flash Support

Willison tested image generation with Gemini 3.7 Flash, asking it to draw pelicans riding bicycles at high, medium, and low thinking efforts. The high-effort result was visually appealing, but rendering varied by browser; Safari tolerated empty SVG filter elements while Firefox and Chrome did not, causing the pelican to disappear in those browsers (Simon Willison, 2026).

- Adds support for Gemini 3.7 Flash, 3.6 Flash, 3.5 Flash Lite, and two embedding models.
- Compatible with LLM 0.32, enabling reasoning traces and server-side tools via -T.
- Demonstrates image generation with high thinking effort, but notes cross-browser SVG rendering differences.
- Minimal thinking effort option was removed in Gemini 3.7 Flash.