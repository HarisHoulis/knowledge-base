---
domain: engineering-culture
subdomain: deploy-freezes
concept: friday-deploy-freezes
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "2025-12-24"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

Charity Majors clarifies that her stance on Friday deploy freezes is pragmatic, not extreme. She agrees with a LinkedIn thread discussing 'icing' and 'defrosting' periods around freezes. She argues that deploy freezes are a sensible workaround when teams lack the observability to move with confidence, but they should not be treated as a moral virtue (Charity Majors, 2025). The key insight is that if you freeze deploys, you must also freeze merges; otherwise, unreleased changes pile up and cause a catastrophic January recovery. Additionally, she advises against fully stopping deploys: continue running the deployment process without shipping new code to expose systemic issues that surface only when deploys are paused.

- Deploy freezes are pragmatic workarounds, not moral victories; act sheepish, not holier-than-thou.
- If you must freeze deploys, also freeze merges to prevent a January pile-up of unreleased changes.
- Keep running the deploy process without shipping new code to catch systemic issues from inaction.
- Freezes are sensible if you lack observability; with good tooling, you can avoid the need for freezes.