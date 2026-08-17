---
domain: ai-workflows
subdomain: ai-agent-skills
concept: skills-repo-workflow
title: Complete AI Coding Workflow with mattpocock/skills
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16T09:32:49+00:00"
---

# Complete AI Coding Workflow with mattpocock/skills

Matt Pocock walks through setting up and using his skills repository for AI coding agents. The installation process is done via `npx skills@latest add mattpocock/skills`, which downloads the repo and presents a list of 38 skills split into official and experimental groups. The installer guides the user through selecting skills, choosing the target agent (e.g., Claude Code, Cursor, Codex), and deciding between project-level or global installation scope. Pocock recommends project scope for teams and global for solo developers, and he suggests using symlink rather than copying files (Pocock, 2026).

Once installed, the skills become available as user-invoked slash commands within the agent. Unlike other skills repos, these skills are mostly not auto-injected into the AI's context; instead, the user explicitly triggers them when needed. This workflow works for both greenfield and brownfield projects, and the video focuses on the core flow without diving into advanced features. The demonstration uses the AI Hero CLI repo to show real-world application (Pocock, 2026).

- Install skills with `npx skills@latest add mattpocock/skills`, which supports multiple AI agents.
- Choose project-level installation for team consistency, global for solo work; use symlink for simplicity.
- The repo contains 38 skills; official ones are recommended for public use, while experimental ones may change.
- Skills are user-invoked via slash commands, not automatically injected into agent context.
- The setup works on both new and existing codebases.