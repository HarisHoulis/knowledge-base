---
domain: ai-workflows
subdomain: ai-coding-skills
concept: skills-repo-installation
title: Matt Pocock's AI Coding Workflow with the Skills Repo
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16"
---

# Matt Pocock's AI Coding Workflow with the Skills Repo

Matt Pocock demonstrates how to set up his popular 'skills' repository for AI coding workflows. The process begins with running `npx skills@latest add mattpocock/skills`, which installs a GitHub repo of reusable skills via Vercel's CLI. Users can select from 38 available skills, including official ones marked by Pocock and experimental ones. The installer supports multiple agents like Claude Code, Cursor, and Codex, with configuration options per agent (Pocock, 2026).

Pocock recommends choosing project-level installation for teams so everyone shares the same skill set, while global installation is fine for solo developers. He also advises using the symlink option when installing, as it links the skills neatly into the agent's configuration folder. After installation, skills appear as slash commands in Claude Code (e.g., `/grill-me`, `/way-finder`), and most of Pocock's skills are explicitly user-invoked rather than automatically injected into the agent's context (Pocock, 2026).

- Install skills with `npx skills@latest add mattpocock/skills` and choose the desired agent(s).
- Select project-scoped installation for team consistency, global for personal use.
- Use the symlink installation method as the recommended approach.
- Skills appear as slash commands in agents like Claude Code.
- Most skills are user-invoked, keeping the agent's context clean.