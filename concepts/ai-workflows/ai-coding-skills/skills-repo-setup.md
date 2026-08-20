---
domain: ai-workflows
subdomain: ai-coding-skills
concept: skills-repo-setup
title: A Complete AI Coding Workflow with Matt Pocock's Skills Repo
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16T09:32:49+00:00"
---

# A Complete AI Coding Workflow with Matt Pocock's Skills Repo

Matt Pocock presents a tutorial for his 'skills' repo, a collection of AI agent skills with over 162,000 stars and 7.5 million downloads. The main flow involves installing the repo via the Vercel Skills CLI using `npx skills@latest add mattpocock/skills`. The installer prompts the user to select which skills to install, choosing between official skills and experimental ones, and then configures the skills for a specific agent like Claude Code, Cursor, or Codex. The user also chooses the installation scope—project-level (recommended for teams) or global (fine for solo developers)—and the installation method, with symlink recommended over copying.

Once installed, the skills appear as slash commands in Claude Code, such as 'grill me' and 'way finder'. A key design principle is that these skills are mostly user-invoked rather than automatically injected into the agent's context, keeping descriptions short and intentional. The tutorial targets both brownfield and greenfield projects, showing that the setup works in any directory. The overall workflow emphasizes simplicity, team collaboration through shared project skills, and a clean agent integration via symlinks.

- Install skills with `npx skills@latest add mattpocock/skills`, which runs the Vercel CLI and guides through configuration.
- Choose project-scoped skills for team consistency; global scope is acceptable for solo developers.
- Select symlink as the installation method—it's the recommended and easiest way to link skills into the agent.
- Skills are user-invoked (e.g., via slash commands in Claude Code) rather than auto-loaded, keeping agent context uncluttered.
- The setup works on both existing codebases and empty projects, making it flexible for any workflow.