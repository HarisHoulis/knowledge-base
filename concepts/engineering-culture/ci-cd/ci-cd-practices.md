---
domain: engineering-culture
subdomain: ci-cd
concept: ci-cd-practices
title: CI/CD with Robert Erez
sources:
  - title: "CI/CD with Robert Erez"
    url: "https://newsletter.pragmaticengineer.com/p/cicd-with-robert-erez"
    author: "Gergely Orosz"
    date: "Wed, 17 Jun 2026"
---

# CI/CD with Robert Erez

In this episode of The Pragmatic Engineer, Gergely Orosz interviews Robert Erez, a principal engineer at Octopus Deploy, about deploying software safely and efficiently at scale. They discuss Kubernetes, GitOps, platform engineering, progressive delivery, feature flags, cloud development environments, and AI's impact on CI/CD workflows. The conversation highlights practical tradeoffs in deployment strategies, emphasizing that roll-forward is often safer than rollback when stateful systems are involved, and that continuous delivery is more pragmatic than continuous deployment for many teams (Orosz, 2026).

A key takeaway is that GitOps, despite its name, does not inherently require Git; its four pillars—declarative, versioned and immutable, pulled not pushed, and continuously reconciled—can be satisfied without a Git repository. However, the industry has become dogmatic about storing everything, even secrets, in Git, which can be problematic. Additionally, Rob notes that pull-based GitOps can become a bottleneck for organizations running thousands of Kubernetes clusters, as these clusters may get throttled by a single Git repo (Orosz, 2026).

The episode also explores the evolving landscape of development environments and AI in CI/CD. Ephemeral environments are replacing static test/staging environments, enabling per-feature-branch evaluation before merge. As AI agents generate more code, the CI/CD calculus shifts from minimizing build time to reducing the risk of shipping bugs to production, making additional and slower tests more valuable. Rob also points out that major institutions like banks and governments remain on-premises due to control requirements, a trend unlikely to change (Orosz, 2026).

- Prefer roll-forward (push a v3 with a fix) over rollback when systems have state, as rollback can cause schema/code mismatches.
- GitOps is not actually about Git; its principles are declarative, versioned/immutable, pulled, and continuously reconciled, yet teams often over-index on storing secrets in Git.
- Continuous delivery is often more practical than continuous deployment, allowing teams to validate the pipeline and manually trigger production releases when needed.
- Feature flags offer a faster safety net than rollbacks, but they become a hygiene crisis if not cleaned up regularly.
- AI in CI/CD will shift priorities from speed to risk reduction, making slower, more thorough tests worthwhile when AI agents are writing most of the code.