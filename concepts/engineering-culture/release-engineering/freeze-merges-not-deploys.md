---
domain: engineering-culture
subdomain: release-engineering
concept: freeze-merges-not-deploys
title: On Friday Deploys: Freeze Merges, Not Deploys
sources:
  - title: "On Friday Deploys: Sometimes that Puppy Needs Murdering"
    url: "https://charity.wtf/p/on-friday-deploys-sometimes-that"
    author: "Charity Majors"
    date: "2025-12-24"
---

# On Friday Deploys: Freeze Merges, Not Deploys

Charity Majors clarifies that she does not oppose deploy freezes outright; they are a pragmatic workaround for teams that lack the observability and confidence to move swiftly. The real problem, she argues, is treating deploy freezes as a moral virtue rather than a hack. If you cannot safely deploy, a freeze is sensible—but you should not pretend it is the 'right thing' rather than a concession to limitations.

Majors warns against a common trap: freezing deploys while allowing developers to keep merging changes into main. This builds up a 'snowdrift' of unreleased diffs that all collide at once when deploys resume, turning January into a disaster. Her advice is to freeze merges too, so people can work on other valuable tasks instead of accumulating dangerous inventory.

She also notes that teams accustomed to frequent deploys can suffer outages from simply stopping deploys, because regular deployment helps flush out systemic issues like memory leaks. To mitigate this, she suggests continuing to run the deploy process regularly—just without shipping new code. This keeps the system exercised while maintaining stability during holidays.

- Deploy freezes are pragmatic hacks, not moral achievements; don't be sanctimonious about them.
- If you freeze deploys, freeze merges too, or unreleased changes will pile up and explode later.
- Stopping frequent deploys can itself cause instability; keep running deploys without shipping new code.
- Freezes are reasonable when teams lack observability or confidence to move fast safely.