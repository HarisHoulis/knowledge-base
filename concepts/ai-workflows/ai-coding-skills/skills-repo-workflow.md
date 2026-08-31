---
domain: ai-workflows
subdomain: ai-coding-skills
concept: skills-repo-workflow
title: mattpocock/skills: A Complete AI Coding workflow, end-to-end
sources:
  - title: "mattpocock/skills: A Complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16T09:32:49+00:00"
---

# mattpocock/skills: A Complete AI Coding workflow, end-to-end

Matt Pocock presents a tutorial for his popular skills repository, which has reached 162,000 stars and 7.5 million downloads. The video walks through setting up the skills on a new or existing project using the command `npx skills@latest add mattpocock/skills`, which requires Node.js and leverages Vercel's skills.sh installer. The installer presents a selection of 38 skills, divided into official mattpocock/skills and experimental others; users can select all official skills with a space bar and return (Pocock, 2026).

The installer supports multiple AI agents, including Claude Code, Cursor, and Codex, with agent-specific setup for tools like Claude Code. The installation scope can be project-local or global; Pocock recommends project scope for teams to ensure everyone uses the same skills and can collaborate on skill evolution, while global scope is fine for solo developers. For installation method, symlink is recommended as the cleanest approach over copying. After installation, skills appear as slash commands in the agent (e.g., "grill me", "way finder"), and a key design principle is that his skills are mostly user-invoked, with short descriptions to avoid polluting the agent's context (Pocock, 2026).

- Install with `npx skills@latest add mattpocock/skills`, requiring Node.js and the skills.sh installer from Vercel.
- Choose from 38 skills, selecting all official mattpocock/skills to get the curated set.
- Project-scoped installation is recommended for teams; global is acceptable for solo developers.
- Symlink installation is the recommended way to link skills to agent folders.
- Skills are user-invoked via slash commands in Claude Code, keeping descriptions short to minimize context overhead.