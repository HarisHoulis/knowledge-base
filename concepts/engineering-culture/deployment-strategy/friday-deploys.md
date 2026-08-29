---
domain: engineering-culture
subdomain: deployment-strategy
concept: friday-deploys
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "Wed, 24 Dec 2025 00:54:45 GMT"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

Charity Majors clarifies her stance on Friday deploy freezes, revisiting her earlier post about 'murdering puppies.' She emphasizes that she is not an extremist: if a team lacks the observability and tooling to move swiftly with confidence, deploy freezes before holidays or weekends are a sensible workaround. She respects that engineers know their systems best and believes freezes are acceptable when necessary, but she objects to the holier-than-thou attitude that treats them as a moral victory rather than a pragmatic hack.

Majors argues that the worst approach is to let developers keep merging changes during a freeze, creating a snowdrift of unreleased code that explodes in January. She advises that if you freeze deploys, you should also freeze merges, and have developers work on other valuable tasks. Additionally, she warns that teams accustomed to frequent deployments may see outages from inaction during long freezes; to mitigate this, she suggests running the deploy process without shipping new code, just to keep the system exercised and detect systemic issues.

Ultimately, she advocates for a balanced approach: a calm holiday period with low change rate does not require high-stakes locks and freezes if teams adopt these two practices—freezing merges and continuing deploy runs without new code. She also notes that her title was hyperbole and that she grew up on a farm, but she loves her cats and has not eaten them.

- Deploy freezes are a pragmatic workaround for teams without robust observability, not a moral achievement.
- If you freeze deploys, also freeze merges to avoid a build-up of unreleased changes that cause problems later.
- Frequent deployers should not stop deploying entirely; run the deploy process without new code to prevent outages from inaction.
- The ability to deploy safely on Fridays depends on your confidence in finding problems before customers do, which hinges on observability tooling.