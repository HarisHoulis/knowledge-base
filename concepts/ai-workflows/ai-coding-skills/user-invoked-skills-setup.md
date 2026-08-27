---
domain: ai-workflows
subdomain: ai-coding-skills
concept: user-invoked-skills-setup
title: AI Coding Workflow with Matt Pocock's Skills Repo
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16T09:32:49+00:00"
---

# AI Coding Workflow with Matt Pocock's Skills Repo

Matt Pocock's skills repo provides a complete, end-to-end AI coding workflow by offering a curated collection of reusable skills for AI agents like Claude Code. The repo has gained significant traction (162k stars, 7.5M downloads) and is designed to be user-invoked rather than auto-injected, meaning skills only appear when the developer explicitly calls them via slash commands. This keeps the agent's context clean and gives developers control over when to apply specific workflows (source: https://www.youtube.com/watch?v=M6mYodf0dJM).

Installation is straightforward using `npx skills@latest add mattpocock/skills`, which runs Vercel's skills installer. The installer lists 38 skills split into official and experimental groups, lets users select which agents to support (Cursor, Codex, Claude, etc.), and asks for installation scope. The video recommends project-level installation for teams to ensure consistency and shared decision-making, while global installation is fine for solo developers. Symlinking is presented as the cleanest installation method, avoiding messy file copying (source: https://www.youtube.com/watch?v=M6mYodf0dJM).

After installation, skills appear as slash commands in Claude Code. The key design choice is that most skills are user-invoked—they have short descriptions and don't leech into the agent's system prompt. This differs from many other skills repos and ensures the agent remains focused unless the developer explicitly activates a skill, making the workflow more predictable and efficient (source: https://www.youtube.com/watch?v=M6mYodf0dJM).

- The skills repo is a curated set of AI coding skills with 162k stars and 7.5M downloads, designed for user-invoked workflows rather than always-on agent behavior.
- Install with `npx skills@latest add mattpocock/skills`; the installer supports multiple agents and offers both official and experimental skill groups.
- Choose project-level installation for team consistency and shared contribution, or global installation for solo projects; symlinking is the recommended method.
- Skills appear as slash commands in Claude Code and are triggered on-demand, keeping the agent's context clean and focused.