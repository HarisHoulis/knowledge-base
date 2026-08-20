---
domain: engineering-culture
subdomain: release-management
concept: deploy-freeze-pragmatism
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "Wed, 24 Dec 2025 00:54:45 GMT"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

Charity Majors clarifies that despite her famous 'Friday Deploy Freezes are Exactly Like Murdering Puppies' post, she is not an extremist about deploy freezes. She explicitly agrees with teams that need to freeze deploys, especially when they lack the observability and confidence to move swiftly. In her view, if you can't find problems before customers do, freezes are a sensible workaround, not a moral failing. She urges humility: freezes are a 'hack' to cope with constraints, not something to be holier-than-thou about ([source](https://charity.wtf/p/on-friday-deploys-sometimes-that)).

She also warns against the common practice of letting developers keep merging during a freeze, only to deploy a huge batch later. This builds up risk like a snowdrift over grenades. Her advice: if you freeze deploys, freeze merges too, and let teams work on other things. Additionally, she cautions that stopping deployments entirely can itself cause instability for teams used to frequent releases. To mitigate this, she suggests running the deploy process without shipping new code, keeping the system exercised ([source](https://charity.wtf/p/on-friday-deploys-sometimes-that)).

Ultimately, the article is a nuanced take on release cadence and risk management, acknowledging real-world constraints while pushing back on self-congratulatory freeze policies and offering concrete mitigations like freezing merges and practicing 'empty' deploys.

- Deploy freezes are acceptable when teams lack the observability and confidence to move quickly, but they should be seen as pragmatic hacks, not moral victories.
- If you must freeze deploys, also freeze merges to avoid accumulating unreleased changes that create a risky catch-up deploy later.
- Teams used to frequent deploys may see outages from inactivity; run the deploy pipeline without shipping new code to keep systems exercised.
- Holiday or event-based freezes can be a good time for low-risk work, but only if you avoid piling up hidden changes.
- The author is not an extremist; she agrees with thoughtful approaches like 'icing' and 'defrosting' periods from the community.