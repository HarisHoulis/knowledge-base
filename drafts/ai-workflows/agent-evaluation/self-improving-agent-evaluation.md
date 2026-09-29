---
domain: ai-workflows
subdomain: agent-evaluation
concept: self-improving-agent-evaluation
title: How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases
sources:
  - title: "How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases"
    url: "https://www.youtube.com/watch?v=XyV6bSMyq-I"
    author: "Zubin Aysola (AI Engineer)"
    date: "2026-09-26T16:00:08+00:00"
---

# How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases

Zubin Aysola describes Weights & Biases' Agent Arya, released publicly on Monday, and the evaluation framework used to build it. He focuses on how the team evaluates the agent and uses Arya to self-reinforce the research cycle (source).

The core problem is that tests, assessments, agents, and how they are configured are covariant. For dynamically changing systems, principled assessment requires good measurements of actual performance in both production and offline environments, related to the simulation-to-reality gap (source).

Weave for agents is presented as a monitoring platform for production and offline agent tracing. Offline, Aysola creates simulation environments, runs the Arya agent, and monitors them in Weave; production work logs in the same format so production traces can be copied into offline environments and used to fix bugs. This creates a flywheel (source). Arya itself is used to self-build because it is sophisticated enough to do hill climbing autonomously (source).

In a demo, Arya runs automated research from a Weights & Biases artifact codebase, runs learning tasks, reviews production routes, adds step-by-step analysis tasks, and attempts to write a new version for herself (source). A production trace is moved into the offline evaluation framework for step-by-step analysis; Arya is asked to record it in offline assessments and run candidate and production agents on it, with estimates recorded in Weave (source).

- Weights & Biases released Agent Arya publicly and uses it for automated research and self-improvement.
- Tests, assessments, agents, and their configuration are covariant, so evaluating dynamic systems requires good measurements in production and offline.
- Weave for agents monitors both offline simulations and production traces in the same format.
- Production traces can be copied into offline evaluation for step-by-step analysis and bug fixing.
- Arya can autonomously hill-climb and attempt to write a new version of itself.