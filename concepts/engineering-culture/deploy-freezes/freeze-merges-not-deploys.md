---
domain: engineering-culture
subdomain: deploy-freezes
concept: freeze-merges-not-deploys
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "2025-12-24"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

Charity Majors clarifies that she is not categorically opposed to deploy freezes, including on Fridays or holidays. She acknowledges that if a team lacks the ability to move swiftly with confidence—especially due to poor observability or inability to explore high-cardinality data in real time—then freezes are a sensible workaround. Her objection is to moralizing the practice; deploy freezes are pragmatic hacks, not grand moral gestures.

- Deploy freezes are acceptable when teams lack observability and confidence; the key is not to pretend they are virtuous.
- If you freeze deploys, you should also freeze merges. Continuing to merge while withholding deployment creates a snowdrift of risky changes that all surface at once.
- Freezing deploys when a team is used to frequent deploys can itself cause instability. Run the deploy process regularly, but ship no new code.
- Ideally, merging to main and deploying to production should feel atomic; developers should not merge unless they are prepared for immediate production exposure.
- Holidays can still be a quiet, productive period if you intentionally reduce change rate without locking everyone down.