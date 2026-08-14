---
domain: ai-workflows
subdomain: ai-coding-skills
concept: ai-skills-repo-workflow
title: mattpocock/skills: A complete AI Coding workflow, end-to-end
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16T09:32:49+00:00"
---

# mattpocock/skills: A complete AI Coding workflow, end-to-end

Matt Pocock walks through setting up his skills repository, which provides AI coding skills for agents like Claude Code. The process begins with running `npx skills@latest add mattpocock/skills`, which invokes Vercel's skills.sh installer to clone the GitHub repo and present a list of 38 available skills. Users can select official skills (blessed by Matt) and configure the installation for their preferred agent, with support for universal harnesses like Cursor and Codex, while Claude Code requires additional setup.

The installer prompts for installation scope: project-level skills are recommended for teams to ensure consistency and collaborative contribution, while global installation is fine for solo developers. The installer also offers a symlink option as the recommended way to link skills into the agent's folder. After installation, skills appear in the agent's interface (e.g., forward slash menu in Claude Code). A key design point is that most skills are user-invoked rather than automatically injected, meaning they are triggered on demand by the developer.

- Install Matt's skills via `npx skills@latest add mattpocock/skills` to get the full repo and setup wizard.
- Choose project-level installation for team consistency or global for solo projects.
- Use symlink rather than copy when installing to agent directories.
- Skills are intentionally user-invoked (slash commands) rather than auto-loading into context.
- The workflow works on both greenfield and brownfield codebases.