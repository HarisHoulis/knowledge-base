---
domain: ai-workflows
subdomain: agent-evaluation
concept: statistical-precipice
title: Computer Use at the Edge of the Statistical Precipice
sources:
  - title: "Computer Use at the Edge of the Statistical Precipice"
    url: "https://www.youtube.com/watch?v=CTLa_p6iOiY"
    author: "Pierluca D'Oro"
    date: "2026-08-14T14:30:31+00:00"
---

# Computer Use at the Edge of the Statistical Precipice

D'Oro (2026) introduces the concept of a "replay agent" — a trivial script that records successful trajectories of a frontier model on a benchmark and blindly replays them. On standard computer-use benchmarks like OSWorld and MobileWorld, this replay agent achieves success rates equal to or better than the original model, exposing a critical flaw in benchmark design: determinism. When an environment is static, it becomes gameable by simple memorization, undermining the validity of the evaluation.

The paper formally proves that pass@k metrics on deterministic environments effectively measure the success rate of such replay agents, meaning pass@k itself acts as a metrification of this exploit. This highlights two broad issues in computer-use evaluation: environments with exploitable structure and fragile metrics. To address these, D'Oro (2026) proposes the PRISM principles for building robust environments — multifactorial (stochastic) generation with validation, sandboxing, verifier support, and faithful realism. Existing benchmarks fail to satisfy all these principles, so the authors built a new benchmark that meets them, aiming for trustworthy and generalizable agent evaluation.

- Replay agents that replay successful trajectories can match or beat frontier models on deterministic benchmarks like OSWorld and MobileWorld.
- Deterministic benchmarks contain exploitable structure, making them trivially gameable by memorization.
- Pass@k on deterministic environments is formally equivalent to evaluating replay-agent success, invalidating the metric.
- Robust evaluation requires multifactorial environments with stochasticity and validation of all generated combinations.
- The PRISM principles provide a framework for building trustworthy computer-use benchmarks.