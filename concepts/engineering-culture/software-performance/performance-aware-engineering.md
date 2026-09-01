---
domain: engineering-culture
subdomain: software-performance
concept: performance-aware-engineering
title: Why performant code matters (but gets widely ignored), with Casey Muratori
sources:
  - title: "Why performant code matters (but gets widely ignored), with Casey Muratori"
    url: "https://newsletter.pragmaticengineer.com/p/why-performant-code-matters-but-gets"
    author: "Gergely Orosz"
    date: "Wed, 26 Aug 2026 15:59:59 GMT"
---

# Why performant code matters (but gets widely ignored), with Casey Muratori

In this episode of The Pragmatic Engineer, Gergely Orosz talks with Casey Muratori about why software performance is critical yet widely ignored in the industry. Muratori points out that despite overwhelming evidence from leading software companies showing performance impacts business outcomes, many developers dismiss it. He argues that the common approach of profiling and tweaking hotspots only finds local minima; instead, engineers should first establish what the hardware can theoretically do and then close the gap to that level (The Pragmatic Engineer, "Why performant code matters...").

- Performance optimization should start with understanding the theoretical hardware ceiling, not with profiling hotspots.
- Learning to read assembly (about 20-30 instructions) is a key skill for writing performant code.
- The conventional wisdom that "premature optimization is the root of all evil" is often misused to delay architectural decisions that hurt performance.
- Understanding how CPUs work boils down to three pillars: data movement (load/store, caches), instruction flow (branch prediction, i-cache), and execution unit scheduling.
- Test-driven development should be a cost/benefit decision, not a default practice; great engineers question received wisdom and test it in the real world.