---
domain: engineering-culture
subdomain: ai-assisted-development
concept: cursor-framework-migration
title: How I used Cursor to Migrate Frameworks
sources:
  - title: "How I used Cursor to Migrate Frameworks"
    url: "https://kentcdodds.com/blog/how-i-used-cursor-to-migrate-frameworks"
    author: "Kent C. Dodds"
    date: "2026-02-20"
---

# How I used Cursor to Migrate Frameworks

Kent C. Dodds describes using Cursor, an AI-powered code editor, to upgrade dependencies and migrate frameworks on his website kentcdodds.com. He prompted Cursor to list outdated packages grouped by difficulty, then tackled them in stages: easy, medium, and major upgrades. Easy and medium upgrades went smoothly with only minor issues; major upgrades (Vite 5→7, Vitest 1→4, Zod 3→4, XState 4→5) were handled one at a time, with Cursor searching migration docs and executing plans. The most complex migration, from Remix v2 to React Router v7, was delegated to Cursor's long-running background agent, which iterated for 21 minutes, integrated with BugBot and CodeRabbit for issue detection, and produced a successful pull request (kentcdodds.com#658). (Source: https://kentcdodds.com/blog/how-i-used-cursor-to-migrate-frameworks)

- AI assistants like Cursor can effectively categorize and upgrade dependencies when given clear prompts and access to existing tests and documentation.
- Major framework migrations benefit from using long-running background agents that can research migration guides, plan, and execute over extended periods.
- The success of AI-driven migrations relies on having good test coverage and documentation, which allow the agent to verify its work.
- The workflow highlights a shift in engineering culture toward heavy AI collaboration, with many concurrent agents and a constant stream of notifications.