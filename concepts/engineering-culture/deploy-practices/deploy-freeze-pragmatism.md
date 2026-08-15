---
domain: engineering-culture
subdomain: deploy-practices
concept: deploy-freeze-pragmatism
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "2025-12-24"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

Charity Majors clarifies her stance on Friday deploy freezes, emphasizing that she is not an extremist. She acknowledges that deploy freezes are sensible for teams that lack the observability and confidence to move swiftly, meaning they cannot find problems before customers do. She criticizes the moral posturing around freezes, calling them a 'hack' rather than a virtuous practice, and encourages teams to be pragmatic and sheepish about them instead of self-congratulatory (Majors, 2025).

Majors advises that if you need to freeze deploys, you should freeze merges instead to avoid a snowdrift of changes accumulating and exploding later. She also warns against completely stopping the deploy process, as systemic issues can arise from inaction. Her mitigation is to keep running the deploy pipeline every day or two without shipping new code, allowing for stability and peace during holidays while avoiding terrifying January recoveries (Majors, 2025).

- Deploy freezes are acceptable when you lack observability or confidence, but they are hacks, not moral achievements.
- Freeze merges, not deploys, to prevent a buildup of unreleased changes that can cause major issues later.
- If you do freeze deploys, continue running the deploy process without new code to uncover systemic issues.
- Pragmatism is key: acknowledge the limitations of your systems and do the best you can with the hand you're dealt.