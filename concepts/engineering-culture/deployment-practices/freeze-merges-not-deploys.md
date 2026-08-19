---
domain: engineering-culture
subdomain: deployment-practices
concept: freeze-merges-not-deploys
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "2025-12-24"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

Charity Majors clarifies that her infamous "Friday Deploy Freezes are Exactly Like Murdering Puppies" post was hyperbolic, and she is actually pragmatic about deploy freezes. She acknowledges that if a team lacks good observability and the ability to quickly detect problems in production, deploy freezes before holidays or weekends are sensible. She agrees with commenters who discuss easing into and out of freezes with "icing" and "defrosting" periods, and emphasizes that freezes are a workaround, not a moral virtue.

- Deploy freezes are a hack, not a virtuous practice; teams should admit when they need them rather than being holier-than-thou.
- If you need a freeze, freeze merges, not deploys. Let developers stop merging and work on other valuable tasks to avoid a pileup of unreleased changes.
- If you actually freeze deploys, keep running the deploy process without shipping new code to catch systemic issues that might surface during the freeze.
- Accumulating unreleased changes for days or weeks creates a dangerous 'snowdrift of grenades' that can explode when you finally deploy.
- The ability to deploy confidently depends on observability and real-time exploration of high-cardinality dimensions.