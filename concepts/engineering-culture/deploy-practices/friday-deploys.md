---
domain: engineering-culture
subdomain: deploy-practices
concept: friday-deploys
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "2025-12-24"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

Charity Majors clarifies her stance on Friday deploys and deploy freezes, emphasizing that she is not an extremist. She explicitly states that not everyone should eliminate deploy freezes; if a team lacks the ability to move swiftly with confidence—often due to poor observability and inability to explore high-cardinality data—deploy freezes before holidays, events, or weekends are sensible. She agrees with the nuanced approaches mentioned in a LinkedIn thread, such as 'icing' and 'defrosting' periods (Majors, 2025).

Majors criticizes the 'holier-than-thou' posture some adopt around deploy freezes, calling them a 'fucking hack' rather than a moral gesture. She advises that if you want to freeze deploys, you should freeze merges instead, preventing developers from accumulating unreleased changes that create a 'snowdrift' of risk. She also warns that actually stopping deploys for weeks can cause outages from inaction, and suggests running the deploy process without shipping new code to keep systems stable (Majors, 2025).

- Deploy freezes are a practical workaround for teams lacking observability and confidence, not a moral imperative.
- To avoid risk buildup, freeze merges rather than deploys when a freeze is necessary.
- Long deploy freezes can introduce instability; running the deploy pipeline without new code mitigates this.
- Endorse 'icing' and 'defrosting' periods for easing into and out of freezes.