---
domain: android-kotlin
subdomain: kotlin-collections
concept: intermediate-collection-avoidance
title: Intermediate collection avoidance
sources:
  - title: "Intermediate collection avoidance"
    url: "https://jakewharton.com/intermediate-collection-avoidance/"
    author: "Jake Wharton"
---

# Intermediate collection avoidance

The article demonstrates how to avoid intermediate collections in Kotlin by fusing operations. For example, `users.map { it.name }.joinToString()` can be simplified to `users.joinToString() { it.name }`, which eliminates the intermediate list and iterator. The IDE's intention action can automatically perform this refactoring, producing code that is both shorter and faster. [1](https://jakewharton.com/intermediate-collection-avoidance/)

Similarly, when creating arrays or pre-sized lists, using lambda initializers such as `Array(users.size) { users[it].name }`, `IntArray(users.size) { users[it].age }`, or `MutableList(users.size) { users[it].name }` avoids the overhead of an intermediate `map` collection by using indexed loops instead of iterators. This technique is especially useful in performance-sensitive code or when calling Java APIs. [1](https://jakewharton.com/intermediate-collection-avoidance/)

A caveat is that the source list must support random access; using this pattern with linked or persistent lists will result in abysmal performance. It is best suited for internal library usage where the list type is controlled. Benchmarks in the article show that the lambda-initialized variants are significantly faster and allocate fewer bytes. [1](https://jakewharton.com/intermediate-collection-avoidance/)

- Use fused operations like `joinToString { ... }` instead of separate `map` and `joinToString` to eliminate intermediate collections.
- Initialize arrays and pre-sized lists with lambdas (`Array(size)`, `IntArray(size)`, `MutableList(size)`) to avoid intermediate `map` results.
- This optimization relies on random-access sources; avoid using it with linked or persistent lists.
- Benchmarks show the lambda forms are faster and allocate less memory than the `map`-based equivalents.