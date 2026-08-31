---
domain: engineering-culture
subdomain: deployment-practices
concept: deploy-freezes
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "2025-12-24"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

Charity Majors clarifies her position on deploy freezes, explaining that they are not inherently bad but are a workaround for teams lacking confidence or observability. She criticizes the moral posturing around freezes, calling them a 'hack' rather than a virtuous act. If teams cannot deploy quickly with confidence, freezes before holidays or weekends are pragmatic and acceptable (source: Charity Majors).

The core recommendation is to freeze merges, not just deploys, to avoid accumulating unreleased changes that can cause painful post-freeze failures. She warns that letting developers merge diffs during a freeze creates a 'snowdrift' of issues that will surface later. Instead, developers should work on other valuable tasks (source: Charity Majors).

She also advises against halting the deployment process entirely. If a team deploys frequently, a sudden pause can itself trigger instability. She bets that something will break if an active deployment system sits idle for two weeks, and recommends running the deploy process regularly without shipping new code to keep the system exercised and catch systemic issues (source: Charity Majors).

Ultimately, Majors supports a peaceful holiday period with low change rate, but achieved through careful merge management and continuous deployment drills, not rigid locks. She emphasizes pragmatism and honesty about the reasons for freezes (source: Charity Majors).

- Deploy freezes are a pragmatic workaround, not a moral achievement; if you need them, use them without self-righteousness.
- When freezing deploys, also freeze merges to prevent dangerous accumulation of unreleased changes.
- Continuing to run the deploy process (without shipping code) avoids instability caused by a sudden halt in deployment cadence.
- High-quality observability is the key to moving fast with confidence and reducing the need for freezes.