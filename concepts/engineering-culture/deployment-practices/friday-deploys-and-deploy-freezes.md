---
domain: engineering-culture
subdomain: deployment-practices
concept: friday-deploys-and-deploy-freezes
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "Wed, 24 Dec 2025 00:54:45 GMT"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

Charity Majors clarifies that she is not an extremist about Friday deploys or deploy freezes, despite her provocative earlier post comparing deploy freezes to murdering puppies. She acknowledges that freezes before holidays or events are sensible for teams that lack the observability and confidence to move quickly and catch problems before customers do. She emphasizes pragmatism over moral posturing, noting that deploy freezes are often a necessary hack rather than a virtuous practice.

- Deploy freezes are acceptable when teams lack the ability to detect issues quickly, such as without robust observability.
- If you must freeze deploys, also freeze merges to prevent a snowdrift of changes that will explode later.
- To avoid 'inaction' outages, continue running the deploy process without shipping new code during freezes.
- Avoid moralizing about deploy freezes; they are a pragmatic workaround, not a moral victory.
- Holiday periods can be a peaceful time for low change rate and creative work, if managed properly.