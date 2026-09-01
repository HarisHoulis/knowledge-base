---
domain: ai-workflows
subdomain: ai-assisted-dependency-upgrades
concept: ai-framework-migration
title: How I used Cursor to Migrate Frameworks
sources:
  - title: "How I used Cursor to Migrate Frameworks"
    url: "https://kentcdodds.com/blog/how-i-used-cursor-to-migrate-frameworks"
    author: "Kent C. Dodds"
    date: "2026-02-20"
---

# How I used Cursor to Migrate Frameworks

The author emphasizes that having good tests and documentation was critical for the AI to perform correctly. He also notes that giving agents a way to verify their work (e.g., running `npx react-router routes` to compare routes) greatly improved results. The migration was completed successfully and merged via PR #658. The article reflects on the excitement and challenges of heavy AI-assisted development, noting hundreds of prompts daily and a fast-paced workflow.

- Cursor AI can group outdated packages by upgrade difficulty and execute bulk upgrades with minimal human intervention.
- Long-running background agents can autonomously handle complex framework migrations (e.g., Remix v2 to React Router v7) by consulting docs and iterating on issues.
- Good test coverage and documentation are essential for AI-assisted refactoring to succeed safely.
- Providing the agent with a verification step (like checking routes) improves its performance significantly.
- Auto-fix tools (BugBot, CodeRabbit) and human oversight remain necessary to catch and resolve edge cases.