---
domain: ai-workflows
subdomain: coding-agents
concept: agent-skills-workflow
title: Matt Pocock's Skills: A Complete AI Coding Workflow
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16T09:32:49+00:00"
---

# Matt Pocock's Skills: A Complete AI Coding Workflow

Matt Pocock's skills repository provides a comprehensive AI coding workflow, installable via a simple NPX command. The installer, `npx skills@latest add mattpocock/skills`, sets up the skills for use with any agent, including Claude Code, Cursor, and Codex. The repository currently contains 38 skills, split into 'official' blessed skills and experimental ones, allowing users to select which to install. The installation process supports both project-level and global scope, with symlink recommended for ease of use, making it suitable for both team collaboration and solo development (Pocock, 2026).

- Skills are installed via `npx skills@latest add mattpocock/skills`, requiring Node.js.
- The repo includes 38 skills, with official skills curated by Matt and experimental ones marked separately.
- Installation can be scoped to the project or globally; project scope is recommended for teams, global for solo developers.
- The setup supports multiple AI agents and uses symlinks for clean installation.
- Most skills are user-invoked rather than auto-injected, keeping agent contexts clean.