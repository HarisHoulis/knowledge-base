---
domain: ai-workflows
subdomain: ai-coding-agents
concept: skills-v1.2-release
title: New Skills! v1.2 brings /wait-what, /writing-for-agents, and fixes /grill-me
sources:
  - title: "New Skills! v1.2 brings /wait-what, /writing-for-agents, and fixes /grill-me"
    url: "https://www.youtube.com/watch?v=gaDdrDdczO4"
    author: "Matt Pocock"
    date: "2026-08-05T15:28:41+00:00"
---

# New Skills! v1.2 brings /wait-what, /writing-for-agents, and fixes /grill-me

Matt Pocock announces Skills v1.2, featuring a new documentation portal at aihero.dev/skills that organizes skills into workflows, provides full references, a FAQ sourced from his personal wiki, and links to an AI coding dictionary. The skills are also now officially listed in the Claude Code plugin marketplace, enabling one-command installation and automatic updates (Pocock, 2026).

Key updates include Codex compatibility via OpenAI.YAML sidecar files for every skill, preserving the `allow implicit invocation: false` setting that keeps user-invoked skills out of the agent's context window until called. A new skill, `/wait-what`, addresses overly verbose or nonsensical LLM output by enforcing ASD-STE-100 simplified technical English and grounding responses in the project's `context.md` ubiquitous language (Pocock, 2026).

Finally, the popular `/grill-me` skill has been updated to fix a failure mode where easy questions were asked one per turn at the end of sessions, dragging out the process. The update targets this inefficiency, though the specific mechanism is not detailed in the announcement (Pocock, 2026).

- New docs site at aihero.dev/skills groups skills into flows, includes references and FAQ, and links to an AI coding dictionary.
- Skills are now available via the Claude Code plugin marketplace with automatic updates.
- OpenAI.YAML sidecar files added for every skill to support Codex UI and preserve allow implicit invocation false.
- New 'wait-what' skill reduces verbose/garbage LLM output using STE-100 and project ubiquitous language.
- Grill Me skill updated to fix the one-question-per-turn failure mode at the end of sessions.