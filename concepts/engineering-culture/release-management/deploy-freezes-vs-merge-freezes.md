---
domain: engineering-culture
subdomain: release-management
concept: deploy-freezes-vs-merge-freezes
title: On Friday Deploys: Sometimes that Puppy Needs Murdering
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "Wed, 24 Dec 2025 00:54:45 GMT"
---

# On Friday Deploys: Sometimes that Puppy Needs Murdering

Charity Majors clarifies that she is not an extremist about deploy freezes. She argues that freezes are a pragmatic workaround for teams that lack the observability and confidence to deploy safely at any time, not a moral virtue. She criticizes the holier-than-thou attitude some adopt toward Friday freezes, insisting that if you need them, admit they're a hack and move on.

Majors advises that if you must freeze deploys, you should freeze merges instead. This prevents unreleased changes from accumulating into a risky snowdrift. She also warns that stopping deploys entirely can lead to systemic instability; the deploy pipeline should be run regularly without shipping new code to catch hidden issues.

She endorses the holiday period as a time for peace and creative work, citing a LinkedIn thread by Michael Davis where commenters like Payam Azadi discuss 'icing' and 'defrosting' periods. Ultimately, she believes teams can have both stability and safety by freezing merges, not deploys, and staying humble about the practice.

- Deploy freezes are a workaround for teams lacking observability and confidence, not a moral achievement.
- If you need to freeze, freeze merges to avoid accumulating unreleased changes that cause chaotic January recoveries.
- Don't actually stop deploying; run the deploy process without new code to detect systemic issues from inactivity.
- Holiday quiet periods are valuable, but avoid high-stakes freezes by easing in and out (e.g., 'icing' and 'defrosting').
- Don't act holier-than-thou about freezes; admit they're a hack and stay pragmatic.