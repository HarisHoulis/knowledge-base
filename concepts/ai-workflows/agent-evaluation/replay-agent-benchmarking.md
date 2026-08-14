---
domain: ai-workflows
subdomain: agent-evaluation
concept: replay-agent-benchmarking
title: Computer Use at the Edge of the Statistical Precipice
sources:
  - title: "Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs"
    url: "https://www.youtube.com/watch?v=CTLa_p6iOiY"
    author: "AI Engineer"
    date: "2026-08-14"
---

# Computer Use at the Edge of the Statistical Precipice

The talk introduces 'replay agents'—scripts that record successful trajectories from a frontier model on a benchmark and then replay those actions blindly. Astonishingly, on deterministic benchmarks like OSWorld or MobileWorld, these replay agents match or even beat the original model's success rate, exposing a critical vulnerability in current evaluation methods (D'Oro, 2026).

- Replay agents achieve comparable or better success than frontier models on static, deterministic benchmarks, proving these benchmarks are gameable.
- Pass@K on deterministic environments is formally equivalent to evaluating a replay agent, making it a fragile metric for computer use tasks.
- Robust environments must be multifactorial (with stochastic variation), validated for all combinations, sandboxed, and equipped with verifiers and faithful real-world reproductions.
- The PRISM principles guide the construction of such environments, and the speakers built a benchmark satisfying all these criteria.