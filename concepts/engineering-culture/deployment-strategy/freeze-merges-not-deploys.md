---
domain: engineering-culture
subdomain: deployment-strategy
concept: freeze-merges-not-deploys
title: On Friday Deploys: Sometimes That Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "Wed, 24 Dec 2025 00:54:45 GMT"
---

# On Friday Deploys: Sometimes That Puppy Needs Murdering

Charity Majors revisits her controversial post about Friday deploy freezes, clarifying that she is not an extremist. She acknowledges that deploy freezes are sensible for teams that lack the observability and confidence to move swiftly, and she agrees with commenters who note that not every team can simply eliminate freezes. The key is to be pragmatic and admit that freezes are a workaround, not a moral virtue (Majors, 2025).

- Deploy freezes are a legitimate workaround when you lack the tooling or confidence to move fast safely.
- If you must freeze deploys, also freeze merges—otherwise changes accumulate and explode in January.
- Avoid actually halting deploys unless you intentionally want to test system stability; run the deploy process with no new code instead.
- Don't moralize deploy freezes; they are a hack, not a noble act.