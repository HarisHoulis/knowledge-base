---
domain: engineering-culture
subdomain: performance-engineering
concept: performance-aware-development
title: Why performant code matters (but gets widely ignored), with Casey Muratori
sources:
  - title: "Why performant code matters (but gets widely ignored), with Casey Muratori"
    url: "https://newsletter.pragmaticengineer.com/p/why-performant-code-matters-but-gets"
    author: "Gergely Orosz"
    date: "2026-08-26"
---

# Why performant code matters (but gets widely ignored), with Casey Muratori

In this podcast episode, Casey Muratori argues that software performance is critically important to business success yet is widely ignored in the industry. He points to evidence from leading software companies and debunks common excuses for deprioritizing performance, emphasizing that architectural decisions made early determine whether performance problems can be fixed later [1]. Muratori believes that performance should be considered during design, not bolted on after profiling, and that waiting too long means only hotspots can be addressed while fundamental design issues remain [1].

Muratori recommends that developers learn to read assembly (not necessarily write it) and understand three key aspects of CPUs: how data moves via load/store units and caches, how instructions flow through branch prediction and instruction caches, and how execution units schedule raw throughput. This knowledge allows engineers to estimate what hardware can theoretically do, which he says is the starting point for great optimizers. He criticizes profiler-driven optimization as finding only local minima, and instead suggests using 'napkin math' to establish performance goals upfront [1].

Muratori also challenges conventional wisdom such as 'premature optimization is the root of all evil,' arguing it is often used as an excuse to delay necessary performance design. He critiques 'clean code' when it harms performance and takes a pragmatic view of test-driven development, noting that tests should be a cost/benefit decision rather than a default. He admires engineers who refuse to accept received programming wisdom without testing it in practice [1].

Finally, Muratori reflects on the game industry, where licensable engines democratized development but flooded the market, making organic discovery nearly impossible. He also explains why he avoids AI coding tools in his own work, preferring to handcraft code for the enjoyment and control it provides. His stance is that focusing on what actually works in practice, rather than following mainstream trends, is a hallmark of great engineering [1].

- Performance should be considered during software design, not added later via profiling; architecting for performance avoids costly rewrites.
- Learn to read assembly and understand CPU fundamentals—data movement, instruction flow, and execution scheduling—to reason about theoretical hardware limits.
- Profiler-driven optimization only finds local minima; top optimizers first establish the hardware's theoretical ceiling and work to close the gap.
- Conventional wisdom like 'premature optimization is the root of all evil' is often misused to postpone necessary performance work; test received wisdom in practice.
- Tests should be a cost/benefit decision, not a default; great engineers focus on what actually works in the real world.