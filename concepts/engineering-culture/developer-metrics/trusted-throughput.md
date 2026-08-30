---
domain: engineering-culture
subdomain: developer-metrics
concept: trusted-throughput
title: Measuring Trusted Throughput Instead of Token Usage
sources:
  - title: "From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad"
    url: "https://www.youtube.com/watch?v=dSg0pu8d6qg"
    author: "AI Engineer"
    date: "2026-08-29T15:30:28+00:00"
---

# Measuring Trusted Throughput Instead of Token Usage

Token usage dashboards can become de facto leaderboards, but Mingsheng Hong argues they should be treated as smoke detectors rather than competition. At Ironclad, dashboards are used to surface anomalies—like a team using unexpectedly few tokens—and nobody is rewarded for burning more. He draws a parallel to lines of code: a number worth tracking, but terrible to optimize, since deleting code is often the better outcome.

Ironclad's productivity metric evolved from lines of code to open pull requests, then merged pull requests, and finally merged pull requests weighted by a complexity score. The goal is “trusted throughput”: work that clears objective checks, human review, and eventually contact with customers. Cutting cost first is premature; one must measure value simultaneously, treating cost as one side of a ratio.

As the bottleneck shifts downstream to code review and CI, slow pipelines push engineers toward large, batched pull requests that are harder to review. The fixes are pragmatic: kill flaky tests, cap agent retry loops, and measure the wait time from ready to merge.

- Token dashboards should act as smoke detectors, not leaderboards; low usage is worth investigating, high usage is not rewarded.
- Avoid optimizing token cost in isolation; measure value alongside cost, as part of a ratio.
- Trusted throughput is measured by merged pull requests weighted by complexity, not raw lines of code or open PRs.
- Address review and CI bottlenecks—such as flaky tests and agent retry loops—to reduce the ready-to-merge wait time.