---
domain: engineering-culture
subdomain: deploy-practices
concept: friday-deploy-freezes
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "2025-12-24"
  - title: "Friday Deploy Freezes are Exactly Like Murdering Puppies"
    url: "https://charity.wtf/2019/05/01/friday-deploy-freezes-are-exactly-like-murdering-puppies/"
    author: "Charity Majors"
    date: "2019-05-01"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

Charity Majors clarifies that her infamous "Friday Deploy Freezes are Exactly Like Murdering Puppies" post is hyperbolic and not an absolute prohibition on deploy freezes. She acknowledges that if a team lacks the observability and confidence to catch problems before customers do, freezing deploys ahead of holidays or weekends is a sensible workaround. She endorses a LinkedIn discussion where people suggest practices like "icing" and "defrosting" around freezes, and she agrees with those pragmatic approaches (Charity Majors, https://charity.wtf/p/on-friday-deploys-sometimes-that).

Majors' core argument is that if you must freeze deploys, you should also freeze merges. Otherwise, changes pile up like a snowdrift over grenades, and the eventual January deployment will find the issues "with your face." She also advises against fully stopping the deploy machinery: if you're used to deploying frequently, going two weeks without deploying can itself introduce instability. Instead, keep running the deploy process (without shipping new code) to surface memory leaks and other systemic issues. Her overall tone is pragmatic: freezes are a hack, not a moral triumph, and should be treated with appropriate sheepishness rather than self-congratulation (Charity Majors, https://charity.wtf/p/on-friday-deploys-sometimes-that).

- Deploy freezes are acceptable when teams lack the observability and confidence to move fast; they are a workaround, not a virtue.
- If you freeze deploys, also freeze merges to avoid a dangerous backlog of unshipped changes detonating later.
- Don't let the deployment process sit idle for weeks; run it without new code to catch systemic issues like memory leaks.
- The famous "murdering puppies" framing was deliberate hyperbole, not a literal call to ban all deploy freezes.
- Support practical transitions like "icing" and "defrosting" rather than all-or-nothing freezes.