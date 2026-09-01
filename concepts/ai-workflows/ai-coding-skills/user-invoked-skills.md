---
domain: ai-workflows
subdomain: ai-coding-skills
concept: user-invoked-skills
title: Matt Pocock's Skills Repo: A Complete AI Coding Workflow
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16T09:32:49+00:00"
---

# Matt Pocock's Skills Repo: A Complete AI Coding Workflow

The installation scope can be project-specific or global; Matt recommends project-scoped skills for teams to ensure everyone uses the same set, while global is fine for solo developers. The installation method uses symlinks, which is described as the recommended approach. Once installed, skills appear as slash commands in Claude Code (e.g., /grill-me, /way-finder). A key design principle is that these skills are user-invoked rather than automatically injected into the agent's context; their descriptions are intentionally short, so they only execute when explicitly triggered by the user.

- Install via `npx skills@latest add mattpocock/skills` (requires Node.js).
- Select all official skills from the 38 available; the rest are experimental.
- Configure for your agent (e.g., Claude Code) during installation.
- Choose project scope for team consistency, global for solo work; use symlink.
- Skills are user-invoked slash commands, not auto-loaded into context.