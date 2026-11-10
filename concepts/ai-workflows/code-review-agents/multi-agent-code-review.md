---
domain: ai-workflows
subdomain: code-review-agents
concept: multi-agent-code-review
title: How LinkedIn Uses AI to Review 40,000 Pull Requests a Week
sources:
  - title: "How LinkedIn Uses AI to Review 40,000 Pull Requests a Week"
    url: "https://blog.bytebytego.com/p/how-linkedin-uses-ai-to-review-40000"
    author: "ByteByteGo"
    date: "2026-11-09"
---

# How LinkedIn Uses AI to Review 40,000 Pull Requests a Week

LinkedIn operates over 10,000 active repositories with tens of thousands of PRs opened weekly, and as coding agents accelerate code writing, review has become the bottleneck. To address this, LinkedIn built an in-house AI reviewer that covers more than 40,000 PRs a week, posting most reviews before a human opens the PR. The article, based on interviews with Min Chen and Balaji Srinivasan, describes the design and tradeoffs of that system.

The piece frames AI review as partial automation: AI gives the first pass while humans retain approval, since full automation (AI approving changes) remains difficult. A reliable reviewer must be grounded (flags real problems), high-signal (real bugs, not style nits), codebase-aware (follows conventions), and timely. LinkedIn tried three directions: a vendor's hosted reviewer (rejected as noisy, generic, and uncontrollable), an off-the-shelf model with custom rules (plagued by hallucinations and knowledge gaps), and finally a custom multi-agent system.

The multi-agent design uses an orchestrator-subagent pattern with layered rules (company-wide YAML, repository markdown, and PR-specific rules). Subagents review the same diff independently so their agreement counts as evidence; the orchestrator then merges overlapping findings (deterministic line-range check plus an LLM semantic dedupe) and verifies single-agent findings with another model, suppressing cosmetic or already-fixed issues. The article also stresses evaluation, covering pre-release evals and production evals after merge, to judge whether model, prompt, or harness changes actually improve review quality.

- Review, not writing, is now the bottleneck as coding agents produce more PRs; LinkedIn's AI reviewer covers 40,000+ PRs weekly, mostly before human review.
- Partial automation (AI first pass, human approval) is the practical approach; full AI approval remains hard.
- A reliable reviewer must be grounded, high-signal, codebase-aware, and timely; vendor reviewers and single-model setups failed on noise, hallucination, and knowledge gaps.
- The multi-agent orchestrator-subagent design uses independent parallel reviews, layered rules, semantic deduplication, and cross-model verification to produce trustworthy comments.
- Continuous evaluation before release and in production is needed to validate changes to models, prompts, and harnesses.