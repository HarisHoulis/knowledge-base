---
domain: engineering-culture
subdomain: ai-transformation
concept: agentic-software-development
title: The State of the Tech Industry in 2026
sources:
  - title: "The state of the tech industry in 2026"
    url: "https://newsletter.pragmaticengineer.com/p/the-state-of-the-tech-industry-in"
    author: "Gergely Orosz"
    date: "2026-10-06"
---

# The State of the Tech Industry in 2026

Gergely Orosz's keynote at the LDX3 engineering leadership conference presents a snapshot of the tech industry in late 2026, arguing that AI has caused change at a scale and pace without precedent. Industry veteran Martin Fowler is quoted saying "Nothing has hit with the magnitude of AI," noting that unlike prior shifts such as object-oriented languages, the internet, or agile, there is no argument about AI's importance (Orosz 2026).

A central change is that practically nobody writes code by hand anymore, and highly productive engineers now run 5-10 parallel agents. Claude Code creator Boris Cherny described running five terminal tabs plus 5-10 Claudes on Claude Web, while Cockroach Labs cofounder Peter Mattis and Linear engineer Dima Zaytsev reported similar parallel-agent workflows. GitHub data shared with Orosz shows more agent-authored PRs than human-authored ones in August 2026, with roughly 75M+ AI-generated PRs per month versus 25M human PRs in December 2023 (Orosz 2026).

The IDE is fading as the primary interface. Steve Yegge argues "AI-pilled" engineers will abandon the IDE, and market data backs this: Antigravity 2.0 moved away from the IDE concept, Codex launched as a non-IDE, Cursor relaunched without its IDE interface, and JetBrains is pivoting to agentic development environments. Orosz suggests the IDE is evolving into a conversation, monitoring, and validation interface rather than an editor. Meanwhile, most mid-sized-and-above companies have built their own agent harnesses, and development increasingly kicks off inside Slack via agents like @Codex, @Claude, and @Linear (Orosz 2026).

AI is also compressing migration timelines dramatically: Anthropic migrated Bun from Zig to Rust in 11 days, OpenAI is migrating its API layer from Python to Rust in about 5 months, Airbnb migrated 3,500 test files in 6 weeks, Asana migrated 4,000 test files in 2 weeks, and Uber migrated 600,000 JUnit 4 tests across 15 million lines of code in 4 months. Orosz also notes what remains unchanged—teams and planning still matter, and non-engineers still are not shipping code—and flags concerns that code reviews have become theatrical and quality and reliability are down (Orosz 2026).

- Most engineers have stopped writing code by hand, and highly productive engineers now run 5-10 parallel agents, according to multiple sources including Boris Cherny, Peter Mattis, and Dima Zaytsev.
- GitHub data shows more agent-authored PRs than human-authored ones in August 2026, with roughly 75M+ AI-generated PRs per month.
- The IDE is fading: Antigravity 2.0, Codex, Cursor, and JetBrains are all pivoting away from the traditional IDE toward agentic interfaces.
- Most mid-sized-and-above companies have built their own agent harnesses, and development increasingly starts in Slack via agents like @Codex, @Claude, and @Linear.
- AI has compressed migrations from years to weeks or months, including Bun's Zig-to-Rust rewrite in 11 days and Uber's 600,000-test JUnit migration in 4 months.