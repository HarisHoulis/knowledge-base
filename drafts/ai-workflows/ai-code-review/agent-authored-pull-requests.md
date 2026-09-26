---
domain: ai-workflows
subdomain: ai-code-review
concept: agent-authored-pull-requests
title: AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile
sources:
  - title: "AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile"
    url: "https://www.youtube.com/watch?v=474j-n1Ltxc"
    author: "AI Engineer"
    date: "2026-09-25"
---

# AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile

Greptile co-founder Daksh Gupta analyzed more than a million pull requests a month from companies including NVIDIA, Coinbase and Scale to test whether fully vibe-coded PRs hold up in enterprise codebases (Daksh Gupta, Greptile talk). Detection relied on signals like author fields, co-author footers and branch prefixes. More than a quarter of the PRs Greptile reviewed in April showed signs of being written largely or entirely by AI agents, up from under 1% a year earlier.

Gupta compared agent-written PRs from Codex, Claude Code, Devin and Cursor against human-written ones on four measures: revert rates, revert rates by PR size, the severity of issues Greptile flags (P0/P1/P2), and the number of review rounds needed to reach a mergeable PR. On all four, agent code landed in the same range as human code — and humans were actually more likely to introduce P0 bugs.

The differences appear in how each fails rather than how often. Claude is about 1.5x more likely than humans to introduce SQL injection, Devin is half as likely to cause auth bypasses, and N+1 queries are far more common from Cursor.

Gupta argues this changes code review needs: the median Greptile user makes fewer than 50 commits a month, while the 99th percentile makes close to 1,000, making manual review impossible at that scale. He proposes validation answer three questions — does the change violate the user contract, does it make a future violation more likely, and does it do what the author intended — which Greptile addresses with blast-radius analysis and sandboxed browser agents that try to break the app.

- More than 25% of PRs Greptile reviewed in April showed signs of being largely or entirely AI-written, up from under 1% a year earlier.
- Agent-written PRs from Codex, Claude Code, Devin and Cursor matched human PRs on revert rates, revert rates by size, issue severity and review rounds to merge; humans were more likely to introduce P0 bugs.
- Failure modes differ by tool: Claude ~1.5x more likely than humans to introduce SQL injection, Devin half as likely to cause auth bypasses, and Cursor far more likely to produce N+1 queries.
- At scale — median users under 50 commits/month, 99th percentile near 1,000 — manual review is infeasible; Gupta frames validation around user-contract violations, future-violation risk and author intent.
- Greptile implements this with blast-radius analysis and sandboxed browser agents that attempt to break the application.