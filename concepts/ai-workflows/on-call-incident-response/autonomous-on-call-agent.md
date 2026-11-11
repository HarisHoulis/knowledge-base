---
domain: ai-workflows
subdomain: on-call-incident-response
concept: autonomous-on-call-agent
title: Give Your On-Call Its Own AI Teammate
sources:
  - title: "Give Your On-Call Its Own AI Teammate - Swaapnika Motapothula, Chinmay Gandhi & Vlad Tsvang, Meta"
    url: "https://www.youtube.com/watch?v=_NBx2NNOuA4"
    author: "AI Engineer"
    date: "2026-11-10"
---

# Give Your On-Call Its Own AI Teammate

Meta engineers describe building an AI colleague for on-call rotations, motivated by the observation that roughly three-quarters of new code is now AI-written while incident response has not sped up correspondingly. The bottleneck has shifted from writing code to operating it, and on-call engineers bear that burden. Their core diagnosis is fragmentation: notification scripts, ticket bots, deployment bots, and remediation agents each hold a piece of context but nothing connects them, so the human becomes the link between isolated automations.

The proposed design is a single AI colleague per rotation: one loop over all signals, a shared team memory that learns each shift, its own identity for autonomous work, and human control so engineers approve rather than perform the work. Under the hood it is a simple agent — a model using tools in a loop, acting on the environment and reading feedback — with everything else built around that cycle to make continuous operation safe.

Autonomy is granted in stages modeled on onboarding a new engineer: shadowing (investigate and report, change nothing), then acting only on approval, then handling less critical tasks independently while highly critical work stays with humans. Promotion between stages is gated by a simple test: how expensive is a mistake, how easily is it detected (tests, CI, verification), and whether the agent already has successful experience with that action. This is why an agent can close a noisy notification on its own while a human is still needed to mitigate consequences.

- About 3/4 of new code at Meta is AI-written, but on-call response speed has not kept pace, shifting the bottleneck to operations
- Isolated per-team automations (notification, ticket, deployment, remediation bots) each hold partial context, forcing humans to connect the clues
- The design is one AI colleague per rotation with a single signal loop, shared learning memory, and human approval rather than human execution
- Autonomy is earned in stages: shadowing, then act-on-approval, then autonomous handling of low-criticality tasks
- Promotion criteria are mistake cost, detectability via tests/CI, and prior successful experience with the action