---
domain: ai-workflows
subdomain: ai-coding-skills
concept: skills-repo-setup
title: Skill-Based AI Coding Workflows with mattpocock/skills
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16"
---

# Skill-Based AI Coding Workflows with mattpocock/skills

Matt Pocock walks through the main end-to-end workflow for his skills repository, which has over 162,000 stars and 7.5 million downloads. The setup begins by running `npx skills@latest add mattpocock/skills` inside a project directory; this uses Vercel's skills CLI to install the repository and presents a list of 38 available skills (Pocock, 2026). The installer separates official "blessed" skills from experimental ones, and users can select which to install using the spacebar.

- Install with `npx skills@latest add mattpocock/skills` and select the desired skills interactively.
- Skills can be installed at project scope or globally; project scope is recommended for team projects, global for solo developers.
- Configure the skills for your specific AI agent; with Claude Code, users must explicitly select it during setup.
- Prefers symlink installation over copying for a cleaner setup.
- The skills are mostly user-invoked via slash commands rather than auto-injected into the agent's context.