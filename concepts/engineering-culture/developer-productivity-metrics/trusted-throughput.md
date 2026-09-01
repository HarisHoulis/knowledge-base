---
domain: engineering-culture
subdomain: developer-productivity-metrics
concept: trusted-throughput
title: From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad
sources:
  - title: "From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad"
    url: "https://www.youtube.com/watch?v=dSg0pu8d6qg"
    author: "AI Engineer"
    date: "2026-08-29T15:30:28+00:00"
---

# From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad

Mingsheng Hong warns against turning AI token dashboards into leaderboards. At Ironclad, dashboards are treated as smoke detectors rather than competitions; a team using surprisingly few tokens is worth a conversation, while rewarding those who burn more encourages waste. He draws a parallel to lines of code—a metric worth tracking but dangerous to optimize, especially since deleting code is often the better outcome (Mingsheng Hong, Ironclad).

Ironclad's value metric evolved over time: from lines of code to open pull requests, then merged pull requests, and finally merged pull requests weighted by a complexity score, because a ten-line concurrency fix is worth more than a thousand lines of boilerplate. The goal is 'trusted throughput': work that clears objective checks, human review, and contact with customers. Hong argues that cutting cost before measuring value is premature, since cost is only one side of a ratio (Mingsheng Hong, Ironclad).

The bottleneck has moved downstream to review and CI. Slow pipelines quietly push engineers toward large batched pull requests that are harder to review well. The fixes are unglamorous: kill flaky tests, cap agent retry loops, and measure the wait from ready to merged (Mingsheng Hong, Ironclad).

- Token dashboards should be smoke detectors, not leaderboards; unusual usage patterns prompt conversations, while optimizing raw usage encourages waste.
- Cost metrics must be paired with value metrics; otherwise cutting cost is premature.
- Ironclad's throughput metric evolved to merged pull requests weighted by complexity, emphasizing trusted work over raw volume.
- Trusted throughput = work passing automated checks, human review, and customer contact.
- Slow review and CI are the real bottleneck; fixing flaky tests and capping agent retries improves wait times and review quality.