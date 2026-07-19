---
domain: ai-workflows
subdomain: context-engineering
concept: context-engineering
title: Context engineering with Dex Horthy
sources:
  - title: "Context engineering with Dex Horthy"
    url: "https://newsletter.pragmaticengineer.com/p/context-engineering-with-dex-horthy"
    author: "Gergely Orosz"
    date: "Wed, 15 Jul 2026 16:08:59 GMT"
---

# Context engineering with Dex Horthy

Dex Horthy, CEO of HumanLayer, coined the term 'context engineering' to describe the emerging discipline of working effectively within the limitations of LLM context windows. He emphasizes that the size of the context window does not equate to model intelligence; rather, the model's ability to use the provided context determines performance. A key heuristic is that using too much of the context window leads to a 'dumb zone' where the model makes increasingly poor decisions, such as deleting critical files. Horthy recommends keeping context usage to around 30-40% of the maximum window size for large models (e.g., 300-400K out of 1M) and stopping at ~100K for smaller models. He also introduces 'intentional compaction': taking a long, noisy context and compressing it into a Markdown document to start a fresh session, which improves focus and reduces errors. Ultimately, Horthy advocates for keeping humans in the loop, especially for design and architecture decisions, and using AI for implementation to achieve a 2-3x productivity gain (source: article).

- Context windows have a 'dumb zone': performance degrades once usage exceeds ~30-40% of the maximum, causing erratic model behavior.
- Frequent, intentional compaction of context (e.g., into Markdown summaries) resets the session and keeps the model in its 'smart zone'.
- Human oversight remains critical: Horthy found that shipping unread AI-generated code leads to disaster within months, and that human review of architecture and design is essential.
- Loop engineering, such as nightly automated PRs for code quality fixes, can increase productivity by 30-50% without sacrificing quality when reviewed.
- The most effective strategy is to 'find leverage': invest human time in planning and design, then let AI generate code without reviewing every line, achieving 2-3x faster development.