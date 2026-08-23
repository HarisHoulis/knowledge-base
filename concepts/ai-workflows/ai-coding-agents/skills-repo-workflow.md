---
domain: ai-workflows
subdomain: ai-coding-agents
concept: skills-repo-workflow
title: mattpocock/skills: A complete AI Coding workflow, end-to-end
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16T09:32:49+00:00"
---

# mattpocock/skills: A complete AI Coding workflow, end-to-end

In this walkthrough, Matt Pocock demonstrates how to set up and use his skills repository for AI coding agents. The repo has grown to 162,000 stars and 7.5 million downloads. Installation is done via the command `npx skills@latest add mattpocock/skills`, which relies on Node.js and runs Vercel's skills CLI installer. The installer guides users through selecting skills, configuring agent support (e.g., Claude Code, Cursor, Codex), choosing an installation scope (project or global), and picking a symlink method. The repo currently contains 38 skills split into two groups: official skills from Matt Pocock and experimental "other" skills. Pocock recommends selecting all official skills and using symlinks as the simplest approach. (Pocock, 2026)

After installation, skills become available directly inside the AI agent. In Claude Code, pressing "/" reveals skills such as "grill me", "way finder", and "grill with docs". A key design choice is that most of these skills are user-invoked rather than automatically injected into the agent's context, keeping descriptions short and preventing prompt bloat. The workflow works for both brownfield and greenfield projects, and scoping skills to a project is recommended for team consistency, while global installation is fine for solo developers. (Pocock, 2026)

- Install skills with `npx skills@latest add mattpocock/skills`; requires Node.js and uses Vercel's CLI.
- Select the official skills, agent support, installation scope, and symlink method during setup.
- The repo offers 38 skills in two tiers: official and experimental.
- Skills appear as slash commands in Claude Code, e.g., /grill-me.
- Skills are primarily user-invoked to avoid cluttering the agent's context.