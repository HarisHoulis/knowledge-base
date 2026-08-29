---
domain: engineering-culture
subdomain: developer-productivity
concept: trusted-throughput
title: From Tokenmaxxing to Trusted Throughput
sources:
  - title: "From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad"
    url: "https://www.youtube.com/watch?v=dSg0pu8d6qg"
    author: "AI Engineer"
    date: "2026-08-29T15:30:28+00:00"
---

# From Tokenmaxxing to Trusted Throughput

Token usage dashboards can easily turn into leaderboards, which backfire by rewarding consumption rather than value. Mingsheng Hong describes how his team runs the same dashboards but treats them as smoke detectors: unexpectedly low token usage triggers a conversation, and nobody is rewarded for burning more. He draws a parallel to lines of code—a metric worth tracking but terrible to optimize, since deleting code is often the better outcome (0:00–2:56).

Ironclad's approach is to measure value alongside cost, because cutting cost before understanding value is premature. The team's metric evolved from lines of code to open pull requests, then merged pull requests, and finally merged pull requests weighted by complexity—a ten-line concurrency fix should count more than a thousand lines of boilerplate. Hong calls the goal 'trusted throughput': work that passes objective checks, human review, and contact with customers (5:44–12:43).

The real bottleneck has shifted downstream to review and CI. Slow pipelines push engineers toward giant, batched pull requests that are harder to review well. His fixes are unglamorous: kill flaky tests, cap agent retry loops, and measure the wait from ready to merged (14:06–18:19).

- Dashboards should be smoke detectors, not leaderboards: high token usage is not a win, and surprisingly low usage deserves a conversation.
- Don't optimize cost before measuring value; focus on trusted throughput, not raw token burn.
- Merged pull requests weighted by complexity are a better productivity metric than lines of code or open PRs.
- Review and CI are the bottleneck; improve them by killing flaky tests, capping agent retries, and tracking time from ready to merged.