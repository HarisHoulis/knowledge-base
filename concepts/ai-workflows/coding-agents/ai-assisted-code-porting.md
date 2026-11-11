---
domain: ai-workflows
subdomain: coding-agents
concept: ai-assisted-code-porting
title: How GitHub Used AI to Port Copilot From TypeScript to Rust in Record Time
sources:
  - title: "How GitHub Used AI to Port Copilot From TypeScript to Rust in Record Time"
    url: "https://blog.bytebytego.com/p/how-github-used-ai-to-port-copilot"
    author: "ByteByteGo"
    date: "2026-11-10"
---

# How GitHub Used AI to Port Copilot From TypeScript to Rust in Record Time

GitHub ported the Copilot agent runtime from TypeScript to Rust, moving roughly 430K lines of production TypeScript through the migration, largely using the GitHub Copilot app, Copilot CLI, and AI agents. The port was motivated by the original TypeScript/Node runtime's costs: each client bore about 100 MB of memory overhead, required launching a separate background process, and forced non-JS applications to carry Node and V8 machinery. Rust offered low overhead and predictable resource usage, and a standalone runtime library could be loaded directly into host applications.

The team used an incremental, in-place porting strategy rather than a big-bang rewrite. Each component's TypeScript implementation was replaced with Rust in a single pull request, with temporary thin wrappers bridging remaining TypeScript callers, and the old implementation deleted in the same change. Work started with small, independent helpers with strong test suites, then moved to stateful components, tools, and model clients, leaving session orchestration for the end. Existing end-to-end tests served as the reference for expected behavior, and changes failing tests were not merged.

Agent fleets divided the work: subagents investigated code within a parent session, while child sessions with their own branches made independent changes. For example, a coordinating agent analyzed the ~30K-line session.ts file for an hour, then split the work across 15 child sessions. Running many agents concurrently overwhelmed the developer's laptop, so child agents skipped expensive builds and tests, which were serialized through a separate build-access session. Review used a reusable "rust-rebase-review" instruction: rebasing onto main, checking that new TypeScript changes were also ported, and having multiple review agents with different models compare old and new code line by line, iterating until reviews were clean, with humans focusing on architecture and interface contracts.

Regressions included subtle behavior changes (whole numbers becoming decimals, empty-string, time-zone, and error-handling differences), state-management and cancellation bugs, and integration issues like long work on Node's main thread and unwanted console windows on Windows. Performance improved substantially: a client create/turn/cleanup trial dropped from 5.25 seconds to 292 milliseconds (~18x), throughput rose from 7.55 to 120 completed session lifecycles per second, and peak private memory in a 10-client test fell from 1383 MB to 126 MB. The port cost around $120K in AI token costs across roughly 136 billion tokens, mostly cached input, plus developer time. A key learning was that clear, explicit instructions were critical, since early requests led agents to translate only central logic and leave surrounding work in TypeScript.

- Incremental in-place porting with per-component PRs and temporary TypeScript-to-Rust wrappers kept risk low and let feature development continue during migration.
- Agent fleets split work via subagents and branch-isolated child sessions; build/test contention forced serializing expensive operations through a dedicated session.
- Multi-model review agents compared TypeScript and Rust line by line, iterating until clean, while humans reviewed architecture and interface contracts.
- Performance gains were large: ~18x faster client lifecycle, throughput from 7.55 to 120 session lifecycles/sec, and peak memory down from 1383 MB to 126 MB in a 10-client test.
- The port cost about $120K in tokens (~136B, mostly cached input) plus developer time; precise instructions were essential to avoid partial translations.