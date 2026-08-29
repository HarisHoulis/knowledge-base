---
domain: engineering-culture
subdomain: performance-engineering
concept: performance-matters
title: Why performant code matters (but gets widely ignored), with Casey Muratori
sources:
  - title: "Why performant code matters (but gets widely ignored), with Casey Muratori"
    url: "https://newsletter.pragmaticengineer.com/p/why-performant-code-matters-but-gets"
    author: "Gergely Orosz"
    date: "Wed, 26 Aug 2026 15:59:59 GMT"
---

# Why performant code matters (but gets widely ignored), with Casey Muratori

In this episode, Casey Muratori, creator of Handmade Hero and performance advocate, discusses why software performance is often overlooked despite strong evidence of its importance. He notes that enterprise buyers focus on cost, compliance, and capabilities, not performance, yet some products like File Pilot and Blick are gaining traction by prioritizing speed. The conversation highlights the need to shift engineering culture toward performance awareness (Orosz, 2026).

Muratori argues that profiler-driven optimization only finds local minima; instead, engineers should understand the theoretical limits of hardware and close the gap to that performance level. He recommends learning to read assembly (roughly 20-30 instructions) and understanding three key CPU pillars: how data moves through caches, how instructions flow through pipes, and execution unit scheduling. He also warns against the overused adage that 'premature optimization is the root of all evil,' explaining that it often delays architectural decisions that are costly to fix later (Orosz, 2026).

The episode also covers game development history, including DirectX's roots in the unauthorized WinG project, and the impact of licensable engines like Unity and Unreal flooding the market. Muratori critiques clean code and TDD, advocating for a cost/benefit approach to testing rather than dogmatic defaults. He also explains why he avoids AI in his work, preferring to program manually for the sake of programming itself (Orosz, 2026).

- Performance is undervalued in most software engineering, but a few products show it can be a competitive advantage.
- Profiler-driven optimization finds local minima; instead, establish the hardware's theoretical peak and close the gap.
- Learning to read assembly and understanding CPU fundamentals (caches, instruction flow, execution units) empowers performance-aware development.
- Doubting received wisdom like 'premature optimization is the root of all evil' is essential; design for performance early to avoid rewrites.
- TDD should be a cost/benefit decision, not a universal default.
- Licensable game engines democratized game creation but destroyed organic discovery due to market flooding.