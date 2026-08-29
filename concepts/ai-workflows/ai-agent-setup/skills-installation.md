---
domain: ai-workflows
subdomain: ai-agent-setup
concept: skills-installation
title: Complete AI Coding Workflow with mattpocock/skills
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16T09:32:49+00:00"
---

# Complete AI Coding Workflow with mattpocock/skills

Matt Pocock presents a complete AI coding workflow using his 'skills' repository, which has gained significant popularity. The workflow begins with installing the skills via `npx skills@latest add mattpocock/skills`, leveraging the Vercel skills.sh CLI. The installer discovers 38 available skills and lets you select which ones to install, distinguishing between official public-facing skills and experimental ones. You can configure the installation for specific AI agents like Claude Code, Cursor, or Codex, and choose between project-scoped or global installation, with symlinking recommended for simplicity (Pocock, 2026).

- Install skills with `npx skills@latest add mattpocock/skills`
- Choose between official and experimental skills; select the ones you need
- Configure for your AI agent (Claude Code, Cursor, etc.) and installation scope
- Symlink is recommended for easy installation
- Skills are user-invoked via slash commands rather than auto-injected, keeping agent context clean