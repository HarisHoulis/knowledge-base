---
domain: engineering-culture
subdomain: deployment-strategies
concept: roll-forward-over-rollback
title: CI/CD with Robert Erez
sources:
  - title: "CI/CD with Robert Erez"
    url: "https://newsletter.pragmaticengineer.com/p/cicd-with-robert-erez"
    author: "Gergely Orosz"
    date: "Wed, 17 Jun 2026 16:41:01 GMT"
---

# CI/CD with Robert Erez

In this Pragmatic Engineer episode, Robert Erez, principal engineer at Octopus Deploy, argues that rollbacks are risky for stateful systems because code and database schemas can drift out of sync. Instead, teams should roll forward by deploying a fix (v3) rather than reverting to v1 (Orosz, 2026). He also clarifies that GitOps is not intrinsically tied to Git: its four pillars—declarative, versioned/immutable, pulled, and continuously reconciled—can be implemented with other backends, and the industry's dogmatic focus on Git leads to anti-patterns like storing secrets in repos.

- Prefer roll-forward to rollback for stateful systems; deploy a fix (v3) rather than reverting to v1.
- GitOps principles don't require Git; forcing secrets into repos is an anti-pattern.
- Continuous delivery is often more practical than continuous deployment; validate the pipeline and decide when to promote.
- Feature flags are a better safety net than rollbacks, but toggles must be cleaned up to avoid technical debt.
- With AI-generated code, prioritize risk reduction over CI speed; run more thorough tests.