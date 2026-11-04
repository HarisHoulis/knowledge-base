---
domain: ai-workflows
subdomain: ai-agents
concept: agentic-performance-profiling
title: How Netflix Uses AI Agents for Performance Engineering
sources:
  - title: "How Netflix Uses AI Agents for Performance Engineering"
    url: "https://blog.bytebytego.com/p/how-netflix-uses-ai-agents-for-performance"
    author: "ByteByteGo"
    date: "2026-11-03"
---

# How Netflix Uses AI Agents for Performance Engineering

Netflix built an autonomous performance agent system to address the tension between AI-accelerated code generation and the subtle performance regressions that fast-shipped code introduces. Traditional performance engineering was a slow, manual loop—triggering profilers, downloading flame graphs, hunting cryptic method names, and patching—that depended on a few domain experts and only scaled to major incidents, leaving steady resource drains unnoticed (ByteByteGo).

The core insight is that LLMs can read raw profiling data because profilers across languages (JVM async-profiler, Python py-spy, Go pprof) share a common structure of call stacks with inclusive and self CPU time, so a single analytical pipeline can understand almost any runtime. LLMs also already know classic anti-patterns like quadratic loops, loop invariants, excessive allocation, and N+1 queries, so the agent can pattern-match known bugs against actual call stacks rather than guessing. Netflix wraps the LLM in a scoped pipeline that uses strict package-prefix rules to ignore platform noise like GC pauses and kernel syscalls.

In production the agent found four bug categories: an O(N^2) immutable-map reduction wasting 8.8% CPU, a per-request regex consuming 46% CPU (fixed with a lookup table, 22x faster), redundant HashSet allocation driving 47% of heap collections, and metric-registry lookups consuming 66% CPU versus 0.3% for business logic. Safety relies on a standard SDLC: tests must pass, a canary runs side-by-side with a baseline, hard telemetry is collected without AI judgment, and a human reviews the final PR.

Because production profiling pays for wasted compute before finding bugs, Netflix shifted left into CI/CD and local development, and built a Git-based Pattern Catalog to give stateless LLMs persistent, shared memory of known anti-patterns across teams.

- LLMs can interpret raw profile data across runtimes because profilers share call-stack structure with inclusive and self CPU time
- Scoping the agent with package-prefix rules prevents it from wasting reasoning on GC, kernel, and framework noise
- Production findings included an 8.8% CPU quadratic reduction, a 46% CPU regex (22x speedup via lookup table), 47% heap churn from redundant allocation, and 66% CPU metric lookups
- Verification uses tests, side-by-side canary telemetry, and human-reviewed PRs rather than trusting the agent
- A Git-based Pattern Catalog gives stateless LLMs shared persistent memory and shifts checks left into CI/CD