---
domain: ai-workflows
subdomain: coding-agents
concept: ai-rewrite-maintenance-gap
title: AI Rust Rewrites of curl vs. Real Maintenance
sources:
  - title: "Quoting Daniel Stenberg"
    url: "https://simonwillison.net/2026/Nov/18/daniel-stenberg/"
    author: "Simon Willison"
    date: "2026-11-18"
---

# AI Rust Rewrites of curl vs. Real Maintenance

Daniel Stenberg reports that while AI agents converted 185,000 lines of C into 340,000 lines of Rust during a roughly three-week period, the actual curl project merged over 300 commits in the same window, including more than 200 bugfixes and several vulnerability fixes. In the following month, another 200 fixes landed.

His point is that the generated rewrites capture a snapshot of the code but not the ongoing maintenance work—bugfixes and security patches—that the real project accumulates. He closes with an open question: will these clones keep up with that continuous stream of fixes?

- AI agents produced 185k lines of C to 340k lines of Rust in about three weeks
- Real curl merged 300+ commits including 200+ bugfixes and vulnerability fixes in the same period
- Another ~200 fixes followed in the next month
- Generated rewrites may not keep pace with ongoing bugfix and security maintenance