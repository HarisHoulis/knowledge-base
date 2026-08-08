---
domain: ai-workflows
subdomain: agent-environments
concept: long-horizon-definition
title: Rethinking Environments for Long-Horizon Work
sources:
  - title: "Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software"
    url: "https://www.youtube.com/watch?v=2aS7aKoXn64"
    author: "AI Engineer"
    date: "2026-08-01T00:00:06+00:00"
---

# Rethinking Environments for Long-Horizon Work

The talk argues that the definition of 'long-horizon' is relative and evolving, acting as a scalar metric rather than a binary category. As AI agents become more capable, tasks once considered long-horizon become shorter, so evaluations must adapt over time. The speakers reference METR's benchmark methodology, which defines long-horizon capability via human time thresholds, such as achieving a 50% success rate on tasks that take humans 16 hours [1]. This human-relative approach provides an intuitive measure but is complemented by model-relative metrics like token consumption, number of steps, and tool calls. These model-based units are noisy—heavily influenced by model choice and harness implementation—yet they reveal the technical frontier, including challenges like context window limits, compaction, and maintaining coherence over long trajectories [1]. Ultimately, the talk emphasizes that no single definition suffices; long-horizon must be assessed dynamically, and environment design should account for the shifting nature of task difficulty as models improve.

- Long-horizon is a scalar, context-dependent metric, not a fixed binary; tasks shift in difficulty as agent capabilities grow.
- Human-relative benchmarks like METR use time thresholds (e.g., 16-hour tasks) to define long-horizon capability.
- Model-relative metrics (tokens, steps, tool calls) are noisy but useful for understanding the technical limits of current agents.
- Compaction and context window constraints are major bottlenecks for maintaining coherence over long trajectories.
- Environment design must adapt to evolving definitions of long-horizon work.