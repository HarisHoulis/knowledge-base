---
domain: ai-workflows
subdomain: ai-pr-automation
concept: ai-driven-merge-pipeline
title: Forget "read the code," I don't even merge PRs myself
sources:
  - title: "Forget "read the code," I don't even merge PRs myself"
    url: "https://www.youtube.com/watch?v=lfSnYGdtbqE"
    author: "Kent C. Dodds"
    date: "2026-07-30T11:46:10+00:00"
---

# Forget "read the code," I don't even merge PRs myself

In this video, Kent C. Dodds argues that the traditional expectation of reading every line of code is becoming obsolete in AI-assisted development. He frames the decision to read code as a spectrum determined by the risk of changes and the reliability of the agentic loop, noting that as AI produces code at an unprecedented scale, manual review can no longer keep pace. He advocates for shifting from line-by-line code review to higher-level system review, where humans supervise agents rather than act as bottlenecks (Dodds, 2026).

Dodds describes his own workflow: an AI agent named Cody generates pull requests, iterates with automated review bots, merges the PRs, deletes branches, and monitors production deployments. He receives notifications in Discord containing summaries and relevant links, allowing him to review the outcome without reading the entire diff. However, not all PRs auto-merge—changes that are medium-risk or have broad impact are flagged for human attention, preserving oversight where it matters most.

The video also references community discussions triggered by a post from Mitchell and a follow-up take from The Primagen, both of whom contributed to the 'read the code' debate. Dodds concludes that while reading code is still necessary in certain situations, the industry is moving toward a factory-engineering model where human involvement is minimized and trust in AI agents is increased, making skills like system thinking and workflow design more durable than manual code reading.

- Reading code is a spectrum, not a binary; the right amount depends on risk tolerance and the quality of AI review.
- AI agents can own the entire PR lifecycle, from opening and reviewing to merging and deploying.
- Engineers should focus on reviewing systems and outcomes, not every line of code.
- High-impact or medium-risk changes should still trigger human review.
- The goal is to keep humans out of the loop as much as possible while maintaining safety and quality.