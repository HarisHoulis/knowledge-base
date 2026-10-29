---
domain: engineering-culture
subdomain: large-scale-refactoring-and-cs-education
concept: codebase-maintainability-and-curriculum-reform
title: Software Engineering at Google & CS Education with Titus Winters
sources:
  - title: "Software engineering at Google & CS education with Titus Winters"
    url: "https://newsletter.pragmaticengineer.com/p/software-engineering-at-google-and"
    author: "Gergely Orosz"
    date: "2026-10-29"
---

# Software Engineering at Google & CS Education with Titus Winters

Titus Winters, lead author of Software Engineering at Google and former leader of Google's readability program and Abseil, discusses with Gergely Orosz how Google tackled a massive refactor of its ~250M-line C++ codebase in 2010. A dozen engineers used MapReduce-based parsing into abstract syntax trees, pattern matching, code generation, side-by-side coexistence of old and new APIs, sharded edits, blocking of old patterns, and final deletion of the old API — all before LLMs existed. The clang-format toolkit was created because the team needed it for this work.

Google made automated tests mandatory around 2007 after Search could no longer ship at a monthly cadence and slipped to quarterly, since nearly every change touched Search's code. Winters argues fear is not an acceptable basis for engineering: a codebase is unsustainable if valuable changes can't be made safely, and security nets that catch errors are strategically valuable. Google's readability program — requiring an owner and a certified readability reviewer to sign off on each change — grew into what may be the largest engineering classroom ever, with 10,000+ engineers enrolled at any time when Winters left.

On AI, Winters observes that code output is up hugely while outages are up roughly 30% and features shipped are static — treading water at best. Yet he is optimistic about AI as a net productivity boost, valuing it for enabling ambitious projects that previously didn't make sense rather than for doing the same work faster. He frames AI as a tool for the engineer's will ("Remember Andrew's axe"), warning against anthropomorphizing it.

Winters, the only working engineer on the 2023 ACM/IEEE/AAAI CS curriculum steering committee, believes the undergraduate curriculum is hopelessly out of date — largely unchanged since around 2000 and missing testing and verification, which matter greatly for new joiners. He forecasts falling CS enrollment unless it changes, and notes professors see a "middle group" of students collapse in understanding while the best thrive with AI as a tutor. He'd grade students' prompts and testing processes rather than just their code, and advises students to pursue unique passion projects rather than copying what everyone else does.

- Google's 2010 refactor of ~250M lines of C++ used AST parsing, pattern matching, code generation, coexistence, sharding, blocking old patterns, and deletion — and spawned clang-format.
- Automated tests became mandatory after Search's shipping cadence collapsed to quarterly; fear of making changes is not an acceptable basis for engineering.
- Google's readability program required owner plus certified readability reviewer sign-off and enrolled 10,000+ engineers at a time.
- With AI, code output is up but outages rose ~30% while features shipped stayed static; the real value is enabling previously unrealistic ambitious projects.
- Winters argues the undergrad CS curriculum is outdated and missing testing/verification, and advises students to grade thinking processes and pursue unique passion projects.