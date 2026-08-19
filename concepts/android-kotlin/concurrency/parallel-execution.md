---
domain: android-kotlin
subdomain: concurrency
concept: parallel-execution
title: Kotlin Concurrency - Para Exec llel ution
sources:
  - title: "Kotlin Concurrency - Para Exec llel ution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Pairing with Duncan"
    date: "2022-02-27T14:45:26+00:00"
---

# Kotlin Concurrency - Para Exec llel ution

In this episode, Duncan continues his test-driven development series on the Gilded Rose stock control system. He had designed what he believed was a robust approach to safely reading and updating the stock list across concurrent web requests. However, through live coding and testing, he discovers that his strategy fails under real concurrency, illustrating that TDD alone cannot prevent all race conditions. The video serves as a practical lesson on the subtleties of Kotlin concurrency, and Duncan points viewers to the book 'Java to Kotlin: A Refactoring Guidebook' for further insight ([Pairing with Duncan, 2022](https://www.youtube.com/watch?v=y4OqpW4EMDk)).

- TDD helps guide design but does not automatically guarantee thread safety.
- Concurrent stock updates from multiple web requests can expose hidden race conditions.
- Kotlin concurrency requires explicit synchronization or carefully chosen data structures.
- The author's initial safe-update strategy was proven flawed through practical experimentation.