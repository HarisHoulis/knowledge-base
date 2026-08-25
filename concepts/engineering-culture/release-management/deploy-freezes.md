---
domain: engineering-culture
subdomain: release-management
concept: deploy-freezes
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "Wed, 24 Dec 2025 00:54:45 GMT"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

Charity Majors clarifies that she is not an extremist when it comes to Friday deploys or deploy freezes. She acknowledges that deploy freezes before holidays or big events are sensible when teams lack the ability to move swiftly with confidence—meaning they cannot quickly find problems in new code before customers do, which depends on the quality of observability tooling and the ability to explore high cardinality dimensions in real time. She agrees with commenters on a LinkedIn thread who discussed easing into and out of freezes, and she emphasizes that if you need a freeze, it's a pragmatic workaround, not a moral virtue. The worst behavior is adopting a 'holier-than-thou' posture; instead, you should act a little sheepish and admit it's a hack (Majors, https://charity.wtf/p/on-friday-deploys-sometimes-that).

- Deploy freezes are a sensible workaround when teams lack strong observability and confidence in rapid deployment, not a moral virtue.
- If you must freeze deploys, also freeze merges to prevent unreleased changes from piling up and creating hidden problems.
- Keep the deploy pipeline running (without new code) to avoid systemic issues caused by the absence of regular deploys.
- The holiday period can be both peaceful and safe if you reduce change rate without completely stopping deployment practice.