---
domain: ai-workflows
subdomain: ai-coding-skills
concept: skills-repo-workflow
title: A Complete AI Coding Workflow with mattpocock/skills
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16"
---

# A Complete AI Coding Workflow with mattpocock/skills

Matt Pocock walks through the end-to-end setup of his skills repository, mattpocock/skills, which has gained significant traction (162,000 stars and 7.5 million downloads). The workflow begins with a single command: `NPX skills@latest add mattpocock/skills`, which requires Node.js and uses Vercel's skills.sh CLI. This installer fetches the GitHub repo and presents a list of 38 available skills, split into official skills (blessed by Matt) and experimental ones. Users can select all official skills with a spacebar toggle, then configure the installation for their preferred AI agent—though Claude Code requires additional manual configuration (Pocock, 2026).

The installer then prompts for installation scope, where Matt recommends project-level installation for teams to ensure shared skill sets and collaborative maintenance, while global installation suits solo developers. He also recommends choosing symlink over copy for a cleaner setup. After installation, skills become available as slash commands in the agent (e.g., Claude Code). A key design principle is that most skills are user-invoked rather than automatically injected into context, keeping agent descriptions short and avoiding unnecessary context bloat (Pocock, 2026).

- Install with `NPX skills@latest add mattpocock/skills`; requires Node.js and Vercel's skills.sh CLI.
- Choose official skills and configure the target agent; Claude Code requires manual setup.
- Use project-level installation for team consistency; global for solo work.
- Symlink is the recommended installation method.
- Skills are mostly user-invoked via slash commands, not auto-loaded into context.