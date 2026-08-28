---
domain: ai-workflows
subdomain: ai-assisted-refactoring
concept: ai-framework-migration
title: How I used Cursor to Migrate Frameworks
sources:
  - title: "How I used Cursor to Migrate Frameworks"
    url: "https://kentcdodds.com/blog/how-i-used-cursor-to-migrate-frameworks"
    author: "Kent C. Dodds"
    date: "2026-02-20"
---

# How I used Cursor to Migrate Frameworks

For the major upgrades, Dodds used separate conversations for Vite/Vitest, Zod, and XState, asking the agent to consult migration docs and execute the plan. He leveraged Cursor's long-running background agent feature for the Remix v2 to React Router v7 migration, providing detailed instructions about route conventions, patch files, and alternative libraries. The agent ran for 21 minutes overnight, iterating with Cursor BugBot and CodeRabbit to fix issues automatically. Dodds emphasizes that giving the agent a way to verify its work (e.g., running `react-router routes`) significantly improved the outcome, and that the overall experience was both exciting and overwhelming, with hundreds of prompts sent daily ([source](https://kentcdodds.com/blog/how-i-used-cursor-to-migrate-frameworks)).

- AI agents can categorize dependency upgrades by difficulty and execute routine upgrades with minimal guidance.
- Major framework migrations require providing migration docs, context, and verification commands to the agent.
- Long-running background agents with auto-fix loops (e.g., BugBot) can complete multi-step refactors overnight.
- Good test coverage and documentation are essential for AI-assisted migration success.
- The process shifts developer focus to high-level decisions, but can lead to notification overload.