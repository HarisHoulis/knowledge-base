---
domain: system-design
subdomain: ci-cd
concept: ci-cd-practices
title: CI/CD with Robert Erez
sources:
  - title: "CI/CD with Robert Erez"
    url: "https://newsletter.pragmaticengineer.com/p/cicd-with-robert-erez"
    author: "Gergely Orosz"
    date: "Wed, 17 Jun 2026 16:41:01 GMT"
---

# CI/CD with Robert Erez

In this Pragmatic Engineer episode, Gergely Orosz interviews Robert Erez, a principal engineer at Octopus Deploy and former Skype colleague, about deploying software safely and efficiently at scale. They discuss Kubernetes, GitOps, platform engineering, progressive delivery, feature flags, cloud development environments, and how AI is reshaping CI/CD workflows. The conversation draws on Rob's experience with large-scale deployments and release processes, offering practical tradeoffs rather than one-size-fits-all advice (source: CI/CD with Robert Erez, The Pragmatic Engineer).

- Roll forward, never backward: for stateful systems, a failed v2 should be followed by v3 with the fix, not a rollback to v1.
- GitOps isn't actually about Git: its four pillars (declarative, versioned/immutable, pulled, continuously reconciled) don't require Git, yet the industry dogmatically crams everything into a repo.
- Continuous delivery is often more practical than continuous deployment: shipping every change to prod is frequently overkill, and validating the deployment process itself has more value.
- Feature flags are a better safety net than rollbacks, but they can become addictive and require regular cleanup to avoid a hygiene crisis.
- AI shifts the CI/CD focus from speed to risk: when AI agents write most code, slower and more thorough tests become more valuable than shaving minutes off build times.