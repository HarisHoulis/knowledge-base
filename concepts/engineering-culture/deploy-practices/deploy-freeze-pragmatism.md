---
domain: engineering-culture
subdomain: deploy-practices
concept: deploy-freeze-pragmatism
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "Wed, 24 Dec 2025 00:54:45 GMT"
  - title: "Friday Deploy Freezes are Exactly Like Murdering Puppies"
    url: "https://substack.com/home/post/p-181561576"
    author: "Charity Majors"
    date: "May 1, 2019"
  - title: "LinkedIn thread by Michael Davis on Friday Deploy Freezes"
    url: "https://www.linkedin.com/posts/michael-davis-7033548_friday-deploy-freezes-are-exactly-like-murdering-activity-7408181339444707328-8GjS?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAEP-B4Bn1IFS4Br7okfkI7z81XqQEOEKro"
    author: "Michael Davis"
    date: "unknown"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

Charity Majors clarifies her stance on deploy freezes, which she feels is often misunderstood as extremism. She acknowledges that freezes are a sensible workaround when teams lack the ability to move swiftly with confidence—specifically due to poor observability and inability to explore high cardinality dimensions in real time. She points to a LinkedIn thread where commenters discuss pragmatic approaches like 'icing' and 'defrosting' periods, and she agrees with those insights. Her main criticism is not the freeze itself, but the moral posturing that treats it as a virtuous act rather than a practical hack. She emphasizes that there is no shame in using freezes as a workaround, but one should be honest about it.

She advises two key practices for managing freezes effectively. First, if you freeze deploys, you should also freeze merges; otherwise, unreleased changes accumulate and cause difficult problems when finally deployed after the freeze. Second, rather than completely stopping the deploy process, teams should run deploys regularly without shipping new code, to avoid triggering hidden systemic issues that would otherwise surface during a long inactivity period. She bets that something will break when teams that deploy frequently suddenly stop for weeks, and recommends keeping the deployment engine running to avoid such surprises.

- Deploy freezes are acceptable and necessary when teams lack the observability and confidence to move quickly; they are a workaround, not a moral virtue.
- If you freeze deploys, freeze merges too, preventing unshipped changes from piling up and creating a painful recovery.
- Continue running deploy processes without new code during a freeze to avoid hidden systemic issues caused by inactivity.
- Embrace pragmatic approaches like 'icing' and 'defrosting' periods to ease into and out of freezes.