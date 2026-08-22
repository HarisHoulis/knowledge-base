---
domain: ai-workflows
subdomain: ai-coding-skills
concept: skills-setup
title: mattpocock/skills: A complete AI Coding workflow, end-to-end
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16T09:32:49+00:00"
---

# mattpocock/skills: A complete AI Coding workflow, end-to-end

Matt Pocock demonstrates how to set up his popular skills repository for AI coding agents. The installation uses the Vercel skills CLI via `npx skills@latest add mattpocock/skills`, which installs the repo and displays 38 skills for selection. Users can choose from official skills he has blessed or experimental ones he is still developing. The installer supports multiple agents, including Claude Code, Cursor, and Codex; for Claude Code, users must explicitly select it during setup. The installation scope can be project-local or global, with the author recommending project-local for teams to ensure consistent skill usage, while global is suitable for solo developers. The recommended installation method is symlinking to avoid copying files. Once installed, skills appear in the agent's slash-command menu and are user-invoked rather than automatically injected, keeping the AI's context clean and focused. Pocock highlights that these skills are designed to be deliberately triggered by the user, maintaining a simple and controlled workflow.

- Use `npx skills@latest add mattpocock/skills` to install the skills repository.
- The installer presents 38 skills, divided into official and experimental categories.
- Installation supports multiple AI agents; for Claude Code, select it during setup.
- Choose project scope for team collaboration, global scope for solo work, and use symlink installation for simplicity.
- Skills are user-invoked via slash commands, not auto-injected, keeping the agent's context minimal.