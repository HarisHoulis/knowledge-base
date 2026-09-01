---
domain: engineering-culture
subdomain: release-management
concept: friday-deploys
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "2025-12-24"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

Additionally, she highlights the often-forgotten risk of inaction: systems that are used to frequent deploys can break when deploys stop entirely. To mitigate this, she recommends running the deploy process every day or two without shipping new code, which exercises the system and surfaces hidden issues. This way, teams can enjoy a peaceful holiday without the high-stakes drama of freeze-induced outages (Majors, 2025).

- Deploy freezes are pragmatic workarounds, not moral victories—admit they are hacks and you can be pragmatic.
- If you freeze deploys, also freeze merges to avoid an unreleased snowdrift of code that explodes later.
- Ceasing deploys can cause instability from inaction; run the deploy pipeline without new code as a mitigation.
- The ideal is fast, atomic merge-to-deploy cycles so the act of merging and deploying feels like one action.
- Respect team judgments: if you need a freeze, that's fine as long as you're honest about its tradeoffs.