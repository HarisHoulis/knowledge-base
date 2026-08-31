---
domain: engineering-culture
subdomain: software-performance
concept: performance-aware-engineering
title: Why Performant Code Matters (But Gets Widely Ignored), with Casey Muratori
sources:
  - title: "Why performant code matters (but gets widely ignored), with Casey Muratori"
    url: "https://newsletter.pragmaticengineer.com/p/why-performant-code-matters-but-gets"
    author: "Gergely Orosz"
    date: "Wed, 26 Aug 2026 15:59:59 GMT"
---

# Why Performant Code Matters (But Gets Widely Ignored), with Casey Muratori

In this episode, Casey Muratori discusses why software performance is often overlooked despite strong evidence that it matters to business outcomes. He points to products like File Pilot and Blick gaining popularity due to performance, and argues that the industry's default indifference to performance is a cultural problem rather than a technical one (Orosz, 2026). Muratori also shares history, such as how DirectX emerged from an unauthorized Microsoft project called WinG, showing that performance-focused work can succeed even without official approval.

Muratori challenges common practices like profiler-driven optimization and the adage that 'premature optimization is the root of all evil.' He advocates for understanding the theoretical limits of hardware and designing systems with performance in mind from the start, rather than only patching hotspots. He also explains that reading assembly, along with understanding three key aspects of CPUs—data movement, instruction flow, and execution unit scheduling—can help developers reason about performance more effectively.

The conversation also covers game industry evolution, the impact of licensable engines, and why Muratori is skeptical of 'clean code' and test-driven development. He emphasizes that received wisdom should be tested in practice, and that tests should be a cost/benefit decision, not a default. He also explains why he avoids AI in his own game development: he wants to program things himself, not just produce output (Orosz, 2026).

- Performance is critical to business success but widely ignored; some newer products are winning on speed.
- Profiler-driven optimization only finds local minima; effective optimization starts from knowing hardware's theoretical limits.
- Learning to read assembly (about 20-30 instructions) and understanding three CPU pillars helps developers design performant systems.
- The 'premature optimization' warning is overused; architectural performance choices must be made early to avoid rewrites.
- Casey critiques clean code and TDD as unproven received wisdom, advocating for practical, cost/benefit-driven testing.