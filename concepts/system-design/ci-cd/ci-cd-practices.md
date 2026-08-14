---
domain: system-design
subdomain: ci-cd
concept: ci-cd-practices
title: CI/CD with Robert Erez
sources:
  - title: "CI/CD with Robert Erez"
    url: "https://newsletter.pragmaticengineer.com/p/cicd-with-robert-erez"
    author: "Gergely Orosz"
    date: "2026-06-17"
---

# CI/CD with Robert Erez

The conversation also distinguishes continuous deployment from continuous delivery, arguing that continuous delivery is often more practical because it validates the deployment process and allows teams to choose when to release. Feature flags are highlighted as a better safety net than rollbacks, though they require discipline to avoid accumulating obsolete toggles. At scale, a Git repository can become a bottleneck for thousands of Kubernetes clusters, and some major institutions remain on-premises for control. The episode also covers the rise of platform teams, the shift toward ephemeral environments, and how AI is changing CI/CD priorities from speed to risk reduction.

- Roll forward, not back: fixing a bad release with a new version is safer than reverting when schemas are involved.
- GitOps isn't inherently Git: the four principles don't require Git, and forcing secrets into repos is harmful.
- Continuous delivery beats continuous deployment for most teams: it validates the pipeline and retains release flexibility.
- Feature flags stop bleeding faster than rollbacks, but toggles need regular cleanup to avoid technical debt.
- AI shifts CI/CD from optimizing for developer time to optimizing for safety, favoring more thorough testing.