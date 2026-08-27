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

In an interview with Gergely Orosz on The Pragmatic Engineer, Casey Muratori argues that software performance is critical to business outcomes yet widely ignored by the industry. He points to evidence from leading software companies and notes that while few rebut the importance of performance, prevailing attitudes remain dismissive. Muratori calls for considering performance during design, rather than treating it as an afterthought (Orosz, 2026).

Muratori critiques common optimization practices: profiler-driven optimization only finds local minima; engineers should instead establish the theoretical hardware ceiling and work to close the gap. He recommends learning to read assembly, focusing on about 20-30 instructions, and understanding three CPU pillars: data movement, instruction flow, and execution unit scheduling. He also pushes back on the adage that premature optimization is the root of all evil, saying delayed optimization can leave only hotspots fixable, not architectural issues (Orosz, 2026).

Muratori extends his critique to 'clean code' and TDD, viewing them as received wisdom not empirically validated. He believes testing should be a cost/benefit decision, not a default. In the games context, he notes that licensable engines democratized creation but flooded the market, breaking discovery, and that older games now compete visually with new ones. He prefers hand-writing code over using AI because he wants to program, not merely produce output (Orosz, 2026).

- Performance is often ignored despite strong evidence it matters; developers should design for performance from the start.
- Profiler-driven optimization finds local minima; instead, know the theoretical hardware limits and close the gap.
- Learn to read assembly and understand CPU fundamentals: data movement, instruction flow, and execution unit scheduling.
- Be skeptical of received wisdom like 'premature optimization is the root of all evil' and TDD; test based on cost/benefit.
- The games industry shows how tool democratization can flood markets and hurt discovery; performance can be a differentiator.