---
domain: ai-workflows
subdomain: multi-agent-systems
concept: subagents-as-distributed-systems
title: Your Sub-Agents Are a Distributed System. Treat Them Like One.
sources:
  - title: "Your Sub-Agents Are a Distributed System. Treat Them Like One. - Girish Konda, Microsoft"
    url: "https://www.youtube.com/watch?v=DxP5aW4VknQ"
    author: "AI Engineer"
    date: "2026-11-10"
---

# Your Sub-Agents Are a Distributed System. Treat Them Like One.

Girish Konda (Microsoft) argues that multi-agent architectures—an orchestrator delegating work to parallel sub-agents that share state and call real tools—are structurally identical to classic distributed systems, yet are typically built with a naive string-in/string-out interface that hides all the failure modes distributed-systems engineers have studied for decades. The orchestrator, performers, shared mutable state, and merged parallel results map directly onto known distributed-system patterns.

He catalogs the recurring failures: partial failure, where a sub-agent returns text that looks like success but isn't; dirty reads, where agents read shared context containing work others only assumed was done; unbounded fan-out, where the orchestrator spawns more agents instead of honoring backpressure like 429/503 responses; and non-idempotent retries that re-execute the whole task including side effects. He also highlights the Byzantine-style case where a sub-agent returns normal-looking output with no evidence of how much work actually happened, making it indistinguishable from genuine success.

For the no-response case, he cites the FLP result (1985) showing consensus is impossible in a fully asynchronous system with even one faulty process, and Chandra and Toueg's 1996 unreliable failure detectors as the practical answer: treat timeouts as suspicion, not proof. He draws on his MCP Pacemaker project, where a slow-loading server was wrongly marked dead (fixed with a separate init timeout) and a crashed server's timeout masked the real exit code (fixed by recording timeouts only while live).

His prescription is to make rejection a first-class value: sub-agents should return status, what was done and not done, evidence, and side effects, with "partly" as a normal outcome—something protocols like A2A already accommodate via task states.

- Multi-agent orchestrator/sub-agent topologies are distributed systems and inherit their failure modes (partial failure, dirty reads, unbounded fan-out, non-idempotent retries).
- A sub-agent that fails often returns success-shaped text, so the orchestrator cannot distinguish real work from a plausible-looking answer.
- Timeouts are suspicion, not proof of failure—record them as unknown and preserve the real cause (e.g., crash exit codes).
- Make rejection a value: return status, evidence, and side effects, and treat partial completion as a normal outcome.