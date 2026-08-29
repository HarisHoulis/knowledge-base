---
domain: python-backend
subdomain: python-migration
concept: python3-migration
title: EVE Online: The Move to Python 3 Begins!
sources:
  - title: "EVE Online: The Move to Python 3 Begins!"
    url: "https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/"
    date: "2026-08-25T22:59:30+00:00"
---

# EVE Online: The Move to Python 3 Begins!

EVE Online, which has run on Stackless Python since its launch in 2003 and upgraded to Stackless Python 2.7 in 2010, has announced the start of its migration to Python 3. The migration plan involves using the futurize script on 2.4 million lines of code, followed by careful manual review of roughly 20,000 places where Python 2 and 3 behavior differ, such as integer division (1 / 2 returning 0 in Python 2 vs 0.5 in Python 3).

- EVE Online has used Stackless Python since 2003, with the last major upgrade to 2.7 in 2010.
- The migration to Python 3 uses the futurize script on 2.4 million lines of code.
- About 20,000 compatibility issues between Python 2 and 3 require manual review.
- The announcement doesn't specify how Stackless will be replaced, but a prior presentation introduced the carbonengine/scheduler for EVE Frontier's Carbon engine.