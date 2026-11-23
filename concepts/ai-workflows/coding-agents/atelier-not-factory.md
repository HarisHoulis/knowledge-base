---
domain: ai-workflows
subdomain: coding-agents
concept: atelier-not-factory
title: Build the Workshop Before the Software Factory
sources:
  - title: "Build the Workshop Before the Software Factory — Armin Ronacher, Earendil"
    url: "https://www.youtube.com/watch?v=JNexz3Tbiu8"
    author: "AI Engineer"
    date: "2026-11-22"
---

# Build the Workshop Before the Software Factory

Armin Ronacher argues that teams adopting coding agents should aim to build an "atelier" or workshop rather than a "software factory." Drawing an analogy to artists using CNC machines, 3D printers, and power tools, he suggests the goal is not to maximize code output but to raise the ambition and quality of the software being built. The framing is about augmenting human craft, not industrializing code production.

A central observation is that agent capability has improved dramatically without changes to the underlying tooling. Ronacher notes that Earendil's Pi coding agent has barely changed in basic structure over the past year and uses the same tools as last December, yet it has become far more powerful purely through better models. Many earlier prompting tricks and plugins, such as PyAutoResearch for goal pursuit, are no longer needed with modern models, and agents now exhibit emergent behavior like using Bash far more often than other provided tools.

He backs this with session data from Pi using default settings: the number of fixes and interventions shrinks with each better model, and the 90th-percentile task duration rose from about two and a half minutes with Opus 4.6 last December to 14 minutes or more with the latest models. This changes how one works with the tools even though the tools themselves are unchanged.

What has not changed is the human. Ronacher argues people remain limited by fundamental capabilities, with human attention as the key constraint on the pace of agent-driven work. Starting new projects with agents is now trivially easy, but supporting them has not gotten easier, and teams increasingly burden external systems that should not be part of this revolution.

- Build an atelier/workshop that raises ambition and quality, not a factory optimizing code volume.
- Agent capability improved dramatically with no structural changes to the Pi agent's tools—better models did the work.
- Session data shows fewer interventions and longer autonomous runs (90th percentile from ~2.5 to 14+ minutes).
- Human attention, not model capability, is the limiting factor on how fast agent-driven work can scale.
- Starting projects is easy with agents, but supporting them and the external systems they touch has not gotten easier.