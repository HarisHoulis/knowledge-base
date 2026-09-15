---
domain: engineering-culture
subdomain: testing-methodology
concept: tdd-refactor-step
title: The Time I Messed Up: Skipping Refactor in TDD
sources:
  - title: "The time I messed up"
    url: "https://kentcdodds.com/blog/the-time-i-messed-up"
    author: "Kent C. Dodds"
    date: "2018-10-22"
---

# The Time I Messed Up: Skipping Refactor in TDD

Kent C. Dodds recounts building `api-check`, a runtime validation library for `angular-formly`, after discovering React's PropTypes. He was excited about pure functions and test-driven development, and began writing tests first and implementing as he went. The process initially felt exhilarating ([source](https://kentcdodds.com/blog/the-time-i-messed-up)).

Over time, adding behaviors became less fun and more difficult; the library code grew complicated, to the point Dodds says he would not want to work on it again. He identifies the cause: he skipped the refactor step of TDD. TDD's cycle is red (write a failing test), green (write just enough code to pass), refactor (improve design while tests protect against regressions), and repeat ([source](https://kentcdodds.com/blog/the-time-i-messed-up)).

By moving from red to green and immediately on to the next feature, he built code that was difficult to understand and became legacy as soon as it was written. His conclusion is that TDD is awesome and can help produce great code, but skipping refactor and not being intentional about what you're building can lead to disaster ([source](https://kentcdodds.com/blog/the-time-i-messed-up)).

- TDD is a three-step cycle: red, green, refactor, repeat.
- The author skipped the refactor step while building api-check.
- Skipping refactor led to difficult-to-maintain code and a "monstrosity" of difficult-to-understand code.
- TDD can help develop great code, but skipping refactor and lacking intentional design can lead to disaster.