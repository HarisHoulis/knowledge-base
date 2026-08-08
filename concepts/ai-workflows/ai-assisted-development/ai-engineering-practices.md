---
domain: ai-workflows
subdomain: ai-assisted-development
concept: ai-engineering-practices
title: How building software is changing at Anthropic
sources:
  - title: "How building software is changing at Anthropic"
    url: "https://newsletter.pragmaticengineer.com/p/inside-anthropic"
    author: "Gergely Orosz"
    date: "2026-07-28"
---

# How building software is changing at Anthropic

In a report from The Pragmatic Engineer (Orosz, 2026), the author visits Anthropic to explore how AI is transforming software engineering at one of the most AI-forward labs. The article highlights two major projects: the six-month development of Claude Managed Agents and the 11-day AI-assisted rewrite of Bun from Zig to Rust. These cases illustrate that while AI dramatically accelerates implementation and enables new workflows, complex architecture, planning, and human oversight remain essential.

At Anthropic, engineering practices have shifted significantly. Engineers routinely run 3–10 parallel AI agents, have unlimited token budgets, and operate with high autonomy. Prototyping is more fluid, verification now consumes more time than implementation, and code review and testing are increasingly delegated to AI. The Bun rewrite, completed using 64 parallel agents and $165,000 in tokens, shows how AI can compress a year-long, three-engineer migration into less than two weeks—but only with deep domain expertise and rigorous test suites.

Despite the AI-driven changes, some fundamentals persist. Complex projects like Claude Managed Agents still require PRDs, cross-team alignment, and mid-course architecture changes. Context switching remains a challenge, and the ratio of coding to testing time has not changed dramatically. The article concludes that AI amplifies the impact of senior engineers rather than replacing them, as deep understanding and coordination skills become even more valuable in an AI-augmented workflow.

- Anthropic engineers run 3–10 AI agents in parallel with no token limits, enabling high autonomy and rapid prototyping.
- Bun's 535K-line Zig-to-Rust rewrite was completed in 11 days using 64 parallel agents and $165K in tokens—previously estimated at a year for a small team.
- Complex projects like Claude Managed Agents still take six months and require traditional planning, PRDs, and architecture rework despite AI assistance.
- AI shifts engineering effort from implementation to verification: testing and code review become the bottlenecks and are increasingly automated by AI.
- Deep domain expertise and coordination skills are critical; AI makes senior engineers more productive but does not eliminate the need for human judgment.