---
domain: ai-workflows
subdomain: agent-evaluation
concept: replay-agent-benchmark-fragility
title: Computer Use at the Edge of the Statistical Precipice
sources:
  - title: "Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs"
    url: "https://www.youtube.com/watch?v=CTLa_p6iOiY"
    author: "AI Engineer"
    date: "2026-08-14T14:30:31+00:00"
---

# Computer Use at the Edge of the Statistical Precipice

Pierluca D'Oro discusses the fragility of computer use agent benchmarks. He introduces the concept of a 'replay agent' that records successful trajectories from a frontier model and blindly replays them on benchmark tasks. Surprisingly, this simple script can match or even exceed the success rate of the original frontier model on standard benchmarks like OSWorld and MobileWorld. This occurs because these benchmarks are deterministic, making them exploitable by memorized action sequences.

- Replay agents, which blindly execute pre-recorded successful trajectories, can match or beat frontier models on static, deterministic computer use benchmarks.
- The pass@k metric, commonly used in computer use evaluation, is formally equivalent to evaluating a replay agent in a deterministic environment, meaning it inadvertently rewards memorization rather than generalization.
- To build robust benchmarks, environments should follow PRISM principles: multi-factorial (stochastic variation), verifiable (checking all generated combinations), sandboxed, and realistic (faithful reproductions of real systems).