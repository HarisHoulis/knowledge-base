---
domain: ai-workflows
subdomain: ai-assisted-code-migration
concept: cursor-framework-migration
title: How I Used Cursor to Migrate Frameworks
sources:
  - title: "How I Used Cursor to Migrate Frameworks"
    url: "https://kentcdodds.com/blog/how-i-used-cursor-to-migrate-frameworks"
    author: "Kent C. Dodds"
    date: "2026-02-20"
---

# How I Used Cursor to Migrate Frameworks

In this article, Kent C. Dodds describes using Cursor's AI agents to upgrade the substantial dependency set of his website kentcdodds.com, which contains over 42k lines of code and 330k words of content. He initially prompted Cursor to list outdated packages grouped by upgrade difficulty (easy, medium, hard), then used the AI to perform the upgrades incrementally. The easy and medium upgrades went smoothly, with occasional issues that were resolved through iteration and the help of tests and documentation already in the project (Kent C. Dodds, 2026).

For major upgrades, such as Vite 5 to 7, Zod 3 to 4, and especially the Remix v2 to React Router v7 migration, Dodds leveraged Cursor's long-running background agent. He gave the agent a high-level prompt, provided feedback on routing conventions and patch file removal, and allowed the agent to work autonomously overnight. The agent used migration docs, verified its output via route generation, and integrated with BugBot and CodeRabbit to fix issues automatically. This resulted in a successful migration merged as PR #658 (Kent C. Dodds, 2026).

Dodds emphasizes that the success of such AI-assisted upgrades depends on having robust tests and documentation, as well as giving the agent ways to check its own work (e.g., running `npx react-router routes`). He also reflects on the transformative yet demanding nature of AI-driven development: he now sends hundreds of prompts daily and enjoys the speed, but acknowledges the challenge of maintaining balance when the next problem is always one prompt away (Kent C. Dodds, 2026).

- AI agents can categorize dependency upgrades by difficulty and handle most migrations with minimal human intervention, especially when the project has good tests and documentation.
- Using long-running background agents enables complex framework migrations (e.g., Remix v2 to React Router v7) to be executed autonomously over hours, with automatic bug-fixing via tools like BugBot.
- Giving the agent explicit instructions, migration docs, and a way to verify its work (such as comparing route output) significantly improves success rates.
- The article highlights the productivity gains of AI-assisted development, but also notes the potential for overwhelm and the need to find balance.
- The source code changes were published in PR #658 for kentcdodds.com, providing a real-world example of AI-driven migration.