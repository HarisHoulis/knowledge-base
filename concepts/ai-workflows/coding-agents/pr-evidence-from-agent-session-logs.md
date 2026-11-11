---
domain: ai-workflows
subdomain: coding-agents
concept: pr-evidence-from-agent-session-logs
title: Your PR Says the Tests Passed. Prove It.
sources:
  - title: "Your PR Says the Tests Passed. Prove It. - Stephen Chin & Cassandra Chin"
    url: "https://www.youtube.com/watch?v=gbeuC0ud1p4"
    author: "AI Engineer"
    date: "2026-11-10"
---

# Your PR Says the Tests Passed. Prove It.

Stephen and Cassandra Chin present Trace Tune, a framework Cassandra created to improve pull requests (PRs) produced with AI coding agents. They observe that many PRs are rejected not because the code is bad but because the PRs contain incorrect information or are poorly written, and they aim to fix that by grounding PR descriptions in verifiable evidence rather than agent self-reporting.

The core problem is that when an agent writes a PR from within a single session, it reads its own session log and relies on an expanded context window to reconstruct what it did. As the context window shrinks, that reconstruction becomes increasingly inaccurate over time. Trace Tune instead reads across different sessions on the computer to understand what was actually created and what happened, so the PR can cite accurate URL preview links, command attribution, and prior work.

The approach builds on Cassandra's earlier Showtale project for education, which addressed the problem that students' AI-generated programs were submitted without any record of the work behind them—the clues and process that led to the final artifact. The same audit-log theory applies to PRs: capturing evidence such as directory changes before running commands or the working directory before a cd makes the claimed results checkable. Cassandra also used Trace Tune on itself while building it, iterating on its own PRs, and added an optional comic to explain PRs in a fun way.

- Many PRs are rejected for incorrect or poorly written information rather than bad code.
- Agents writing PRs from a single session rely on a shrinking context window, making their accounts increasingly inaccurate.
- Trace Tune reads across multiple sessions to reconstruct what actually happened and attach evidence to the PR.
- The approach extends the Showtale idea of auditing AI-assisted work by capturing process evidence, not just the final artifact.