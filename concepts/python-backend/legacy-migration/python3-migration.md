---
domain: python-backend
subdomain: legacy-migration
concept: python3-migration
title: EVE Online: The Move to Python 3 Begins!
sources:
  - title: "EVE Online: The Move to Python 3 Begins!"
    url: "https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/"
    date: "2026-08-25T22:59:30+00:00"
  - title: "EVE Online: The Move to Python 3 Begins!"
    url: "https://www.eveonline.com/news/view/the-move-to-python-3-begins"
---

# EVE Online: The Move to Python 3 Begins!

EVE Online, a long-running MMO, is finally beginning its migration from Python 2 to Python 3. The game has been running on Stackless Python since its launch in 2003, with its last major upgrade to Stackless Python 2.7 occurring in 2010. The migration will use the futurize script to automatically convert 2.4 million lines of code, followed by manual review of approximately 20,000 places where Python 2 and 3 behaviors differ, such as the change in division semantics where `1 / 2` returns 0 in Python 2 but 0.5 in Python 3.

- EVE Online has used Stackless Python since 2003 and upgraded to Stackless Python 2.7 in 2010, remaining on that version for over a decade.
- The migration to Python 3 begins with the futurize script applied to 2.4 million lines of code.
- Manual review is required for ~20,000 code locations where Python 2 and 3 behavior differs, including division and other semantic changes.
- The announcement does not detail how Stackless will be replaced, but a prior conference talk described replacing it with the Carbon engine scheduler in EVE Frontier, using the open-source carbonengine/scheduler library.