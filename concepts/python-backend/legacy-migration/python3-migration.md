---
domain: python-backend
subdomain: legacy-migration
concept: python3-migration
title: EVE Online: The Move to Python 3 Begins!
sources:
  - title: "EVE Online: The Move to Python 3 Begins!"
    url: "https://www.eveonline.com/news/view/the-move-to-python-3-begins"
    date: "2026-08-25"
  - title: "EVE Online: The Move to Python 3 Begins!"
    url: "https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/"
    author: "Simon Willison"
    date: "2026-08-25"
---

# EVE Online: The Move to Python 3 Begins!

EVE Online, which has run on Stackless Python since its 2003 launch and upgraded to Stackless Python 2.7 in 2010, is beginning its long-awaited migration to Python 3. The process starts by running the futurize script across 2.4 million lines of code, followed by manual review of roughly 20,000 places where Python 2 and 3 behavior differs, such as integer division. The announcement does not detail how they will replace Stackless Python, but a presentation from their conference last year described a scheduling solution called 'Carbon' used in EVE Frontier, which replaces Stackless with an open-source scheduler library. This migration highlights the challenges of upgrading large, legacy codebases and the importance of automated tooling combined with human oversight.

- EVE Online is migrating from Stackless Python 2.7 to Python 3 after 16 years without a major upgrade.
- The migration uses the futurize script on 2.4 million lines of code, then manual review of ~20,000 semantic differences.
- Stackless Python replacement is not covered in the announcement, but a prior talk introduced the open-source 'carbonengine/scheduler' used in EVE Frontier.
- The scale of the codebase and the long gap between upgrades make careful automated and manual steps necessary.