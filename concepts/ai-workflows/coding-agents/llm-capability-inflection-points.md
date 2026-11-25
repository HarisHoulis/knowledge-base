---
domain: ai-workflows
subdomain: coding-agents
concept: llm-capability-inflection-points
title: Three LLM Inflection Points in Twelve Months
sources:
  - title: "Three LLM inflection points in twelve months"
    url: "https://simonwillison.net/2026/Nov/24/llm-inflection-points/"
    author: "Simon Willison"
    date: "2026-11-24"
---

# Three LLM Inflection Points in Twelve Months

Simon Willison argues that LLM and coding-agent capabilities crossed three distinct inflection points in the twelve months leading up to November 2026. The first came with Claude Opus 4.5 (released November 2025) and OpenAI's GPT-5.1 family, which made coding agents like Claude Code and Codex reliably useful by default rather than requiring constant correction. Willison notes that Opus 4.5 was the first model where the default result was generally the right thing, making it a clear accelerant over working manually.

The second inflection point was the arrival of "Fable class models," introduced with Claude Fable 5 in June 2026 (a defanged version of the too-dangerous Claude Mythos). Willison defines these as models that, given a goal and the right tools, will relentlessly and proactively pursue it—citing examples like Fable spinning up its own screenshot mechanism and localhost logging server to debug a Safari glitch, and triangulating a mysterious beep to within 40cm using five WebAudio microphones. He currently classes Fable 5, 5.1, 5.2, Opus 5.5, GPT-6 Astra, and possibly Gemini 4 Neon as Fable class.

The third inflection point concerns 3D modeling and game design. Over roughly four months, frontier models became genuinely good at 3D modeling via Blender or Three.js, and Claude Opus 5.5 (September 2026) was the first model Willison used that appeared to understand fun—turning a boring RTS game into a deeply entertaining one after 12 hours of autonomous playtesting and rebalancing. He notes the indie games scene has descended into a culture war over AI-assisted programming.

Willison is still deciding whether Fable 5.2 is a fourth inflection point or incremental improvement, but reports getting enormous amounts of work done with it—shipping a flood of Datasette and LLM releases in three weeks—and suggests the key feature may be that if you can imagine and clearly describe a piece of software, Fable can build it.

- Claude Opus 4.5 (Nov 2025) and GPT-5.1 made coding agents reliably useful by default, marking the first inflection point.
- "Fable class models" (starting with Claude Fable 5, June 2026) are defined by relentless proactivity: given a goal and tools, they pursue it autonomously.
- Frontier models became genuinely capable at 3D modeling and game design, with Opus 5.5 the first to appear to understand fun.
- Willison is unsure whether Fable 5.2 is a new inflection point, but reports it can build software from a clear description and has accelerated his Datasette and LLM releases dramatically.