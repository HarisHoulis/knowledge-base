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

The article discusses how Kotlin's collection extension functions like `map` can create intermediate collections and iterators, which are unnecessary for simple transformations. Jake Wharton shows how to avoid these overheads using fused operations such as `joinToString { }` instead of `map { }.joinToString()`, and array/list initializers with lambdas. These techniques reduce allocations and speed up execution, especially when the source list supports random access. The IDE's intention actions can automatically suggest these improvements, making the code both shorter and faster.

- Fuse operations like `map` with terminal operations to avoid intermediate collections and iterators.
- Use `Array(size) { ... }` or `MutableList(size) { ... }` for indexed initialization to replace `map` plus array/list conversion.
- These fused forms are faster and allocate less memory, as shown by benchmarks.
- The technique relies on random access; use it carefully with non-array-backed collections.