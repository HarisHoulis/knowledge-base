---
domain: ai-workflows
subdomain: ai-coding-agents
concept: skills-installation-workflow
title: A Complete AI Coding Workflow with mattpocock/skills
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16T09:32:49+00:00"
---

# A Complete AI Coding Workflow with mattpocock/skills

Matt Pocock walks through the end-to-end setup and usage of his `skills` repository, which has gained significant traction with 162,000 stars and 7.5 million downloads. The main flow begins by installing the skills via the command line using `npx skills@latest add mattpocock/skills`, which leverages Node.js and Vercel's skills.sh installer (Matt Pocock, 2026). The installer presents a list of 38 available skills, split into official 'blessed' skills and experimental ones. Users can select all or specific skills, with a note that the CLI selection interface is somewhat buggy but functional.

- Install skills using `npx skills@latest add mattpocock/skills` in any project (brownfield or greenfield).
- Choose project-level installation for team collaboration or global installation for solo work.
- Use symlink as the recommended installation method to avoid copying files.
- Skills are mostly user-invoked rather than auto-leeching into agent context, keeping descriptions short.
- The workflow supports multiple AI agents including Claude Code, Cursor, and Codex.