---
domain: ai-workflows
subdomain: ai-assisted-migrations
concept: cursor-framework-migration
title: How I used Cursor to Migrate Frameworks
sources:
  - title: "How I used Cursor to Migrate Frameworks"
    url: "https://kentcdodds.com/blog/how-i-used-cursor-to-migrate-frameworks"
    author: "Kent C. Dodds"
    date: "2026-02-20"
---

# How I used Cursor to Migrate Frameworks

Kent C. Dodds describes using Cursor's Composer and long-running background agents to perform large-scale dependency upgrades on kentcdodds.com. He first asked Cursor to list outdated packages grouped by upgrade difficulty, then auto-updated the easy and medium ones. The process went smoothly largely because the project had good tests and documentation, which the agent could use to validate changes.

- Cursor can categorize outdated dependencies by upgrade difficulty and execute incremental upgrades, but requires a strong test suite and documentation for safety.
- For major upgrades like Vite and Vitest, running them together worked well; for XState, the agent searched for migration docs and followed them.
- For the Remix v2 to React Router v7 migration, a long-running background agent was used, with the user providing constraints and alternatives (e.g. switching from remix-flat-routes to react-router-auto-routes).
- Giving the agent a way to verify its work (e.g. running `npx react-router routes` and comparing output) significantly improved the routing migration result.
- Background agents combined with automated bug detection (Cursor BugBot, CodeRabbit) allowed the migration to complete overnight with minimal manual intervention.