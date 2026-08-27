---
domain: ai-workflows
subdomain: llm-agent-discovery
concept: llm-friendly-docs-pipeline
title: How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth
sources:
  - title: "How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth"
    url: "https://www.youtube.com/watch?v=V_5bn4q-vAI"
    author: "Christopher Burns"
    date: "2026-08-26"
---

# How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth

Christopher Burns shares how his open-source cookie banner library C15T saw a dramatic shift in inbound traffic: starting April 13th, AI assistants like Claude, ChatGPT, Codex, and Gemini became the number one source of inbound. To capitalize on this, he treated agent optimization as a "utility belt" of small, targeted improvements rather than a single magic SEO tool. The key components include a hand-written LLM.txt (where about 40 good lines outperformed 1,000 lines of auto-generated noise), sitemaps, RSS feeds, and robots.txt. These micro-optimizations were abstracted into an open-source framework called Lead Type, which takes .mdx files and generates everything needed for an optimized agent experience.

- AI assistants became the top inbound source for C15T, with Claude, ChatGPT, Codex, and Gemini driving traffic.
- Hand-written LLM.txt files are more effective than auto-generated ones: ~40 good lines beat 1,000 lines of noise.
- Multiple micro-optimizations (LLM.txt, sitemaps, RSS, robots.txt) work together like Batman's utility belt.
- Lead Type is an open-source framework that turns .mdx docs into agent-optimized outputs.
- Developer experience primitives now double as agent primitives.