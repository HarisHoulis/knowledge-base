---
domain: python-backend
subdomain: python-migration
concept: stackless-python3-migration
title: EVE Online: The Move to Python 3 Begins!
sources:
  - title: "EVE Online: The Move to Python 3 Begins!"
    url: "https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/"
    date: "2026-08-25"
---

# EVE Online: The Move to Python 3 Begins!

EVE Online has been running on Stackless Python since its launch in 2003, with the last major upgrade being to Stackless Python 2.7 in 2010. The company has now announced the beginning of its migration to Python 3, a significant undertaking given the age and scale of the codebase. The migration plan involves using the futurize script to process 2.4 million lines of code, followed by a careful manual review of approximately 20,000 places where Python 2 and 3 behaviors differ—such as the division operator, where `1 / 2` evaluates to `0` in Python 2 but `0.5` in Python 3. This manual review is crucial to ensuring correctness across the entire codebase. The announcement does not specify how Stackless Python itself will be replaced, but at a conference last year, the team presented a talk titled 'Scheduling in Carbon: Leaving Stackless Python Behind,' which described how they replaced Stackless in the Carbon engine for their more recent game, EVE Frontier. That solution uses the now open-source `carbonengine/scheduler` library, which may offer a viable path forward for EVE Online's own migration.

- EVE Online has been on Stackless Python since 2003, last upgraded to Stackless Python 2.7 in 2010.
- Migration will use the futurize script on 2.4 million lines of code, plus manual review of ~20,000 Python 2/3 behavior differences.
- One key behavioral difference is division: `1 / 2` returns `0` in Python 2 but `0.5` in Python 3.
- The announcement doesn't detail Stackless replacement, but a prior talk described replacing Stackless with the open-source carbonengine/scheduler library for EVE Frontier.