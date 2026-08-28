---
domain: python-backend
subdomain: python-migration
concept: python3-migration
title: EVE Online: The Move to Python 3 Begins!
sources:
  - title: "EVE Online: The Move to Python 3 Begins!"
    url: "https://www.eveonline.com/news/view/the-move-to-python-3-begins"
    date: "2026-08-25"
  - title: "Stackless Python"
    url: "https://github.com/stackless-dev/stackless/wiki/"
  - title: "Stackless Python 2.7"
    url: "https://www.eveonline.com/news/view/stackless-python-2.7"
    date: "2010"
  - title: "futurize"
    url: "https://python-future.org/futurize.html"
  - title: "Scheduling in Carbon: Leaving Stackless Python Behind"
    url: "https://youtu.be/-x299qHLQs0"
  - title: "carbonengine/scheduler"
    url: "https://github.com/carbonengine/scheduler"
---

# EVE Online: The Move to Python 3 Begins!

EVE Online, running on Stackless Python since 2003 and last upgraded to Stackless Python 2.7 in 2010, has announced the start of their migration to Python 3. The upgrade process will use the futurize script against 2.4 million lines of code, followed by careful manual review of approximately 20,000 places where Python 2 and 3 behavior differ, such as integer division where `1 / 2` returns `0` in Python 2 but `0.5` in Python 3. The announcement does not detail how they will replace Stackless, but at their previous conference they presented a solution for their newer game EVE Frontier: the Carbon engine scheduler, which uses the open source carbonengine/scheduler library. This migration highlights the challenges of upgrading large, long-lived Python codebases and the need for automated tooling combined with manual analysis.

- EVE Online has run on Stackless Python since 2003, with the last major upgrade to Stackless Python 2.7 in 2010.
- Migration to Python 3 begins by running the futurize script across 2.4 million lines of code.
- Manual review is required for ~20,000 Python 2 vs Python 3 behavioral differences, e.g., division semantics.
- The announcement does not explain Stackless replacement; a previous talk describes replacing it in the Carbon engine for EVE Frontier using the open source carbonengine/scheduler library.