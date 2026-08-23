---
domain: engineering-culture
subdomain: deploy-practices
concept: freeze-merges-not-deploys
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "2025-12-24"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

The core recommendation is to freeze merges, not deploys, if you want stability. Allowing developers to keep merging changes over days or weeks creates a snowdrift of untested changes that explode in January. Instead, let people work on other valuable tasks during the freeze period. Also, if you do freeze deploys, don't stop the deploy pipeline entirely—run it without shipping new code to catch systemic issues that regular deploys might mask. Majors argues that inaction can cause as many outages as action, so maintaining the deployment process is key.

- Freezing deploys is a sensible workaround for teams without strong observability, but it's a hack, not a moral virtue.
- Freeze merges rather than deploys to avoid accumulating untested changes that surface later.
- If you freeze deploys, keep running the deploy process without new code to catch systemic issues.
- Regular deploys hide problems; a sudden freeze can reveal them, so expect surprises.
- Majors is pragmatic, not extreme: she supports freezes when needed and values the peace of holiday periods.