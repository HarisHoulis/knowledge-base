---
domain: python-backend
subdomain: python migration
concept: python3-migration
title: EVE Online: The Move to Python 3 Begins!
sources:
  - title: "EVE Online: The Move to Python 3 Begins!"
    url: "https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/"
    date: "2026-08-25"
---

# EVE Online: The Move to Python 3 Begins!

EVE Online, which has run on Stackless Python since its 2003 launch, is finally beginning its migration to Python 3. Their last major upgrade was to Stackless Python 2.7 in 2010, and the move involves using the futurize script on their 2.4 million lines of code, followed by manual review of approximately 20,000 places where Python 2 and 3 behavior differ, such as integer division. The announcement does not detail how they will replace Stackless, but a previous conference talk described their approach for EVE Frontier using the Carbon engine's scheduler, which is available as an open-source library.

- EVE Online has used Stackless Python since 2003 and upgraded to Stackless Python 2.7 in 2010.
- Migration to Python 3 starts with the futurize script on 2.4 million lines of code.
- Around 20,000 behavioral differences between Python 2 and 3 need manual review.
- The replacement for Stackless may be based on Carbon's scheduler, presented at a prior conference.