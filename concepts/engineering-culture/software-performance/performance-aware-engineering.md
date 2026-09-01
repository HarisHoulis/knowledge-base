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

In this podcast episode, Gergely Orosz interviews Casey Muratori about why software performance is critical yet widely overlooked in the industry. Muratori argues that performance directly impacts business bottom lines, citing evidence from leading software companies, but the prevailing attitude remains dismissive. He suggests that performance should be considered during system design, not bolted on later, and that profiler-driven optimization often finds only local minima. Instead, engineers should start by understanding the theoretical limits of hardware and work to close the gap to that level. (Orosz, 2026)

- Performance matters to business outcomes, yet is frequently ignored; evidence from top companies is often undisputed but does not change industry habits.
- Profiler-driven optimization only finds local minima; instead, understand what the hardware can theoretically do and optimize toward that ceiling.
- Learn to read basic assembly (20-30 instructions) and understand how CPUs move data, flow instructions, and schedule execution to make better performance decisions.
- Beware of using 'premature optimization is the root of all evil' as an excuse; consider performance during design to avoid costly rewrites later.
- Great engineers test received wisdom and focus on what actually works in practice, not dogma.