---
domain: ai-workflows
subdomain: agent-evaluation
concept: computer-use-benchmarking
title: Computer Use at the Edge of the Statistical Precipice
sources:
  - title: "Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs"
    url: "https://www.youtube.com/watch?v=CTLa_p6iOiY"
    author: "AI Engineer"
    date: "2026-08-14T14:30:31+00:00"
---

# Computer Use at the Edge of the Statistical Precipice

In this talk, Pierluca D'Oro of Programma Labs (work done at Meta Super Intelligent Labs) warns that current computer-use agent benchmarks are fundamentally gameable. He introduces the concept of a "replay agent": a blind script that replays successful trajectories collected from a frontier model on a deterministic benchmark. On standard benchmarks like OSWorld or MobileWorld, this replay agent matches or even beats the original model, exposing that static, deterministic environments are trivially exploitable. He further shows that the popular pass@k metric, when applied to such deterministic settings, is mathematically equivalent to scoring this replay agent, making it a fragile and misleading statistic (source).

To address these issues, D'Oro proposes a set of environment-design principles called PRISM: multifactorial variation (stochasticity in data, appearance, or initial state), verification that all generated combinations are valid, sandboxing, support for privileged verifiers, and realism through faithful reproduction of real systems. He argues that current benchmarks fail to combine all these properties, leading to untrustworthy evaluations. The talk emphasizes that both environment building and metric design must be overhauled to prevent simple scripts from gaming evaluations and to produce scores that genuinely reflect an agent's computer-use ability (source).

- A replay agent—a script replaying successful trajectories—can match or beat frontier models on deterministic computer-use benchmarks.
- Pass@k on deterministic environments is equivalent to evaluating a replay agent, making it a fragile and exploitable metric.
- Robust environments should follow PRISM: multifactorial variation, verification, sandboxing, verifiers, and realism.
- Current benchmarks lack a unified combination of these principles, leading to untrustworthy agent evaluations.