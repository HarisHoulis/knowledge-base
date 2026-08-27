---
domain: ai-workflows
subdomain: ai-assisted-migrations
concept: cursor-framework-migration
title: How I Used Cursor to Migrate Frameworks
sources:
  - title: "How I used Cursor to Migrate Frameworks"
    url: "https://kentcdodds.com/blog/how-i-used-cursor-to-migrate-frameworks"
    date: "2026-02-20"
---

# How I Used Cursor to Migrate Frameworks

The article describes using Cursor's AI composer and long-running background agents to upgrade dependencies on kentcdodds.com, a large project with over 42k lines of code and 330k words of content (source: https://kentcdodds.com/blog/how-i-used-cursor-to-migrate-frameworks). The process began with a prompt asking for a categorized list of outdated packages by difficulty, which yielded 19 easy, 42 medium, and 14 hard upgrades. Easy and medium updates were handled via follow-up prompts with only minor issues, while major upgrades like Vite (v5 to v7) and Vitest (v1 to v4) were run together without issues. For Zod, the author specifically directed Cursor to use Conform's special export for Zod v4, making the migration smooth. XState was handled in a fresh conversation with instructions to look up migration docs first (source: https://kentcdodds.com/blog/how-i-used-cursor-to-migrate-frameworks).

- Cursor can categorize outdated packages by upgrade difficulty and automate many routine updates effectively.
- Complex migrations like Remix v2 to React Router v7 benefit from long-running background agents with detailed prompts and verification steps.
- Providing tests and documentation helps AI agents handle breaking changes more gracefully.
- Letting agents run overnight with auto-fix (BugBot) and review tools can complete large migrations with minimal manual intervention.
- The author sends hundreds of prompts daily and finds AI-assisted development exciting but acknowledges the challenge of balancing many concurrent agents and notifications.