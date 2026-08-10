---
domain: ai-workflows
subdomain: codex-harness
concept: codex-harness-architecture
title: Codex, Behind the Harness — Dominik Kundel
sources:
  - title: "Codex, Behind the Harness — Dominik Kundel"
    url: "https://www.youtube.com/watch?v=shRR1e2HXMk"
    author: "AI Engineer"
    date: "2026-08-07T06:14:03+00:00"
---

# Codex, Behind the Harness — Dominik Kundel

The talk explains how OpenAI's Codex harness evolved once inference stopped being the bottleneck. With GPT 5.3 Codex Spark serving a thousand tokens per second on Cerebras, network latency became critical, leading to websocket mode: a persistent connection with stateful context that sends only tool call results rather than resending full context. Context construction balances size, flexibility, and cachability: tools can be marked deferred to avoid entering the context window and instead surface via tool search; the available skills list is capped at 2% of the context window with descriptions trimmed beyond that.

- Websocket mode replaces HTTP SSE to reduce network overhead in high-token-throughput scenarios.
- Deferred tools and a capped skills list manage context window size and flexibility.
- File edits use an apply-patch tool; the shell runs inside a sandbox (seatbelt, bubblewrap, custom Windows sandbox).
- Approval fatigue is addressed with an auto-review subagent that has read-only permissions and no spawning ability.
- Long-horizon goals use continuation prompts and an update-goal tool; concrete verifiable objectives are preferred.