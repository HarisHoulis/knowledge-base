---
domain: ai-workflows
subdomain: ai-native-engineering
concept: ai-native-development
title: Building an AI-Native Health Company: Planning, Code Review, and Reliability
sources:
  - title: "How to build an AI-Native Health Company — Dan Feng, Maven Clinic"
    url: "https://www.youtube.com/watch?v=WJRdLNhrsLQ"
    author: "AI Engineer"
    date: "2026-08-19T17:30:19+00:00"
---

# Building an AI-Native Health Company: Planning, Code Review, and Reliability

Dan Feng of Maven Clinic explains how AI shifts the costly part of software development from implementation to planning and arguing. Since building features now takes minutes, teams spend their effort aligning on requirements and trade-offs. Maven's planning therefore maintains only a one-year directional view and commits to two-to-four-week sprints; three-to-six-month plans are considered unplannable because model capabilities change too fast (source: Dan Feng, Maven Clinic, 2026).

Code review had to adapt to a tenfold increase in lines written per engineer. Maven now uses self-certification, where engineers decide which pull requests need a second reader, while capping PR size near 500 lines and stacking large features into smaller changes. The key failure mode is the rubber stamp—false confidence from a reviewer who doesn't truly review (source: Dan Feng, Maven Clinic, 2026).

Reliability is no longer a single bar but tiered by consequence. For example, a scheduling action failing once in 10,000 is acceptable because the user can retry, but reimbursement claims demand zero tolerance for errors—multiple models must agree on the same receipt before processing. Integration tests are run many times rather than once, since a single pass on a nondeterministic system proves little (source: Dan Feng, Maven Clinic, 2026).

- AI makes implementation cheap, so the bottleneck shifts to planning and argument; Maven uses one-year directions and 2-4 week sprints, abandoning 3-6 month plans.
- Code review scales via self-certification: engineers choose which PRs need review, PRs are capped near 500 lines, and large changes are stacked; rubber-stamping is the main anti-pattern.
- Reliability criteria are tiered: tolerable failures for reversible actions (e.g., scheduling retry) vs. zero tolerance for irreversible ones (e.g., claims), with multiple model agreement required for high-stakes decisions.
- Integration tests must be repeated because a single pass on nondeterministic AI systems is not evidence of reliability.