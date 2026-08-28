---
domain: engineering-culture
subdomain: software-performance-culture
concept: performance-aware-development
title: Why performant code matters (but gets widely ignored), with Casey Muratori
sources:
  - title: "Why performant code matters (but gets widely ignored), with Casey Muratori"
    url: "https://newsletter.pragmaticengineer.com/p/why-performant-code-matters-but-gets"
    author: "Gergely Orosz"
    date: "2026-08-26"
---

# Why performant code matters (but gets widely ignored), with Casey Muratori

In this podcast episode, Casey Muratori argues that software performance is critical but widely overlooked in the industry. He cites evidence from leading companies and debunks common excuses, noting that enterprise buyers tend to prioritize cost, compliance, and capabilities over performance. Still, some fast products like File Pilot and Blick are gaining traction, suggesting a possible shift (Orosz, 2026).

- Profiler-driven optimization only finds local minima; great optimizers first establish theoretical hardware limits and then close the gap.
- Developers should learn to read assembly (about 20-30 instructions) and understand CPU fundamentals: data movement, instruction flow, and execution scheduling.
- Architecting for performance from the start is essential; deferring optimization can leave only hotspots fixable, not architectural issues.
- Received programming wisdom like 'premature optimization is the root of all evil' should be tested; Casey also critiques clean code and TDD as default practices.
- Casey avoids AI-assisted coding because he wants to program things himself, just as some prefer handmade furniture over flatpack.