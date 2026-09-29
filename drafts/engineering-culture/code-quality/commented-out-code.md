---
domain: engineering-culture
subdomain: code-quality
concept: commented-out-code
title: Please, don't commit commented out code
sources:
  - title: "Please, don't commit commented out code"
    url: "https://kentcdodds.com/blog/please-dont-commit-commented-out-code"
    author: "Kent C. Dodds"
    date: "2015-10-27"
---

# Please, don't commit commented out code

Kent C. Dodds argues against committing commented-out code, using a simple example where a function can be reduced to one line and the old implementation remains only as comments. The primary reason is focus and cognitive load: encountering commented code often derails a developer’s workflow as they stop to read it and wonder whether it matters (Kent C. Dodds, 2015).

Commented-out code can also hide important code when scanning, especially in long blocks, and it inevitably becomes out of date: it is no longer tested, linted, or run, and the APIs it used may have changed or been removed (Kent C. Dodds, 2015). Dodds favors relying on version control to recover old code, citing git diff and file history tools as sufficient for looking back months or years.

He addresses common objections: work-in-progress should live in a branch (even broken commits), TODOs belong in a story, and third-party integration examples are documentation rather than commented-out code. He suggests eslint’s no-commented-out-code rule as a way to enforce the practice and notes exceptions are rare.

- Commented-out code increases cognitive load and can derail a developer's focus.
- It can hide important code and becomes stale, untested, unlinted, and unrun.
- Version control (git diff/history) is the right place to preserve removed code.
- Work-in-progress belongs in branches; TODOs belong in stories/issue trackers.
- Documentation examples for third-party integrators are an exception; eslint's no-commented-out-code rule can help enforce the practice.