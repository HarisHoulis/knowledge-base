---
domain: ai-workflows
subdomain: ai-coding-skills
concept: skills-repo-installation
title: Complete AI Coding Workflow: Installing and Using Matt Pocock's Skills Repo
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16T09:32:49+00:00"
---

# Complete AI Coding Workflow: Installing and Using Matt Pocock's Skills Repo

Once installed, the skills appear in the agent's interface, such as Claude Code's slash commands (e.g., /grill-me, /way-finder, /grill-with-docs). A key design principle of these skills is that they are mostly user-invoked rather than auto-injected into the model's context, keeping descriptions short and minimizing overhead.

- Install the skills repo with `npx skills@latest add mattpocock/skills`.
- Project-level installation is recommended for teams; global works for solo developers.
- Symlink is the recommended installation mode over copying.
- Skills are user-invoked via slash commands, not auto-injected into every prompt.