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

In this article, Charity Majors clarifies that she is not as extreme as her earlier post 'Friday Deploy Freezes are Exactly Like Murdering Puppies' might suggest. She acknowledges that deploy freezes are sensible when teams lack the observability and tooling to move swiftly with confidence. The key is honesty: freezes are pragmatic hacks, not moral victories. She argues that the worst approach is to keep merging changes during a freeze, creating a snowdrift of unreleased code that will explode when deploys resume. Instead, if you must freeze deploys, freeze merges too, and use the quiet time for other valuable work. She also warns that stopping deploys entirely can trigger outages from inaction; if you normally deploy frequently, run deploys with no new code to keep the system exercised. The article emphasizes that holiday calm and stability are achievable without dangerous freezes.

- Deploy freezes are acceptable when teams lack confidence or observability, but they should be seen as workarounds, not moral achievements.
- Freezing merges while letting developers keep merging creates a buildup of unreleased changes that will likely cause a painful January recovery.
- If you freeze deploys, also freeze merges, and have developers work on other tasks instead.
- If you are accustomed to frequent deploys, continue running deploy processes without shipping new code to avoid outages caused by inaction.