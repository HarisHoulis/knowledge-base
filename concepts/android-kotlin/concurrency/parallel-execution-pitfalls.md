---
domain: android-kotlin
subdomain: concurrency
concept: parallel-execution-pitfalls
title: Kotlin Concurrency - Parallel Execution
sources:
  - title: "Kotlin Concurrency - Parallel Execution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Pairing with Duncan"
    date: "2022-02-27T14:45:26+00:00"
---

# Kotlin Concurrency - Parallel Execution

This video is part 10 of a series exploring where a Test Driven Development (TDD) implementation of the Gilded Rose stock control system might lead. The author discusses a strategy for safely loading and updating a stock list from multiple web requests, but discovers that their approach has flaws. The episode highlights the complexity of concurrent programming in Kotlin and the importance of verifying assumptions through testing. The author references the book 'Java to Kotlin: A Refactoring Guidebook' as a related resource.

- Concurrent stock list updates from multiple web requests can introduce subtle bugs.
- TDD helps uncover concurrency issues that might otherwise go unnoticed.
- A previously thought-out strategy for thread safety may still be incorrect.
- Learning Kotlin concurrency benefits from resources like 'Java to Kotlin'.