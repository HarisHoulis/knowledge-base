---
domain: ai-workflows
subdomain: ai-skills-installation
concept: ai-coding-skills-repo
title: A Complete AI Coding Workflow with mattpocock/skills
sources:
  - title: "mattpocock/skills: A complete AI Coding workflow, end-to-end"
    url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
    author: "Matt Pocock"
    date: "2026-07-16T09:32:49+00:00"
---

# A Complete AI Coding Workflow with mattpocock/skills

In this tutorial, Matt Pocock walks through setting up his AI coding skills repository, mattpocock/skills, on a new or existing project. The installation uses the command `npx skills@latest add mattpocock/skills`, which runs the Vercel skills CLI installer and requires Node.js. The CLI presents a list of 38 skills split into official mattpocock/skills and experimental ones; Pocock recommends selecting all official skills by navigating to the top and pressing space (Pocock, 2026).

After selecting the skills, the installer configures them for use with a range of AI agents, including Claude Code, Cursor, and Codex. For agent-specific skills like those used in Claude Code, additional manual setup may be required. The installer also asks for an installation scope: project-local or global. Pocock suggests project-local for teams to ensure consistent skill usage, while global is acceptable for solo developers. He also recommends choosing the symlink option rather than copying files, as it is simpler (Pocock, 2026).

Once installed, the skills appear as slash commands in Claude Code, such as /grill-me, /wayfinder, and /grill-with-docs. A key design philosophy of Pocock's skills is that they are mostly user-invoked, meaning they do not automatically inject themselves into the agent's context. They have short descriptions and only run when explicitly triggered, giving developers more control over when and how AI assistance is used (Pocock, 2026).

- Install skills with `npx skills@latest add mattpocock/skills`, which requires Node.js and the Vercel skills CLI.
- The repository includes both official and experimental skills; select the official ones for a stable set.
- Project-level installation is recommended for teams, while global installation works for solo developers.
- Use symlink instead of copy to integrate skills with the agent's folder.
- Skills are user-invoked slash commands rather than auto-injected context, providing on-demand assistance.