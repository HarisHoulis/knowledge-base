---
domain: system-design
subdomain: ci-cd
concept: progressive-delivery
title: CI/CD with Robert Erez
sources:
  - title: "CI/CD with Robert Erez"
    url: "https://newsletter.pragmaticengineer.com/p/cicd-with-robert-erez"
    author: "Gergely Orosz"
    date: "Wed, 17 Jun 2026 16:41:01 GMT"
---

# CI/CD with Robert Erez

Ephemeral environments are replacing static test/staging environments, and AI is shifting CI/CD priorities from build speed to risk reduction. Because AI agents can babysit slow pipelines without context switching, the new priority is reducing the risk of AI-generated bugs reaching production, making extra and even slower tests more worthwhile.

- Roll forward, never backward: with stateful systems, fix forward to v3 instead of rolling back to v1.
- GitOps isn't about Git: its four pillars don't require a repo; avoid putting secrets in Git.
- Prefer continuous delivery over continuous deployment to validate the deployment process while keeping human control over prod pushes.
- Use feature flags as a safety net to stop the bleeding, but treat cleanup as gardening to avoid flag hygiene issues.
- AI will change CI/CD from optimizing for speed to reducing risk of AI-written bugs, making extra slower tests worthwhile.