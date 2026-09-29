---
domain: engineering-culture
subdomain: automated testing
concept: testing-for-confidence
title: Confidently Shipping Code: Why I Write Tests
sources:
  - title: "Confidently Shipping Code"
    url: "https://kentcdodds.com/blog/confidently-shipping-code"
    author: "Kent C. Dodds"
    date: "2018-10-08"
---

# Confidently Shipping Code: Why I Write Tests

Kent C. Dodds applies Simon Sinek's "Start With Why" framework to automated testing, arguing that developers adopt testing more readily when they understand their own motivation for it. He traces his personal journey: introduced to testing as an intern by Joe Eames, he only internalized it when maintaining his first JavaScript library, geniejs, made manual verification of every bug fix and feature tedious. Writing tests for that library saved him significant time and became part of his workflow (source).

A turning point came while working on angular-formly: a coworker watched him write a test, implement a feature, and push a commit that triggered a release, and was shocked that Dodds could trust the tests enough to be confident he hadn't broken anything. This shifted his view of testing from a time-saving default to a mechanism for gaining confidence (source).

Dodds reports having 111 packages published on npm, nearly all at 100% code coverage, and argues he could not maintain them otherwise given contributions from thousands of people. Because months or years may pass between his own touches to a codebase, continuous integration (TravisCI) running the test suite acts as "Past Kent" reassuring "Present Kent" that a change is unlikely to break anything — saving time and providing peace of mind to him and library users (source).

His stated why: tests let him accomplish more than he could alone, functioning as "thousands of Kents" verifying that changes don't break use cases. He closes by asking readers why they want to learn testing, what has held them back, and teases an upcoming comprehensive project (source).

- Dodds frames testing adoption around a personal "why," borrowing Simon Sinek's idea that people buy into an idea only when they understand the reason behind it.
- Tests serve as a confidence mechanism, not just a time-saver: they let a developer ship changes without manually re-verifying everything.
- With 111 npm packages at near-100% coverage and thousands of contributors, automated tests plus CI let Dodds safely accept changes to code he hasn't touched in months or years.
- He attributes his productivity to tests acting as an "army of robots" — thousands of automated Kents checking that changes don't break use cases.