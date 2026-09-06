---
domain: engineering-culture
subdomain: technical-debt
concept: rewrite-vs-migration
title: There's No Limit to How Bad Code Can Get
sources:
  - title: "There's No Limit to How Bad Code Can Get"
    url: "https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/"
    author: "Simon Willison"
    date: "2026-09-06"
---

# There's No Limit to How Bad Code Can Get

Simon Willison argues that the common impulse to rewrite a legacy system from scratch in response to overwhelming technical debt rarely succeeds. He explains that while a new team starts building a greenfield replacement, the old system remains a moving target that still runs the core business and requires ongoing changes. Since developers on the legacy system know it will be replaced, they make only minimal efforts, adding features without mitigating debt. Meanwhile, the rewrite team discovers that the old system's full behavior and scope are poorly understood — otherwise it wouldn't need replacing in the first place.

- Greenfield rewrites often fail because the legacy system keeps evolving and its hidden complexity is underestimated.
- Rewrites commonly result in two production systems: the janky old one and a new one that only handles a subset of features with much inactive code.
- Priorities may shift, leaving the rewrite abandoned and the company with double the maintenance burden.
- Will Larson's 'Migrations' article is recommended as a responsible approach to tech debt reduction.
- A better alternative is to shore up the existing system with automated testing and perform targeted refactors rather than chasing a rewrite.